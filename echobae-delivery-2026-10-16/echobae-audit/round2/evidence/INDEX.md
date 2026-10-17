# 第二轮证据索引

2026-10-14当前HTTP/API/资源与2026-10-13历史DOM/截图/Performance严格分开。没有新浏览器截图/trace；未来probe草案未执行。

## 结构化证据

- [current-shell-analysis.json](current-shell-analysis.json)：成功HTTP文档的Title/H/meta/Canonical、theme ready与data状态；含robots/Sitemap文本，只有shellLoading=true才是加载壳样本
- [current-capture.json](current-capture.json)：样本HTTP/公开JS/CSS响应；错误与原始SHA/格式化镜像及CSS恢复区分
- [current-catalog-pages.json](current-catalog-pages.json)：当前英文4页72个唯一SKU及命名检查，不是浏览器页面验收
- [demo-api-followup.json](demo-api-followup.json)：三个代表退休Demo/测试/复制SKU API404
- [catalog-locale-comparison.json](catalog-locale-comparison.json)：en72/root0，不能把root当语言发布计划
- [public-products.json](public-products.json)：三个正式SKU及随机不存在slug的公开API选定字段，无凭据
- [public-theme-request.json](public-theme-request.json)：当前主题配置API200及字段名，不推断SSR服务器内部调用是否成功
- [public-ui-payment-metadata.json](public-ui-payment-metadata.json)：英文Footer缺poweredBy及公开支付可用性布尔值，已排除凭据字段
- [active-module-map.json](active-module-map.json)：当前入口直接指向的layout/product/cart/checkout模块
- [active-dependencies.json](active-dependencies.json)：当前SEO/图像wrapper/breadcrumb/Checkout依赖
- [active-image-layout-map.json](active-image-layout-map.json)：当前NuxtImage provider与layout组件的直接依赖
- [initial-code-search.json](initial-code-search.json)：最初从第一轮公开构建产物提取的搜索片段，非当前入口身份认证
- [ssr-payload-fields.json](ssr-payload-fields.json)：第一轮公开SSR载荷选定字段（SEO/price/status）；时间为历史，不混为今天载荷
- [schema-consistency.json](schema-consistency.json)：历史默认Product Schema与当前API三SKU对比，非本轮浏览器Schema输出
- [faq-schema-check.json](faq-schema-check.json)：从第一轮JSON-LD结构补查空FAQPage与错误定制答案
- [image-probe.json](image-probe.json)：11条图片：文件像素/字节今天实测，DOM/fit等来自昨天
- [downloaded-image-index.json](downloaded-image-index.json)：本轮原图查看的实际下载文件映射，非浏览器截图
- [http-metrics.json](http-metrics.json)：三个首页HTTP成功、三个商品无响应超时，不能以http0计成0秒性能
- [performance-diagnostics.json](performance-diagnostics.json)：第一轮27个真实Lighthouse报告的诊断抽取，无新运行
- [link-graph.json](link-graph.json)：第一轮a图+当前72SKU交叉；历史32/当前交叉18候选不是今天已证明孤立
- [revisions.json](revisions.json)：9条过度归因/旧假设修正
- [issues-round2.json](issues-round2.json)：原37+新增5的深度追踪数据、优先级和状态

## 当前代码定位（格式化行号，不是内部源码路径）

|公开模块|角色|相关定位|
|---|---|---|
|[BFXRDhpD.js](code/BFXRDhpD.js)|当前入口|主题ready/formatPageTitle、年龄/营销/运行模块插件|
|[CYM8kJOs.js](code/CYM8kJOs.js)|default布局|第23行shell-loading、tokensReady选择分支|
|[DL_6UJog.js](code/DL_6UJog.js)|商品/PdpGalleryV2|752数据加载、1911 sizes、5656一次error检查|
|[B63DM7Lk.js](code/B63DM7Lk.js)|CartV2|635单价×1.2|
|[B7-ND3fn.js](code/B7-ND3fn.js)|CheckoutV2|2158比较价、3317纯span条款|
|[BK9qvGFY.js](code/BK9qvGFY.js)|NuxtImg provider|134域名校验、290白名单、Z/re sizes解析|
|[C6D29uTs.js](code/C6D29uTs.js)|ProductImage|adaptive默认false、onload改ratio、sizes输入|
|[4FfVxrIF.js](code/4FfVxrIF.js)|SEO helper|brand格式化、robots优先级、canonical、Product生成|
|[DsOVWUii.js](code/DsOVWUii.js)|布局/面包屑/Footer|3739 footer.poweredBy与共享title fallback|
|[C_kT0Sim.js](code/C_kT0Sim.js)|面包屑共享状态|按path读写page-breadcrumb-store|
|[CNpsGre3.js](code/CNpsGre3.js)|ProductCard/helper|adaptive调用参数、card结构|

当前入口通过今天HTML确定，再沿直接import映射。旧DNfd1SfM/Dly等文件仅供第一轮对照，虽然hash地址仍可获取，不能因此说页面正在使用旧文件。公开构建产物行号是格式化副本的行号，代码SHA和原始字节另存。

## CSS定位

- [home-inline.css](css/home-inline.css)：第一轮初始HTML提取/格式化的Banner CSS；2629媒体无ratio、2634 img height:auto、2741移动nav定位。不是今天computed style。

- [_slug_.DW03sqVO.css](css/_slug_.DW03sqVO.css)：公开旧hashCSS镜像；pdp-gallery main4:5、image cover、thumb舞台。当前活跃渲染未复检。

- [ProductCard.RK14Wzbu.css](css/ProductCard.RK14Wzbu.css)：旧卡片1:1；新adaptive组件支持不等于已启用此处。

- raw-css/保留与原capture摘要匹配的30个响应；css/为格式化方便定位。

## 历史截图（真实日期2026-10-13）

- [首页移动390×844](../../evidence/browser/mobile-8a5edab282-settled.png)：历史，非本轮新截图
- [首页桌面1440×900](../../evidence/browser/desktop-8a5edab282-settled.png)：历史，非本轮新截图
- [新款分类移动](../../evidence/browser/mobile-8f6d729883-settled.png)：历史，非本轮新截图
- [Lydia主图移动](../../evidence/browser/mobile-5b0c2ba7b3-settled.png)：历史，非本轮新截图
- [已加AI的购物车移动价格](../../evidence/browser/verify-client-cart.png)：历史，非本轮新截图
- [结账优惠入口和条款移动](../../evidence/browser/checkout-coupon-open.png)：历史，非本轮新截图
- [年龄键盘场景](../../evidence/browser/age-keyboard.png)：历史，非本轮新截图

## 原始基线

- [第一轮CSV](../../ISSUES.csv) · [第一轮详细报告](../../FULL_AUDIT.md) · [第一轮性能](../../PERFORMANCE_REPORT.md)

- [原始浏览器DOM/网络](../../evidence/browser/deep.json) · [购物流程](../../evidence/browser/cart-verify.json) · [分页记录](../../evidence/pagination.json)

- [第一轮Lighthouse27次参数与指标](../../evidence/performance-summary.json)，原JSON/HTML在../../evidence/lighthouse/；完整交付包保留JSON用于复核。


## 完整性

hashes.sha256覆盖第二轮证据文件，不包含自身。格式化镜像与原始响应SHA分开；原始首轮证据未覆盖修改。没有生产凭据或真实客户个人地址写入。

## 本轮受限检查记录

浏览器最初Page.goto因ERR_CERT_AUTHORITY_INVALID失败。CA信任库持久变更被自动审批拒绝（扩大TLS信任边界），用户选择不授权。之后没有绕过证书或运行新browser/Lighthouse。interaction_probe.py仅py_compile语法检查，无结果目录/伪trace。
