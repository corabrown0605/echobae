# 开发公司任务

所有改动需用户另行授权，本次只交付计划。后台菜单、源文件路径均未取得访问权限；不编造菜单或源码位置。工期为粗估。

## CAT-01 · P0 · 主商品列表公开展示 Demo、测试及复制商品

状态：待修改；验证：已验证

页面：https://echobae.com/products、https://echobae.com/pages/help、https://echobae.com/p/demo-sh-020、https://echobae.com/p/demo-sh-030、https://echobae.com/p/demo-sh-060、https://echobae.com/p/demo-sh-080、https://echobae.com/p/demo-sh-090、https://echobae.com/p/demo-sh-100（完整列表见FULL_AUDIT.md）

问题与证据：evidence/browser-discovery.json：/products 显示189 items，首屏 Pro Smart Scale、Video Doorbell 等；99个 /p/demo-sh-* URL；另有test888命名及4个(copy)商品，测试用途需运营核实。evidence/pagination.json 完整分页。

操作/修复建议：运营确认正式 SKU 白名单，草稿/下架 Demo 和复制商品；开发确保列表、搜索、推荐、SSR、Schema、Sitemap 仅输出发布且有效商品。不要仅靠 noindex 隐藏测试商品。

复现：打开/products并查看首屏商品、切换Next分页；打开/pages/help的Best seller；对比正式分类new-arrival。记录智能家居Demo与copy标题，test888命名需运营确认是否测试商品。

验收：全部列表分页、搜索、Help推荐和Sitemap无测试商品；测试详情按下架策略返回404/410或有意义的301；真实商品数量与后台白名单一致

责任：运营+开发；预计：1–2人日（估算）

## SEO-01 · P0 · 全站禁止抓取与索引（上线前可能有意设置）

状态：待发布时解除；验证：已验证

页面：https://echobae.com/、https://echobae.com/products、https://echobae.com/collections/new-arrival、https://echobae.com/collections/best-value、https://echobae.com/custom-made、https://echobae.com/contact-us、https://echobae.com/blog、https://echobae.com/pages/help（完整列表见FULL_AUDIT.md）

问题与证据：evidence/crawl.json：227个HTTP200 URL均有noindex,nofollow；evidence/http-checks.json：robots.txt为User-agent:* / Disallow:/。

操作/修复建议：保留预发布限制直到正式验收。发布时仅对公开营销/商品/文章页解除noindex并开放robots；购物车、结账、账户、站内搜索继续按用途排除。先允许抓取，Google才能读取noindex变更；同步Sitemap和GSC检查。

复现：分别GET /robots.txt、首页、正式商品和文章；查看原始HTML meta[name=robots]及X-Robots-Tag，不用浏览器插件替代HTTP证据。

验收：正式页面200、可抓取且无meta或X-Robots-Tag noindex；私有/交易页面仍适当排除；GSC实时测试通过，实际索引另行追踪

责任：运营+开发；预计：0.5–1人日（估算）

## SEO-02 · P1 · sitemap.xml为空索引

状态：待修改；验证：已验证

页面：https://echobae.com/sitemap.xml

问题与证据：evidence/http-checks.json：HTTP200，<sitemapindex ...></sitemapindex>，0个子Sitemap。

操作/修复建议：生成只包含已发布、200、自引用规范且允许索引页面的urlset或非空索引；剔除Demo、参数、搜索、账户、交易及失效URL；发布后提交GSC。

复现：GET /sitemap.xml，按XML解析sitemapindex的sitemap/loc子项；当前数量为0。

验收：XML可解析且非空，所有loc为HTTPS规范URL；覆盖正式SKU和文章清单；GSC能读取且无测试URL

责任：开发+运营；预计：0.5–1人日（估算）

## POL-01 · P1 · 隐私政策保留服务器国家占位符

状态：待修改；验证：已验证

页面：https://echobae.com/privacy-policy

问题与证据：evidence/page-text.json：[Country, e.g., United States / Germany / Singapore]、[Country Where Servers Are Located]。

操作/修复建议：运营向开发/供应商核实国家、法律实体、数据处理和真实保留期限；据事实替换两处占位并审核承诺，不编造数据位置。

复现：打开隐私政策，搜索[Country与Country Where Servers；核对数据存储章节与国际转移章节。

验收：政策无方括号占位，实际国家/供应商/联系主体准确，必要法律审核完成

责任：运营（开发提供事实）；预计：0.5–1人日（估算）

## POL-02 · P1 · 配送时效在首页和政策中矛盾

状态：待修改；验证：已验证

页面：https://echobae.com/、https://echobae.com/shipping-policy

问题与证据：首页FAQ发货后3–7 days；Shipping Policy Express 10–14 business days、Standard 30–35 days after dispatch，均不含生产。

操作/修复建议：运营核实真实路线和生产周期，统一所有FAQ、商品FAQ、政策和结账配送说明。建议首页改为：“Delivery time depends on your destination and shipping method. See our Shipping Policy for current estimates. Production time is additional.”

复现：展开首页How Long Does It Take FAQ，读取3–7days；对照Shipping Policy的Standard/Express与production分段。

验收：同一配送方式在首页/商品/政策/结账估计一致，明确工作日、生产时间和例外

责任：运营+开发；预计：0.5–1人日（估算）

## CART-01 · P1 · 购物车及结账划线价与商品页不一致

状态：待修改；验证：已验证

页面：https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia、https://echobae.com/cart、https://echobae.com/checkout

问题与证据：evidence/browser/cart-verify.json：选AI后PDP $1689.98/$1800.00，购物车$1689.98/$2027.98，节省$338；无AI结账$1609.99/$1931.99。

操作/修复建议：统一PDP/cart/checkout的SKU和选项价格模型，保留真实compare_at_price，缺失原价则不展示划线价或节省金额；禁止自动虚构原价。

复现：新匿名会话正常确认年龄；打开QY029 Lydia，选AI Companion Voice +79.99；记录PDP1689.98/1800；ADD TO CART后点击页头Cart，等初始化，记录1689.98/2027.98；数量2小计3379.96；进入结账只观察，不点击PLACE ORDER。

验收：基础价1609.99；AI后1689.98；2件3379.96；各页真实比较价/节省金额完全一致，无空原价推算

责任：开发（运营核对原价）；预计：1人日（估算）

## POL-04 · P1 · 结账要求同意条款，但没有可访问的条款链接

状态：待修改；验证：已验证

页面：https://echobae.com/checkout

问题与证据：evidence/browser/checkout-checks.json：I have read and agree ... terms and conditions，links内无terms链接；导航也未发现条款页；猜测/terms-and-conditions返回404仅作辅助。

操作/修复建议：运营提供适用条款正文和实际公开URL；开发把确认文案链接到200可读条款并保留购物车状态；补充Footer链接。不要假定404猜测路径即为唯一合法地址。

复现：从带商品购物车进入Checkout，滚动至terms checkbox；检查是否有可打开的条款a[href]并阅读页面，不提交订单。

验收：结账可打开完整条款，返回购物流程不丢数据；未同意不能提交，提交行为须在开发测试环境验收

责任：运营+开发；预计：0.5–1人日（估算）

## SEO-03 · P1 · 不存在的商品详情返回200空商品壳

状态：待修改；验证：已验证

页面：https://echobae.com/p/audit-nonexistent-20261013

问题与证据：evidence/http-checks.json与browser/search-checks.json：HTTP200，Title Product | Echobae，仅Products标题和Footer，没有商品。普通不存在路径则404。

操作/修复建议：在SSR商品查询返回not-found时输出HTTP404/410，展示清楚提示和分类返回入口；真正重命名的商品做有意义301；不得统一跳首页。

复现：请求随机不存在/p/audit-nonexistent-20261013，检查HTTP200及空商品壳；对照普通随机路径404。

验收：随机不存在商品URL直接GET与浏览器都返回404/410；真实商品保持200；不制造空200

责任：开发；预计：0.5–1人日（估算）

## IMG-01 · P1 · 商品图片srcset多候选指向同一个文件

状态：待修改；验证：已验证

页面：https://echobae.com/collections/new-arrival、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia、https://echobae.com/p/149cm-white-hair-silicone-doll-siwei

问题与证据：evidence/browser/deep.json：分类同一600×900 URL声明400w、800w；PDP同一600×900 URL声明720w、1440w，sizes=720px。

操作/修复建议：开发生成实际400/800/1200等宽度变体或使用可验证图片服务；描述符对应实际固有宽度，sizes匹配断点；运营保留清晰原图，禁止把600px文件伪称1440w。

复现：Inspect分类第一张图和Lydia主图；读取srcset的URL/width候选，再读naturalWidth：不同w值指向同一URL。

验收：候选URL对应实际不同宽度；390/768/1440视口currentSrc选择符合布局/DPR；无伪描述符、明显糊图或额外CLS

责任：开发+运营；预计：1–2人日（估算）

## IMG-02 · P1 · 主要商品图在不同模板强制裁剪

状态：待修改；验证：裁剪已验证；是否不当需设计确认

页面：https://echobae.com/collections/new-arrival、https://echobae.com/collections/best-value、https://echobae.com/collections/best-sellers、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia

问题与证据：evidence/browser/deep.json：600×900分类图340×340 cover，约裁掉原图高度1/3；Lydia主图342×427.5 cover，约裁掉1/6高度。这是CSS几何裁剪，不等于原文件损坏。

操作/修复建议：主要商品展示优先2:3容器或contain完整展示；需方形卡片时由运营上传专用方形构图并设置焦点；不要全站盲目禁用cover。开发按图片类型区分容器。

复现：390×844打开分类/商品，读取图像naturalWidth/Height与DOMRect和object-fit；对比原2:3照片和方形/4:5容器。

验收：代表全身主图头部/脚部不被误裁、无拉伸，分类卡片构图一致；390/768/1440截图经运营确认

责任：设计+开发+运营；预计：1–2人日（估算）

## PERF-01 · P1 · 代表页面移动端LCP持续偏慢

状态：待修改；验证：已验证

页面：https://echobae.com/、https://echobae.com/collections/new-arrival、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia、https://echobae.com/blog/tpe-vs-silicone-sex-doll

问题与证据：evidence/lighthouse：4页×2设备×3次；首页首次mobile LCP中位5.6s，分类约5.6s，产品约5.9s，文章约4.9s；具体数字见PERFORMANCE_REPORT.md。

操作/修复建议：先稳定首屏与加载遮罩，优先LCP图片，高优先级只给当前首屏图；减少初始依赖/未使用CSS/JS。按报告网络链与LCP分段验证，保留年龄验证机制。

复现：使用performance.py指定代表URL，mobile新浏览器连续3次，保留JSON，按每指标取中位数；先核对代理资源失败与测试负载。

验收：同机同配置冷启动3次中位LCP≤2.5s、CLS≤0.1；复检第三方正常环境；上线后观察真实p75 CWV

责任：开发；预计：2–4人日（估算）

## PERF-02 · P1 · 主线程脚本开销与阻塞仍高

状态：待修改；验证：已验证

页面：https://echobae.com/、https://echobae.com/collections/new-arrival、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia

问题与证据：home-mobile-1主线程Script Evaluation约3148ms；DNfd1SfM.js未使用估算86240B；确认年龄后的3次TBT中位2150ms，不能解释为真实INP。

操作/修复建议：对公共运行时、动态块注册、builder初始化和视口外组件做性能profile；按路由拆包、延后非首屏组件，保留交互和隐私校验。只把Lighthouse估计当诊断，不把节约量累加成收益。

复现：打开home-mobile与home-accepted-mobile JSON的mainthread-work-breakdown/bootup-time和TBT；对公共builder初始化作Chrome Performance录制，勿把TBT当INP。

验收：冷/保留存储场景各3次TBT中位≤200ms或提供分阶段改善证据；关键点击无明显长任务；生产INP用真实数据独立验收

责任：开发；预计：2–4人日（估算）

## CONT-01 · P1 · 五星Reviews营销文字与0条评论展示不一致

状态：待修改；验证：展示矛盾已验证；真实性待运营核验

页面：https://echobae.com/、https://echobae.com/customer-reviews、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia、https://echobae.com/p/149cm-white-hair-silicone-doll-siwei

问题与证据：首页客户引语和星级；Customer Reviews实际All Reviews(0)；正式商品文案⭐⭐⭐⭐⭐ Reviews但Reviews(0)。无证据证明引语真假。

操作/修复建议：运营核验评价来源和授权；有真实来源则按SKU导入可追溯评价并显示数量；没有则删除五星/verified暗示，保留客观商品信息。不得编造评论或AggregateRating。

复现：对比首页客户引语、Customer Reviews All Reviews(0)、QY029商品⭐⭐⭐⭐⭐ Reviews和Reviews(0)；运营提供真实来源后核验，不自行认定伪造。

验收：星级、数量、商品归属与可见真实记录一致；零评论不展示假星级；Schema评分与真实可见评论一致

责任：运营+开发；预计：1–2人日（估算）

## SHIP-01 · P1 · 结账国家及免运费展示与政策范围不一致

状态：待修改；验证：展示不一致已验证；实际运费/税费待测试环境验证

页面：https://echobae.com/checkout

问题与证据：evidence/browser/checkout-checks.json：US/Canada/Brazil均可选择且显示Standard—Free，政策仅列10个配送国家、两种路线和按目的地计费；未填写地址、未提交订单。

操作/修复建议：运营确认支持国家、标准/快递费率及包税策略；开发在选择国家后明确可用路线/不可配送状态，必要时提示完整地址后报价。不能凭当前UI宣称最终订单可运巴西。

复现：有商品进入Checkout，不填个人信息；依次选择US、Canada、Brazil，记录国家/地区候选和Standard Free；对照Shipping Policy国家与两种路线。

验收：政策国家与结账可服务国家一致；非支持国家明确提示；已支持国家运费与规则一致；地址报价/税费在测试环境完成验收

责任：运营+开发；预计：1–2人日（估算）

## UX-01 · P1 · 年龄验证弹窗没有键盘焦点约束

状态：待修改；验证：已验证

页面：https://echobae.com/

问题与证据：evidence/browser/age-keyboard.json：前2次Tab聚焦确认/离开，第3次进入背景Shop now，后续Search/Cart等背景控件。确认后刷新ageVisible=0且存储存在。

操作/修复建议：在正常年龄弹窗内设初始焦点、Tab/Shift+Tab循环，背景inert；确认后还原焦点。保留确认/离开功能，不增加可绕过年龄验证的关闭方式。

复现：全新会话等待Age Verification；连续按Tab12次，第3次进入背景Shop now；正常点成年确认再刷新，确认弹窗消失。

验收：首次访问焦点在弹窗；连续20次Tab/Shift+Tab不进入背景；确认后正常导航且刷新记忆符合配置

责任：开发；预计：0.5–1人日（估算）

## PERF-04 · P1 · 首页桌面CLS三次均约0.457

状态：待修改；验证：已验证

页面：https://echobae.com/

问题与证据：home-desktop-1/2/3累计布局位移均0.456637；layout-shifts将主要0.416346位移关联Find Your Perfect Doll区块，并标记Banner img Media element lacking an explicit size。

操作/修复建议：给Banner图片真实width/height及容器稳定aspect-ratio；同步SSR与客户端断点尺寸，确保轮播当前项变化不改父容器高度。

复现：新浏览器以desktop preset跑首页3次，检查CLS及layout-shifts：Banner无显式尺寸，下方Find Your Perfect Doll发生主要位移。

验收：同一desktop配置冷启动3次CLS中位≤0.1，Banner加载前后高度稳定；移动布局不退化

责任：开发；预计：0.5–1人日（估算）

## FE-01 · P2 · runtime-blocks在所有深度样本中返回404

状态：待修改；验证：已验证

页面：https://echobae.com/、https://echobae.com/about-us、https://echobae.com/blog、https://echobae.com/blog/silicone-sex-doll-buying-guide、https://echobae.com/blog/tpe-vs-silicone-sex-doll、https://echobae.com/blog/what-are-the-most-realistic-sex-dolls、https://echobae.com/cart、https://echobae.com/collections/best-sellers（完整列表见FULL_AUDIT.md）

问题与证据：evidence/browser/deep.json 58个视口记录均404；evidence/public-js/DNfd1SfM.js公开函数z$在!response.ok时返回[]，W$只在列表非空时注册T$。

操作/修复建议：开发核查公开/content/runtime-blocks路由、模块注册表和当前发布配置；功能启用则实现/恢复200数据；未使用则停请求或约定200空列表。源码路径未知，不虚构文件名。

复现：清空Network后打开首页/分类/商品，筛选runtime-blocks并观察404；在已下载公开DNfd1SfM.js定位content/runtime-blocks与!r.ok return[]。

验收：代表页无该404；现有模块、商品和购物流程不退化；若空列表则开发确认无必需模块丢失

责任：开发；预计：0.5–1人日（估算）

## FE-02 · P2 · 多模板出现Hydration mismatch

状态：待修改；验证：已验证

页面：https://echobae.com/about-us、https://echobae.com/blog、https://echobae.com/blog/silicone-sex-doll-buying-guide、https://echobae.com/blog/tpe-vs-silicone-sex-doll、https://echobae.com/blog/what-are-the-most-realistic-sex-dolls、https://echobae.com/cart、https://echobae.com/collections/best-sellers、https://echobae.com/collections/best-value（完整列表见FULL_AUDIT.md）

问题与证据：evidence/browser/deep.json：49/58个记录含Hydration completed but contains mismatches，无未捕获pageerror；首始H1/DOM变化另见SEO-04。

操作/修复建议：开发用Nuxt/Vue hydration调试定位最小差异，比较服务端数据与客户端首轮数据、tokens/locale；只把浏览器专属渲染放在正确边界，避免全页client-only。

复现：新会话加载代表模板，打开Console查Hydration mismatch；保存SSR HTML与首轮DOM，借开发调试找最小节点差异。

验收：首页/分类/商品/文章/政策冷启动无hydration警告，初始重要文本与DOM一致，不丢SSR SEO

责任：开发；预计：1–2人日（估算）

## SEO-04 · P2 · 初始HTML与渲染DOM的主标题不一致

状态：待修改；验证：已验证

页面：https://echobae.com/products、https://echobae.com/collections/new-arrival、https://echobae.com/collections/best-value、https://echobae.com/custom-made、https://echobae.com/contact-us、https://echobae.com/pages/help、https://echobae.com/collections/best-sellers、https://echobae.com/customer-reviews（完整列表见FULL_AUDIT.md）

问题与证据：evidence/crawl.json含Home/Collections/Products通用H1；deep.json中Contact变Contact Us、分类变New Arrivals、正式商品只留商品H1。/blog则渲染后仍两个The Blog H1。

操作/修复建议：SSR直接输出真实页面名称；商品保留唯一主要商品H1，面包屑用nav/普通文本；博客列表保留一个The Blog主标题。不要机械增加正文。

复现：用GET/view-source查H1，等待浏览器初始化后查询document.querySelectorAll(h1)，比较Home/Collections/Products占位与真实标题；Blog确认两个The Blog。

验收：view-source与渲染DOM的主要H1一致；分类分别New Arrivals/Best Value/Best Sellers；博客主标题无模板重复

责任：开发；预计：1人日（估算）

## SEO-05 · P2 · Title品牌后缀重复

状态：待修改；验证：已验证

页面：https://echobae.com/blog、https://echobae.com/blog/silicone-sex-doll-buying-guide、https://echobae.com/p/149cm-christmas-silicone-love-doll-huaze、https://echobae.com/p/170cm-realistic-silicone-sex-doll-jiachen、https://echobae.com/p/159cm-natural-look-silicone-doll-jiachen、https://echobae.com/p/170cm-real-skin-texture-silicone-sex-doll-jiachen、https://echobae.com/p/169cm-silicone-realistic-sex-doll-jieman、https://echobae.com/p/159cm-realistic-silicone-sex-doll-lanxin（完整列表见FULL_AUDIT.md）

问题与证据：evidence/crawl.json：76个页面Title出现多次Echobae，如Lydia ... | Echobae | Echobae、buying guide ... | Echobae | Echobae。

操作/修复建议：优先统一titleTemplate去重或明确后台填写规范。Lydia推荐“159cm Lifelike Silicone Sex Doll Lydia | Echobae”，核心主题保留；购买指南只保留一个品牌。

复现：查看URL_INVENTORY中Title含两次Echobae的76页；以Lydia和buying-guide直接view-source验证。

验收：所有公开Title只保留一个品牌，产品名称/尺寸和文章意图不变；首页当前Title无需改写

责任：开发+运营；预计：0.5人日（估算）

## SEO-06 · P2 · 参数页重复标题并自引用Canonical

状态：待修改；验证：已验证

页面：https://echobae.com/blog?category=Buyer+Guide、https://echobae.com/blog?category=updates、https://echobae.com/products?tag=bestseller、https://echobae.com/products?tag=smart-home、https://echobae.com/products?tag=sale、https://echobae.com/products?tag=voice-control、https://echobae.com/products?tag=new、https://echobae.com/products?tag=budget（完整列表见FULL_AUDIT.md）

问题与证据：evidence/crawl.json：10个products?tag页Title相同且Canonical含tag；2个blog?category页也自引用。当前全局noindex。

操作/修复建议：运营选定独立有价值分类落地页，其余搜索/筛选保持noindex；相同内容参数使用规范URL，实质不同内容不要虚假canonical；分页用稳定可抓取href和各页正确canonical。

复现：请求products?tag=smart-home与products?tag=sale，比较Title/Canonical/robots；观察分类内容不同，不统一canonical至无关页面。

验收：发布后索引白名单清楚；搜索/低价值筛选不收录；无所有分页canonical到第一页的错误；有价值分类保留独立主题

责任：开发+运营；预计：0.5–1人日（估算）

## SEO-07 · P2 · 购买指南链接到404护理文章

状态：待修改；验证：已验证

页面：https://echobae.com/blog/silicone-sex-doll-buying-guide、https://echobae.com/blogs/silicone-doll-care-guide

问题与证据：crawl.json：指南链接/blogs/silicone-doll-care-guide；目标404，现有护理页/sex-doll-care返回200。

操作/修复建议：运营将该文链接改为真实相关护理内容（当前/sex-doll-care可作为候选）；若旧链接曾对外传播开发设置一对一301。

复现：打开buying-guide点击/检查护理链接/blogs/silicone-doll-care-guide，GET404；对照/sex-doll-care 200，不提交任何表单。

验收：指南内护理链接200、内容相关；无/blogs旧404，跳转最多一跳

责任：运营+开发；预计：0.25人日（估算）

## UX-02 · P2 · 移动端轮播箭头覆盖正文区域

状态：待修改；验证：已验证

页面：https://echobae.com/

问题与证据：evidence/previous/mobile-viewport.png（390×844）：左右白色圆箭头叠在“A private space...”文字所在高度；本次settled截图供复核。

操作/修复建议：设计/开发将移动箭头移至底部独立区域或使用明确分页控制，保留触摸切换；正文不能被控件覆盖。

复现：390×844查看首页首屏，比较轮播圆箭头与A private space正文的边界；切换滑块再次检查，截图留证。

验收：390/412/768首屏正文与控制无重叠，CTA可点击，按钮触摸区域清晰

责任：设计+开发；预计：0.5人日（估算）

## UX-03 · P2 · Footer暴露翻译键footer.poweredBy

状态：待修改；验证：已验证

页面：https://echobae.com/cart、https://echobae.com/checkout

问题与证据：cart-verify.json和checkout-checks.json可见footer.poweredBy；某些初始HTML/其他页正常Powered by wiipoo。

操作/修复建议：开发统一加载语言字典，补缺项/安全fallback；检查前后端locale初始化。

复现：正常购物车与Checkout等待初始化后搜索正文footer.poweredBy，比较首页正常Footer。

验收：所有模板初始与渲染页面都不显示翻译key、undefined或占位文本

责任：开发；预计：0.25–0.5人日（估算）

## SEC-01 · P2 · Demo详情HTML暴露私有HTTP图片地址

状态：待修改；验证：已验证

页面：https://echobae.com/p/demo-sh-020、https://echobae.com/p/demo-sh-030、https://echobae.com/p/demo-sh-060、https://echobae.com/p/demo-sh-100、https://echobae.com/p/demo-sh-009、https://echobae.com/p/demo-sh-011、https://echobae.com/p/demo-sh-012、https://echobae.com/p/demo-sh-095（完整列表见FULL_AUDIT.md）

问题与证据：evidence/private-image-urls.json：28个公开Demo商品页面img指向http://172.17.0.1:8093/...；不是凭此证明服务器被入侵。

操作/修复建议：随CAT-01移除Demo；开发统一媒体存储规范公网HTTPS URL并拦截内容录入内部IP/localhost引用。停止测试这些内部地址，不开展私网探测。

复现：仅检查已保存Demo HTML img/src及private-image-urls.json，不请求或探测内部地址。

验收：所有公开HTML/JSON-LD/图片候选无RFC1918/localhost/http混合图片引用；真实媒体全部HTTPS可加载

责任：开发+运营；预计：0.5–1人日（估算）

## SEC-02 · P2 · 公开200页面缺少统一安全响应头

状态：待修改；验证：环境所见已验证；源站头待开发复核

页面：https://echobae.com/、https://echobae.com/products、https://echobae.com/collections/new-arrival、https://echobae.com/collections/best-value、https://echobae.com/custom-made、https://echobae.com/contact-us、https://echobae.com/blog、https://echobae.com/pages/help（完整列表见FULL_AUDIT.md）

问题与证据：crawl.json：227个200均有HSTS；未见CSP/X-Content-Type-Options/X-Frame-Options/Referrer-Policy，404页反而带nosniff/DENY/no-referrer。代理可能影响响应头可见性。

操作/修复建议：开发核查源站与CDN实测头；对HTML启用nosniff和适当Referrer-Policy，设计frame-ancestors；CSP先Report-Only并兼容支付/必要外域，再收紧。勿盲目DENY导致支付集成故障。

复现：读取已保存200与404响应头，比较HSTS/CSP/nosniff/frame/referrer；开发从源站与正常公网重复GET确认代理是否改写。

验收：外网正常浏览确认各模板头一致，CSP不破坏支付/图片/脚本；不以缺头宣称漏洞利用成功

责任：开发；预计：0.5–1人日（估算）

## TRACK-01 · P2 · GTM已嵌入，但事件与隐私承诺未验证

状态：未验证；验证：GTM公开嵌入已验证；账户/事件/同意待验证

页面：https://echobae.com/、https://echobae.com/privacy-policy

问题与证据：公开请求GTM-T2DKHJKK；请求在代理中失败。政策承诺不向外部营销/第三方分析披露成人浏览信息，并列Optional Analytics Cookies。无法读取容器/GA4/GSC账户。

操作/修复建议：运营和开发在GTM预览/GA4 DebugView验证view_item/add_to_cart/begin_checkout（purchase用测试环境）；审核数据最小化与同意管理，避免不必要成人商品/身份数据外发；按真实情况修订政策。

复现：检查公开GTM容器请求与隐私政策承诺；账户验证仅由运营在GTM Preview/GA4 DebugView完成，线上审计不提交真实purchase。

验收：账号配置、同意前后网络及事件单次触发有证据；无PII外发，政策与实际标签一致

责任：运营+开发；预计：1–2人日（估算）

## PERF-03 · P2 · 首屏存在可减小的公共CSS/JS负载

状态：待修改；验证：已验证

页面：https://echobae.com/

问题与证据：home-mobile-1：blocks-built.css 26251B，unused估计22227B；StoreFooter CSS约10016B阻塞；DNfd1SfM.js传输约243593B、未使用估计86240B。

操作/修复建议：按当前页面block拆分样式，保留关键CSS并延后非关键样式；按路由拆分公共JS。避免purge动态类后破坏builder；实测而非累加Lighthouse估算收益。

复现：查看home-mobile-1 unused-css-rules/unused-javascript/render-blocking-insight与network-requests；核对公共CSS/JS资源字节。

验收：相同功能截图不退化，初始CSS/JS传输量和未使用字节下降，LCP/FCP重复测试改善

责任：开发；预计：1–2人日（估算）

## IMG-03 · P2 · 移动Banner复用大图且无srcset

状态：待修改；验证：已验证

页面：https://echobae.com/

问题与证据：deep.json：Banner固有1672×941，移动390×219.48，无srcset/sizes，首图fetchPriority auto、两张eager；LCP诊断优先级提示未满足。

操作/修复建议：生成符合真实构图的移动/桌面候选，当前首屏图fetchpriority=high且eager，其他轮播按交互/预加载窗口延后；不延迟真实LCP图。

复现：读取390px首页Banner的natural/render/srcset/fetchPriority与loading；对照LCP节点和首图请求时间。

验收：移动选择更小候选且清晰，首屏图提前请求；切换不出现空白，LCP和总图片字节改善

责任：开发+设计；预计：0.5–1人日（估算）

## UX-04 · P2 · CTA和比较价文字对比度未达到自动化阈值

状态：待修改；验证：已验证

页面：https://echobae.com/、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia

问题与证据：home-mobile-1 color-contrast：Explore #ff2929/白色比3.74:1；product-mobile-1 比较价#9ca3af/白色2.53:1，16px普通文本预期4.5:1。

操作/修复建议：设计/开发调整CTA文字或背景、比较价灰色，普通文本至少4.5:1，大文本至少3:1；保留品牌色用于适合的非文字装饰。

复现：打开home-mobile-1/product-mobile-1 color-contrast失败节点；核对Explore/比较价CSS色值及16px字体。

验收：对应CSS节点对比度复测通过；各hover/focus/disabled状态分别检查，不以总分代替具体节点

责任：设计+开发；预计：0.5人日（估算）

## UX-05 · P2 · 营销弹窗在购物及结账过程中打断操作

状态：待修改；验证：已验证

页面：https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia、https://echobae.com/checkout

问题与证据：commerce-popup-attempt.json与checkout-initial-attempt.json中Get an extra discount!对话框拦截ADD TO CART/Use coupon；正常点击×可关闭，未证明按钮本身失效。

操作/修复建议：运营/开发限制营销弹窗在checkout触发，或改非阻塞提示；避免年龄验证后马上叠营销弹窗；保留可关闭、键盘可用与会话频率控制。

复现：正常成年确认后停留商品/Checkout，等待营销弹窗，检查遮挡购物或优惠入口；正常点击×恢复操作，不提交邮箱订阅。

验收：完整购物到结账过程中无非必要阻塞弹窗；年龄验证正常、优惠入口仍可见；测试不触发订阅邮件

责任：运营+开发；预计：0.5人日（估算）

## SEO-08 · P3 · 商品Schema基础有效但变体/图片字段仍需发布校验

状态：待优化；验证：基础语法/样本字段已验证；富结果及变体规则待验证

页面：https://echobae.com/p/demo-sh-020、https://echobae.com/p/demo-sh-030、https://echobae.com/p/demo-sh-060、https://echobae.com/p/demo-sh-080、https://echobae.com/p/demo-sh-090、https://echobae.com/p/demo-sh-100、https://echobae.com/p/robovac-x1、https://echobae.com/p/demo-sh-001（完整列表见FULL_AUDIT.md）

问题与证据：crawl.json：JSON-LD均可解析；Lydia Product name/sku QY029/Offer USD1609.99/InStock与基础页一致。Demo有相对image和评分；正式样本没有AggregateRating。

操作/修复建议：先清理Demo；确保绝对图片URL和真实库存/价格，适用时补SKU/商品变体模型，禁止无评价造评分；按Google产品与成人内容富结果规范人工复核。不优先添加FAQPage争取普通电商FAQ富结果。

复现：从代表SKU初始HTML解析Product/Offer/BreadcrumbList，比较默认USD价格、SKU、图片和库存标签；后台真实库存另验。

验收：正式商品Schema可解析且与默认配置一致；代表变体价格/库存策略明确；官方验证工具检查后保存结果，不承诺展示

责任：开发+运营；预计：0.5–1人日（估算）
