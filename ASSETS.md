# 漫架网站素材溯源

品牌与应用截图取自所有者的 `SeeComicsShare` 工程，没有重新生成应用界面或引入第三方书籍封面；平台图标来源见下方补充说明。

| 网站文件 | 原工程内来源 | 用途 |
| --- | --- | --- |
| `dist/assets/manjia/icon.png` | `assets/branding/seecomics-logo-master-1024.png` | 已确认的品牌 Logo |
| `dist/assets/manjia/hero.jpg` | `store/screenshots/huawei-appgallery-2026-09-11/final/recommendation/1920x1080.jpg` | 已有原创营销插画，不作为实际界面 |
| `windows-library.png` | `store/screenshots/1.0.0/windows-desktop/01-shelf-light.png` | Windows 书架实拍 |
| `windows-dark.png` | `store/screenshots/1.0.0/windows-desktop/02-series-night.png` | Windows 夜间分册实拍 |
| `windows-comic.png` | `store/screenshots/1.0.0/windows-desktop/03-comic-reader.png` | Windows 漫画阅读实拍 |
| `windows-novel.png` | `store/screenshots/1.0.0/windows-desktop/04-novel-reader.png` | Windows 小说阅读实拍 |
| `phone-library.png` | `store/screenshots/huawei-appgallery-2026-09-11/raw/phone/01-shelf-light.png` | HarmonyOS 商店预览书架 |
| `ipad-comic.png` | `store/screenshots/1.0.0/ipad/03-comic-reader.png` | iPad 漫画阅读实拍 |
| `apple-tv.png` | `store/screenshots/1.0.0/apple-tv/01-shelf-light.png` | Apple TV 书架实拍 |

表中短文件名均位于 `dist/assets/manjia/`。原截图未修改；手机、平板画框和局部展示由网页 CSS 布局实现。

来源说明：原工程 `assets/branding/README.md`、`store/screenshots/1.0.0/windows-desktop-manifest.json`、`store/screenshots/huawei-appgallery-2026-09-11/README.md`。Windows 素材清单标记内容为 `first-party-fictional`；HarmonyOS 说明确认截图来自真实运行的预览构建，品牌插画为原创生成式宣传图。

2026-11-05 介绍页改版复用原始 Logo 与应用截图，宣传插画不再用于介绍页首屏。新增 `windows.svg`、`android.svg` 来自 [Simple Icons v11.15.0](https://github.com/simple-icons/simple-icons/tree/11.15.0/icons)，按 CC0-1.0 分发；平台名称及标识属于各自权利方。图标在本地提供，页面不依赖外部图标或字体服务。
