# 漫架介绍页改版视觉与交互检查

日期：2026-11-05。范围：`dist/apps/manjia/index.html` 及独立样式、平台图标；应用目录首页及 SeeComicsShare 应用代码未修改。

## 对照依据

- 用户选择：本次会话中第二张生成效果图，暖白底色、居中标题、黑色主按钮、大幅真实界面、底部截图选项及浅灰本地阅读说明。
- source visual truth path: `/Users/apple/.codex/generated_images/01a1aa2c-24d9-7360-9e49-9a2a5c2aa1e7/exec-2d0132cf-c64e-46ec-af9c-8b57641054e2.png`
- implementation screenshot path: `/Users/apple/.codex/visualizations/2026/11/05/01a1aa2c-24d9-7360-9e49-9a2a5c2aa1e7/manjia-desktop-final.jpg`
- 本地页面：`http://127.0.0.1:4173/apps/manjia/`，使用 ChatGPT in-app browser 实际打开并检查。
- 状态：页面顶部、本地书架选中、FAQ 收起，浅色主题。
- 源图与最终截图均为 1036 × 1518 像素。CSS 视口 1051 × 1518，DPR 1；桌面滚动条占用 15px，内容区为 1036px，截图裁取实际内容区，不缩放或拉伸。
- 完整同尺寸合成对照：`/Users/apple/.codex/visualizations/2026/11/05/01a1aa2c-24d9-7360-9e49-9a2a5c2aa1e7/manjia-comparison-final.jpg`
- 标题、描述、下载按钮的原尺寸局部合成对照：`/Users/apple/.codex/visualizations/2026/11/05/01a1aa2c-24d9-7360-9e49-9a2a5c2aa1e7/manjia-headline-comparison-final.jpg`

## 对比与修正记录

第一轮结果为 blocked，依据 `manjia-comparison-initial.jpg`、`manjia-headline-comparison.jpg` 与 `manjia-mobile-initial.jpg`：

- [P2，已修正] 本地阅读说明的标题偏小、左右布局过宽，弱化了参考图的中段层级。调整 `.local-inner` 内容宽度和列比例，标题改为 48px，手机恢复单列。
- [P2，已修正] 390px CSS 视口中 Windows 下载按钮文案换行，而 Android 按钮保持单行。420px 以下改为两个等宽、50px 高的纵向按钮；最终 `manjia-mobile-390.jpg` 两按钮均为 335 × 50px，没有文字换行。
- [P3，已修正] 主标题笔画和字号略弱。将标题字重调整为 800，调整字号和行高；最终局部合成图已重新检查。
- 为截图面板提供向内的键盘焦点轮廓，避免轮廓被画框裁切；保留原有截图切换脚本和无 JavaScript 降级。

第二轮依据最终完整、局部合成图，以及 320、390、768、1440px 布局截图重新检查；没有剩余需要修正的 P0/P1/P2 项目。

## 五项视觉检查

- 字体与排版：采用系统无衬线字体，主标题保持两行、灰色说明与橙色句号；手机标题与 CTA 不截断。系统字体的笔形及光栅化与生成图存在轻微差异，属于可接受的 P3 差异。
- 留白与布局：保留居中首屏、水平下载入口、宽幅截图、底部下划线标签和浅灰说明区。中下段沿用相同字号、分隔线、灰色文字与空间节奏，完成原页面功能、设备、下载和 FAQ 内容。
- 颜色：主背景 `#fcfbf8`、浅灰背景 `#f2f0eb`、正文 `#20211f`、次要文字 `#64655f`、橙色强调 `#ce431b`。没有使用原首屏的大幅插画、黑色底色或强烈橙色整段背景。
- 图片与图标：复用批准的 Logo、真实书架、漫画、小说、夜间、手机、iPad 和 TV 截图，未生成替代应用界面。书架只裁去底部空白，其他截图等比完整展示。生成效果图里的应用内部细节和 Android 图形不作为产品事实；采用真实截图及 Simple Icons 的平台标识，这是有意的素材修正。
- 产品文案：保留本地漫画、小说、PDF 阅读器定位、原创示例说明、导入自有内容、离线阅读、无需漫架账号、无内置在线资源以及无自动云同步边界。保留两项已发布入口与七项尚未发布状态，没有新增定价、人数、评价或发布日期。

## 浏览器与静态验证

- 截图切换：实际点击漫画标签，验证仅对应面板可见；右方向键进入小说、End 进入夜间、Home 返回书架，焦点和 `aria-selected` 正确更新。
- 页面内导航：实际点击下载和平台链接；动画结束后，目标区块距离视口顶部分别约 28.16px 和 28.33px，符合滚动留白。
- FAQ：实际展开“阅读需要联网或注册账号吗？”，确认正文显示。
- 下载链接：检查首屏及下载区的四个入口均指向原有 Microsoft Store / Google Play 地址，使用新窗口及 `noopener noreferrer`。未执行商店下载安装，也未重新核验价格或地区。
- 响应式：CSS 视口 320、390、768、1440px 的文档宽度分别为 305、375、753、1425px，均等于 `scrollWidth`，没有横向溢出。已查看完整桌面、平板及手机截图。
- 所有可见图片完成加载，没有损坏项；浏览器记录中没有 error 或 warn 日志。
- `python3 scripts/validate-site.py` 通过：两页的资源、相对路径、锚点、图片元数据、H1 和 ID 检查。
- `node --check dist/assets/site.js`、`git diff --check` 通过。Node 使用本机 DevEco Studio 内置运行时。
- 纯静态网站，无需编译或安装；未运行应用构建、真机、屏幕阅读器或应用商店安装验收。响应式检查属于桌面浏览器模拟。
- 本报告记录发布前本地验收；所有者随后已确认提交并发布至原 GitHub Pages。公开部署和线上页面的结果需单独核对，不以本地预览代替。

## 其他证据

证据目录：`/Users/apple/.codex/visualizations/2026/11/05/01a1aa2c-24d9-7360-9e49-9a2a5c2aa1e7/`。

- `manjia-desktop-1440.jpg`：完整宽屏页面。
- `manjia-tablet-768.jpg`：完整平板尺寸页面。
- `manjia-mobile-390.jpg`、`manjia-mobile-320.jpg`：完整手机尺寸页面。
- `manjia-mobile-review.jpg`：手机页面连续分段合成，检查全部中下段。
- `manjia-gallery-dark.jpg`：夜间截图切换状态。
- `manjia-download-desktop.jpg`：下载区实际锚点定位。
- `manjia-download-faq.jpg`：FAQ 实际展开状态。

## 交付清单

- [x] 用户选中方向的完整介绍页已实现。
- [x] 原有核心内容、真实素材与下载入口保留。
- [x] 桌面和手机核心交互已验证，视觉对照已通过。
- [x] 本地预览服务保留运行，浏览器预览交给用户查看。

final result: passed
