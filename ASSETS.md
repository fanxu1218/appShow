# AppShow 网站素材溯源

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

同日首页风格统一复用既有 `favicon.svg`、漫架 Logo 和 Windows 书架截图，移除首页插画海报与装饰色带，未新增图片或第三方素材。旧插画文件保留用于历史兼容。

## 2026-11-27 HappyVPN

HappyVPN 使用所有者 `HarmonyShadowrocket` 工程中已确认的 Liquid Cobalt 正式品牌素材，以下文件均原样复制；网页使用 CSS 排版，未生成或伪造应用界面。

| 网站文件 | 原工程内来源 | 用途 |
| --- | --- | --- |
| `dist/assets/happyvpn/icon.png` | `AppScope/resources/base/media/app_icon.png` | 正式应用图标、站点图标与应用条目 |
| `dist/assets/happyvpn/background.png` | `entry/src/main/resources/base/media/lc_ui_background.png` | 蓝色品牌背景 |
| `dist/assets/happyvpn/flight.png` | `entry/src/main/resources/base/media/lc_ui_flight.png` | 蓝紫飞行标品牌插画 |

来源清单：原工程 `docs/ui-liquid-cobalt/assets.json`。正式名称和配置、订阅、节点、规则等功能介绍依据当前 README；封测状态和公开申请邮箱由所有者在本次任务中确认。素材不含实际节点、订阅地址、凭据或个人设备信息。
