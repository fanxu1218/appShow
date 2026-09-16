# AppShow

fanxu 的独立应用展示网站。首页是可扩展的应用目录，每个应用拥有独立介绍页；目前收录 **漫架（SeeComics）**。

## 内容与目录

```text
dist/
  index.html                 应用展示首页
  apps/manjia/index.html     漫架介绍、真实界面、下载状态与常见问题
  assets/site.css            共享样式和响应式布局
  assets/site.js             截图切换（键盘及无 JavaScript 降级）
  assets/favicon.svg         AppShow 标识
  assets/manjia/             漫架品牌与商店截图
```

网站为原生 HTML、CSS、JavaScript，无第三方运行依赖、外部字体、分析脚本或后端。`dist` 是直接维护的源码和发布目录，不是生成缓存，须提交到版本控制。所有站内链接使用相对路径，适用于站点根目录，也兼容 GitHub Pages 的 `/appShow/` 项目路径。

## 本地预览

在本仓库执行：

```sh
python3 -m http.server 4173 --bind 127.0.0.1 --directory dist
```

访问 `http://127.0.0.1:4173/`，漫架独立页面为 `http://127.0.0.1:4173/apps/manjia/`。纯静态网站无需安装依赖或编译。

## 平台发布状态

以所有者本次提供的发布信息为准（2026-09-16）：

- Windows 已发布：[Microsoft Store](https://apps.microsoft.com/detail/9n62c3shvr6n?hl=zh-CN&gl=US)。
- macOS、iOS、iPadOS、Android、HarmonyOS、Android TV、Apple TV 尚未发布，不提供占位下载链接。
- Xbox 已由所有者明确纳入上架计划，目前尚未发布，不将 Windows 商店链接当作 Xbox 下载入口。
- 多平台适配不等于各平台已上架，也不代表云端自动同步。
- 不展示未确认的售价、发布日期、用户数量或评价；价格、地区和系统要求以商店页面为准。

新平台发布时，修改 `dist/apps/manjia/index.html` 中该平台卡片，将“尚未发布”替换为真实商店链接，同时更新首屏、下载区说明、FAQ、首页发布标签和本节。保留外链 `rel="noopener noreferrer"`。

## 增加下一个应用

1. 在 `dist/apps/<应用英文标识>/index.html` 新增应用介绍页。
2. 将该应用素材放入 `dist/assets/<应用英文标识>/`，复用共享布局；用独立的 body 类名隔离品牌样式。
3. 在首页 `#apps` 新增一个应用条目，链接到独立页面，并更新应用数量。
4. 更新独立页面标题、描述、图标和下载状态，保持手机、平板及桌面可用。

## 素材与文案来源

见 [ASSETS.md](ASSETS.md)。介绍页使用真实应用截图，首屏明确使用品牌宣传插画；截图里的作品为第一方虚构示例，不暗示应用内提供在线内容。产品文案依据 SeeComicsShare 当前 README、品牌说明及商店截图说明整理，未将内部计划、测试完成度、平台凭证或审核资料复制进网站。

## 发布

网站使用 GitHub Pages，发布目录为 `dist/`：

- 首页：https://fanxu1218.github.io/appShow/
- 漫架：https://fanxu1218.github.io/appShow/apps/manjia/
- [发布工作流](https://github.com/fanxu1218/appShow/actions/workflows/deploy-pages.yml)

仓库 Settings → Pages → Source 设为 **GitHub Actions**。推送到 `main` 且修改了网站、校验脚本或部署工作流时自动发布，也可从 Actions 手动运行。工作流先检查站内资源与 JavaScript 语法，再上传 `dist/` 并部署；README、素材来源说明和本地验收记录不进入网站发布目录。

提交前可运行：

```sh
python3 scripts/validate-site.py
node --check dist/assets/site.js
```

公开发布已获所有者授权；最新部署结果以仓库 `github-pages` 环境及工作流状态为准。
