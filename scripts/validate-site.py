"""Check publishable pages and relative URLs without third-party dependencies."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []
        self.ids = []
        self.h1_count = 0
        self.images = []

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "h1":
            self.h1_count += 1
        if tag == "img":
            self.images.append(attrs)
        self.references.extend(attrs[key] for key in ("href", "src") if key in attrs)


def main():
    root = Path(__file__).resolve().parents[1] / "dist"
    if not (root / "index.html").is_file():
        raise SystemExit("Missing dist/index.html")
    pages = {}
    errors = []
    for path in root.rglob("*.html"):
        page = Page()
        page.feed(path.read_text(encoding="utf-8"))
        pages[path] = page
        if page.h1_count != 1:
            errors.append(f"{path.relative_to(root)}: expected one H1")
        if len(set(page.ids)) != len(page.ids):
            errors.append(f"{path.relative_to(root)}: duplicate element ID")
        for image in page.images:
            if not all(key in image for key in ("alt", "width", "height")):
                errors.append(f"{path.relative_to(root)}: incomplete image metadata")

    for path, page in pages.items():
        for reference in page.references:
            url = urlparse(reference)
            if url.scheme or url.netloc:
                continue
            if url.path.startswith("/"):
                errors.append(f"{path.relative_to(root)}: root URL breaks project Pages: {reference}")
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if root not in target.parents and target != root:
                errors.append(f"{path.relative_to(root)}: URL outside public directory: {reference}")
                continue
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                errors.append(f"{path.relative_to(root)}: missing resource: {reference}")
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f"{path.relative_to(root)}: missing anchor: {reference}")

    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Validated {len(pages)} pages: assets, project-relative URLs, anchors and image metadata.")


if __name__ == "__main__":
    main()
