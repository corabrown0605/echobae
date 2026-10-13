# 原始证据索引

时间均取原始HTTP Date或Lighthouse fetchTime（UTC）；报告用户时间为UTC+8。保留脚本与失败尝试，用于说明修正前后，不把失败尝试当最终结果。

## 主要数据

- [crawl.json](crawl.json)：228URL HTTP/初始HTML/meta/H/Canonical/JSON-LD/链接/图片属性
- [page-text.json](page-text.json)：228页去除script/style的公开文本
- [http-checks.json](http-checks.json)：robots、Sitemap、HTTP/www、随机404、公开API、Googlebot UA请求
- [browser/deep.json](browser/deep.json)：25唯一样本×58视口、DOM/网络/Console/尺寸
- [browser-discovery.json](browser-discovery.json)：分类/列表发现及正文
- [pagination.json](pagination.json)：实际分页商品URL
- [browser/cart-verify.json](browser/cart-verify.json)：稳定等待后的价格、数量、刷新、删除
- [browser/cart-network.json](browser/cart-network.json)：购物流程响应URL与状态，不含凭据
- [browser/checkout-checks.json](browser/checkout-checks.json)：国家选择、优惠码入口和条款缺少链接
- [browser/commerce.json](browser/commerce.json)：正常年龄/选项/搜索/排序流程
- [browser/search-checks.json](browser/search-checks.json)：搜索结果/随机商品200空壳
- [browser/age-keyboard.json](browser/age-keyboard.json)：12次Tab及成年确认刷新
- [product-main-resources.json](product-main-resources.json)：189页主图HEAD或明确跳过
- [assets-deep.json](assets-deep.json)：62个代表资源GET响应、字节与部分固有尺寸
- [private-image-urls.json](private-image-urls.json)：28Demo页面引用内部HTTP图片地址清单
- [performance-summary.json](performance-summary.json)：27次Lighthouse实际分数/指标/时间/配置
- [issues.json](issues.json)：37项结构化问题与受影响URL
- [official-reference-access.json](official-reference-access.json)：官方参考文档请求代理拒绝的事实

## 最终代表截图（等待初始化及正常按钮流程后）

|页面|视口|截图|
|---|---|---|
|https://echobae.com/|desktop {'width': 1440, 'height': 900}|[desktop-8a5edab282-settled.png](browser/desktop-8a5edab282-settled.png)|
|https://echobae.com/products|desktop {'width': 1440, 'height': 900}|[desktop-d66ca189b1-settled.png](browser/desktop-d66ca189b1-settled.png)|
|https://echobae.com/collections/new-arrival|desktop {'width': 1440, 'height': 900}|[desktop-8f6d729883-settled.png](browser/desktop-8f6d729883-settled.png)|
|https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia|desktop {'width': 1440, 'height': 900}|[desktop-5b0c2ba7b3-settled.png](browser/desktop-5b0c2ba7b3-settled.png)|
|https://echobae.com/blog/tpe-vs-silicone-sex-doll|desktop {'width': 1440, 'height': 900}|[desktop-85ecc6aca5-settled.png](browser/desktop-85ecc6aca5-settled.png)|
|https://echobae.com/customer-reviews|desktop {'width': 1440, 'height': 900}|[desktop-158470beca-settled.png](browser/desktop-158470beca-settled.png)|
|https://echobae.com/|mobile {'width': 390, 'height': 844}|[mobile-8a5edab282-settled.png](browser/mobile-8a5edab282-settled.png)|
|https://echobae.com/products|mobile {'width': 390, 'height': 844}|[mobile-d66ca189b1-settled.png](browser/mobile-d66ca189b1-settled.png)|
|https://echobae.com/collections/new-arrival|mobile {'width': 390, 'height': 844}|[mobile-8f6d729883-settled.png](browser/mobile-8f6d729883-settled.png)|
|https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia|mobile {'width': 390, 'height': 844}|[mobile-5b0c2ba7b3-settled.png](browser/mobile-5b0c2ba7b3-settled.png)|
|https://echobae.com/blog/tpe-vs-silicone-sex-doll|mobile {'width': 390, 'height': 844}|[mobile-85ecc6aca5-settled.png](browser/mobile-85ecc6aca5-settled.png)|
|https://echobae.com/customer-reviews|mobile {'width': 390, 'height': 844}|[mobile-158470beca-settled.png](browser/mobile-158470beca-settled.png)|

## 全部深度样本截图

下列初始截图可能仍处于加载或弹窗阶段；最终代表图以上表为准。

- https://echobae.com/ desktop：[desktop-8a5edab282.png](browser/desktop-8a5edab282.png)
- https://echobae.com/products desktop：[desktop-d66ca189b1.png](browser/desktop-d66ca189b1.png)
- https://echobae.com/collections/new-arrival desktop：[desktop-8f6d729883.png](browser/desktop-8f6d729883.png)
- https://echobae.com/collections/best-value desktop：[desktop-19784c4cf9.png](browser/desktop-19784c4cf9.png)
- https://echobae.com/collections/best-sellers desktop：[desktop-27a169a0db.png](browser/desktop-27a169a0db.png)
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia desktop：[desktop-5b0c2ba7b3.png](browser/desktop-5b0c2ba7b3.png)
- https://echobae.com/p/149cm-white-hair-silicone-doll-siwei desktop：[desktop-ce32aba957.png](browser/desktop-ce32aba957.png)
- https://echobae.com/p/170cm-realistic-silicone-sex-doll-jiachen desktop：[desktop-2532c46d87.png](browser/desktop-2532c46d87.png)
- https://echobae.com/p/demo-sh-030 desktop：[desktop-a04bae3fc5.png](browser/desktop-a04bae3fc5.png)
- https://echobae.com/blog desktop：[desktop-8caafe4386.png](browser/desktop-8caafe4386.png)
- https://echobae.com/blog/tpe-vs-silicone-sex-doll desktop：[desktop-85ecc6aca5.png](browser/desktop-85ecc6aca5.png)
- https://echobae.com/blog/what-are-the-most-realistic-sex-dolls desktop：[desktop-d0590e3aa7.png](browser/desktop-d0590e3aa7.png)
- https://echobae.com/blog/silicone-sex-doll-buying-guide desktop：[desktop-7fdca57034.png](browser/desktop-7fdca57034.png)
- https://echobae.com/custom-made desktop：[desktop-223ec7d37c.png](browser/desktop-223ec7d37c.png)
- https://echobae.com/contact-us desktop：[desktop-0353b78845.png](browser/desktop-0353b78845.png)
- https://echobae.com/help desktop：[desktop-1d63d79177.png](browser/desktop-1d63d79177.png)
- https://echobae.com/customer-reviews desktop：[desktop-158470beca.png](browser/desktop-158470beca.png)
- https://echobae.com/shipping-policy desktop：[desktop-643cc6ba47.png](browser/desktop-643cc6ba47.png)
- https://echobae.com/return-refund-policy desktop：[desktop-27c9cd765f.png](browser/desktop-27c9cd765f.png)
- https://echobae.com/privacy-policy desktop：[desktop-81e51d8c79.png](browser/desktop-81e51d8c79.png)
- https://echobae.com/payment-method desktop：[desktop-2a08dddde7.png](browser/desktop-2a08dddde7.png)
- https://echobae.com/faq desktop：[desktop-1965ee0fd5.png](browser/desktop-1965ee0fd5.png)
- https://echobae.com/about-us desktop：[desktop-57424c1fb2.png](browser/desktop-57424c1fb2.png)
- https://echobae.com/sex-doll-care desktop：[desktop-f16133f95d.png](browser/desktop-f16133f95d.png)
- https://echobae.com/cart desktop：[desktop-edf54f1e1e.png](browser/desktop-edf54f1e1e.png)
- https://echobae.com/ mobile：[mobile-8a5edab282.png](browser/mobile-8a5edab282.png)
- https://echobae.com/products mobile：[mobile-d66ca189b1.png](browser/mobile-d66ca189b1.png)
- https://echobae.com/collections/new-arrival mobile：[mobile-8f6d729883.png](browser/mobile-8f6d729883.png)
- https://echobae.com/collections/best-value mobile：[mobile-19784c4cf9.png](browser/mobile-19784c4cf9.png)
- https://echobae.com/collections/best-sellers mobile：[mobile-27a169a0db.png](browser/mobile-27a169a0db.png)
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia mobile：[mobile-5b0c2ba7b3.png](browser/mobile-5b0c2ba7b3.png)
- https://echobae.com/p/149cm-white-hair-silicone-doll-siwei mobile：[mobile-ce32aba957.png](browser/mobile-ce32aba957.png)
- https://echobae.com/p/170cm-realistic-silicone-sex-doll-jiachen mobile：[mobile-2532c46d87.png](browser/mobile-2532c46d87.png)
- https://echobae.com/p/demo-sh-030 mobile：[mobile-a04bae3fc5.png](browser/mobile-a04bae3fc5.png)
- https://echobae.com/blog mobile：[mobile-8caafe4386.png](browser/mobile-8caafe4386.png)
- https://echobae.com/blog/tpe-vs-silicone-sex-doll mobile：[mobile-85ecc6aca5.png](browser/mobile-85ecc6aca5.png)
- https://echobae.com/blog/what-are-the-most-realistic-sex-dolls mobile：[mobile-d0590e3aa7.png](browser/mobile-d0590e3aa7.png)
- https://echobae.com/blog/silicone-sex-doll-buying-guide mobile：[mobile-7fdca57034.png](browser/mobile-7fdca57034.png)
- https://echobae.com/custom-made mobile：[mobile-223ec7d37c.png](browser/mobile-223ec7d37c.png)
- https://echobae.com/contact-us mobile：[mobile-0353b78845.png](browser/mobile-0353b78845.png)
- https://echobae.com/help mobile：[mobile-1d63d79177.png](browser/mobile-1d63d79177.png)
- https://echobae.com/customer-reviews mobile：[mobile-158470beca.png](browser/mobile-158470beca.png)
- https://echobae.com/shipping-policy mobile：[mobile-643cc6ba47.png](browser/mobile-643cc6ba47.png)
- https://echobae.com/return-refund-policy mobile：[mobile-27c9cd765f.png](browser/mobile-27c9cd765f.png)
- https://echobae.com/privacy-policy mobile：[mobile-81e51d8c79.png](browser/mobile-81e51d8c79.png)
- https://echobae.com/payment-method mobile：[mobile-2a08dddde7.png](browser/mobile-2a08dddde7.png)
- https://echobae.com/faq mobile：[mobile-1965ee0fd5.png](browser/mobile-1965ee0fd5.png)
- https://echobae.com/about-us mobile：[mobile-57424c1fb2.png](browser/mobile-57424c1fb2.png)
- https://echobae.com/sex-doll-care mobile：[mobile-f16133f95d.png](browser/mobile-f16133f95d.png)
- https://echobae.com/cart mobile：[mobile-edf54f1e1e.png](browser/mobile-edf54f1e1e.png)
- https://echobae.com/ tablet：[tablet-8a5edab282.png](browser/tablet-8a5edab282.png)
- https://echobae.com/products tablet：[tablet-d66ca189b1.png](browser/tablet-d66ca189b1.png)
- https://echobae.com/collections/new-arrival tablet：[tablet-8f6d729883.png](browser/tablet-8f6d729883.png)
- https://echobae.com/collections/best-value tablet：[tablet-19784c4cf9.png](browser/tablet-19784c4cf9.png)
- https://echobae.com/collections/best-sellers tablet：[tablet-27a169a0db.png](browser/tablet-27a169a0db.png)
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia tablet：[tablet-5b0c2ba7b3.png](browser/tablet-5b0c2ba7b3.png)
- https://echobae.com/p/149cm-white-hair-silicone-doll-siwei tablet：[tablet-ce32aba957.png](browser/tablet-ce32aba957.png)
- https://echobae.com/p/170cm-realistic-silicone-sex-doll-jiachen tablet：[tablet-2532c46d87.png](browser/tablet-2532c46d87.png)

## Lighthouse原始报告

标准24次与已确认/保留存储3次分组，不混用缓存条件。HTML为可视报告，JSON为计算依据。

- [article-desktop-1.report.json](lighthouse/article-desktop-1.report.json) · [HTML](lighthouse/article-desktop-1.report.html)
- [article-desktop-2.report.json](lighthouse/article-desktop-2.report.json) · [HTML](lighthouse/article-desktop-2.report.html)
- [article-desktop-3.report.json](lighthouse/article-desktop-3.report.json) · [HTML](lighthouse/article-desktop-3.report.html)
- [article-mobile-1.report.json](lighthouse/article-mobile-1.report.json) · [HTML](lighthouse/article-mobile-1.report.html)
- [article-mobile-2.report.json](lighthouse/article-mobile-2.report.json) · [HTML](lighthouse/article-mobile-2.report.html)
- [article-mobile-3.report.json](lighthouse/article-mobile-3.report.json) · [HTML](lighthouse/article-mobile-3.report.html)
- [collection-desktop-1.report.json](lighthouse/collection-desktop-1.report.json) · [HTML](lighthouse/collection-desktop-1.report.html)
- [collection-desktop-2.report.json](lighthouse/collection-desktop-2.report.json) · [HTML](lighthouse/collection-desktop-2.report.html)
- [collection-desktop-3.report.json](lighthouse/collection-desktop-3.report.json) · [HTML](lighthouse/collection-desktop-3.report.html)
- [collection-mobile-1.report.json](lighthouse/collection-mobile-1.report.json) · [HTML](lighthouse/collection-mobile-1.report.html)
- [collection-mobile-2.report.json](lighthouse/collection-mobile-2.report.json) · [HTML](lighthouse/collection-mobile-2.report.html)
- [collection-mobile-3.report.json](lighthouse/collection-mobile-3.report.json) · [HTML](lighthouse/collection-mobile-3.report.html)
- [home-accepted-mobile-1.report.json](lighthouse/home-accepted-mobile-1.report.json) · [HTML](lighthouse/home-accepted-mobile-1.report.html)
- [home-accepted-mobile-2.report.json](lighthouse/home-accepted-mobile-2.report.json) · [HTML](lighthouse/home-accepted-mobile-2.report.html)
- [home-accepted-mobile-3.report.json](lighthouse/home-accepted-mobile-3.report.json) · [HTML](lighthouse/home-accepted-mobile-3.report.html)
- [home-desktop-1.report.json](lighthouse/home-desktop-1.report.json) · [HTML](lighthouse/home-desktop-1.report.html)
- [home-desktop-2.report.json](lighthouse/home-desktop-2.report.json) · [HTML](lighthouse/home-desktop-2.report.html)
- [home-desktop-3.report.json](lighthouse/home-desktop-3.report.json) · [HTML](lighthouse/home-desktop-3.report.html)
- [home-mobile-1.report.json](lighthouse/home-mobile-1.report.json) · [HTML](lighthouse/home-mobile-1.report.html)
- [home-mobile-2.report.json](lighthouse/home-mobile-2.report.json) · [HTML](lighthouse/home-mobile-2.report.html)
- [home-mobile-3.report.json](lighthouse/home-mobile-3.report.json) · [HTML](lighthouse/home-mobile-3.report.html)
- [product-desktop-1.report.json](lighthouse/product-desktop-1.report.json) · [HTML](lighthouse/product-desktop-1.report.html)
- [product-desktop-2.report.json](lighthouse/product-desktop-2.report.json) · [HTML](lighthouse/product-desktop-2.report.html)
- [product-desktop-3.report.json](lighthouse/product-desktop-3.report.json) · [HTML](lighthouse/product-desktop-3.report.html)
- [product-mobile-1.report.json](lighthouse/product-mobile-1.report.json) · [HTML](lighthouse/product-mobile-1.report.html)
- [product-mobile-2.report.json](lighthouse/product-mobile-2.report.json) · [HTML](lighthouse/product-mobile-2.report.html)
- [product-mobile-3.report.json](lighthouse/product-mobile-3.report.json) · [HTML](lighthouse/product-mobile-3.report.html)

## HTML、脚本与历史证据

- HTML路径按URL哈希命名，映射见crawl.json或根目录URL_INVENTORY.csv。
- public-js/只包含公开页面加载的构建产物；仅用于调查已观察runtime-blocks与年龄记忆逻辑，不是后台源代码。
- previous/保留先前任务的首页截图/HTML/单次Lighthouse，不计入本次27次结果。
- scripts/位于仓库根目录，所有审计逻辑可复查。无用户凭据或真实个人地址写入。
- hashes.sha256覆盖证据文件（不含自身），可核对原始证据是否变更。
