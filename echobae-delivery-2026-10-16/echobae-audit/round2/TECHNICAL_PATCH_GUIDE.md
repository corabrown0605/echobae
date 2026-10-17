# 技术实施蓝图（建议代码，不是已取得的第三方源码）

以下是交给开发映射到源码的实现方式。本轮未修改应用、服务器或后台。公开构建产物可定位组件/函数，但不能据此捏造内部Vue文件路径。

## 1. SSR就绪、HTTP状态与缓存准入：SEO-09 / SEO-03 / FE-02 / SEO-04

当前入口 `_nuxt/BFXRDhpD.js` 的主题状态 `tokensReady` 初始false；default layout `_nuxt/CYM8kJOs.js` 仅在就绪时渲染header/main/footer，否则输出shell-loading。今天成功HTML的公开载荷同样是false。公开客户端插件启动异步主题加载，但没有证明服务器使用相同实现或缺少哪一行await。

推荐开发检查链：**请求URL/locale → 活跃主题 → theme tokens/branding/messages → 页面数据 → layout/breadcrumb/SEO → SSR输出 → 缓存**。分别记录服务器实际请求目标、状态、耗时、缓存键和完成顺序，不能拿Cloud代理配置推断源站网络。

建议的Nuxt式伪代码：

```ts
// 建议新增/调整SSR bootstrap；名字和文件位置由开发映射。
export default defineNuxtPlugin({
  name: 'storefront-bootstrap',
  async setup() {
    const context = resolveStoreContextFromRequest(); // 不用window
    const config = await loadRequiredStoreConfig(context);
    applySerializableRequestScopedState(config);
    // page/layout仅在必需状态完成后SSR；不要跨用户复用请求态。
  }
});

// 建议商品路由处理方式；不是现有文件的原文。
const { data, error } = await useAsyncData(key, loadPublishedProduct);
if (error.value?.statusCode === 404 || (!error.value && !data.value)) {
  throw createError({ statusCode: 404, statusMessage: 'Product not found' });
}
if (error.value) {
  // 上游失败不能假报商品不存在；根据实际错误返回503并no-store。
  throw createError({ statusCode: 503, statusMessage: 'Temporarily unavailable' });
}
```

如果运营允许默认主题降级，可用安全默认样式渲染主要正文/SEO，同时清楚禁用无法确认的交易功能；不要隐藏整个main。确实无法提供页面时返回正确错误状态并禁止缓存，不能把HTTP200加载壳当“成功SSR”。

页面缓存键至少按真实站点、locale、主题/发布版本和路由区分；不缓存未准备完成/空商品/错误响应。必要时按受影响键清理旧响应，由开发在获准发布时操作；本次未清缓存。修复后分别测试MISS首次和HIT后续，均必须包含业务内容。

面包屑共享store由子页面写入而父布局读取：SSR已输出父层后不能靠客户端更新使初始H1正确。优选页面H1由页面拥有，面包屑只用nav和普通文本；或在父布局开始渲染前准备完整标题。不能用屏蔽hydration日志或全页ClientOnly代替修复。

## 2. 比较价/实付价的数据契约：CART-01

当前 `CartV2`：B63DM7Lk.js:635；`CheckoutV2`：B7-ND3fn.js:2158。两者确有 `Math.round(unit_price * 1.2 * 100) / 100`。PDP来自真实`compare_at_price`，所以加AI后1689.98/1800在车里变1689.98/2027.98。

**最小方案**：移除计算出的划线价和Saved；实付金额、小计仍使用服务器返回。**完整方案**：服务端cart和quote提供真实比较价及明确适用配置，PDP/车/结账共同格式化。示例契约：

```ts
interface CartLinePrice {
  currency: string;
  unitPriceMinor: number;       // 必须来自服务器重新计算
  compareAtMinor: number|null;  // 真实原价；缺失不虚构
  quantity: number;
  lineTotalMinor: number;
}
const showCompare = line.compareAtMinor !== null &&
                    line.compareAtMinor > line.unitPriceMinor;
```

用整数最小货币单位或准确Decimal处理金额；不能把客户端传来的价格当可信订单价。附加配置价格、比较价、优惠基数、税费/运费分开计算。实际服务端字段/币种精度需开发确认，不能只在页面做减法蒙混。

## 3. Title职责边界：SEO-05

SKU公开`seo.meta_title`是已带品牌的成品，例如“159cm Lifelike Silicone Sex Doll Lydia | Echobae”。当前入口 `up().formatPageTitle`又无条件追加站点名。这里定位到的是具体函数，不是凭空认定Vue全局titleTemplate。

建议明确两种输入：

```ts
function resolveTitle({ seoTitle, contentTitle, brand, separator, homeTitle, isHome }) {
  if (isHome && homeTitle?.trim()) return homeTitle.trim();
  if (seoTitle?.trim()) return seoTitle.trim(); // 约定：后台完整SEO标题
  return [contentTitle?.trim(), brand?.trim()].filter(Boolean).join(separator || ' | ');
}
```

另一方案是后台SEO字段都不含品牌、由前端统一拼接，但需要批量规范历史字段。不要把商品正文/品牌词全局正则删除。发布前检查全部当前有效页面，不盲改首页已合理标题。

## 4. Nuxt Image候选/尺寸语法：IMG-01

当前链：PDP `DL_6UJog.js` → NuxtImg provider `BK9qvGFY.js`；ProductImage `C6D29uTs.js`同样使用它。

- provider是ipx，域名只含127.0.0.1/localhost/172.17.0.1，**没有echobae.com**。绝对同源媒体地址走域名检查直接返回原URL，因此不同w候选仍相同。
- 该版本sizes解析器将字符串按空白/逗号分割、按冒号取断点键。`(max-width: 768px) 100vw, 720px`不是这个组件所需输入语法，最终输出固定720px。

可选方案：同源URL在组件入口转成相对`/api/v1/media/...`，或将精确公共媒体域名加入图片模块白名单（不是扩大Cloud网络权限），或用预生成CDN候选。内部媒体origin只作服务端取图，不能直接给浏览器私网地址。

```vue
<!-- 建议，具体支持语法需按所安装Nuxt Image版本核对和验证生成结果 -->
<NuxtImg :src="publicOrSameOriginMediaUrl"
         :width="media.actualWidth" :height="media.actualHeight"
         sizes="100vw md:720px"
         quality="80" format="webp"
         loading="eager" fetchpriority="high" />
```

明确组件输入与最终HTML `<img sizes="...">`语法不是同一层。复检必须下载候选核对真实宽度，不能仅看srcset字符串。

## 5. 构图、占位与新版adaptive：IMG-02 / PERF-04

主图4:5容器可以保留，在`.pdp-gallery__image`使用contain+统一背景，让2:3全身照完整显示；这样不会让整张页面突然变高。若改2:3舞台，商品卡片/详情高度与CTA位置需一起回归。缩略图和特写可以保留cover，不能全站盲改。

Banner建议保留当前横图比例：

```css
/* 建议规则，需开发纳入实际scope/主题断点 */
.ecom-ad-carousel-v1__media { aspect-ratio: 1672 / 941; }
.ecom-ad-carousel-v1__media img { width:100%; height:100%; object-fit:contain; }
.pdp-gallery__main { aspect-ratio:4 / 5; background:#f3f4f6; }
.pdp-gallery__image { width:100%; height:100%; object-fit:contain; }
```

图片同时输出真实width/height属性。当前ProductImage已新增`adaptive`：初始1:1，onload读取natural尺寸再更改比例。**存在该功能不等于已经解决裁剪，也不等于无CLS**；调用方是否启用未在本轮渲染验证。若需自适应，比例必须来自媒体元数据并提前序列化，别在图片加载后才改变布局。不能把受srcset密度修正的naturalWidth直接当上传文件的物理宽度。

## 6. Canonical/分页/发布过滤：SEO-06 / SEO-11 / SEO-02

建立可测试策略表：正式商品/分类/文章用自规范HTTPS URL；有独立意图的筛选可建正式落地页；sort/tracking等真正重复内容去规范参数；搜索/低价值筛选保留可读取的noindex；page=2不同商品不是第一页复制，不全部canonical到第一页。

分页使用真正NuxtLink/a href，保留按钮视觉与客户端增强：

```vue
<NuxtLink :to="buildPageUrl(page + 1)">Next</NuxtLink>
```

状态由URL query解析，直接访问/刷新/back-forward显示同一页。首轮已经证实URL会改变，问题不是“缺URL”，而是控件只用button与链接图发现不足。

Sitemap只从当前正式发布清单生成，不能照搬历史228（其中许多测试已退休）。当前72英文SKU+有效内容页规模用urlset即可；需要多语言/分片才使用非空索引。server源文件、robots的开关关联和生成器内部查询未取得，开发需提供对应实现。

## 7. 可访问性、条款与字典

- AgeGate：初始焦点、Tab/Shift+Tab循环、背景inert、确认后restore focus；保持年龄确认/离开入口，不能加绕过门禁关闭。
- Checkout terms：把纯span文案中的Terms变成真实可读链接；前端checkbox guard已存在，后端接受版本/时间在测试环境验收。
- Footer：当前公共英文字典缺poweredBy，而组件调用该键。补键并保证root/en等发布locale基础字典正确合并，不能仅屏蔽缺键日志。
- FAQ/Schema：问答与结构化数据用同一真实内容源，删除空FAQPage，不为了普通电商FAQ富结果堆数据。
- Payment：配置请求失败的公开代码仍回退到Stripe/PayPal可用；目前API返回available=true，但这不证明真实支付成功。建议失败时显示待加载/不可用而非猜可用，故障注入只在沙盒。
