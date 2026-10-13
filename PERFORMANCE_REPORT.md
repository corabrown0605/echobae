# 性能报告

本次27次有效Lighthouse运行：4类代表页×桌面/移动×3次，另首页确认成年后移动3次。此前单次报告保留在evidence/previous，未混入中位数。所有表格来自实际JSON，按每项指标单独取中位数。

## 方法与限制

Chromium154.0.8037.57；Playwright1.62.0；Lighthouse13.5.0。默认mobile为412×823/DPR1.75，simulate限速；desktop使用--preset=desktop。具体CPU/网络参数、UTC时间保存在[evidence/performance-summary.json](evidence/performance-summary.json)，用户当地时间为UTC+8。标准组每次新浏览器、默认storage reset；已确认组使用正常年龄确认按钮后共享浏览器存储并--disable-storage-reset（因此缓存也保留）。

Lighthouse顺序运行，但部分标准组与低并发爬取/浏览采集重叠；不能视为完全无干扰基准，真实代理、服务端缓存和机器调度均影响波动。第三方字体/GTM请求失败，不能推断其公网故障；未关闭TLS校验。

无CrUX/GSC/生产RUM，因此没有真实用户p75 LCP、INP、CLS。TBT不是INP；CLS是加载阶段观测，首页桌面约0.457，其他较低值不能排除后续实际交互位移。禁止把单次数据称为CWV通过。

## 重复测试中位数

|页面/组|次数|Performance|Accessibility|Best Practices|SEO|FCP(s)|LCP(s)|TBT(ms)|CLS|Speed Index(s)|TTFB(ms)|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|article-desktop|3|71|100|96|69|1.02|1.04|387|0.006|3.24|263|
|article-mobile|3|41|100|96|69|3.37|4.94|1703|0.000|8.67|267|
|collection-desktop|3|63|95|96|69|0.80|1.87|451|0.006|3.61|398|
|collection-mobile|3|37|98|96|69|3.23|5.61|1916|0.000|9.34|260|
|home-accepted-mobile|3|72|91|96|69|1.31|1.81|2108|0.000|2.19|261|
|home-desktop|3|48|95|96|69|0.98|1.61|427|0.457|2.96|263|
|home-mobile|3|52|95|96|69|4.28|5.59|472|0.000|7.91|265|
|product-desktop|3|79|95|96|69|1.07|1.43|202|0.027|3.68|275|
|product-mobile|3|51|95|96|69|4.19|5.87|434|0.035|8.81|373|

## 首页原始LCP约5.6秒的构成

之前保存的单次报告LCP5.6s，LCP节点是`.ecom-ad-carousel-v1__media > img`，并非年龄弹窗文本；原始分段TTFB261ms、发现延迟15ms、图片下载982ms、元素渲染延迟1169ms。**这些是实际trace分段，不可直接与模拟限速的5.6秒相加比对。**当前home-mobile-1同类节点：TTFB282ms、发现18ms、下载1006ms、渲染1146ms，模拟LCP5.2s。

图片能在初始HTML发现且eager，因此“LCP图片懒加载”不是已确认根因。首图未设fetchpriority=high；轮播变换、遮罩/初始化和脚本任务与较长渲染延迟相关，但需要开发trace确定因果，不应简单删除年龄验证。

首次mobile Performance中位52，LCP 5.59s；已确认+保留存储中位72，LCP 1.81s，TBT仍2108ms。该对照同时改变存储/缓存，**不能把差值当成年龄弹窗造成的准确开销**。

## 可定位瓶颈与执行顺序

1. 首屏加载/轮播/SSR稳定性：优先固定首屏可见图和加载流程，再优化模块。LCP trace中节点因轮播移动可在采集时位于屏外，需开发按时间线检查轮播初始状态。
2. 主线程：home-mobile-1 Script Evaluation约3.15s，bootup归因包括document初始化和`_nuxt/-OMa2-7R.js`；公开文件名是构建产物，不代表已掌握源代码模块。检查长任务、builder初始化和路由预取。
3. 公共JS：`DNfd1SfM.js` Lighthouse传输243593B，首次加载未使用估算86240B；收益须复测，不保证固定提升百分比。
4. CSS：`blocks-built.css`传输26251B、未使用估算22227B；Footer CSS约10KB及其他组件进入阻塞链。按页面block拆分，避免误删运行时类。
5. 图片：移动Banner1672×941用于390px宽，无srcset；商品伪多宽候选，见IMAGE_AUDIT.csv。
6. 第三方：字体fallback重复失败，GTM失败；另行在允许这些域名的正常网络验证，不将代理错误计作线上源站Bug。

## 缓存、压缩及资源证据

HTML原始字节见URL_INVENTORY/crawl.json，资源传输和解码字节见deep.json；Lighthouse network-requests保留瀑布、protocol和initiator。资源单独GET的压缩头见assets-deep.json，不能仅凭文件后缀推断Brotli。样本57个成功资源GET中12个返回gzip（包括CSS、SVG、部分JS/旧媒体）；哈希_nuxt资源见public,max-age=31536000,immutable；一些媒体和blocks-built.css未见显式Cache-Control，不能据此断言浏览器绝不缓存。没有取得全站Brotli部署证明。首页GET Cache-Control public,max-age=0,must-revalidate，x-ssr-cache HIT；公开观察无法证明CDN供应商或源站拓扑。

实验室复检目标：相同配置冷启动3次中位LCP≤2.5s、TBT≤200ms、CLS≤0.1；真实用户上线后p75 INP≤200ms，需RUM/CrUX独立验证。当前无生产INP结论。

## 每次运行与报告

- 2026-10-13T06:50:24.974Z article-desktop：Performance 71，LCP 1.05s；[article-desktop-1.report.json](evidence/lighthouse/article-desktop-1.report.json)
- 2026-10-13T06:50:45.384Z article-desktop：Performance 70，LCP 1.02s；[article-desktop-2.report.json](evidence/lighthouse/article-desktop-2.report.json)
- 2026-10-13T06:51:04.608Z article-desktop：Performance 73，LCP 1.04s；[article-desktop-3.report.json](evidence/lighthouse/article-desktop-3.report.json)
- 2026-10-13T06:49:26.774Z article-mobile：Performance 39，LCP 5.06s；[article-mobile-1.report.json](evidence/lighthouse/article-mobile-1.report.json)
- 2026-10-13T06:49:46.872Z article-mobile：Performance 41，LCP 4.94s；[article-mobile-2.report.json](evidence/lighthouse/article-mobile-2.report.json)
- 2026-10-13T06:50:05.798Z article-mobile：Performance 42，LCP 4.90s；[article-mobile-3.report.json](evidence/lighthouse/article-mobile-3.report.json)
- 2026-10-13T06:45:58.974Z collection-desktop：Performance 63，LCP 1.87s；[collection-desktop-1.report.json](evidence/lighthouse/collection-desktop-1.report.json)
- 2026-10-13T06:46:21.105Z collection-desktop：Performance 61，LCP 1.85s；[collection-desktop-2.report.json](evidence/lighthouse/collection-desktop-2.report.json)
- 2026-10-13T06:46:43.542Z collection-desktop：Performance 63，LCP 1.92s；[collection-desktop-3.report.json](evidence/lighthouse/collection-desktop-3.report.json)
- 2026-10-13T06:44:52.839Z collection-mobile：Performance 37，LCP 5.61s；[collection-mobile-1.report.json](evidence/lighthouse/collection-mobile-1.report.json)
- 2026-10-13T06:45:15.218Z collection-mobile：Performance 37，LCP 5.48s；[collection-mobile-2.report.json](evidence/lighthouse/collection-mobile-2.report.json)
- 2026-10-13T06:45:36.876Z collection-mobile：Performance 38，LCP 5.64s；[collection-mobile-3.report.json](evidence/lighthouse/collection-mobile-3.report.json)
- 2026-10-13T06:56:11.426Z home-accepted-mobile：Performance 73，LCP 1.81s；[home-accepted-mobile-1.report.json](evidence/lighthouse/home-accepted-mobile-1.report.json)
- 2026-10-13T06:56:31.415Z home-accepted-mobile：Performance 72，LCP 1.27s；[home-accepted-mobile-2.report.json](evidence/lighthouse/home-accepted-mobile-2.report.json)
- 2026-10-13T06:56:50.730Z home-accepted-mobile：Performance 71，LCP 2.11s；[home-accepted-mobile-3.report.json](evidence/lighthouse/home-accepted-mobile-3.report.json)
- 2026-10-13T06:43:46.185Z home-desktop：Performance 48，LCP 1.68s；[home-desktop-1.report.json](evidence/lighthouse/home-desktop-1.report.json)
- 2026-10-13T06:44:07.251Z home-desktop：Performance 57，LCP 1.61s；[home-desktop-2.report.json](evidence/lighthouse/home-desktop-2.report.json)
- 2026-10-13T06:44:30.427Z home-desktop：Performance 44，LCP 1.59s；[home-desktop-3.report.json](evidence/lighthouse/home-desktop-3.report.json)
- 2026-10-13T06:42:42.779Z home-mobile：Performance 59，LCP 5.16s；[home-mobile-1.report.json](evidence/lighthouse/home-mobile-1.report.json)
- 2026-10-13T06:43:03.877Z home-mobile：Performance 52，LCP 5.59s；[home-mobile-2.report.json](evidence/lighthouse/home-mobile-2.report.json)
- 2026-10-13T06:43:25.034Z home-mobile：Performance 38，LCP 7.29s；[home-mobile-3.report.json](evidence/lighthouse/home-mobile-3.report.json)
- 2026-10-13T06:48:17.268Z product-desktop：Performance 79，LCP 1.43s；[product-desktop-1.report.json](evidence/lighthouse/product-desktop-1.report.json)
- 2026-10-13T06:48:40.110Z product-desktop：Performance 83，LCP 1.41s；[product-desktop-2.report.json](evidence/lighthouse/product-desktop-2.report.json)
- 2026-10-13T06:49:01.964Z product-desktop：Performance 70，LCP 1.43s；[product-desktop-3.report.json](evidence/lighthouse/product-desktop-3.report.json)
- 2026-10-13T06:47:06.988Z product-mobile：Performance 36，LCP 5.78s；[product-mobile-1.report.json](evidence/lighthouse/product-mobile-1.report.json)
- 2026-10-13T06:47:31.511Z product-mobile：Performance 51，LCP 6.01s；[product-mobile-2.report.json](evidence/lighthouse/product-mobile-2.report.json)
- 2026-10-13T06:47:54.779Z product-mobile：Performance 51，LCP 5.87s；[product-mobile-3.report.json](evidence/lighthouse/product-mobile-3.report.json)