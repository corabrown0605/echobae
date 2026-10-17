# 开发技术需求与验收

所有线上改动由用户另行安排并批准，本次未修改。后台菜单与内部源码未取得，不编造路径。以下工作量是缺少源码条件下的粗估人日，不是报价。当前公开部署已有变化，先验收再改。

## 推荐工作包顺序

1. SSR bootstrap/业务HTML/错误与缓存：SEO-09、SEO-03、SEO-04、FE-02。
2. 当前目录验收与价格/条款/配送：CAT-01、CART-01、POL-04、SHIP-01。
3. 图片provider/sizes/占位及可访问：IMG-01、IMG-02、PERF-04、UX-01、UX-03、UX-04。
4. 性能profile/组件按需、菜单/购物时延受控复测：PERF-01、PERF-02；PERF-03已合并。
5. 真实分页href/政策FAQ与Schema/可选模块/链接：SEO-11、CONT-06、SEO-10、FE-01、SEO-07、SEO-06。
6. 正式发布窗口robots/SEO全局锁/非空Sitemap/GSC：SEO-01、SEO-02；业务与沙盒验收先于开放收录。

详细建议代码与取舍见[TECHNICAL_PATCH_GUIDE.md](TECHNICAL_PATCH_GUIDE.md)。共享工作包不要把每项粗估累加收费；原ID保留用于分别验收。

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

### CAT-01 · P1 · 主商品列表公开展示 Demo、测试及复制商品

状态：部分改善，待前台验收

页面：https://echobae.com/products、https://echobae.com/pages/help、https://echobae.com/p/demo-sh-020、https://echobae.com/p/demo-sh-030；完整URL见CSV，退休历史URL需与当前目录交叉

证据：当前英文公开列表API四页合计72个唯一商品，未发现demo/e2e/copy/test命名；demo-sh-030、e2e-ship-heavy、代表复制SKU的API均404。首轮已确认这些SKU公开为active。

未确定：后台如何下架/删除、其他语言与缓存推荐是否同步未知；当前浏览器页面尚未复测。

修改位置：后台商品发布/语言可见性；公开catalog/products服务和各推荐数据源。无后台菜单证据。

实施/选择：A保留现有清理并做72 SKU白名单验收，最低风险；B对残余旧URL返回404/410，只有真正迁移商品一对一301。不要根据旧清单批量删除已清理内容。

成本：复检0.5人日，残余修复另估

验收：当前72 SKU浏览器分页、搜索、Help推荐均无Demo；旧Demo HTML状态与API404一致；其他语言如要发布再验。

### SEO-02 · P1 · sitemap.xml为空索引

状态：待修改

页面：https://echobae.com/sitemap.xml

证据：今天sitemap.xml仍为空sitemapindex；公开SEO载荷product limit5000，当前72商品远低于限制，不能用数量上限解释空表。

未确定：是有意预发布禁用、发布过滤还是路由生成失败未知；未访问服务器Sitemap源码。

修改位置：Sitemap服务端查询/输出、正式内容发布清单、canonical策略。

实施/选择：A单urlset用于当前规模，简单且够用；B索引+按语言/类型分片，适合扩展。以已发布、200、规范、允许索引页面为数据源。

成本：0.5–1人日（估算）

验收：不要把历史228全放入；只纳入当前正式72 SKU和有效分类/文章/内容页；排除退休测试、搜索、交易、低价值参数；lastmod只反映真实内容更新。

### POL-01 · P1 · 隐私政策保留服务器国家占位符

状态：历史已验证，现状待复检

页面：https://echobae.com/privacy-policy

证据：首轮公开正文两处服务器国家占位，属于已输出内容未完成，不是根据行业模板推测。

未确定：真实服务器国家、法律实体、第三方处理与数据保留承诺未获后台证据；本轮未复测正文。

修改位置：运营政策正文编辑；开发/供应商提供真实数据处理信息。

实施/选择：A核实事实后完整修订；B无法确认的承诺先改为准确可验证说明，不能猜国家或法律义务。

成本：0.5–1人日（估算）

验收：两处占位移除；主体、存储/跨境和联系信息经负责人确认；保存政策版本和更新时间。

### POL-02 · P1 · 配送时效在首页和政策中矛盾

状态：历史已验证，现状待复检

页面：https://echobae.com/、https://echobae.com/shipping-policy

证据：首轮首页3–7天与物流页10–14工作日/30–35天并存；同一业务信息的输出不一致。

未确定：具体真实时效、生产周期和不同目的地是否确实不同未知。

修改位置：首页FAQ内容、商品FAQ、物流政策与结账配送率文案。

实施/选择：A用统一配送事实表生成各页面；B先把首页改成到物流政策的清楚指引，减少多处独立维护。

成本：0.5–1人日（估算）

验收：分别验证Standard/Express+生产期+目的地；FAQ Schema同步内容，不只改可见文本。

### CART-01 · P1 · 购物车及结账划线价与商品页不一致

状态：公开实现已确认，待修改

页面：https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia、https://echobae.com/cart、https://echobae.com/checkout

证据：当前入口映射CartV2 B63DM7Lk.js:635和CheckoutV2 B7-ND3fn.js:2158均用单价×1.2算比较价；PDP用API compare_at_price1800。不是仅仅猜价格映射错误。

未确定：服务端cart/quote DTO是否有真实compare_at_price字段仍需开发确认；本轮未重新加车。

修改位置：CartV2的K()与CheckoutV2的ee()；PDP价格模型；cart/quote响应序列化字段。

实施/选择：A立即删掉派生划线价和Saved，最小安全修复；B数据契约传真实比较价（SKU+配置），三页统一；绝不拿售价固定加20%制造折扣。

成本：1人日（估算）

验收：Lydia基础1609.99/真实1800；AI1689.98，2件3379.96，三页相同真实原价或统一不显示；运费/优惠后按真实基准计算，后台重算实付金额。

### POL-04 · P1 · 结账要求同意条款，但没有可访问的条款链接

状态：公开实现已确认，待修改

页面：https://echobae.com/checkout

证据：当前CheckoutV2条款是纯span翻译文案，无a[href]；Ce()先检查同意checkbox后调用提交。缺的是可阅读链接，不是已经证明同意校验失效。

未确定：Terms正式URL和后台是否可设置未知；服务端是否记录接受版本/时间未知。

修改位置：CheckoutV2条款label/span；公开条款CMS页、Footer导航；订单协议字段。

实施/选择：A新增真正的Terms链接（新页或保留会话打开）；B把政策中真实完整条款公开为独立可访问URL。不能把猜测404路径当唯一条款地址。

成本：0.5–1人日（估算）

验收：可打开完整Terms且返回不丢车；不勾选拒绝提交；订单接受记录只在测试环境验证。

### SEO-03 · P1 · 不存在的商品详情返回200空商品壳

状态：API边界已验证；页面缺陷需SSR修复后复检

页面：https://echobae.com/p/audit-nonexistent-20261013

证据：当前随机不存在商品API404；公开PDP setup只在初始化检查error.value，无商品分支显示loading；首轮HTML确返回空200。

未确定：API错误何时到达、SSR缓存为何保留200须服务端源代码/日志确认；不能说初始guard永远不会抛错。当前全局加载壳还会掩盖此问题。

修改位置：DL_6UJog.js:5656及末尾无商品loading分支；商品useAsyncData加载与Nuxt SSR错误传播。

实施/选择：A页面async setup await加载后throw createError({statusCode:404})；B服务端路由校验+客户端响应式错误UI。区分真404与上游失败503，不把网络失败都返回404。

成本：0.5–1人日（估算）

验收：随机不存在slug直接HTTP404/410且有恢复导航；有效SKU200+真实正文；上游超时503/no-store或明确降级，不能缓存加载壳。

### IMG-01 · P1 · 商品图片srcset多候选指向同一个文件

状态：当前配置链已确认，待修改

页面：https://echobae.com/collections/new-arrival、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia、https://echobae.com/p/149cm-white-hair-silicone-doll-siwei

证据：当前BK9qvGFY.js:290 image.domains不含echobae.com，绝对媒体URL会在域名检查后原样返回；PDP和ProductImage传入普通HTML媒体sizes，当前解析器按断点键分割，退化为固定尺寸。

未确定：是否存在运行时provider覆盖、服务端IPX可达性和新页面最终currentSrc需复检。不能把优化服务全局不可用当确定原因。

修改位置：Nuxt Image配置domains/alias；PdpGalleryV2 sizes:1911；ProductImage C6D29uTs.js；NuxtImg getSizes/域名校验。

实施/选择：A同源媒体标准化为相对/api/v1/media并使用已支持的IPX；B加入精确公共媒体域名白名单；C生成预制尺寸CDN文件。配合Nuxt sizes="100vw md:720px"等符合此版本语法的表达式，实际输出应按布局验。

成本：1–2人日（估算）

验收：候选URL不同、物理像素匹配400w/800w等；断点HTML sizes有效；缩略图不下载1707px原图；不直接请求内部IP。

### PERF-01 · P1 · 代表页面移动端LCP持续偏慢

状态：历史实验室缺陷，控制复测待完成

页面：https://echobae.com/、https://echobae.com/collections/new-arrival、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia、https://echobae.com/blog/tpe-vs-silicone-sex-doll

证据：首轮三次中位mobile：首页LCP5.59s，分类5.61s，商品5.87s，文章4.94s；本轮未运行新Lighthouse。主Banner本轮物理30KB，不能把大图字节当唯一根因。

未确定：代理/背景采集、renderer初始化、轮播与渲染阻塞贡献未完成单因素实验；没有真实用户CWV。

修改位置：首页轮播/SSR初始化、公共CSS/JS；首轮LCP breakdown与network/long task记录。

实施/选择：A优先SSR与布局保留，稳定首屏；B减少首屏公共资源/延后非必要模块；C只对已确认大资源优化。按独立冷/热和年龄条件重新测量，不相加Lighthouse节约估计。

成本：2–4人日（估算）

验收：同配置无背景标签3次中位LCP≤2.5s；FCP/LCP/可见主内容分别记录；所有第三方成功场景补测，不能以本轮HTTP壳0.65s算性能通过。

### PERF-02 · P1 · 主线程脚本开销与阻塞仍高

状态：阻塞已观察，具体归因待验证

页面：https://echobae.com/、https://echobae.com/collections/new-arrival、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia

证据：首轮home-mobile-1最长任务1111ms，归因document/Other，不是已定位某个hydration函数；Script Evaluation约3148ms；有长任务是事实。

未确定：为何document Other很长、具体业务函数、真实交互是否卡顿未知；首轮确认组保留额外背景页面且缓存，TBT高不能等同INP。

修改位置：公开入口、主题加载/动态块/轮播挂载；DevTools主线程stack/profile需要开发采集。

实施/选择：A采样profile找函数后拆长任务/延迟非首屏；B按路由拆包；C若是测试干扰先清理背景进程重测。不能直接断言删某bundle可省整段耗时。

成本：2–4人日（估算）

验收：EventTiming记录input/processing/presentation，关键交互3次；LongTask分解有调用栈；TBT≤200ms为实验室目标，生产p75 INP另验。

### CONT-01 · P1 · 五星Reviews营销文字与0条评论展示不一致

状态：历史矛盾，来源待运营核验

页面：https://echobae.com/、https://echobae.com/customer-reviews、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia、https://echobae.com/p/149cm-white-hair-silicone-doll-siwei

证据：首轮五星Reviews与0条评价系统不一致，评价数量本身未证明引语真假。

未确定：是否有历史真实评价、授权或不同商品来源未知；当前目录变化后不能强称所有旧问题还存在。

修改位置：商品富文本评分文案、Customer Reviews数据源、首页客户引语、Product aggregateRating。

实施/选择：A有来源则按SKU导入并显示真实数量；B无来源先去五星/verified暗示，保留真实已授权引语的明确归属。

成本：1–2人日（估算）

验收：零评价不显示可误读为评分的五星；评分/数量/Schema一致，来源授权记录可供运营核验。

### SHIP-01 · P1 · 结账国家及免运费展示与政策范围不一致

状态：展示风险已观察，费率/服务端待验证

页面：https://echobae.com/checkout

证据：首轮US/Canada/Brazil可选择且Standard Free；当前Checkout公共代码有quote(country,province,zip)和region not served错误映射，不是完全没有地区校验逻辑。

未确定：具体后台服务地区、缺邮编时报价语义、税费与最终下单校验未执行。

修改位置：Checkout quote函数、国家/省/邮编联动、shipping_rate_id、服务端quote与订单再校验。

实施/选择：A仅展示支持国家/路线；B允许全国家选择但对不服务地区明确拒绝；C完整地址前标“待计算”而非默认免费。按真实经营覆盖选方案。

成本：1–2人日（估算）

验收：已支持/不支持/偏远地区/免运阈值/税费/优惠各测试；country改后旧quote不残留；最终费用只在沙盒订单验证。

### UX-01 · P1 · 年龄验证弹窗没有键盘焦点约束

状态：首轮行为+当前组件证据，待复检

页面：https://echobae.com/

证据：首轮12次Tab第三次离开AgeGate；当前公开AgeGate有aria-modal与两个按钮、记忆到期逻辑，组件未见focus trap/inert实现。

未确定：本轮未重新键盘验证；外围层是否新加约束未确认。

修改位置：AgeGateOverlay，页面根元素焦点/滚动约束，确认后焦点恢复。

实施/选择：A使用已有成熟可访问dialog组件，去掉绕过关闭入口；B手动focus循环、inert背景、restore focus。不能只添加aria-modal就认为行为已实现。

成本：0.5–1人日（估算）

验收：20次Tab/Shift+Tab不离开；回车正常确认/离开；未确认不能操作背景；正常确认记忆符合30天配置。

### PERF-04 · P1 · 首页桌面CLS三次均约0.457

状态：历史稳定复现，当前渲染未复测

页面：https://echobae.com/

证据：首轮桌面CLS三次0.456637；最大位移0.416346关联Find Your Perfect Doll。Banner CSS width100%/height:auto且未预留图像比例，与unsized诊断吻合。

未确定：移位的全部因果与新部署结果需要trace；Lighthouse关联不是完整调用栈证明。

修改位置：Banner .ecom-ad-carousel-v1__media/img；首屏容器和图片width/height；新adaptive图片初始比例。

实施/选择：A原尺寸width1672 height941+aspect-ratio:1672/941，保留当前视觉；B桌/移动预设各自固定比例；C容器由CMS媒体元数据先确定。不要onload后才换ratio。

成本：0.5–1人日（估算）

验收：冷加载前后Banner占位一致；desktop三次CLS≤0.1；轮播切换不改容器高度，移动回归。

### SEO-09 · P1 · 当前首页与商品SSR只输出加载壳

状态：本轮输出已确认；服务端原因待开发

页面：https://echobae.com/、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia

证据：6份成功HTML样本（5首页+1商品）都无Title/业务meta/H1/正文，shell-loading存在，tokensReady=false、branding空、业务data未填；当前CYM8kJOs layout按tokensReady选择加载壳。

未确定：配置初始化在SSR是否被await、内部请求失败还是已有缓存故障未知；客户端随后恢复情况未验证。不是证明Google一定不收录。

修改位置：当前入口BFXRDhpD主题bootstrap、default/blog layout的ready门禁、SSR错误传播与缓存准入。

实施/选择：A在server-safe async bootstrap await主题/品牌/locale及页面关键数据后SSR；B安全默认主题仍渲染正文和meta，必要交易禁用；C临时客户端渲染只能作为有明确SEO权衡的降级。失败不要200缓存空壳，使用准确错误状态/no-store。

成本：1–3人日（含源码定位，粗估）

验收：正常GET各模板有Title/meta/H1/Canonical/Schema及主要正文；模拟配置失败不产生可缓存200空壳；公开脚本和图片依然加载；正常浏览器冷启动/谷歌渲染另验。

### CONT-06 · P1 · 定制页FAQ答案错位并遗留30天退货模板

状态：从首轮证据补发现，当前现状待复检

页面：https://echobae.com/custom-made

证据：首轮DOM首题“定制与批量有什么不同”答“Most orders ship within 2–3 business days”；HTML/FAQPage其余多题答“We offer 30-day returns on unused items in original packaging.”，与退款政策冲突。

未确定：本轮无新DOM，不知道运营是否已修正；不是已经证明实际处理退货不合法。

修改位置：定制页FAQ block的问答数据及自动FAQPage生成，不仅通用Return政策。

实施/选择：按每个问题的真实业务回答重写或暂时隐藏未定稿项；网页问答和JSON-LD由同一事实源生成，明确报价/材料参考/订单确认/运输/取消条件。

成本：0.5–1人日

验收：逐题与问题相关、无Demo物流/退货承诺；可见答案与FAQPage一致，与正式政策一致。

### IMG-02 · P2 · 主要商品图在不同模板强制裁剪

状态：几何已确认；不当程度/新改造待复检

页面：https://echobae.com/collections/new-arrival、https://echobae.com/collections/best-value、https://echobae.com/collections/best-sellers、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia

证据：首轮分类方形cover裁600×900图约33%，PDP4:5裁约17%；当前ProductImage新增adaptive支持，但默认false，是否调用已启用本轮未渲染验证。

未确定：是否裁到关键身体/细节因图片构图而异，不能把任何cover都判错；新adaptive是否解决具体模板未知。

修改位置：ProductCard/ProductImage的容器比例；PdpGalleryV2 .pdp-gallery__main/.pdp-gallery__image；缩略图样式。

实施/选择：A保留方形/4:5舞台改contain+一致背景，整体布局最稳定；B主要全身照片舞台2:3，手机页面变长；C运营上传专用方形构图。新增adaptive必须在加载前预留正确比例。

成本：1–2人日（估算）

验收：主图/放大图保留需要的头身细节；缩略图可适度聚焦；混合竖/横图不拉伸；390/768/1440截图人工确认且CLS≤0.1。

### FE-01 · P2 · runtime-blocks在所有深度样本中返回404

状态：接口/前端fallback已确认，依赖待开发核实

页面：https://echobae.com/、https://echobae.com/about-us、https://echobae.com/blog、https://echobae.com/blog/silicone-sex-doll-buying-guide；完整URL见CSV，退休历史URL需与当前目录交叉

证据：当前入口runtime-blocks的函数遇非OK返回[]，插件await后只在非空列表注册模块；这是可选注册机制失败，不足说明全站功能失效。

未确定：服务端接口为何404、有没有必需扩展模块未知；不能把所有商品/图片问题归因该API。

修改位置：入口z$/W$/K$，公开/content/runtime-blocks，动态模块注册表。

实施/选择：A不使用扩展则不请求；B使用但无记录返回200 []；C有记录返回完整清单并验证module_url。按真实用途处理，不加无意义假模块。

成本：0.5–1人日（估算）

验收：冷启动无无意义404；所有必需block/模块实际存在；一次SPA初始化与每路由请求区分。

### FE-02 · P2 · 多模板出现Hydration mismatch

状态：警告已验证，根因未完全确定

页面：https://echobae.com/about-us、https://echobae.com/blog、https://echobae.com/blog/silicone-sex-doll-buying-guide、https://echobae.com/blog/tpe-vs-silicone-sex-doll；完整URL见CSV，退休历史URL需与当前目录交叉

证据：首轮49/58记录Hydration警告，无未捕获pageerror。新HTML tokensReady=false与客户端布局按ready分支可产生状态差异，但未捕获同节点差异的trace。

未确定：SSR父子状态更新时间、主题tokens、locale字典、page-breadcrumb-store等都是候选，不当成确定内部根因。

修改位置：主题bootstrap、default/blog layout、Nuxt async data、面包屑状态。

实施/选择：A先解决SEO-09完整SSR、序列化相同初始状态；B按具体节点修复；不把全站包ClientOnly或屏蔽Console当修复。

成本：1–2人日（估算）

验收：开发模式定位mismatch节点/文本；初始DOM/首次hydrate一致，警告消失；重测冷启动及SPA。

### SEO-04 · P2 · 初始HTML与渲染DOM的主标题不一致

状态：输出差异已确认，SSR时序待验证

页面：https://echobae.com/products、https://echobae.com/collections/new-arrival、https://echobae.com/collections/best-value、https://echobae.com/custom-made；完整URL见CSV，退休历史URL需与当前目录交叉

证据：首轮初始Home/Collections/Products与DOM真实H1不同；页面写page-breadcrumb-store，布局读它并有通用fallback，PDP showPageTitle:false。

未确定：父布局何时SSR读取子页写入状态需要源码调试；H1差异与hydration警告不能直接等同一原因。

修改位置：C_kT0Sim.js共享breadcrumb store；DsOVWUii.js布局title fallback；DL_6UJog.js页面breadcrumb设置。

实施/选择：A父层从已await页面数据/路由meta取标题，避免子组件渲染中改父SSR状态；B面包屑只nav文字、H1由页面自己渲染。博客移除重复外层H1。

成本：1人日（估算）

验收：修SEO-09后view-source/DOM主H1一致；商品只有主商品H1、Blog无两份The Blog，H2/H3层级按正文。

### SEO-05 · P2 · Title品牌后缀重复

状态：生成机制已确认，待修改

页面：https://echobae.com/blog、https://echobae.com/blog/silicone-sex-doll-buying-guide、https://echobae.com/p/149cm-christmas-silicone-love-doll-huaze、https://echobae.com/p/170cm-realistic-silicone-sex-doll-jiachen；完整URL见CSV，退休历史URL需与当前目录交叉

证据：当前PDP seo.meta_title已含|Echobae；当前入口up().formatPageTitle对非首页无条件追加separator+site_name。不是已证明某Vue titleTemplate造成。

未确定：第三方后台是否有全局批量SEO模板未知；本轮HTML缺title，不能称今天DOM已看到双后缀。

修改位置：BFXRDhpD.js:35901格式化；4FfVxrIF.js调用；SKU seo.meta_title字段。

实施/选择：A明确seo.meta_title为最终成品，存在时不再追加，内容title才格式化；B运营统一SEO字段不含品牌；C格式化器仅去重精确尾部品牌，不全局删除商品中品牌词。

成本：0.5人日（估算）

验收：QY029最终159cm Lifelike Silicone Sex Doll Lydia | Echobae，只一个后缀；首页当前合理标题不改；覆盖首轮76页并与现存SKU清单交叉。

### SEO-06 · P2 · 参数页重复标题并自引用Canonical

状态：策略缺口/生成来源待复核

页面：https://echobae.com/blog?category=Buyer+Guide、https://echobae.com/blog?category=updates、https://echobae.com/products?tag=bestseller、https://echobae.com/products?tag=smart-home；完整URL见CSV，退休历史URL需与当前目录交叉

证据：首轮12参数页自引用query Canonical和重复Title；当前通用SEO helper默认route.path，不直接取fullPath，因此“全局按当前完整URL生成”不是已证实根因。

未确定：参数是由调用方path、canonical override或SSR层注入未知；自引用筛选不必然错误，也没有排名数据证明蚕食。

修改位置：SEO helper canonicalOverride/path；列表SEO调用方；服务端canonical处理。

实施/选择：A有独立价值的筛选升级正式分类并index；B其余noindex且可抓取；C真正相同内容sort/tracking规范到无参数。分页内容不同不全canonical到第一页。

成本：0.5–1人日（估算）

验收：明确url规则表；sort追踪参数去重、内容型筛选按白名单；page=2独立规范；直接HTTP与DOM策略一致。

### SEO-07 · P2 · 购买指南链接到404护理文章

状态：历史已验证，现状待复检

页面：https://echobae.com/blog/silicone-sex-doll-buying-guide、https://echobae.com/blogs/silicone-doll-care-guide

证据：首轮buying-guide的护理链接确指向/blogs旧404；存在/sex-doll-care有效候选。

未确定：内容后台是否已修改、旧链接的真实外链流量未知。

修改位置：文章正文href，旧路由单条重定向。

实施/选择：A替换为现有相关Care页；B发布实际目标文章并一对一301旧地址。不能把所有404重定向首页。

成本：0.25人日（估算）

验收：点击护理内链200且相关，canonical一致；保留旧URL跳转测试。

### UX-02 · P2 · 移动端轮播箭头覆盖正文区域

状态：首轮视觉+CSS定位，待复检

页面：https://echobae.com/

证据：首轮390截图箭头压正文；旧Banner CSS在max639px把42px控件absolute top50% left/right8px。

未确定：今天完整视觉未复测，不能说当前每个滑块都覆盖文字。

修改位置：Banner移动nav/content CSS规则。

实施/选择：A移动箭头下移独立控制区；B留两侧控制安全区/分页点；C正文放图下独立块，移动高度会增加。

成本：0.5人日（估算）

验收：390/412/768各滑块正文不被控件覆盖，按钮点击区域≥合理触摸尺度并可键盘使用。

### UX-03 · P2 · Footer暴露翻译键footer.poweredBy

状态：缺键与调用机制已确认，待修改

页面：https://echobae.com/cart、https://echobae.com/checkout

证据：本轮英文storefront-ui-messages返回footer字典无poweredBy；当前DsOVWUii.js:3739调用$t(footer.poweredBy)，与首轮裸key吻合。

未确定：是否还有其他locale缺项、完整字典合并/切换时序未知；不是已经证明所有i18n初始化失败。

修改位置：公开UI消息footer.poweredBy；FooterPoweredBy组件及locale加载/merge规则。

实施/选择：A补全真实英文poweredBy翻译；B允许明晰安全fallback。其他语言各补，避免用setLocaleMessage覆盖掉基础字典缺项。

成本：0.25–0.5人日（估算）

验收：en及所有发布语言不出现裸key；SSR和SPA购物车/结账Footer一致。

### SEC-01 · P2 · Demo详情HTML暴露私有HTTP图片地址

状态：历史问题，公开目录改善后待验收

页面：https://echobae.com/p/demo-sh-020、https://echobae.com/p/demo-sh-030、https://echobae.com/p/demo-sh-060、https://echobae.com/p/demo-sh-100；完整URL见CSV，退休历史URL需与当前目录交叉

证据：首轮28Demo HTML引用内部HTTP媒体；当前图片provider的内部alias属于服务端图片取图配置，不等同浏览器直接访问内部地址。

未确定：旧Demo清理后残余页面/其他媒体字段是否仍泄露未知；内部端口调整未据此推断服务器架构安全性。

修改位置：公开媒体字段规范化与IPX provider的客户端URL/服务端origin分离。

实施/选择：A先验收现有Demo移除；B对公开content URL拒绝私有host，内部取图origin只作服务端配置。不要盲删合法服务端alias导致所有IPX失效。

成本：0.5–1人日（估算）

验收：当前公开HTML/img/currentSrc/Schema无内部HTTP URL；IPX输出仍公网HTTPS；不做私网探测。

### SEC-02 · P2 · 公开200页面缺少统一安全响应头

状态：公开可见头已观察，源站配置待验证

页面：https://echobae.com/、https://echobae.com/products、https://echobae.com/collections/new-arrival、https://echobae.com/collections/best-value；完整URL见CSV，退休历史URL需与当前目录交叉

证据：首轮200只见HSTS而错误页有nosniff等；本轮成功文档仍见HSTS、未见CSP等。

未确定：代理是否移除头、源站与CDN路由差别未知，无攻击利用测试。

修改位置：源站/CDN HTML响应头与错误响应配置。

实施/选择：A先CSP Report-Only观测必要支付域，后落实frame-ancestors等；B先nosniff/referrer最小加固。不要以缺头声称严重漏洞或统一DENY破坏支付。

成本：0.5–1人日（估算）

验收：正常公网复核headers和支付嵌入，CSP无破坏；有report样本与受控验证，不进行攻击扫描。

### TRACK-01 · P2 · GTM已嵌入，但事件与隐私承诺未验证

状态：待账号与正常网络验证

页面：https://echobae.com/、https://echobae.com/privacy-policy

证据：首轮GTM容器公开可见但代理失败；本轮没有打开GA4/GSC/GTM账号，也没有新的浏览器网络。

未确定：哪些tags/event/Consent Mode、是否实际外发成人商品或PII未知，不能凭GTM存在就指控泄露。

修改位置：GTM预览/GA4 DebugView、dataLayer、隐私政策与同意规则。

实施/选择：A最小必要测量并同意管理；B不开分析则移除未用tag/修正文案。真实purchase仅测试环境；运营选择实际方案。

成本：1–2人日（估算）

验收：view_item/add_to_cart/begin_checkout/purchase单次且参数正确，无PII，拒绝/同意状态网络符合承诺，需账号或开发证据。

### PERF-03 · P2 · 首屏存在可减小的公共CSS/JS负载

状态：合并至PERF-01

页面：https://echobae.com/

证据：首轮unused CSS/JS估计与阻塞链是PERF-01资源瓶颈子任务，不应另算一组重复工期。

未确定：具体未用逻辑能否剔除、实际收益未知。

修改位置：blocks-built.css按block构建，shared runtime按路由/组件分包。

实施/选择：合并到PERF-01资源优化工作包；保留本ID作为CSS/JS验收子项，不另提重复上线工单。

成本：并入PERF-01，不重复计费

验收：CSS/JS字节和阻塞链下降，组件截图/动态类不丢，重复性能有改善。

### UX-04 · P2 · CTA和比较价文字对比度未达到自动化阈值

状态：历史自动化失败，现状待复检

页面：https://echobae.com/、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia

证据：首轮Lighthouse节点Explore红/白3.74:1、比较价灰/白2.53:1，16px普通文本阈值4.5。

未确定：本轮computed色值/hover/focus以及新主题值未复测。

修改位置：主题accent/on-accent/muted组合；Explore按钮与PDP comparison文本。

实施/选择：A加深文字/调整背景确保对比；B保持品牌色于非文字装饰。不能只改背景不看组件状态。

成本：0.5人日（估算）

验收：相关节点普通文字≥4.5:1、大字≥3:1；focus/disabled分别检查。

### UX-05 · P2 · 营销弹窗在购物及结账过程中打断操作

状态：历史摩擦，当前规则待核验

页面：https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia、https://echobae.com/checkout

证据：首轮营销弹窗实际拦截购物/优惠码；当前MarketingPopup公开代码按path/locale取配置并在年龄验证后按delay/scroll触发。

未确定：后台排除路径是否已更新、A/B转化影响未知；正常可关闭，不能称购物按钮失效。

修改位置：MarketingPopupOverlay触发/路径过滤/频次，与年龄门禁不混同。

实施/选择：A运营排除checkout并限制连续弹窗；B改非阻塞提示；C商品页适当频次仍保留。不要关闭必要年龄验证。

成本：0.5人日（估算）

验收：checkout无非必要阻塞，正常×和键盘可关闭；不触发订阅邮件进行测试。

### SEO-10 · P2 · QY073额外FAQPage缺必需mainEntity

状态：本轮字段已确认，待修改

页面：https://echobae.com/p/149cm-white-hair-silicone-doll-siwei

证据：首轮JSON-LD以及本轮公开API seo.structured_data均只有@type FAQPage/@context，没有mainEntity。

未确定：官方Rich Results Test未执行；普通电商FAQ本就不应承诺Google FAQ富结果。

修改位置：QY073 seo.structured_data额外Schema字段；PDP自动Product之外追加JSON-LD的生成边界。

实施/选择：最小修复删除这个空FAQPage；若确有合法问答语义需求，输出真实可见Question/acceptedAnswer/mainEntity，避免与block生成重复。

成本：0.25人日

验收：无空FAQPage；Product/Offer/BreadcrumbList不受影响；适用Schema字段校验通过。

### IMG-04 · P2 · 商品详情图Alt使用设计文件占位名称

状态：历史DOM+本轮原图确认，当前DOM待复检

页面：https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia

证据：首轮DOM图片46/47 Alt分别Your paragraph text.webp、Untitled design.webp；本轮独立原图查看为身体规格/结构展示与面部/手部照片拼图。

未确定：后台是否可单独编辑Alt、其他SKU复用数量和当前DOM是否已修正未知。

修改位置：PDP详情富文本图片/媒体Alt；上传默认文件名fallback。

实施/选择：将Alt按图意改成“Silicone doll body sizes and construction details”与“Close-up views of doll faces, hands and posing”；装饰性图才空Alt，主要规格同时用HTML文字/表格表达。

成本：0.25–0.5人日

验收：Alt自然描述而非文件名、无堆词；规格关键值可从正文读取；可访问树复检。

### SEO-11 · P2 · 分页缺普通href入口与静态链接发现缺口

状态：组件/历史记录已确认，新图待复检

页面：https://echobae.com/products、https://echobae.com/products?page=2、https://echobae.com/products?page=10

证据：首轮pagination.json实际进入?page2…10，故“始终不改URL”被证伪；分页组件用button onClick。首轮228初始a图可达194，32商品无初始a入链，不能等同全站孤立。

未确定：旧图包含已退休测试商品；按当前72商品交叉后的候选另见link-graph.json；新页面/语言/新推荐链接图未采集。

修改位置：Pagination组件页码/Next的a href、列表query路由、HTML链接发现与canonical策略。

实施/选择：按钮外观保留但页码/前后页使用NuxtLink/a href，并可渐进增强；从URL query决定页数、筛选。Sitemap补发现不能代替合理内链。

成本：0.5–1人日

验收：view-source有有效分页href，page2直接访问对应商品；query/canonical合规，活跃SKU在新链接图有有效路径，不把旧图候选当真实孤立。

### IMG-03 · P3 · 移动Banner复用大图且无srcset

状态：原图预算已合理；加载策略待复检

页面：https://echobae.com/

证据：本轮主Banner物理1672×941仅30278B，第二张89526B；首轮移动无srcset/fetchpriority auto，文件没有大到必须进一步压缩。

未确定：当前Banner布局/priority是否调整未知；单换格式的收益不能估计。

修改位置：Banner响应式source和优先级，首图尺寸占位优先归PERF-04。

实施/选择：A先加width/height和当前首图high、延后其他图；B合适尺寸候选作为次要优化；C维持30KB首图质量不做无意义二次压缩。

成本：0.5人日，随图片组件整改

验收：主体清晰且首图早请求，下一张切换不空白；不要只追求更小文件损伤细节。

### SEO-08 · P3 · 商品Schema基础有效但变体/图片字段仍需发布校验

状态：基础已通过，变体/资格待验证

页面：https://echobae.com/p/demo-sh-020、https://echobae.com/p/demo-sh-030、https://echobae.com/p/demo-sh-060、https://echobae.com/p/demo-sh-080；完整URL见CSV，退休历史URL需与当前目录交叉

证据：三SKU首轮Product SKU/USD基础价与本轮API一致；InStock与track_inventory=true、available_quantity100自洽，但实体库存未证。

未确定：变体SKU、生产ready含义、真实库存与Google富结果资格未知。FAQ结构缺陷另见SEO-10。

修改位置：商品Schema生成器4FfVxrIF.js和PDP buildPageSeo; JSON-LD额外数据。

实施/选择：A保持已正确的基础Product，不添加假评分；B有真实独立SKU再建ProductGroup/variants；把HTML excerpt转纯文本及去重图片作为低优先级。

成本：0.5–1人日（估算）

验收：默认SKU/价格/货币对齐；选项语义与实际SKU策略明确，额外Schema和OG图片尺寸与真实资源一致；官方工具由开发执行。

## 发布前共同验收

目录清理/政策与价格→浏览器功能和图片/性能→开发沙盒交易与账户追踪→正式发布窗口索引/Sitemap。任何未执行项保持“未验证”；失败日志不删除，报告记录修复前后日期和版本。
