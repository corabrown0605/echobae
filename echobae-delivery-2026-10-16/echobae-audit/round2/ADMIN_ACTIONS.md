# 运营修改与验收清单

所有线上改动由用户另行安排并批准，本次未修改。后台菜单与内部源码未取得，不编造路径。以下工作量是缺少源码条件下的粗估人日，不是报价。当前公开部署已有变化，先验收再改。

## 先收集事实再编辑

先确认当前72正式英文SKU白名单、库存/生产时间、AI默认与选配含义、实际配送/费用/税费、真实付款/退款取消规则、法律主体/服务器国家和评论来源。没有事实不把占位替换为新编造承诺。后台只能找到实际存在的商品/内容/SEO/活动/导航字段；菜单没有访问证据。

## 可用的具体文案草案（仍须业务确认）

- 首页配送FAQ：`Delivery time depends on your destination and shipping method. See our Shipping Policy for current estimates. Production time is additional.`
- 没有统一最低运费时：`Shipping costs are shown at checkout before payment.`；不要保留`$ *`。
- 定制FAQ取消/退款：`Please review our Return & Refund Policy before ordering. Contact support@echobae.com if you need to request a change or cancellation.`；不要使用30天退货Demo。
- 定制FAQ参考材料：要求由生产方提供实际格式/尺寸清单，不能自行发明格式；未确定可暂隐藏该问题。
- QY029最终SEO标题：`159cm Lifelike Silicone Sex Doll Lydia | Echobae`。需要先统一“后台成品标题还是不带品牌内容”的字段约定。
- Footer缺键：在实际发布语言字典补`footer.poweredBy`对应真实显示文案；英文可以沿已显示的`Powered by wiipoo`，不误改其他品牌字段。
- 详情图Alt：`Silicone doll body sizes and construction details`；`Close-up views of doll faces, hands and posing`。图中多型号不要描述为单个SKU。

## 按ID分项

### SEO-01 · P0 · 全站禁止抓取与索引（上线前可能有意设置）

状态：上线条件（保留预发布限制）

页面：https://echobae.com/、https://echobae.com/products、https://echobae.com/collections/new-arrival、https://echobae.com/collections/best-value；完整URL见CSV，退休历史URL需与当前目录交叉

证据：当前robots仍Disallow:/；SSR载荷discourage_search_engines=true；当前SEO助手先判断该全局标志，再考虑单页robots。

未确定：robots和Sitemap的服务端生成逻辑未见；不能证明其都由同一后台开关控制。当前加载壳还使业务meta根本未输出。

修改位置：当前入口BFXRDhpD.js的主题/SEO配置，4FfVxrIF.js的robots计算；服务端robots端点。

实施/选择：A正式发布窗口解除全局开关、同步公开页meta与robots；B仅暂时局部白名单开放，维护成本更高。不要只改商品meta index而保留全局锁。

成本：0.5–1人日（估算）

验收：先修SEO-09；公开HTML完整且无noindex，robots允许页面/必需资源；交易/搜索/账户按用途排除。GSC实时测试与实际索引分别验证。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### CAT-01 · P1 · 主商品列表公开展示 Demo、测试及复制商品

状态：部分改善，待前台验收

页面：https://echobae.com/products、https://echobae.com/pages/help、https://echobae.com/p/demo-sh-020、https://echobae.com/p/demo-sh-030；完整URL见CSV，退休历史URL需与当前目录交叉

证据：当前英文公开列表API四页合计72个唯一商品，未发现demo/e2e/copy/test命名；demo-sh-030、e2e-ship-heavy、代表复制SKU的API均404。首轮已确认这些SKU公开为active。

未确定：后台如何下架/删除、其他语言与缓存推荐是否同步未知；当前浏览器页面尚未复测。

修改位置：后台商品发布/语言可见性；公开catalog/products服务和各推荐数据源。无后台菜单证据。

实施/选择：A保留现有清理并做72 SKU白名单验收，最低风险；B对残余旧URL返回404/410，只有真正迁移商品一对一301。不要根据旧清单批量删除已清理内容。

成本：复检0.5人日，残余修复另估

验收：当前72 SKU浏览器分页、搜索、Help推荐均无Demo；旧Demo HTML状态与API404一致；其他语言如要发布再验。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### SEO-02 · P1 · sitemap.xml为空索引

状态：待修改

页面：https://echobae.com/sitemap.xml

证据：今天sitemap.xml仍为空sitemapindex；公开SEO载荷product limit5000，当前72商品远低于限制，不能用数量上限解释空表。

未确定：是有意预发布禁用、发布过滤还是路由生成失败未知；未访问服务器Sitemap源码。

修改位置：Sitemap服务端查询/输出、正式内容发布清单、canonical策略。

实施/选择：A单urlset用于当前规模，简单且够用；B索引+按语言/类型分片，适合扩展。以已发布、200、规范、允许索引页面为数据源。

成本：0.5–1人日（估算）

验收：不要把历史228全放入；只纳入当前正式72 SKU和有效分类/文章/内容页；排除退休测试、搜索、交易、低价值参数；lastmod只反映真实内容更新。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### POL-01 · P1 · 隐私政策保留服务器国家占位符

状态：历史已验证，现状待复检

页面：https://echobae.com/privacy-policy

证据：首轮公开正文两处服务器国家占位，属于已输出内容未完成，不是根据行业模板推测。

未确定：真实服务器国家、法律实体、第三方处理与数据保留承诺未获后台证据；本轮未复测正文。

修改位置：运营政策正文编辑；开发/供应商提供真实数据处理信息。

实施/选择：A核实事实后完整修订；B无法确认的承诺先改为准确可验证说明，不能猜国家或法律义务。

成本：0.5–1人日（估算）

验收：两处占位移除；主体、存储/跨境和联系信息经负责人确认；保存政策版本和更新时间。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### POL-02 · P1 · 配送时效在首页和政策中矛盾

状态：历史已验证，现状待复检

页面：https://echobae.com/、https://echobae.com/shipping-policy

证据：首轮首页3–7天与物流页10–14工作日/30–35天并存；同一业务信息的输出不一致。

未确定：具体真实时效、生产周期和不同目的地是否确实不同未知。

修改位置：首页FAQ内容、商品FAQ、物流政策与结账配送率文案。

实施/选择：A用统一配送事实表生成各页面；B先把首页改成到物流政策的清楚指引，减少多处独立维护。

成本：0.5–1人日（估算）

验收：分别验证Standard/Express+生产期+目的地；FAQ Schema同步内容，不只改可见文本。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### POL-03 · P1 · 退款政策含缺失运费金额和未核实支付渠道

状态：历史已验证，现状待复检

页面：https://echobae.com/return-refund-policy

证据：首轮退款正文确有$ *金额占位及支票/fax等渠道；本轮付款可用性API仅确认Stripe/PayPal及钱包布尔状态。

未确定：线下付款、真实最低运费、法定权利、瑕疵处理未知，不能以API没有支票就认定线下付款绝不存在。

修改位置：退款/取消/付款政策正文；商务/法务事实核验。

实施/选择：A仅列实际线上渠道；B如保留线下渠道，明确独立授权流程和联系路径。无统一最低运费时改成checkout显示费率，不编造金额。

成本：0.5–1人日（估算）

验收：$ *清除；线上/线下渠道与已批准业务一致；损坏/错发/取消流程明确。与CONT-06的30天退货Demo同步修正。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### CART-01 · P1 · 购物车及结账划线价与商品页不一致

状态：公开实现已确认，待修改

页面：https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia、https://echobae.com/cart、https://echobae.com/checkout

证据：当前入口映射CartV2 B63DM7Lk.js:635和CheckoutV2 B7-ND3fn.js:2158均用单价×1.2算比较价；PDP用API compare_at_price1800。不是仅仅猜价格映射错误。

未确定：服务端cart/quote DTO是否有真实compare_at_price字段仍需开发确认；本轮未重新加车。

修改位置：CartV2的K()与CheckoutV2的ee()；PDP价格模型；cart/quote响应序列化字段。

实施/选择：A立即删掉派生划线价和Saved，最小安全修复；B数据契约传真实比较价（SKU+配置），三页统一；绝不拿售价固定加20%制造折扣。

成本：1人日（估算）

验收：Lydia基础1609.99/真实1800；AI1689.98，2件3379.96，三页相同真实原价或统一不显示；运费/优惠后按真实基准计算，后台重算实付金额。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### POL-04 · P1 · 结账要求同意条款，但没有可访问的条款链接

状态：公开实现已确认，待修改

页面：https://echobae.com/checkout

证据：当前CheckoutV2条款是纯span翻译文案，无a[href]；Ce()先检查同意checkbox后调用提交。缺的是可阅读链接，不是已经证明同意校验失效。

未确定：Terms正式URL和后台是否可设置未知；服务端是否记录接受版本/时间未知。

修改位置：CheckoutV2条款label/span；公开条款CMS页、Footer导航；订单协议字段。

实施/选择：A新增真正的Terms链接（新页或保留会话打开）；B把政策中真实完整条款公开为独立可访问URL。不能把猜测404路径当唯一条款地址。

成本：0.5–1人日（估算）

验收：可打开完整Terms且返回不丢车；不勾选拒绝提交；订单接受记录只在测试环境验证。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### IMG-01 · P1 · 商品图片srcset多候选指向同一个文件

状态：当前配置链已确认，待修改

页面：https://echobae.com/collections/new-arrival、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia、https://echobae.com/p/149cm-white-hair-silicone-doll-siwei

证据：当前BK9qvGFY.js:290 image.domains不含echobae.com，绝对媒体URL会在域名检查后原样返回；PDP和ProductImage传入普通HTML媒体sizes，当前解析器按断点键分割，退化为固定尺寸。

未确定：是否存在运行时provider覆盖、服务端IPX可达性和新页面最终currentSrc需复检。不能把优化服务全局不可用当确定原因。

修改位置：Nuxt Image配置domains/alias；PdpGalleryV2 sizes:1911；ProductImage C6D29uTs.js；NuxtImg getSizes/域名校验。

实施/选择：A同源媒体标准化为相对/api/v1/media并使用已支持的IPX；B加入精确公共媒体域名白名单；C生成预制尺寸CDN文件。配合Nuxt sizes="100vw md:720px"等符合此版本语法的表达式，实际输出应按布局验。

成本：1–2人日（估算）

验收：候选URL不同、物理像素匹配400w/800w等；断点HTML sizes有效；缩略图不下载1707px原图；不直接请求内部IP。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### CONT-01 · P1 · 五星Reviews营销文字与0条评论展示不一致

状态：历史矛盾，来源待运营核验

页面：https://echobae.com/、https://echobae.com/customer-reviews、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia、https://echobae.com/p/149cm-white-hair-silicone-doll-siwei

证据：首轮五星Reviews与0条评价系统不一致，评价数量本身未证明引语真假。

未确定：是否有历史真实评价、授权或不同商品来源未知；当前目录变化后不能强称所有旧问题还存在。

修改位置：商品富文本评分文案、Customer Reviews数据源、首页客户引语、Product aggregateRating。

实施/选择：A有来源则按SKU导入并显示真实数量；B无来源先去五星/verified暗示，保留真实已授权引语的明确归属。

成本：1–2人日（估算）

验收：零评价不显示可误读为评分的五星；评分/数量/Schema一致，来源授权记录可供运营核验。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### CONT-02 · P1 · Siwei商品标题与正文名称不一致

状态：SKU/选配数据已核对，业务文案待确认

页面：https://echobae.com/p/149cm-white-hair-silicone-doll-siwei

证据：首轮QY073标题Siwei、正文Aurora；当前API仍Title带AI，而Additional Upgrades明确AI+79.99。只能确认数据表达与选配价格，不确认AI是不是另有基础功能。

未确定：Siwei/Aurora是否合法别名、AI基础/升级具体差别和头身型号业务事实未知。

修改位置：QY073商品名称、SEO meta_title、描述、addons及SKU规格表。

实施/选择：A统一正式型号名；B明确别名及头/身体组合。若AI是选配，主名避免标配暗示；若基础与升级不同，写清差异而非盲删AI。

成本：0.5人日（估算）

验收：API/H1/购物车型号一致；AI基础/升级说明和价格明确；用厂家真实配置表对照。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### SHIP-01 · P1 · 结账国家及免运费展示与政策范围不一致

状态：展示风险已观察，费率/服务端待验证

页面：https://echobae.com/checkout

证据：首轮US/Canada/Brazil可选择且Standard Free；当前Checkout公共代码有quote(country,province,zip)和region not served错误映射，不是完全没有地区校验逻辑。

未确定：具体后台服务地区、缺邮编时报价语义、税费与最终下单校验未执行。

修改位置：Checkout quote函数、国家/省/邮编联动、shipping_rate_id、服务端quote与订单再校验。

实施/选择：A仅展示支持国家/路线；B允许全国家选择但对不服务地区明确拒绝；C完整地址前标“待计算”而非默认免费。按真实经营覆盖选方案。

成本：1–2人日（估算）

验收：已支持/不支持/偏远地区/免运阈值/税费/优惠各测试；country改后旧quote不残留；最终费用只在沙盒订单验证。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### CONT-06 · P1 · 定制页FAQ答案错位并遗留30天退货模板

状态：从首轮证据补发现，当前现状待复检

页面：https://echobae.com/custom-made

证据：首轮DOM首题“定制与批量有什么不同”答“Most orders ship within 2–3 business days”；HTML/FAQPage其余多题答“We offer 30-day returns on unused items in original packaging.”，与退款政策冲突。

未确定：本轮无新DOM，不知道运营是否已修正；不是已经证明实际处理退货不合法。

修改位置：定制页FAQ block的问答数据及自动FAQPage生成，不仅通用Return政策。

实施/选择：按每个问题的真实业务回答重写或暂时隐藏未定稿项；网页问答和JSON-LD由同一事实源生成，明确报价/材料参考/订单确认/运输/取消条件。

成本：0.5–1人日

验收：逐题与问题相关、无Demo物流/退货承诺；可见答案与FAQPage一致，与正式政策一致。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### IMG-02 · P2 · 主要商品图在不同模板强制裁剪

状态：几何已确认；不当程度/新改造待复检

页面：https://echobae.com/collections/new-arrival、https://echobae.com/collections/best-value、https://echobae.com/collections/best-sellers、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia

证据：首轮分类方形cover裁600×900图约33%，PDP4:5裁约17%；当前ProductImage新增adaptive支持，但默认false，是否调用已启用本轮未渲染验证。

未确定：是否裁到关键身体/细节因图片构图而异，不能把任何cover都判错；新adaptive是否解决具体模板未知。

修改位置：ProductCard/ProductImage的容器比例；PdpGalleryV2 .pdp-gallery__main/.pdp-gallery__image；缩略图样式。

实施/选择：A保留方形/4:5舞台改contain+一致背景，整体布局最稳定；B主要全身照片舞台2:3，手机页面变长；C运营上传专用方形构图。新增adaptive必须在加载前预留正确比例。

成本：1–2人日（估算）

验收：主图/放大图保留需要的头身细节；缩略图可适度聚焦；混合竖/横图不拉伸；390/768/1440截图人工确认且CLS≤0.1。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### SEO-05 · P2 · Title品牌后缀重复

状态：生成机制已确认，待修改

页面：https://echobae.com/blog、https://echobae.com/blog/silicone-sex-doll-buying-guide、https://echobae.com/p/149cm-christmas-silicone-love-doll-huaze、https://echobae.com/p/170cm-realistic-silicone-sex-doll-jiachen；完整URL见CSV，退休历史URL需与当前目录交叉

证据：当前PDP seo.meta_title已含|Echobae；当前入口up().formatPageTitle对非首页无条件追加separator+site_name。不是已证明某Vue titleTemplate造成。

未确定：第三方后台是否有全局批量SEO模板未知；本轮HTML缺title，不能称今天DOM已看到双后缀。

修改位置：BFXRDhpD.js:35901格式化；4FfVxrIF.js调用；SKU seo.meta_title字段。

实施/选择：A明确seo.meta_title为最终成品，存在时不再追加，内容title才格式化；B运营统一SEO字段不含品牌；C格式化器仅去重精确尾部品牌，不全局删除商品中品牌词。

成本：0.5人日（估算）

验收：QY029最终159cm Lifelike Silicone Sex Doll Lydia | Echobae，只一个后缀；首页当前合理标题不改；覆盖首轮76页并与现存SKU清单交叉。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### SEO-06 · P2 · 参数页重复标题并自引用Canonical

状态：策略缺口/生成来源待复核

页面：https://echobae.com/blog?category=Buyer+Guide、https://echobae.com/blog?category=updates、https://echobae.com/products?tag=bestseller、https://echobae.com/products?tag=smart-home；完整URL见CSV，退休历史URL需与当前目录交叉

证据：首轮12参数页自引用query Canonical和重复Title；当前通用SEO helper默认route.path，不直接取fullPath，因此“全局按当前完整URL生成”不是已证实根因。

未确定：参数是由调用方path、canonical override或SSR层注入未知；自引用筛选不必然错误，也没有排名数据证明蚕食。

修改位置：SEO helper canonicalOverride/path；列表SEO调用方；服务端canonical处理。

实施/选择：A有独立价值的筛选升级正式分类并index；B其余noindex且可抓取；C真正相同内容sort/tracking规范到无参数。分页内容不同不全canonical到第一页。

成本：0.5–1人日（估算）

验收：明确url规则表；sort追踪参数去重、内容型筛选按白名单；page=2独立规范；直接HTTP与DOM策略一致。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### SEO-07 · P2 · 购买指南链接到404护理文章

状态：历史已验证，现状待复检

页面：https://echobae.com/blog/silicone-sex-doll-buying-guide、https://echobae.com/blogs/silicone-doll-care-guide

证据：首轮buying-guide的护理链接确指向/blogs旧404；存在/sex-doll-care有效候选。

未确定：内容后台是否已修改、旧链接的真实外链流量未知。

修改位置：文章正文href，旧路由单条重定向。

实施/选择：A替换为现有相关Care页；B发布实际目标文章并一对一301旧地址。不能把所有404重定向首页。

成本：0.25人日（估算）

验收：点击护理内链200且相关，canonical一致；保留旧URL跳转测试。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### CONT-03 · P2 · FAQ重复问答02与03

状态：历史已验证，现状待复检

页面：https://echobae.com/faq

证据：首轮FAQ第02/03题及答完全相同。

未确定：本轮未验证运营是否已去重；不推断内部导入脚本原因。

修改位置：FAQ条目内容与顺序。

实施/选择：A删掉重复并重编号；B有真实常见问题再替换，别为SEO硬加字数。

成本：0.25人日（估算）

验收：公开问答/相关Schema均无重复，编号连续。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### CONT-04 · P2 · 首页社媒图标链接到平台首页

状态：历史已验证，现状待复检

页面：https://echobae.com/

证据：首轮7个社媒图标href为平台根域。

未确定：真实品牌账号、后台导航编辑能力、本轮链接现状未知。

修改位置：社媒URL配置/公共header-footer或页面block。

实施/选择：A填写真实品牌主页；B无账号的图标隐藏。不要编造账号或保留平台根链接。

成本：0.25人日（估算）

验收：每个保留图标到真实品牌帐号，无平台根URL，标签可读。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### SEC-01 · P2 · Demo详情HTML暴露私有HTTP图片地址

状态：历史问题，公开目录改善后待验收

页面：https://echobae.com/p/demo-sh-020、https://echobae.com/p/demo-sh-030、https://echobae.com/p/demo-sh-060、https://echobae.com/p/demo-sh-100；完整URL见CSV，退休历史URL需与当前目录交叉

证据：首轮28Demo HTML引用内部HTTP媒体；当前图片provider的内部alias属于服务端图片取图配置，不等同浏览器直接访问内部地址。

未确定：旧Demo清理后残余页面/其他媒体字段是否仍泄露未知；内部端口调整未据此推断服务器架构安全性。

修改位置：公开媒体字段规范化与IPX provider的客户端URL/服务端origin分离。

实施/选择：A先验收现有Demo移除；B对公开content URL拒绝私有host，内部取图origin只作服务端配置。不要盲删合法服务端alias导致所有IPX失效。

成本：0.5–1人日（估算）

验收：当前公开HTML/img/currentSrc/Schema无内部HTTP URL；IPX输出仍公网HTTPS；不做私网探测。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### TRACK-01 · P2 · GTM已嵌入，但事件与隐私承诺未验证

状态：待账号与正常网络验证

页面：https://echobae.com/、https://echobae.com/privacy-policy

证据：首轮GTM容器公开可见但代理失败；本轮没有打开GA4/GSC/GTM账号，也没有新的浏览器网络。

未确定：哪些tags/event/Consent Mode、是否实际外发成人商品或PII未知，不能凭GTM存在就指控泄露。

修改位置：GTM预览/GA4 DebugView、dataLayer、隐私政策与同意规则。

实施/选择：A最小必要测量并同意管理；B不开分析则移除未用tag/修正文案。真实purchase仅测试环境；运营选择实际方案。

成本：1–2人日（估算）

验收：view_item/add_to_cart/begin_checkout/purchase单次且参数正确，无PII，拒绝/同意状态网络符合承诺，需账号或开发证据。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### UX-05 · P2 · 营销弹窗在购物及结账过程中打断操作

状态：历史摩擦，当前规则待核验

页面：https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia、https://echobae.com/checkout

证据：首轮营销弹窗实际拦截购物/优惠码；当前MarketingPopup公开代码按path/locale取配置并在年龄验证后按delay/scroll触发。

未确定：后台排除路径是否已更新、A/B转化影响未知；正常可关闭，不能称购物按钮失效。

修改位置：MarketingPopupOverlay触发/路径过滤/频次，与年龄门禁不混同。

实施/选择：A运营排除checkout并限制连续弹窗；B改非阻塞提示；C商品页适当频次仍保留。不要关闭必要年龄验证。

成本：0.5人日（估算）

验收：checkout无非必要阻塞，正常×和键盘可关闭；不触发订阅邮件进行测试。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### SEO-10 · P2 · QY073额外FAQPage缺必需mainEntity

状态：本轮字段已确认，待修改

页面：https://echobae.com/p/149cm-white-hair-silicone-doll-siwei

证据：首轮JSON-LD以及本轮公开API seo.structured_data均只有@type FAQPage/@context，没有mainEntity。

未确定：官方Rich Results Test未执行；普通电商FAQ本就不应承诺Google FAQ富结果。

修改位置：QY073 seo.structured_data额外Schema字段；PDP自动Product之外追加JSON-LD的生成边界。

实施/选择：最小修复删除这个空FAQPage；若确有合法问答语义需求，输出真实可见Question/acceptedAnswer/mainEntity，避免与block生成重复。

成本：0.25人日

验收：无空FAQPage；Product/Offer/BreadcrumbList不受影响；适用Schema字段校验通过。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### IMG-04 · P2 · 商品详情图Alt使用设计文件占位名称

状态：历史DOM+本轮原图确认，当前DOM待复检

页面：https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia

证据：首轮DOM图片46/47 Alt分别Your paragraph text.webp、Untitled design.webp；本轮独立原图查看为身体规格/结构展示与面部/手部照片拼图。

未确定：后台是否可单独编辑Alt、其他SKU复用数量和当前DOM是否已修正未知。

修改位置：PDP详情富文本图片/媒体Alt；上传默认文件名fallback。

实施/选择：将Alt按图意改成“Silicone doll body sizes and construction details”与“Close-up views of doll faces, hands and posing”；装饰性图才空Alt，主要规格同时用HTML文字/表格表达。

成本：0.25–0.5人日

验收：Alt自然描述而非文件名、无堆词；规格关键值可从正文读取；可访问树复检。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### SEO-08 · P3 · 商品Schema基础有效但变体/图片字段仍需发布校验

状态：基础已通过，变体/资格待验证

页面：https://echobae.com/p/demo-sh-020、https://echobae.com/p/demo-sh-030、https://echobae.com/p/demo-sh-060、https://echobae.com/p/demo-sh-080；完整URL见CSV，退休历史URL需与当前目录交叉

证据：三SKU首轮Product SKU/USD基础价与本轮API一致；InStock与track_inventory=true、available_quantity100自洽，但实体库存未证。

未确定：变体SKU、生产ready含义、真实库存与Google富结果资格未知。FAQ结构缺陷另见SEO-10。

修改位置：商品Schema生成器4FfVxrIF.js和PDP buildPageSeo; JSON-LD额外数据。

实施/选择：A保持已正确的基础Product，不添加假评分；B有真实独立SKU再建ProductGroup/variants；把HTML excerpt转纯文本及去重图片作为低优先级。

成本：0.5–1人日（估算）

验收：默认SKU/价格/货币对齐；选项语义与实际SKU策略明确，额外Schema和OG图片尺寸与真实资源一致；官方工具由开发执行。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

### CONT-05 · P3 · Summer Sale 2026横幅在10月仍显示

状态：运营核验项，未证明故障

页面：https://echobae.com/

证据：首轮确有Summer Sale2026横幅；这不证明10月促销无效（地域/活动命名不同）。

未确定：活动有效期、优惠码、折扣规则未知，本轮页面壳没有实际横幅。

修改位置：运营活动名称、有效期/适用SKU/优惠配置。

实施/选择：A有效则澄清真实活动规则；B过期则撤下。仅在事实确认后修改，不为季节审美制造必修任务。

成本：0.25人日（估算）

验收：营销文案与有效折扣规则一致；有效码计算在开发沙盒验。

操作步骤：先导出/备份现有内容和数据，确认以上业务事实；在实际可编辑字段修改；发布后读取公开页面/API，再让开发用正常浏览器复检。后台不支持则交开发，不在没有权限时假设菜单存在。

## 发布前共同验收

目录清理/政策与价格→浏览器功能和图片/性能→开发沙盒交易与账户追踪→正式发布窗口索引/Sitemap。任何未执行项保持“未验证”；失败日志不删除，报告记录修复前后日期和版本。
