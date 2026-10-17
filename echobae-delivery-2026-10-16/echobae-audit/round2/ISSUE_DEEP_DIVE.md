# 问题逐项深度分析

42条追踪记录 = 原37个ID完整保留 + 5项新增。并非42个当前确认未修故障：CAT-01部分改善；PERF-03合并；TRACK-01/SEO-08/CONT-05是待核验/优化。数据日期必须与状态一起读。

第三方内部源码/后台均未访问，构建产物只是公开客户端代码。文中组件名由公开__name读取；原始Vue/Nuxt/后端文件路径需开发自行映射，未假装获得源文件。

## SEO-01 · P0 · 全站禁止抓取与索引（上线前可能有意设置）

原优先级：P0；状态：上线条件（保留预发布限制）

页面/模板：https://echobae.com/、https://echobae.com/products、https://echobae.com/collections/new-arrival、https://echobae.com/collections/best-value、https://echobae.com/custom-made；首轮观察范围完整URL列表在ISSUES_ROUND2.csv（已退休URL不应当作今天仍活跃）

**已确认原因/事实：** 当前robots仍Disallow:/；SSR载荷discourage_search_engines=true；当前SEO助手先判断该全局标志，再考虑单页robots。

**仍为假设/缺信息：** robots和Sitemap的服务端生成逻辑未见；不能证明其都由同一后台开关控制。当前加载壳还使业务meta根本未输出。

**影响：** 正式开放自然搜索前不能满足抓取和索引条件；不说明Google实际收录率

**定位/修改位置：** 当前入口BFXRDhpD.js的主题/SEO配置，4FfVxrIF.js的robots计算；服务端robots端点。

**实施方案：** 保留预发布限制直到正式验收。发布时仅对公开营销/商品/文章页解除noindex并开放robots；购物车、结账、账户、站内搜索继续按用途排除。先允许抓取，Google才能读取noindex变更；同步Sitemap和GSC检查。

**可选方式与影响：** A正式发布窗口解除全局开关、同步公开页meta与robots；B仅暂时局部白名单开放，维护成本更高。不要只改商品meta index而保留全局锁。

**运营/开发：** 运营+开发

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.5–1人日（估算）

**复检：** 先修SEO-09；公开HTML完整且无noindex，robots允许页面/必需资源；交易/搜索/账户按用途排除。GSC实时测试与实际索引分别验证。

**证据：** 首轮：evidence/crawl.json：227个HTTP200 URL均有noindex,nofollow；evidence/http-checks.json：robots.txt为User-agent:* / Disallow:/。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## CAT-01 · P1 · 主商品列表公开展示 Demo、测试及复制商品

原优先级：P0；状态：部分改善，待前台验收

页面/模板：https://echobae.com/products、https://echobae.com/pages/help、https://echobae.com/p/demo-sh-020、https://echobae.com/p/demo-sh-030、https://echobae.com/p/demo-sh-060；首轮观察范围完整URL列表在ISSUES_ROUND2.csv（已退休URL不应当作今天仍活跃）

**已确认原因/事实：** 当前英文公开列表API四页合计72个唯一商品，未发现demo/e2e/copy/test命名；demo-sh-030、e2e-ship-heavy、代表复制SKU的API均404。首轮已确认这些SKU公开为active。

**仍为假设/缺信息：** 后台如何下架/删除、其他语言与缓存推荐是否同步未知；当前浏览器页面尚未复测。

**影响：** 污染商品发现、品牌可信度、搜索内容和误购风险

**定位/修改位置：** 后台商品发布/语言可见性；公开catalog/products服务和各推荐数据源。无后台菜单证据。

**实施方案：** 保持已清理的英文72 SKU目录，先验收旧测试URL/推荐缓存/其他语言；有残余再按正式白名单下架。不要对已经404的商品重复提批量删除任务。

**可选方式与影响：** A保留现有清理并做72 SKU白名单验收，最低风险；B对残余旧URL返回404/410，只有真正迁移商品一对一301。不要根据旧清单批量删除已清理内容。

**运营/开发：** 运营+开发

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 复检0.5人日，残余修复另估

**复检：** 当前72 SKU浏览器分页、搜索、Help推荐均无Demo；旧Demo HTML状态与API404一致；其他语言如要发布再验。

**证据：** 首轮：evidence/browser-discovery.json：/products 显示189 items，首屏 Pro Smart Scale、Video Doorbell 等；99个 /p/demo-sh-* URL；另有test888命名及4个(copy)商品，测试用途需运营核实。evidence/pagination.json 完整分页。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## SEO-02 · P1 · sitemap.xml为空索引

原优先级：P1；状态：待修改

页面/模板：https://echobae.com/sitemap.xml

**已确认原因/事实：** 今天sitemap.xml仍为空sitemapindex；公开SEO载荷product limit5000，当前72商品远低于限制，不能用数量上限解释空表。

**仍为假设/缺信息：** 是有意预发布禁用、发布过滤还是路由生成失败未知；未访问服务器Sitemap源码。

**影响：** GSC无有效URL清单；新站发现效率降低

**定位/修改位置：** Sitemap服务端查询/输出、正式内容发布清单、canonical策略。

**实施方案：** 生成只包含已发布、200、自引用规范且允许索引页面的urlset或非空索引；剔除Demo、参数、搜索、账户、交易及失效URL；发布后提交GSC。

**可选方式与影响：** A单urlset用于当前规模，简单且够用；B索引+按语言/类型分片，适合扩展。以已发布、200、规范、允许索引页面为数据源。

**运营/开发：** 开发+运营

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.5–1人日（估算）

**复检：** 不要把历史228全放入；只纳入当前正式72 SKU和有效分类/文章/内容页；排除退休测试、搜索、交易、低价值参数；lastmod只反映真实内容更新。

**证据：** 首轮：evidence/http-checks.json：HTTP200，<sitemapindex ...></sitemapindex>，0个子Sitemap。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## POL-01 · P1 · 隐私政策保留服务器国家占位符

原优先级：P1；状态：历史已验证，现状待复检

页面/模板：https://echobae.com/privacy-policy

**已确认原因/事实：** 首轮公开正文两处服务器国家占位，属于已输出内容未完成，不是根据行业模板推测。

**仍为假设/缺信息：** 真实服务器国家、法律实体、第三方处理与数据保留承诺未获后台证据；本轮未复测正文。

**影响：** 用户无法了解真实数据存储和跨境处理位置

**定位/修改位置：** 运营政策正文编辑；开发/供应商提供真实数据处理信息。

**实施方案：** 运营向开发/供应商核实国家、法律实体、数据处理和真实保留期限；据事实替换两处占位并审核承诺，不编造数据位置。

**可选方式与影响：** A核实事实后完整修订；B无法确认的承诺先改为准确可验证说明，不能猜国家或法律义务。

**运营/开发：** 运营（开发提供事实）

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.5–1人日（估算）

**复检：** 两处占位移除；主体、存储/跨境和联系信息经负责人确认；保存政策版本和更新时间。

**证据：** 首轮：evidence/page-text.json：[Country, e.g., United States / Germany / Singapore]、[Country Where Servers Are Located]。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## POL-02 · P1 · 配送时效在首页和政策中矛盾

原优先级：P1；状态：历史已验证，现状待复检

页面/模板：https://echobae.com/、https://echobae.com/shipping-policy

**已确认原因/事实：** 首轮首页3–7天与物流页10–14工作日/30–35天并存；同一业务信息的输出不一致。

**仍为假设/缺信息：** 具体真实时效、生产周期和不同目的地是否确实不同未知。

**影响：** 错误交付预期影响售前咨询与退款争议

**定位/修改位置：** 首页FAQ内容、商品FAQ、物流政策与结账配送率文案。

**实施方案：** 运营核实真实路线和生产周期，统一所有FAQ、商品FAQ、政策和结账配送说明。建议首页改为：“Delivery time depends on your destination and shipping method. See our Shipping Policy for current estimates. Production time is additional.”

**可选方式与影响：** A用统一配送事实表生成各页面；B先把首页改成到物流政策的清楚指引，减少多处独立维护。

**运营/开发：** 运营+开发

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.5–1人日（估算）

**复检：** 分别验证Standard/Express+生产期+目的地；FAQ Schema同步内容，不只改可见文本。

**证据：** 首轮：首页FAQ发货后3–7 days；Shipping Policy Express 10–14 business days、Standard 30–35 days after dispatch，均不含生产。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## POL-03 · P1 · 退款政策含缺失运费金额和未核实支付渠道

原优先级：P1；状态：历史已验证，现状待复检

页面/模板：https://echobae.com/return-refund-policy

**已确认原因/事实：** 首轮退款正文确有$ *金额占位及支票/fax等渠道；本轮付款可用性API仅确认Stripe/PayPal及钱包布尔状态。

**仍为假设/缺信息：** 线下付款、真实最低运费、法定权利、瑕疵处理未知，不能以API没有支票就认定线下付款绝不存在。

**影响：** 政策不可执行且可能误导付款/运费

**定位/修改位置：** 退款/取消/付款政策正文；商务/法务事实核验。

**实施方案：** 用经核实费率替换$ *；如没有最低价，改“Shipping costs are shown at checkout before payment.”；删除未提供的付款方式，明确取消、瑕疵/错发处置与法律适用例外；由运营/法务确认，勿捏造退款权利。

**可选方式与影响：** A仅列实际线上渠道；B如保留线下渠道，明确独立授权流程和联系路径。无统一最低运费时改成checkout显示费率，不编造金额。

**运营/开发：** 运营

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.5–1人日（估算）

**复检：** $ *清除；线上/线下渠道与已批准业务一致；损坏/错发/取消流程明确。与CONT-06的30天退货Demo同步修正。

**证据：** 首轮：公开文本International shipping ... starts from $ *；列Personal check/Cashier’s check/Money order/电话fax付款；结账只展示Stripe、PayPal。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## CART-01 · P1 · 购物车及结账划线价与商品页不一致

原优先级：P1；状态：公开实现已确认，待修改

页面/模板：https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia、https://echobae.com/cart、https://echobae.com/checkout

**已确认原因/事实：** 当前入口映射CartV2 B63DM7Lk.js:635和CheckoutV2 B7-ND3fn.js:2158均用单价×1.2算比较价；PDP用API compare_at_price1800。不是仅仅猜价格映射错误。

**仍为假设/缺信息：** 服务端cart/quote DTO是否有真实compare_at_price字段仍需开发确认；本轮未重新加车。

**影响：** 虚高折扣展示影响可信度；实付单价及2件小计本次一致

**定位/修改位置：** CartV2的K()与CheckoutV2的ee()；PDP价格模型；cart/quote响应序列化字段。

**实施方案：** 统一PDP/cart/checkout的SKU和选项价格模型，保留真实compare_at_price，缺失原价则不展示划线价或节省金额；禁止自动虚构原价。

**可选方式与影响：** A立即删掉派生划线价和Saved，最小安全修复；B数据契约传真实比较价（SKU+配置），三页统一；绝不拿售价固定加20%制造折扣。

**运营/开发：** 开发（运营核对原价）

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 1人日（估算）

**复检：** Lydia基础1609.99/真实1800；AI1689.98，2件3379.96，三页相同真实原价或统一不显示；运费/优惠后按真实基准计算，后台重算实付金额。

**证据：** 首轮：evidence/browser/cart-verify.json：选AI后PDP $1689.98/$1800.00，购物车$1689.98/$2027.98，节省$338；无AI结账$1609.99/$1931.99。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## POL-04 · P1 · 结账要求同意条款，但没有可访问的条款链接

原优先级：P1；状态：公开实现已确认，待修改

页面/模板：https://echobae.com/checkout

**已确认原因/事实：** 当前CheckoutV2条款是纯span翻译文案，无a[href]；Ce()先检查同意checkbox后调用提交。缺的是可阅读链接，不是已经证明同意校验失效。

**仍为假设/缺信息：** Terms正式URL和后台是否可设置未知；服务端是否记录接受版本/时间未知。

**影响：** 购买前不能阅读被要求同意的文本

**定位/修改位置：** CheckoutV2条款label/span；公开条款CMS页、Footer导航；订单协议字段。

**实施方案：** 运营提供适用条款正文和实际公开URL；开发把确认文案链接到200可读条款并保留购物车状态；补充Footer链接。不要假定404猜测路径即为唯一合法地址。

**可选方式与影响：** A新增真正的Terms链接（新页或保留会话打开）；B把政策中真实完整条款公开为独立可访问URL。不能把猜测404路径当唯一条款地址。

**运营/开发：** 运营+开发

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.5–1人日（估算）

**复检：** 可打开完整Terms且返回不丢车；不勾选拒绝提交；订单接受记录只在测试环境验证。

**证据：** 首轮：evidence/browser/checkout-checks.json：I have read and agree ... terms and conditions，links内无terms链接；导航也未发现条款页；猜测/terms-and-conditions返回404仅作辅助。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## SEO-03 · P1 · 不存在的商品详情返回200空商品壳

原优先级：P1；状态：API边界已验证；页面缺陷需SSR修复后复检

页面/模板：https://echobae.com/p/audit-nonexistent-20261013

**已确认原因/事实：** 当前随机不存在商品API404；公开PDP setup只在初始化检查error.value，无商品分支显示loading；首轮HTML确返回空200。

**仍为假设/缺信息：** API错误何时到达、SSR缓存为何保留200须服务端源代码/日志确认；不能说初始guard永远不会抛错。当前全局加载壳还会掩盖此问题。

**影响：** 无效URL可被当作软404，浪费抓取并误导用户

**定位/修改位置：** DL_6UJog.js:5656及末尾无商品loading分支；商品useAsyncData加载与Nuxt SSR错误传播。

**实施方案：** 在SSR商品查询返回not-found时输出HTTP404/410，展示清楚提示和分类返回入口；真正重命名的商品做有意义301；不得统一跳首页。

**可选方式与影响：** A页面async setup await加载后throw createError({statusCode:404})；B服务端路由校验+客户端响应式错误UI。区分真404与上游失败503，不把网络失败都返回404。

**运营/开发：** 开发

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.5–1人日（估算）

**复检：** 随机不存在slug直接HTTP404/410且有恢复导航；有效SKU200+真实正文；上游超时503/no-store或明确降级，不能缓存加载壳。

**证据：** 首轮：evidence/http-checks.json与browser/search-checks.json：HTTP200，Title Product | Echobae，仅Products标题和Footer，没有商品。普通不存在路径则404。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## IMG-01 · P1 · 商品图片srcset多候选指向同一个文件

原优先级：P1；状态：当前配置链已确认，待修改

页面/模板：https://echobae.com/collections/new-arrival、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia、https://echobae.com/p/149cm-white-hair-silicone-doll-siwei

**已确认原因/事实：** 当前BK9qvGFY.js:290 image.domains不含echobae.com，绝对媒体URL会在域名检查后原样返回；PDP和ProductImage传入普通HTML媒体sizes，当前解析器按断点键分割，退化为固定尺寸。

**仍为假设/缺信息：** 是否存在运行时provider覆盖、服务端IPX可达性和新页面最终currentSrc需复检。不能把优化服务全局不可用当确定原因。

**影响：** 浏览器无法选择真正对应分辨率资源，可能放大且增加低效下载

**定位/修改位置：** Nuxt Image配置domains/alias；PdpGalleryV2 sizes:1911；ProductImage C6D29uTs.js；NuxtImg getSizes/域名校验。

**实施方案：** 开发生成实际400/800/1200等宽度变体或使用可验证图片服务；描述符对应实际固有宽度，sizes匹配断点；运营保留清晰原图，禁止把600px文件伪称1440w。

**可选方式与影响：** A同源媒体标准化为相对/api/v1/media并使用已支持的IPX；B加入精确公共媒体域名白名单；C生成预制尺寸CDN文件。配合Nuxt sizes="100vw md:720px"等符合此版本语法的表达式，实际输出应按布局验。

**运营/开发：** 开发+运营

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 1–2人日（估算）

**复检：** 候选URL不同、物理像素匹配400w/800w等；断点HTML sizes有效；缩略图不下载1707px原图；不直接请求内部IP。

**证据：** 首轮：evidence/browser/deep.json：分类同一600×900 URL声明400w、800w；PDP同一600×900 URL声明720w、1440w，sizes=720px。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## PERF-01 · P1 · 代表页面移动端LCP持续偏慢

原优先级：P1；状态：历史实验室缺陷，控制复测待完成

页面/模板：https://echobae.com/、https://echobae.com/collections/new-arrival、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia、https://echobae.com/blog/tpe-vs-silicone-sex-doll

**已确认原因/事实：** 首轮三次中位mobile：首页LCP5.59s，分类5.61s，商品5.87s，文章4.94s；本轮未运行新Lighthouse。主Banner本轮物理30KB，不能把大图字节当唯一根因。

**仍为假设/缺信息：** 代理/背景采集、renderer初始化、轮播与渲染阻塞贡献未完成单因素实验；没有真实用户CWV。

**影响：** 首屏内容等待明显；实验室数据不能代替CrUX

**定位/修改位置：** 首页轮播/SSR初始化、公共CSS/JS；首轮LCP breakdown与network/long task记录。

**实施方案：** 先稳定首屏与加载遮罩，优先LCP图片，高优先级只给当前首屏图；减少初始依赖/未使用CSS/JS。按报告网络链与LCP分段验证，保留年龄验证机制。

**可选方式与影响：** A优先SSR与布局保留，稳定首屏；B减少首屏公共资源/延后非必要模块；C只对已确认大资源优化。按独立冷/热和年龄条件重新测量，不相加Lighthouse节约估计。

**运营/开发：** 开发

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 2–4人日（估算）

**复检：** 同配置无背景标签3次中位LCP≤2.5s；FCP/LCP/可见主内容分别记录；所有第三方成功场景补测，不能以本轮HTTP壳0.65s算性能通过。

**证据：** 首轮：evidence/lighthouse：4页×2设备×3次；首页首次mobile LCP中位5.6s，分类约5.6s，产品约5.9s，文章约4.9s；具体数字见PERFORMANCE_REPORT.md。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## PERF-02 · P1 · 主线程脚本开销与阻塞仍高

原优先级：P1；状态：阻塞已观察，具体归因待验证

页面/模板：https://echobae.com/、https://echobae.com/collections/new-arrival、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia

**已确认原因/事实：** 首轮home-mobile-1最长任务1111ms，归因document/Other，不是已定位某个hydration函数；Script Evaluation约3148ms；有长任务是事实。

**仍为假设/缺信息：** 为何document Other很长、具体业务函数、真实交互是否卡顿未知；首轮确认组保留额外背景页面且缓存，TBT高不能等同INP。

**影响：** 初始化及交互可能卡顿，尤其移动设备

**定位/修改位置：** 公开入口、主题加载/动态块/轮播挂载；DevTools主线程stack/profile需要开发采集。

**实施方案：** 对公共运行时、动态块注册、builder初始化和视口外组件做性能profile；按路由拆包、延后非首屏组件，保留交互和隐私校验。只把Lighthouse估计当诊断，不把节约量累加成收益。

**可选方式与影响：** A采样profile找函数后拆长任务/延迟非首屏；B按路由拆包；C若是测试干扰先清理背景进程重测。不能直接断言删某bundle可省整段耗时。

**运营/开发：** 开发

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 2–4人日（估算）

**复检：** EventTiming记录input/processing/presentation，关键交互3次；LongTask分解有调用栈；TBT≤200ms为实验室目标，生产p75 INP另验。

**证据：** 首轮：home-mobile-1主线程Script Evaluation约3148ms；DNfd1SfM.js未使用估算86240B；确认年龄后的3次TBT中位2150ms，不能解释为真实INP。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## CONT-01 · P1 · 五星Reviews营销文字与0条评论展示不一致

原优先级：P1；状态：历史矛盾，来源待运营核验

页面/模板：https://echobae.com/、https://echobae.com/customer-reviews、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia、https://echobae.com/p/149cm-white-hair-silicone-doll-siwei

**已确认原因/事实：** 首轮五星Reviews与0条评价系统不一致，评价数量本身未证明引语真假。

**仍为假设/缺信息：** 是否有历史真实评价、授权或不同商品来源未知；当前目录变化后不能强称所有旧问题还存在。

**影响：** 消费者无法核验“verified”来源和商品评价归属

**定位/修改位置：** 商品富文本评分文案、Customer Reviews数据源、首页客户引语、Product aggregateRating。

**实施方案：** 运营核验评价来源和授权；有真实来源则按SKU导入可追溯评价并显示数量；没有则删除五星/verified暗示，保留客观商品信息。不得编造评论或AggregateRating。

**可选方式与影响：** A有来源则按SKU导入并显示真实数量；B无来源先去五星/verified暗示，保留真实已授权引语的明确归属。

**运营/开发：** 运营+开发

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 1–2人日（估算）

**复检：** 零评价不显示可误读为评分的五星；评分/数量/Schema一致，来源授权记录可供运营核验。

**证据：** 首轮：首页客户引语和星级；Customer Reviews实际All Reviews(0)；正式商品文案⭐⭐⭐⭐⭐ Reviews但Reviews(0)。无证据证明引语真假。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## CONT-02 · P1 · Siwei商品标题与正文名称不一致

原优先级：P1；状态：SKU/选配数据已核对，业务文案待确认

页面/模板：https://echobae.com/p/149cm-white-hair-silicone-doll-siwei

**已确认原因/事实：** 首轮QY073标题Siwei、正文Aurora；当前API仍Title带AI，而Additional Upgrades明确AI+79.99。只能确认数据表达与选配价格，不确认AI是不是另有基础功能。

**仍为假设/缺信息：** Siwei/Aurora是否合法别名、AI基础/升级具体差别和头身型号业务事实未知。

**影响：** 用户难以确认型号及基础配置，退换争议风险

**定位/修改位置：** QY073商品名称、SEO meta_title、描述、addons及SKU规格表。

**实施方案：** 运营确认SKU QY073真实名称、头部/身体和AI是否标配；统一Siwei/Aurora或明确别名；AI为选配时标题移除暗示标配，说明基础配置和升级价。

**可选方式与影响：** A统一正式型号名；B明确别名及头/身体组合。若AI是选配，主名避免标配暗示；若基础与升级不同，写清差异而非盲删AI。

**运营/开发：** 运营

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.5人日（估算）

**复检：** API/H1/购物车型号一致；AI基础/升级说明和价格明确；用厂家真实配置表对照。

**证据：** 首轮：标题149cm White Hair AI Silicone Doll Siwei，Main SKU QY073，正文多次称Aurora；AI在额外升级区+$79.99。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## SHIP-01 · P1 · 结账国家及免运费展示与政策范围不一致

原优先级：P1；状态：展示风险已观察，费率/服务端待验证

页面/模板：https://echobae.com/checkout

**已确认原因/事实：** 首轮US/Canada/Brazil可选择且Standard Free；当前Checkout公共代码有quote(country,province,zip)和region not served错误映射，不是完全没有地区校验逻辑。

**仍为假设/缺信息：** 具体后台服务地区、缺邮编时报价语义、税费与最终下单校验未执行。

**影响：** 可能让不支持地区的买家误认为可配送；最终服务端限制未验证

**定位/修改位置：** Checkout quote函数、国家/省/邮编联动、shipping_rate_id、服务端quote与订单再校验。

**实施方案：** 运营确认支持国家、标准/快递费率及包税策略；开发在选择国家后明确可用路线/不可配送状态，必要时提示完整地址后报价。不能凭当前UI宣称最终订单可运巴西。

**可选方式与影响：** A仅展示支持国家/路线；B允许全国家选择但对不服务地区明确拒绝；C完整地址前标“待计算”而非默认免费。按真实经营覆盖选方案。

**运营/开发：** 运营+开发

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 1–2人日（估算）

**复检：** 已支持/不支持/偏远地区/免运阈值/税费/优惠各测试；country改后旧quote不残留；最终费用只在沙盒订单验证。

**证据：** 首轮：evidence/browser/checkout-checks.json：US/Canada/Brazil均可选择且显示Standard—Free，政策仅列10个配送国家、两种路线和按目的地计费；未填写地址、未提交订单。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## UX-01 · P1 · 年龄验证弹窗没有键盘焦点约束

原优先级：P1；状态：首轮行为+当前组件证据，待复检

页面/模板：https://echobae.com/

**已确认原因/事实：** 首轮12次Tab第三次离开AgeGate；当前公开AgeGate有aria-modal与两个按钮、记忆到期逻辑，组件未见focus trap/inert实现。

**仍为假设/缺信息：** 本轮未重新键盘验证；外围层是否新加约束未确认。

**影响：** 键盘/屏幕阅读器用户可能误操作背景，aria-modal语义与交互不符

**定位/修改位置：** AgeGateOverlay，页面根元素焦点/滚动约束，确认后焦点恢复。

**实施方案：** 在正常年龄弹窗内设初始焦点、Tab/Shift+Tab循环，背景inert；确认后还原焦点。保留确认/离开功能，不增加可绕过年龄验证的关闭方式。

**可选方式与影响：** A使用已有成熟可访问dialog组件，去掉绕过关闭入口；B手动focus循环、inert背景、restore focus。不能只添加aria-modal就认为行为已实现。

**运营/开发：** 开发

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.5–1人日（估算）

**复检：** 20次Tab/Shift+Tab不离开；回车正常确认/离开；未确认不能操作背景；正常确认记忆符合30天配置。

**证据：** 首轮：evidence/browser/age-keyboard.json：前2次Tab聚焦确认/离开，第3次进入背景Shop now，后续Search/Cart等背景控件。确认后刷新ageVisible=0且存储存在。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## PERF-04 · P1 · 首页桌面CLS三次均约0.457

原优先级：P1；状态：历史稳定复现，当前渲染未复测

页面/模板：https://echobae.com/

**已确认原因/事实：** 首轮桌面CLS三次0.456637；最大位移0.416346关联Find Your Perfect Doll。Banner CSS width100%/height:auto且未预留图像比例，与unsized诊断吻合。

**仍为假设/缺信息：** 移位的全部因果与新部署结果需要trace；Lighthouse关联不是完整调用栈证明。

**影响：** 加载过程中内容大幅移动，增加阅读/点击误操作

**定位/修改位置：** Banner .ecom-ad-carousel-v1__media/img；首屏容器和图片width/height；新adaptive图片初始比例。

**实施方案：** 给Banner图片真实width/height及容器稳定aspect-ratio；同步SSR与客户端断点尺寸，确保轮播当前项变化不改父容器高度。

**可选方式与影响：** A原尺寸width1672 height941+aspect-ratio:1672/941，保留当前视觉；B桌/移动预设各自固定比例；C容器由CMS媒体元数据先确定。不要onload后才换ratio。

**运营/开发：** 开发

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.5–1人日（估算）

**复检：** 冷加载前后Banner占位一致；desktop三次CLS≤0.1；轮播切换不改容器高度，移动回归。

**证据：** 首轮：home-desktop-1/2/3累计布局位移均0.456637；layout-shifts将主要0.416346位移关联Find Your Perfect Doll区块，并标记Banner img Media element lacking an explicit size。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## SEO-09 · P1 · 当前首页与商品SSR只输出加载壳

原优先级：新增；状态：本轮输出已确认；服务端原因待开发

页面/模板：https://echobae.com/、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia

**已确认原因/事实：** 6份成功HTML样本（5首页+1商品）都无Title/业务meta/H1/正文，shell-loading存在，tokensReady=false、branding空、业务data未填；当前CYM8kJOs layout按tokensReady选择加载壳。

**仍为假设/缺信息：** 配置初始化在SSR是否被await、内部请求失败还是已有缓存故障未知；客户端随后恢复情况未验证。不是证明Google一定不收录。

**影响：** 初始业务内容/搜索渲染成本和首屏体验依赖额外JS；HTTP200不足表示页面就绪。

**定位/修改位置：** 当前入口BFXRDhpD主题bootstrap、default/blog layout的ready门禁、SSR错误传播与缓存准入。

**实施方案：** 当前API主题/3商品200，因此不能简单把“所有配置/商品不可读”当原因；先对比服务端实际URL/超时/渲染时序和缓存。

**可选方式与影响：** A在server-safe async bootstrap await主题/品牌/locale及页面关键数据后SSR；B安全默认主题仍渲染正文和meta，必要交易禁用；C临时客户端渲染只能作为有明确SEO权衡的降级。失败不要200缓存空壳，使用准确错误状态/no-store。

**运营/开发：** 开发

**后台能力：** 未登录后台，功能与菜单未经验证

**成本粗估：** 1–3人日（含源码定位，粗估）

**复检：** 正常GET各模板有Title/meta/H1/Canonical/Schema及主要正文；模拟配置失败不产生可缓存200空壳；公开脚本和图片依然加载；正常浏览器冷启动/谷歌渲染另验。

**证据：** 见evidence/INDEX.md、ISSUE_DEEP_DIVE.md相关本轮事实及一轮原始文件。

**数据日期：** 当前HTTP/API/资源2026-10-14；复用DOM/截图2026-10-13，不混用

## CONT-06 · P1 · 定制页FAQ答案错位并遗留30天退货模板

原优先级：新增；状态：从首轮证据补发现，当前现状待复检

页面/模板：https://echobae.com/custom-made

**已确认原因/事实：** 首轮DOM首题“定制与批量有什么不同”答“Most orders ship within 2–3 business days”；HTML/FAQPage其余多题答“We offer 30-day returns on unused items in original packaging.”，与退款政策冲突。

**仍为假设/缺信息：** 本轮无新DOM，不知道运营是否已修正；不是已经证明实际处理退货不合法。

**影响：** 造成错误售前预期与购买争议，也向机器输出错误语义。

**定位/修改位置：** 定制页FAQ block的问答数据及自动FAQPage生成，不仅通用Return政策。

**实施方案：** 不是新泛泛内容建议：复核首轮已采集但漏报的具体错误答案。不要编造格式、生产或退款事实。

**可选方式与影响：** 按每个问题的真实业务回答重写或暂时隐藏未定稿项；网页问答和JSON-LD由同一事实源生成，明确报价/材料参考/订单确认/运输/取消条件。

**运营/开发：** 运营+开发

**后台能力：** 未登录后台，功能与菜单未经验证

**成本粗估：** 0.5–1人日

**复检：** 逐题与问题相关、无Demo物流/退货承诺；可见答案与FAQPage一致，与正式政策一致。

**证据：** 见evidence/INDEX.md、ISSUE_DEEP_DIVE.md相关本轮事实及一轮原始文件。

**数据日期：** 当前HTTP/API/资源2026-10-14；复用DOM/截图2026-10-13，不混用

## IMG-02 · P2 · 主要商品图在不同模板强制裁剪

原优先级：P1；状态：几何已确认；不当程度/新改造待复检

页面/模板：https://echobae.com/collections/new-arrival、https://echobae.com/collections/best-value、https://echobae.com/collections/best-sellers、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia

**已确认原因/事实：** 首轮分类方形cover裁600×900图约33%，PDP4:5裁约17%；当前ProductImage新增adaptive支持，但默认false，是否调用已启用本轮未渲染验证。

**仍为假设/缺信息：** 是否裁到关键身体/细节因图片构图而异，不能把任何cover都判错；新adaptive是否解决具体模板未知。

**影响：** 全身商品信息被截断，影响身材/姿态比较；裁剪能否接受需设计/运营确认

**定位/修改位置：** ProductCard/ProductImage的容器比例；PdpGalleryV2 .pdp-gallery__main/.pdp-gallery__image；缩略图样式。

**实施方案：** 主要商品展示优先2:3容器或contain完整展示；需方形卡片时由运营上传专用方形构图并设置焦点；不要全站盲目禁用cover。开发按图片类型区分容器。

**可选方式与影响：** A保留方形/4:5舞台改contain+一致背景，整体布局最稳定；B主要全身照片舞台2:3，手机页面变长；C运营上传专用方形构图。新增adaptive必须在加载前预留正确比例。

**运营/开发：** 设计+开发+运营

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 1–2人日（估算）

**复检：** 主图/放大图保留需要的头身细节；缩略图可适度聚焦；混合竖/横图不拉伸；390/768/1440截图人工确认且CLS≤0.1。

**证据：** 首轮：evidence/browser/deep.json：600×900分类图340×340 cover，约裁掉原图高度1/3；Lydia主图342×427.5 cover，约裁掉1/6高度。这是CSS几何裁剪，不等于原文件损坏。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## FE-01 · P2 · runtime-blocks在所有深度样本中返回404

原优先级：P2；状态：接口/前端fallback已确认，依赖待开发核实

页面/模板：https://echobae.com/、https://echobae.com/about-us、https://echobae.com/blog、https://echobae.com/blog/silicone-sex-doll-buying-guide、https://echobae.com/blog/tpe-vs-silicone-sex-doll；首轮观察范围完整URL列表在ISSUES_ROUND2.csv（已退休URL不应当作今天仍活跃）

**已确认原因/事实：** 当前入口runtime-blocks的函数遇非OK返回[]，插件await后只在非空列表注册模块；这是可选注册机制失败，不足说明全站功能失效。

**仍为假设/缺信息：** 服务端接口为何404、有没有必需扩展模块未知；不能把所有商品/图片问题归因该API。

**影响：** 动态扩展模块无法注册并产生Console噪音；未证实哪个正式模块依赖此接口

**定位/修改位置：** 入口z$/W$/K$，公开/content/runtime-blocks，动态模块注册表。

**实施方案：** 开发核查公开/content/runtime-blocks路由、模块注册表和当前发布配置；功能启用则实现/恢复200数据；未使用则停请求或约定200空列表。源码路径未知，不虚构文件名。

**可选方式与影响：** A不使用扩展则不请求；B使用但无记录返回200 []；C有记录返回完整清单并验证module_url。按真实用途处理，不加无意义假模块。

**运营/开发：** 开发

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.5–1人日（估算）

**复检：** 冷启动无无意义404；所有必需block/模块实际存在；一次SPA初始化与每路由请求区分。

**证据：** 首轮：evidence/browser/deep.json 58个视口记录均404；evidence/public-js/DNfd1SfM.js公开函数z$在!response.ok时返回[]，W$只在列表非空时注册T$。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## FE-02 · P2 · 多模板出现Hydration mismatch

原优先级：P2；状态：警告已验证，根因未完全确定

页面/模板：https://echobae.com/about-us、https://echobae.com/blog、https://echobae.com/blog/silicone-sex-doll-buying-guide、https://echobae.com/blog/tpe-vs-silicone-sex-doll、https://echobae.com/blog/what-are-the-most-realistic-sex-dolls；首轮观察范围完整URL列表在ISSUES_ROUND2.csv（已退休URL不应当作今天仍活跃）

**已确认原因/事实：** 首轮49/58记录Hydration警告，无未捕获pageerror。新HTML tokensReady=false与客户端布局按ready分支可产生状态差异，但未捕获同节点差异的trace。

**仍为假设/缺信息：** SSR父子状态更新时间、主题tokens、locale字典、page-breadcrumb-store等都是候选，不当成确定内部根因。

**影响：** SSR与客户端状态不一致，可能造成重渲染/闪动，具体性能归因待验证

**定位/修改位置：** 主题bootstrap、default/blog layout、Nuxt async data、面包屑状态。

**实施方案：** 开发用Nuxt/Vue hydration调试定位最小差异，比较服务端数据与客户端首轮数据、tokens/locale；只把浏览器专属渲染放在正确边界，避免全页client-only。

**可选方式与影响：** A先解决SEO-09完整SSR、序列化相同初始状态；B按具体节点修复；不把全站包ClientOnly或屏蔽Console当修复。

**运营/开发：** 开发

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 1–2人日（估算）

**复检：** 开发模式定位mismatch节点/文本；初始DOM/首次hydrate一致，警告消失；重测冷启动及SPA。

**证据：** 首轮：evidence/browser/deep.json：49/58个记录含Hydration completed but contains mismatches，无未捕获pageerror；首始H1/DOM变化另见SEO-04。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## SEO-04 · P2 · 初始HTML与渲染DOM的主标题不一致

原优先级：P2；状态：输出差异已确认，SSR时序待验证

页面/模板：https://echobae.com/products、https://echobae.com/collections/new-arrival、https://echobae.com/collections/best-value、https://echobae.com/custom-made、https://echobae.com/contact-us；首轮观察范围完整URL列表在ISSUES_ROUND2.csv（已退休URL不应当作今天仍活跃）

**已确认原因/事实：** 首轮初始Home/Collections/Products与DOM真实H1不同；页面写page-breadcrumb-store，布局读它并有通用fallback，PDP showPageTitle:false。

**仍为假设/缺信息：** 父布局何时SSR读取子页写入状态需要源码调试；H1差异与hydration警告不能直接等同一原因。

**影响：** JS未完成时主题不明确、可访问结构重复；多H1本身不是自动排名惩罚

**定位/修改位置：** C_kT0Sim.js共享breadcrumb store；DsOVWUii.js布局title fallback；DL_6UJog.js页面breadcrumb设置。

**实施方案：** SSR直接输出真实页面名称；商品保留唯一主要商品H1，面包屑用nav/普通文本；博客列表保留一个The Blog主标题。不要机械增加正文。

**可选方式与影响：** A父层从已await页面数据/路由meta取标题，避免子组件渲染中改父SSR状态；B面包屑只nav文字、H1由页面自己渲染。博客移除重复外层H1。

**运营/开发：** 开发

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 1人日（估算）

**复检：** 修SEO-09后view-source/DOM主H1一致；商品只有主商品H1、Blog无两份The Blog，H2/H3层级按正文。

**证据：** 首轮：evidence/crawl.json含Home/Collections/Products通用H1；deep.json中Contact变Contact Us、分类变New Arrivals、正式商品只留商品H1。/blog则渲染后仍两个The Blog H1。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## SEO-05 · P2 · Title品牌后缀重复

原优先级：P2；状态：生成机制已确认，待修改

页面/模板：https://echobae.com/blog、https://echobae.com/blog/silicone-sex-doll-buying-guide、https://echobae.com/p/149cm-christmas-silicone-love-doll-huaze、https://echobae.com/p/170cm-realistic-silicone-sex-doll-jiachen、https://echobae.com/p/159cm-natural-look-silicone-doll-jiachen；首轮观察范围完整URL列表在ISSUES_ROUND2.csv（已退休URL不应当作今天仍活跃）

**已确认原因/事实：** 当前PDP seo.meta_title已含|Echobae；当前入口up().formatPageTitle对非首页无条件追加separator+site_name。不是已证明某Vue titleTemplate造成。

**仍为假设/缺信息：** 第三方后台是否有全局批量SEO模板未知；本轮HTML缺title，不能称今天DOM已看到双后缀。

**影响：** 搜索标题冗余和可读性下降

**定位/修改位置：** BFXRDhpD.js:35901格式化；4FfVxrIF.js调用；SKU seo.meta_title字段。

**实施方案：** 优先统一titleTemplate去重或明确后台填写规范。Lydia推荐“159cm Lifelike Silicone Sex Doll Lydia | Echobae”，核心主题保留；购买指南只保留一个品牌。

**可选方式与影响：** A明确seo.meta_title为最终成品，存在时不再追加，内容title才格式化；B运营统一SEO字段不含品牌；C格式化器仅去重精确尾部品牌，不全局删除商品中品牌词。

**运营/开发：** 开发+运营

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.5人日（估算）

**复检：** QY029最终159cm Lifelike Silicone Sex Doll Lydia | Echobae，只一个后缀；首页当前合理标题不改；覆盖首轮76页并与现存SKU清单交叉。

**证据：** 首轮：evidence/crawl.json：76个页面Title出现多次Echobae，如Lydia ... | Echobae | Echobae、buying guide ... | Echobae | Echobae。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## SEO-06 · P2 · 参数页重复标题并自引用Canonical

原优先级：P2；状态：策略缺口/生成来源待复核

页面/模板：https://echobae.com/blog?category=Buyer+Guide、https://echobae.com/blog?category=updates、https://echobae.com/products?tag=bestseller、https://echobae.com/products?tag=smart-home、https://echobae.com/products?tag=sale；首轮观察范围完整URL列表在ISSUES_ROUND2.csv（已退休URL不应当作今天仍活跃）

**已确认原因/事实：** 首轮12参数页自引用query Canonical和重复Title；当前通用SEO helper默认route.path，不直接取fullPath，因此“全局按当前完整URL生成”不是已证实根因。

**仍为假设/缺信息：** 参数是由调用方path、canonical override或SSR层注入未知；自引用筛选不必然错误，也没有排名数据证明蚕食。

**影响：** 解除全局noindex时可能形成低价值筛选索引与主题重复；不同结果不必一律canonical首页

**定位/修改位置：** SEO helper canonicalOverride/path；列表SEO调用方；服务端canonical处理。

**实施方案：** 运营选定独立有价值分类落地页，其余搜索/筛选保持noindex；相同内容参数使用规范URL，实质不同内容不要虚假canonical；分页用稳定可抓取href和各页正确canonical。

**可选方式与影响：** A有独立价值的筛选升级正式分类并index；B其余noindex且可抓取；C真正相同内容sort/tracking规范到无参数。分页内容不同不全canonical到第一页。

**运营/开发：** 开发+运营

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.5–1人日（估算）

**复检：** 明确url规则表；sort追踪参数去重、内容型筛选按白名单；page=2独立规范；直接HTTP与DOM策略一致。

**证据：** 首轮：evidence/crawl.json：10个products?tag页Title相同且Canonical含tag；2个blog?category页也自引用。当前全局noindex。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## SEO-07 · P2 · 购买指南链接到404护理文章

原优先级：P2；状态：历史已验证，现状待复检

页面/模板：https://echobae.com/blog/silicone-sex-doll-buying-guide、https://echobae.com/blogs/silicone-doll-care-guide

**已确认原因/事实：** 首轮buying-guide的护理链接确指向/blogs旧404；存在/sex-doll-care有效候选。

**仍为假设/缺信息：** 内容后台是否已修改、旧链接的真实外链流量未知。

**影响：** 用户阅读路径中断

**定位/修改位置：** 文章正文href，旧路由单条重定向。

**实施方案：** 运营将该文链接改为真实相关护理内容（当前/sex-doll-care可作为候选）；若旧链接曾对外传播开发设置一对一301。

**可选方式与影响：** A替换为现有相关Care页；B发布实际目标文章并一对一301旧地址。不能把所有404重定向首页。

**运营/开发：** 运营+开发

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.25人日（估算）

**复检：** 点击护理内链200且相关，canonical一致；保留旧URL跳转测试。

**证据：** 首轮：crawl.json：指南链接/blogs/silicone-doll-care-guide；目标404，现有护理页/sex-doll-care返回200。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## UX-02 · P2 · 移动端轮播箭头覆盖正文区域

原优先级：P2；状态：首轮视觉+CSS定位，待复检

页面/模板：https://echobae.com/

**已确认原因/事实：** 首轮390截图箭头压正文；旧Banner CSS在max639px把42px控件absolute top50% left/right8px。

**仍为假设/缺信息：** 今天完整视觉未复测，不能说当前每个滑块都覆盖文字。

**影响：** 文字与控制争夺触摸/阅读区域

**定位/修改位置：** Banner移动nav/content CSS规则。

**实施方案：** 设计/开发将移动箭头移至底部独立区域或使用明确分页控制，保留触摸切换；正文不能被控件覆盖。

**可选方式与影响：** A移动箭头下移独立控制区；B留两侧控制安全区/分页点；C正文放图下独立块，移动高度会增加。

**运营/开发：** 设计+开发

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.5人日（估算）

**复检：** 390/412/768各滑块正文不被控件覆盖，按钮点击区域≥合理触摸尺度并可键盘使用。

**证据：** 首轮：evidence/previous/mobile-viewport.png（390×844）：左右白色圆箭头叠在“A private space...”文字所在高度；本次settled截图供复核。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## UX-03 · P2 · Footer暴露翻译键footer.poweredBy

原优先级：P2；状态：缺键与调用机制已确认，待修改

页面/模板：https://echobae.com/cart、https://echobae.com/checkout

**已确认原因/事实：** 本轮英文storefront-ui-messages返回footer字典无poweredBy；当前DsOVWUii.js:3739调用$t(footer.poweredBy)，与首轮裸key吻合。

**仍为假设/缺信息：** 是否还有其他locale缺项、完整字典合并/切换时序未知；不是已经证明所有i18n初始化失败。

**影响：** 界面出现实现细节破坏可信度

**定位/修改位置：** 公开UI消息footer.poweredBy；FooterPoweredBy组件及locale加载/merge规则。

**实施方案：** 开发统一加载语言字典，补缺项/安全fallback；检查前后端locale初始化。

**可选方式与影响：** A补全真实英文poweredBy翻译；B允许明晰安全fallback。其他语言各补，避免用setLocaleMessage覆盖掉基础字典缺项。

**运营/开发：** 开发

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.25–0.5人日（估算）

**复检：** en及所有发布语言不出现裸key；SSR和SPA购物车/结账Footer一致。

**证据：** 首轮：cart-verify.json和checkout-checks.json可见footer.poweredBy；某些初始HTML/其他页正常Powered by wiipoo。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## CONT-03 · P2 · FAQ重复问答02与03

原优先级：P2；状态：历史已验证，现状待复检

页面/模板：https://echobae.com/faq

**已确认原因/事实：** 首轮FAQ第02/03题及答完全相同。

**仍为假设/缺信息：** 本轮未验证运营是否已去重；不推断内部导入脚本原因。

**影响：** 降低内容清晰度和帮助信息密度

**定位/修改位置：** FAQ条目内容与顺序。

**实施方案：** 运营删除重复条目或替换成真实不同问题并重新编号；不为SEO增加无关问题。

**可选方式与影响：** A删掉重复并重编号；B有真实常见问题再替换，别为SEO硬加字数。

**运营/开发：** 运营

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.25人日（估算）

**复检：** 公开问答/相关Schema均无重复，编号连续。

**证据：** 首轮：page-text.json：02/03标题和回答均为removable vs fixed，完全重复。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## CONT-04 · P2 · 首页社媒图标链接到平台首页

原优先级：P2；状态：历史已验证，现状待复检

页面/模板：https://echobae.com/

**已确认原因/事实：** 首轮7个社媒图标href为平台根域。

**仍为假设/缺信息：** 真实品牌账号、后台导航编辑能力、本轮链接现状未知。

**影响：** 不能找到品牌账号，可能分流访客

**定位/修改位置：** 社媒URL配置/公共header-footer或页面block。

**实施方案：** 运营填写真实品牌主页URL；尚无账号则移除对应图标，勿造账号地址。

**可选方式与影响：** A填写真实品牌主页；B无账号的图标隐藏。不要编造账号或保留平台根链接。

**运营/开发：** 运营（后台功能未验证）

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.25人日（估算）

**复检：** 每个保留图标到真实品牌帐号，无平台根URL，标签可读。

**证据：** 首轮：deep.json首页7个aria标签社媒链接为linkedin.com、x.com、facebook.com、youtube.com、instagram.com、pinterest.com、tiktok.com根路径。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## SEC-01 · P2 · Demo详情HTML暴露私有HTTP图片地址

原优先级：P2；状态：历史问题，公开目录改善后待验收

页面/模板：https://echobae.com/p/demo-sh-020、https://echobae.com/p/demo-sh-030、https://echobae.com/p/demo-sh-060、https://echobae.com/p/demo-sh-100、https://echobae.com/p/demo-sh-009；首轮观察范围完整URL列表在ISSUES_ROUND2.csv（已退休URL不应当作今天仍活跃）

**已确认原因/事实：** 首轮28Demo HTML引用内部HTTP媒体；当前图片provider的内部alias属于服务端图片取图配置，不等同浏览器直接访问内部地址。

**仍为假设/缺信息：** 旧Demo清理后残余页面/其他媒体字段是否仍泄露未知；内部端口调整未据此推断服务器架构安全性。

**影响：** 公网浏览器不可正常加载内部地址并有混合内容/内部拓扑暴露

**定位/修改位置：** 公开媒体字段规范化与IPX provider的客户端URL/服务端origin分离。

**实施方案：** 随CAT-01移除Demo；开发统一媒体存储规范公网HTTPS URL并拦截内容录入内部IP/localhost引用。停止测试这些内部地址，不开展私网探测。

**可选方式与影响：** A先验收现有Demo移除；B对公开content URL拒绝私有host，内部取图origin只作服务端配置。不要盲删合法服务端alias导致所有IPX失效。

**运营/开发：** 开发+运营

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.5–1人日（估算）

**复检：** 当前公开HTML/img/currentSrc/Schema无内部HTTP URL；IPX输出仍公网HTTPS；不做私网探测。

**证据：** 首轮：evidence/private-image-urls.json：28个公开Demo商品页面img指向http://172.17.0.1:8093/...；不是凭此证明服务器被入侵。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## SEC-02 · P2 · 公开200页面缺少统一安全响应头

原优先级：P2；状态：公开可见头已观察，源站配置待验证

页面/模板：https://echobae.com/、https://echobae.com/products、https://echobae.com/collections/new-arrival、https://echobae.com/collections/best-value、https://echobae.com/custom-made；首轮观察范围完整URL列表在ISSUES_ROUND2.csv（已退休URL不应当作今天仍活跃）

**已确认原因/事实：** 首轮200只见HSTS而错误页有nosniff等；本轮成功文档仍见HSTS、未见CSP等。

**仍为假设/缺信息：** 代理是否移除头、源站与CDN路由差别未知，无攻击利用测试。

**影响：** 减少纵深防护；没有实际XSS/点击劫持攻击证据

**定位/修改位置：** 源站/CDN HTML响应头与错误响应配置。

**实施方案：** 开发核查源站与CDN实测头；对HTML启用nosniff和适当Referrer-Policy，设计frame-ancestors；CSP先Report-Only并兼容支付/必要外域，再收紧。勿盲目DENY导致支付集成故障。

**可选方式与影响：** A先CSP Report-Only观测必要支付域，后落实frame-ancestors等；B先nosniff/referrer最小加固。不要以缺头声称严重漏洞或统一DENY破坏支付。

**运营/开发：** 开发

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.5–1人日（估算）

**复检：** 正常公网复核headers和支付嵌入，CSP无破坏；有report样本与受控验证，不进行攻击扫描。

**证据：** 首轮：crawl.json：227个200均有HSTS；未见CSP/X-Content-Type-Options/X-Frame-Options/Referrer-Policy，404页反而带nosniff/DENY/no-referrer。代理可能影响响应头可见性。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## TRACK-01 · P2 · GTM已嵌入，但事件与隐私承诺未验证

原优先级：P2；状态：待账号与正常网络验证

页面/模板：https://echobae.com/、https://echobae.com/privacy-policy

**已确认原因/事实：** 首轮GTM容器公开可见但代理失败；本轮没有打开GA4/GSC/GTM账号，也没有新的浏览器网络。

**仍为假设/缺信息：** 哪些tags/event/Consent Mode、是否实际外发成人商品或PII未知，不能凭GTM存在就指控泄露。

**影响：** 不能证明电商追踪或同意管理正确；潜在承诺与实际配置不符

**定位/修改位置：** GTM预览/GA4 DebugView、dataLayer、隐私政策与同意规则。

**实施方案：** 运营和开发在GTM预览/GA4 DebugView验证view_item/add_to_cart/begin_checkout（purchase用测试环境）；审核数据最小化与同意管理，避免不必要成人商品/身份数据外发；按真实情况修订政策。

**可选方式与影响：** A最小必要测量并同意管理；B不开分析则移除未用tag/修正文案。真实purchase仅测试环境；运营选择实际方案。

**运营/开发：** 运营+开发

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 1–2人日（估算）

**复检：** view_item/add_to_cart/begin_checkout/purchase单次且参数正确，无PII，拒绝/同意状态网络符合承诺，需账号或开发证据。

**证据：** 首轮：公开请求GTM-T2DKHJKK；请求在代理中失败。政策承诺不向外部营销/第三方分析披露成人浏览信息，并列Optional Analytics Cookies。无法读取容器/GA4/GSC账户。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## PERF-03 · P2 · 首屏存在可减小的公共CSS/JS负载

原优先级：P2；状态：合并至PERF-01

页面/模板：https://echobae.com/

**已确认原因/事实：** 首轮unused CSS/JS估计与阻塞链是PERF-01资源瓶颈子任务，不应另算一组重复工期。

**仍为假设/缺信息：** 具体未用逻辑能否剔除、实际收益未知。

**影响：** 增加首屏下载/解析及阻塞链

**定位/修改位置：** blocks-built.css按block构建，shared runtime按路由/组件分包。

**实施方案：** 按当前页面block拆分样式，保留关键CSS并延后非关键样式；按路由拆分公共JS。避免purge动态类后破坏builder；实测而非累加Lighthouse估算收益。

**可选方式与影响：** 合并到PERF-01资源优化工作包；保留本ID作为CSS/JS验收子项，不另提重复上线工单。

**运营/开发：** 开发

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 并入PERF-01，不重复计费

**复检：** CSS/JS字节和阻塞链下降，组件截图/动态类不丢，重复性能有改善。

**证据：** 首轮：home-mobile-1：blocks-built.css 26251B，unused估计22227B；StoreFooter CSS约10016B阻塞；DNfd1SfM.js传输约243593B、未使用估计86240B。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## UX-04 · P2 · CTA和比较价文字对比度未达到自动化阈值

原优先级：P2；状态：历史自动化失败，现状待复检

页面/模板：https://echobae.com/、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia

**已确认原因/事实：** 首轮Lighthouse节点Explore红/白3.74:1、比较价灰/白2.53:1，16px普通文本阈值4.5。

**仍为假设/缺信息：** 本轮computed色值/hover/focus以及新主题值未复测。

**影响：** 低视力用户阅读价格与操作困难

**定位/修改位置：** 主题accent/on-accent/muted组合；Explore按钮与PDP comparison文本。

**实施方案：** 设计/开发调整CTA文字或背景、比较价灰色，普通文本至少4.5:1，大文本至少3:1；保留品牌色用于适合的非文字装饰。

**可选方式与影响：** A加深文字/调整背景确保对比；B保持品牌色于非文字装饰。不能只改背景不看组件状态。

**运营/开发：** 设计+开发

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.5人日（估算）

**复检：** 相关节点普通文字≥4.5:1、大字≥3:1；focus/disabled分别检查。

**证据：** 首轮：home-mobile-1 color-contrast：Explore #ff2929/白色比3.74:1；product-mobile-1 比较价#9ca3af/白色2.53:1，16px普通文本预期4.5:1。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## UX-05 · P2 · 营销弹窗在购物及结账过程中打断操作

原优先级：P2；状态：历史摩擦，当前规则待核验

页面/模板：https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia、https://echobae.com/checkout

**已确认原因/事实：** 首轮营销弹窗实际拦截购物/优惠码；当前MarketingPopup公开代码按path/locale取配置并在年龄验证后按delay/scroll触发。

**仍为假设/缺信息：** 后台排除路径是否已更新、A/B转化影响未知；正常可关闭，不能称购物按钮失效。

**影响：** 用户正在决策/输入时被打断；属于转化体验风险而非购物流程不可用

**定位/修改位置：** MarketingPopupOverlay触发/路径过滤/频次，与年龄门禁不混同。

**实施方案：** 运营/开发限制营销弹窗在checkout触发，或改非阻塞提示；避免年龄验证后马上叠营销弹窗；保留可关闭、键盘可用与会话频率控制。

**可选方式与影响：** A运营排除checkout并限制连续弹窗；B改非阻塞提示；C商品页适当频次仍保留。不要关闭必要年龄验证。

**运营/开发：** 运营+开发

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.5人日（估算）

**复检：** checkout无非必要阻塞，正常×和键盘可关闭；不触发订阅邮件进行测试。

**证据：** 首轮：commerce-popup-attempt.json与checkout-initial-attempt.json中Get an extra discount!对话框拦截ADD TO CART/Use coupon；正常点击×可关闭，未证明按钮本身失效。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## SEO-10 · P2 · QY073额外FAQPage缺必需mainEntity

原优先级：新增；状态：本轮字段已确认，待修改

页面/模板：https://echobae.com/p/149cm-white-hair-silicone-doll-siwei

**已确认原因/事实：** 首轮JSON-LD以及本轮公开API seo.structured_data均只有@type FAQPage/@context，没有mainEntity。

**仍为假设/缺信息：** 官方Rich Results Test未执行；普通电商FAQ本就不应承诺Google FAQ富结果。

**影响：** 结构无效警告；不宣称此项阻止正常自然搜索或商品富结果。

**定位/修改位置：** QY073 seo.structured_data额外Schema字段；PDP自动Product之外追加JSON-LD的生成边界。

**实施方案：** 第一轮“JSON可解析”未检查该必需结构，本轮已从真实字段确认。

**可选方式与影响：** 最小修复删除这个空FAQPage；若确有合法问答语义需求，输出真实可见Question/acceptedAnswer/mainEntity，避免与block生成重复。

**运营/开发：** 运营（如后台可编辑）+开发

**后台能力：** 未登录后台，功能与菜单未经验证

**成本粗估：** 0.25人日

**复检：** 无空FAQPage；Product/Offer/BreadcrumbList不受影响；适用Schema字段校验通过。

**证据：** 见evidence/INDEX.md、ISSUE_DEEP_DIVE.md相关本轮事实及一轮原始文件。

**数据日期：** 当前HTTP/API/资源2026-10-14；复用DOM/截图2026-10-13，不混用

## IMG-04 · P2 · 商品详情图Alt使用设计文件占位名称

原优先级：新增；状态：历史DOM+本轮原图确认，当前DOM待复检

页面/模板：https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia

**已确认原因/事实：** 首轮DOM图片46/47 Alt分别Your paragraph text.webp、Untitled design.webp；本轮独立原图查看为身体规格/结构展示与面部/手部照片拼图。

**仍为假设/缺信息：** 后台是否可单独编辑Alt、其他SKU复用数量和当前DOM是否已修正未知。

**影响：** 屏幕阅读器得到无意义文件名；图中规格信息在手机小图里不易读取。

**定位/修改位置：** PDP详情富文本图片/媒体Alt；上传默认文件名fallback。

**实施方案：** 不把所有有Alt属性的图片称为SEO通过；范围仅2个已观察详情图。

**可选方式与影响：** 将Alt按图意改成“Silicone doll body sizes and construction details”与“Close-up views of doll faces, hands and posing”；装饰性图才空Alt，主要规格同时用HTML文字/表格表达。

**运营/开发：** 运营（开发提供Alt编辑能力）

**后台能力：** 未登录后台，功能与菜单未经验证

**成本粗估：** 0.25–0.5人日

**复检：** Alt自然描述而非文件名、无堆词；规格关键值可从正文读取；可访问树复检。

**证据：** 见evidence/INDEX.md、ISSUE_DEEP_DIVE.md相关本轮事实及一轮原始文件。

**数据日期：** 当前HTTP/API/资源2026-10-14；复用DOM/截图2026-10-13，不混用

## SEO-11 · P2 · 分页缺普通href入口与静态链接发现缺口

原优先级：新增；状态：组件/历史记录已确认，新图待复检

页面/模板：https://echobae.com/products、https://echobae.com/products?page=2、https://echobae.com/products?page=10

**已确认原因/事实：** 首轮pagination.json实际进入?page2…10，故“始终不改URL”被证伪；分页组件用button onClick。首轮228初始a图可达194，32商品无初始a入链，不能等同全站孤立。

**仍为假设/缺信息：** 旧图包含已退休测试商品；按当前72商品交叉后的候选另见link-graph.json；新页面/语言/新推荐链接图未采集。

**影响：** 机器和无JS用户难发现后续商品；当前分页URL变化机制本身正常。

**定位/修改位置：** Pagination组件页码/Next的a href、列表query路由、HTML链接发现与canonical策略。

**实施方案：** 分页9个URL已出现在首轮日志，却没纳入基础228清单，属于覆盖漏项；不伪称已逐页做过Title/Canonical复检。

**可选方式与影响：** 按钮外观保留但页码/前后页使用NuxtLink/a href，并可渐进增强；从URL query决定页数、筛选。Sitemap补发现不能代替合理内链。

**运营/开发：** 开发

**后台能力：** 未登录后台，功能与菜单未经验证

**成本粗估：** 0.5–1人日

**复检：** view-source有有效分页href，page2直接访问对应商品；query/canonical合规，活跃SKU在新链接图有有效路径，不把旧图候选当真实孤立。

**证据：** 见evidence/INDEX.md、ISSUE_DEEP_DIVE.md相关本轮事实及一轮原始文件。

**数据日期：** 当前HTTP/API/资源2026-10-14；复用DOM/截图2026-10-13，不混用

## IMG-03 · P3 · 移动Banner复用大图且无srcset

原优先级：P2；状态：原图预算已合理；加载策略待复检

页面/模板：https://echobae.com/

**已确认原因/事实：** 本轮主Banner物理1672×941仅30278B，第二张89526B；首轮移动无srcset/fetchpriority auto，文件没有大到必须进一步压缩。

**仍为假设/缺信息：** 当前Banner布局/priority是否调整未知；单换格式的收益不能估计。

**影响：** 移动下载无法按布局选图，多轮播图片争用首屏资源

**定位/修改位置：** Banner响应式source和优先级，首图尺寸占位优先归PERF-04。

**实施方案：** 首Banner30KB已合理；先处理PERF-04的占位、首图优先级/轮播加载，再考虑响应式候选。

**可选方式与影响：** A先加width/height和当前首图high、延后其他图；B合适尺寸候选作为次要优化；C维持30KB首图质量不做无意义二次压缩。

**运营/开发：** 开发+设计

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.5人日，随图片组件整改

**复检：** 主体清晰且首图早请求，下一张切换不空白；不要只追求更小文件损伤细节。

**证据：** 首轮：deep.json：Banner固有1672×941，移动390×219.48，无srcset/sizes，首图fetchPriority auto、两张eager；LCP诊断优先级提示未满足。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## SEO-08 · P3 · 商品Schema基础有效但变体/图片字段仍需发布校验

原优先级：P3；状态：基础已通过，变体/资格待验证

页面/模板：https://echobae.com/p/demo-sh-020、https://echobae.com/p/demo-sh-030、https://echobae.com/p/demo-sh-060、https://echobae.com/p/demo-sh-080、https://echobae.com/p/demo-sh-090；首轮观察范围完整URL列表在ISSUES_ROUND2.csv（已退休URL不应当作今天仍活跃）

**已确认原因/事实：** 三SKU首轮Product SKU/USD基础价与本轮API一致；InStock与track_inventory=true、available_quantity100自洽，但实体库存未证。

**仍为假设/缺信息：** 变体SKU、生产ready含义、真实库存与Google富结果资格未知。FAQ结构缺陷另见SEO-10。

**影响：** 语法正确不等于Google富结果资格或实际展示

**定位/修改位置：** 商品Schema生成器4FfVxrIF.js和PDP buildPageSeo; JSON-LD额外数据。

**实施方案：** 先清理Demo；确保绝对图片URL和真实库存/价格，适用时补SKU/商品变体模型，禁止无评价造评分；按Google产品与成人内容富结果规范人工复核。不优先添加FAQPage争取普通电商FAQ富结果。

**可选方式与影响：** A保持已正确的基础Product，不添加假评分；B有真实独立SKU再建ProductGroup/variants；把HTML excerpt转纯文本及去重图片作为低优先级。

**运营/开发：** 开发+运营

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.5–1人日（估算）

**复检：** 默认SKU/价格/货币对齐；选项语义与实际SKU策略明确，额外Schema和OG图片尺寸与真实资源一致；官方工具由开发执行。

**证据：** 首轮：crawl.json：JSON-LD均可解析；Lydia Product name/sku QY029/Offer USD1609.99/InStock与基础页一致。Demo有相对image和评分；正式样本没有AggregateRating。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据

## CONT-05 · P3 · Summer Sale 2026横幅在10月仍显示

原优先级：P3；状态：运营核验项，未证明故障

页面/模板：https://echobae.com/

**已确认原因/事实：** 首轮确有Summer Sale2026横幅；这不证明10月促销无效（地域/活动命名不同）。

**仍为假设/缺信息：** 活动有效期、优惠码、折扣规则未知，本轮页面壳没有实际横幅。

**影响：** 活动时效不清；不能据季节单独认定优惠失效

**定位/修改位置：** 运营活动名称、有效期/适用SKU/优惠配置。

**实施方案：** 运营确认实际促销有效性、代码和适用SKU；过期则撤下，仍有效则改为真实活动名并补规则。

**可选方式与影响：** A有效则澄清真实活动规则；B过期则撤下。仅在事实确认后修改，不为季节审美制造必修任务。

**运营/开发：** 运营

**后台能力：** 未登录后台；仅能指定所需业务字段，菜单路径未验证

**成本粗估：** 0.25人日（估算）

**复检：** 营销文案与有效折扣规则一致；有效码计算在开发沙盒验。

**证据：** 首轮：crawl及所有浏览样本顶部Summer Sale 2026 - Extra10% OFF · Shop now；未获活动起止和折扣规则。；本轮新增证据见evidence/INDEX.md与当前公开代码映射。

**数据日期：** 首轮2026-10-13；当前公开代码/API/图片2026-10-14；本轮未新增浏览器渲染证据
