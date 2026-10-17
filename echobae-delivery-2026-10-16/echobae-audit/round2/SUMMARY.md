# Echobae 第二轮审计摘要

建议：**暂缓正式推广和开放Google收录；优先修复/解释今天的SSR加载壳，再完成前台及沙盒验收。** 不将预发布robots/noindex当作恶意故障，也不未经批准解除。

## 本轮新确认与变化

- 当前首页5个成功样本和Lydia商品1个成功样本HTTP200，却无Title、业务meta、H1、Canonical、Schema/业务正文，只有shell-loading；tokensReady=false。主题API和3个正式商品API却200。加载壳与服务端为何没准备好必须分开诊断（SEO-09）。
- 当前英文公开商品列表4页共72个唯一商品，未发现Demo/e2e/copy/test命名；3个代表退休商品API404。第一轮189混杂目录已有改善，不能照旧批量下架；推荐模块和HTML旧URL状态尚未验收（CAT-01）。
- 当前入口及其依赖已跟踪，购物车/结账划线价仍公开实现为售价×1.2；不是仅推测（CART-01）。
- 图片候选复用的具体链：域名白名单缺echobae.com + NuxtImage sizes语法误用；首Banner实际30KB，不能以压缩大图代替首屏尺寸/渲染修复（IMG-01、PERF-04）。
- footer.poweredBy在当前英文公共字典缺失，组件仍调用该键（UX-03）。
- 首轮漏报定制FAQ问答错位与30天退货Demo、QY073空FAQPage、详情图占位Alt及分页href问题，新增CONT-06/SEO-10/IMG-04/SEO-11。

## 追踪范围与校准

原37个ID逐项保留，新增5项，共42条记录（P0 1、P1 18、P2 20、P3 3；含合并/待核验/历史事项，非当前确诊故障数）。CAT-01降P1并标部分改善；IMG-02降P2（裁剪不等于不当构图）；IMG-03降P3（首图预算已合理）；PERF-03并入PERF-01，不重复计工期。待账号/业务验证的项目明确标识，不能把总条目数当作当前确诊Bug数。

本轮不重跑228URL基础爬虫。复用2026-10-13的25深度页/58视口/27次Lighthouse；新做公开代码/API/样本HTML/11类图片记录、物理像素/字节、链接图交叉与Schema结构分析。图片DOM尺寸仍来自首轮，今天读取文件并不等于今天浏览器重新验证布局。

## 推荐实际执行顺序

1. 开发定位SEO-09：完整SSR、主题bootstrap和错误/缓存边界；同时解决SEO-03/SEO-04/FE-02。
2. 运营+开发验收已清理目录、真实SKU/选项/照片及库存生产承诺；不要删除已退休数据或新添测试SKU。
3. 开发统一CART-01价格模型、POL-04条款可阅读性、SHIP-01地址报价/费用展示；在沙盒补交易校验。
4. 运营修订政策占位、时效、定制FAQ、型号/AI标配含义和评价来源；后台菜单未验证，不编造路径。
5. 开发修正图片provider/sizes、Banner尺寸占位、焦点/字典和当前实际裁剪；通过受控冷/热性能复检。
6. 最后在批准发布窗口解除公开页索引限制、生成非空Sitemap、提交GSC；保留交易/账户/搜索的合适排除。

## 文件

[完整报告](FINAL_REPORT.md)、[42项逐项分析](ISSUE_DEEP_DIVE.md)、[Excel/WPS问题表](ISSUES_ROUND2.csv)、[开发需求](DEVELOPER_REQUIREMENTS.md)、[运营清单](ADMIN_ACTIONS.md)、[待验证与所需信息](UNVERIFIED_AND_REQUIRED_INFO.md)、[性能/交互](PERFORMANCE_AND_INTERACTION.md)、[图片实施](IMAGE_IMPLEMENTATION.md)、[技术实现示例](TECHNICAL_PATCH_GUIDE.md)、[证据索引](evidence/INDEX.md)。

## 真实限制

用户不授权加入浏览器CA；自动审批已拒绝该持久信任变更。当前Chromium访问ERR_CERT_AUTHORITY_INVALID，本轮**没有新浏览器截图、滚动FPS、EventTiming、冷/热对照或Lighthouse**。既有截图/数据标注10月13日；脚本仅为未来复检准备，并未执行。没有付款/订单/订阅/联系消息或生产改动。不使用GitHub交付。
