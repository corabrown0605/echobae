# 运营后台任务

所有改动需用户另行授权，本次只交付计划。后台菜单、源文件路径均未取得访问权限；不编造菜单或源码位置。工期为粗估。

## CAT-01 · P0 · 主商品列表公开展示 Demo、测试及复制商品

状态：待修改；验证：已验证

页面：https://echobae.com/products、https://echobae.com/pages/help、https://echobae.com/p/demo-sh-020、https://echobae.com/p/demo-sh-030、https://echobae.com/p/demo-sh-060、https://echobae.com/p/demo-sh-080、https://echobae.com/p/demo-sh-090、https://echobae.com/p/demo-sh-100（完整列表见FULL_AUDIT.md）

问题与证据：evidence/browser-discovery.json：/products 显示189 items，首屏 Pro Smart Scale、Video Doorbell 等；99个 /p/demo-sh-* URL；另有test888命名及4个(copy)商品，测试用途需运营核实。evidence/pagination.json 完整分页。

操作/修复建议：运营确认正式 SKU 白名单，草稿/下架 Demo 和复制商品；开发确保列表、搜索、推荐、SSR、Schema、Sitemap 仅输出发布且有效商品。不要仅靠 noindex 隐藏测试商品。

复现：打开/products并查看首屏商品、切换Next分页；打开/pages/help的Best seller；对比正式分类new-arrival。记录智能家居Demo与copy标题，test888命名需运营确认是否测试商品。

验收：全部列表分页、搜索、Help推荐和Sitemap无测试商品；测试详情按下架策略返回404/410或有意义的301；真实商品数量与后台白名单一致

责任：运营+开发；预计：1–2人日（估算）

后台对应功能：仅根据任务类型寻找商品发布/内容编辑/SEO或配置功能，实际菜单未经验证。如后台不支持该字段，将该任务交开发；修改前备份当前文本并记录正式SKU白名单，修改后读公开页复核。

## SEO-01 · P0 · 全站禁止抓取与索引（上线前可能有意设置）

状态：待发布时解除；验证：已验证

页面：https://echobae.com/、https://echobae.com/products、https://echobae.com/collections/new-arrival、https://echobae.com/collections/best-value、https://echobae.com/custom-made、https://echobae.com/contact-us、https://echobae.com/blog、https://echobae.com/pages/help（完整列表见FULL_AUDIT.md）

问题与证据：evidence/crawl.json：227个HTTP200 URL均有noindex,nofollow；evidence/http-checks.json：robots.txt为User-agent:* / Disallow:/。

操作/修复建议：保留预发布限制直到正式验收。发布时仅对公开营销/商品/文章页解除noindex并开放robots；购物车、结账、账户、站内搜索继续按用途排除。先允许抓取，Google才能读取noindex变更；同步Sitemap和GSC检查。

复现：分别GET /robots.txt、首页、正式商品和文章；查看原始HTML meta[name=robots]及X-Robots-Tag，不用浏览器插件替代HTTP证据。

验收：正式页面200、可抓取且无meta或X-Robots-Tag noindex；私有/交易页面仍适当排除；GSC实时测试通过，实际索引另行追踪

责任：运营+开发；预计：0.5–1人日（估算）

后台对应功能：仅根据任务类型寻找商品发布/内容编辑/SEO或配置功能，实际菜单未经验证。如后台不支持该字段，将该任务交开发；修改前备份当前文本并记录正式SKU白名单，修改后读公开页复核。

## SEO-02 · P1 · sitemap.xml为空索引

状态：待修改；验证：已验证

页面：https://echobae.com/sitemap.xml

问题与证据：evidence/http-checks.json：HTTP200，<sitemapindex ...></sitemapindex>，0个子Sitemap。

操作/修复建议：生成只包含已发布、200、自引用规范且允许索引页面的urlset或非空索引；剔除Demo、参数、搜索、账户、交易及失效URL；发布后提交GSC。

复现：GET /sitemap.xml，按XML解析sitemapindex的sitemap/loc子项；当前数量为0。

验收：XML可解析且非空，所有loc为HTTPS规范URL；覆盖正式SKU和文章清单；GSC能读取且无测试URL

责任：开发+运营；预计：0.5–1人日（估算）

后台对应功能：仅根据任务类型寻找商品发布/内容编辑/SEO或配置功能，实际菜单未经验证。如后台不支持该字段，将该任务交开发；修改前备份当前文本并记录正式SKU白名单，修改后读公开页复核。

## POL-01 · P1 · 隐私政策保留服务器国家占位符

状态：待修改；验证：已验证

页面：https://echobae.com/privacy-policy

问题与证据：evidence/page-text.json：[Country, e.g., United States / Germany / Singapore]、[Country Where Servers Are Located]。

操作/修复建议：运营向开发/供应商核实国家、法律实体、数据处理和真实保留期限；据事实替换两处占位并审核承诺，不编造数据位置。

复现：打开隐私政策，搜索[Country与Country Where Servers；核对数据存储章节与国际转移章节。

验收：政策无方括号占位，实际国家/供应商/联系主体准确，必要法律审核完成

责任：运营（开发提供事实）；预计：0.5–1人日（估算）

后台对应功能：仅根据任务类型寻找商品发布/内容编辑/SEO或配置功能，实际菜单未经验证。如后台不支持该字段，将该任务交开发；修改前备份当前文本并记录正式SKU白名单，修改后读公开页复核。

## POL-02 · P1 · 配送时效在首页和政策中矛盾

状态：待修改；验证：已验证

页面：https://echobae.com/、https://echobae.com/shipping-policy

问题与证据：首页FAQ发货后3–7 days；Shipping Policy Express 10–14 business days、Standard 30–35 days after dispatch，均不含生产。

操作/修复建议：运营核实真实路线和生产周期，统一所有FAQ、商品FAQ、政策和结账配送说明。建议首页改为：“Delivery time depends on your destination and shipping method. See our Shipping Policy for current estimates. Production time is additional.”

复现：展开首页How Long Does It Take FAQ，读取3–7days；对照Shipping Policy的Standard/Express与production分段。

验收：同一配送方式在首页/商品/政策/结账估计一致，明确工作日、生产时间和例外

责任：运营+开发；预计：0.5–1人日（估算）

后台对应功能：仅根据任务类型寻找商品发布/内容编辑/SEO或配置功能，实际菜单未经验证。如后台不支持该字段，将该任务交开发；修改前备份当前文本并记录正式SKU白名单，修改后读公开页复核。

## POL-03 · P1 · 退款政策含缺失运费金额和未核实支付渠道

状态：待修改；验证：已验证

页面：https://echobae.com/return-refund-policy

问题与证据：公开文本International shipping ... starts from $ *；列Personal check/Cashier’s check/Money order/电话fax付款；结账只展示Stripe、PayPal。

操作/修复建议：用经核实费率替换$ *；如没有最低价，改“Shipping costs are shown at checkout before payment.”；删除未提供的付款方式，明确取消、瑕疵/错发处置与法律适用例外；由运营/法务确认，勿捏造退款权利。

复现：打开Returns政策，定位International Sex Doll Shipping的$ *与Accepted payment methods列表；对照实际结账支付选项。

验收：政策无金额占位；付款渠道与实际可用方式一致；瑕疵和错发流程明确并经业务负责人审核

责任：运营；预计：0.5–1人日（估算）

后台对应功能：仅根据任务类型寻找商品发布/内容编辑/SEO或配置功能，实际菜单未经验证。如后台不支持该字段，将该任务交开发；修改前备份当前文本并记录正式SKU白名单，修改后读公开页复核。

## CART-01 · P1 · 购物车及结账划线价与商品页不一致

状态：待修改；验证：已验证

页面：https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia、https://echobae.com/cart、https://echobae.com/checkout

问题与证据：evidence/browser/cart-verify.json：选AI后PDP $1689.98/$1800.00，购物车$1689.98/$2027.98，节省$338；无AI结账$1609.99/$1931.99。

操作/修复建议：统一PDP/cart/checkout的SKU和选项价格模型，保留真实compare_at_price，缺失原价则不展示划线价或节省金额；禁止自动虚构原价。

复现：新匿名会话正常确认年龄；打开QY029 Lydia，选AI Companion Voice +79.99；记录PDP1689.98/1800；ADD TO CART后点击页头Cart，等初始化，记录1689.98/2027.98；数量2小计3379.96；进入结账只观察，不点击PLACE ORDER。

验收：基础价1609.99；AI后1689.98；2件3379.96；各页真实比较价/节省金额完全一致，无空原价推算

责任：开发（运营核对原价）；预计：1人日（估算）

后台对应功能：仅根据任务类型寻找商品发布/内容编辑/SEO或配置功能，实际菜单未经验证。如后台不支持该字段，将该任务交开发；修改前备份当前文本并记录正式SKU白名单，修改后读公开页复核。

## POL-04 · P1 · 结账要求同意条款，但没有可访问的条款链接

状态：待修改；验证：已验证

页面：https://echobae.com/checkout

问题与证据：evidence/browser/checkout-checks.json：I have read and agree ... terms and conditions，links内无terms链接；导航也未发现条款页；猜测/terms-and-conditions返回404仅作辅助。

操作/修复建议：运营提供适用条款正文和实际公开URL；开发把确认文案链接到200可读条款并保留购物车状态；补充Footer链接。不要假定404猜测路径即为唯一合法地址。

复现：从带商品购物车进入Checkout，滚动至terms checkbox；检查是否有可打开的条款a[href]并阅读页面，不提交订单。

验收：结账可打开完整条款，返回购物流程不丢数据；未同意不能提交，提交行为须在开发测试环境验收

责任：运营+开发；预计：0.5–1人日（估算）

后台对应功能：仅根据任务类型寻找商品发布/内容编辑/SEO或配置功能，实际菜单未经验证。如后台不支持该字段，将该任务交开发；修改前备份当前文本并记录正式SKU白名单，修改后读公开页复核。

## IMG-01 · P1 · 商品图片srcset多候选指向同一个文件

状态：待修改；验证：已验证

页面：https://echobae.com/collections/new-arrival、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia、https://echobae.com/p/149cm-white-hair-silicone-doll-siwei

问题与证据：evidence/browser/deep.json：分类同一600×900 URL声明400w、800w；PDP同一600×900 URL声明720w、1440w，sizes=720px。

操作/修复建议：开发生成实际400/800/1200等宽度变体或使用可验证图片服务；描述符对应实际固有宽度，sizes匹配断点；运营保留清晰原图，禁止把600px文件伪称1440w。

复现：Inspect分类第一张图和Lydia主图；读取srcset的URL/width候选，再读naturalWidth：不同w值指向同一URL。

验收：候选URL对应实际不同宽度；390/768/1440视口currentSrc选择符合布局/DPR；无伪描述符、明显糊图或额外CLS

责任：开发+运营；预计：1–2人日（估算）

后台对应功能：仅根据任务类型寻找商品发布/内容编辑/SEO或配置功能，实际菜单未经验证。如后台不支持该字段，将该任务交开发；修改前备份当前文本并记录正式SKU白名单，修改后读公开页复核。

## IMG-02 · P1 · 主要商品图在不同模板强制裁剪

状态：待修改；验证：裁剪已验证；是否不当需设计确认

页面：https://echobae.com/collections/new-arrival、https://echobae.com/collections/best-value、https://echobae.com/collections/best-sellers、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia

问题与证据：evidence/browser/deep.json：600×900分类图340×340 cover，约裁掉原图高度1/3；Lydia主图342×427.5 cover，约裁掉1/6高度。这是CSS几何裁剪，不等于原文件损坏。

操作/修复建议：主要商品展示优先2:3容器或contain完整展示；需方形卡片时由运营上传专用方形构图并设置焦点；不要全站盲目禁用cover。开发按图片类型区分容器。

复现：390×844打开分类/商品，读取图像naturalWidth/Height与DOMRect和object-fit；对比原2:3照片和方形/4:5容器。

验收：代表全身主图头部/脚部不被误裁、无拉伸，分类卡片构图一致；390/768/1440截图经运营确认

责任：设计+开发+运营；预计：1–2人日（估算）

后台对应功能：仅根据任务类型寻找商品发布/内容编辑/SEO或配置功能，实际菜单未经验证。如后台不支持该字段，将该任务交开发；修改前备份当前文本并记录正式SKU白名单，修改后读公开页复核。

## CONT-01 · P1 · 五星Reviews营销文字与0条评论展示不一致

状态：待修改；验证：展示矛盾已验证；真实性待运营核验

页面：https://echobae.com/、https://echobae.com/customer-reviews、https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia、https://echobae.com/p/149cm-white-hair-silicone-doll-siwei

问题与证据：首页客户引语和星级；Customer Reviews实际All Reviews(0)；正式商品文案⭐⭐⭐⭐⭐ Reviews但Reviews(0)。无证据证明引语真假。

操作/修复建议：运营核验评价来源和授权；有真实来源则按SKU导入可追溯评价并显示数量；没有则删除五星/verified暗示，保留客观商品信息。不得编造评论或AggregateRating。

复现：对比首页客户引语、Customer Reviews All Reviews(0)、QY029商品⭐⭐⭐⭐⭐ Reviews和Reviews(0)；运营提供真实来源后核验，不自行认定伪造。

验收：星级、数量、商品归属与可见真实记录一致；零评论不展示假星级；Schema评分与真实可见评论一致

责任：运营+开发；预计：1–2人日（估算）

后台对应功能：仅根据任务类型寻找商品发布/内容编辑/SEO或配置功能，实际菜单未经验证。如后台不支持该字段，将该任务交开发；修改前备份当前文本并记录正式SKU白名单，修改后读公开页复核。

## CONT-02 · P1 · Siwei商品标题与正文名称不一致

状态：待修改；验证：已验证

页面：https://echobae.com/p/149cm-white-hair-silicone-doll-siwei

问题与证据：标题149cm White Hair AI Silicone Doll Siwei，Main SKU QY073，正文多次称Aurora；AI在额外升级区+$79.99。

操作/修复建议：运营确认SKU QY073真实名称、头部/身体和AI是否标配；统一Siwei/Aurora或明确别名；AI为选配时标题移除暗示标配，说明基础配置和升级价。

复现：打开QY073 Siwei，比较H1/Main SKU/正文Aurora及AI升级价格，运营确认名称/标配。

验收：Title/H1/正文/SKU/购物车型号一致；AI标配/选配明确；不改无问题商品

责任：运营；预计：0.5人日（估算）

后台对应功能：仅根据任务类型寻找商品发布/内容编辑/SEO或配置功能，实际菜单未经验证。如后台不支持该字段，将该任务交开发；修改前备份当前文本并记录正式SKU白名单，修改后读公开页复核。

## SHIP-01 · P1 · 结账国家及免运费展示与政策范围不一致

状态：待修改；验证：展示不一致已验证；实际运费/税费待测试环境验证

页面：https://echobae.com/checkout

问题与证据：evidence/browser/checkout-checks.json：US/Canada/Brazil均可选择且显示Standard—Free，政策仅列10个配送国家、两种路线和按目的地计费；未填写地址、未提交订单。

操作/修复建议：运营确认支持国家、标准/快递费率及包税策略；开发在选择国家后明确可用路线/不可配送状态，必要时提示完整地址后报价。不能凭当前UI宣称最终订单可运巴西。

复现：有商品进入Checkout，不填个人信息；依次选择US、Canada、Brazil，记录国家/地区候选和Standard Free；对照Shipping Policy国家与两种路线。

验收：政策国家与结账可服务国家一致；非支持国家明确提示；已支持国家运费与规则一致；地址报价/税费在测试环境完成验收

责任：运营+开发；预计：1–2人日（估算）

后台对应功能：仅根据任务类型寻找商品发布/内容编辑/SEO或配置功能，实际菜单未经验证。如后台不支持该字段，将该任务交开发；修改前备份当前文本并记录正式SKU白名单，修改后读公开页复核。

## SEO-05 · P2 · Title品牌后缀重复

状态：待修改；验证：已验证

页面：https://echobae.com/blog、https://echobae.com/blog/silicone-sex-doll-buying-guide、https://echobae.com/p/149cm-christmas-silicone-love-doll-huaze、https://echobae.com/p/170cm-realistic-silicone-sex-doll-jiachen、https://echobae.com/p/159cm-natural-look-silicone-doll-jiachen、https://echobae.com/p/170cm-real-skin-texture-silicone-sex-doll-jiachen、https://echobae.com/p/169cm-silicone-realistic-sex-doll-jieman、https://echobae.com/p/159cm-realistic-silicone-sex-doll-lanxin（完整列表见FULL_AUDIT.md）

问题与证据：evidence/crawl.json：76个页面Title出现多次Echobae，如Lydia ... | Echobae | Echobae、buying guide ... | Echobae | Echobae。

操作/修复建议：优先统一titleTemplate去重或明确后台填写规范。Lydia推荐“159cm Lifelike Silicone Sex Doll Lydia | Echobae”，核心主题保留；购买指南只保留一个品牌。

复现：查看URL_INVENTORY中Title含两次Echobae的76页；以Lydia和buying-guide直接view-source验证。

验收：所有公开Title只保留一个品牌，产品名称/尺寸和文章意图不变；首页当前Title无需改写

责任：开发+运营；预计：0.5人日（估算）

后台对应功能：仅根据任务类型寻找商品发布/内容编辑/SEO或配置功能，实际菜单未经验证。如后台不支持该字段，将该任务交开发；修改前备份当前文本并记录正式SKU白名单，修改后读公开页复核。

## SEO-06 · P2 · 参数页重复标题并自引用Canonical

状态：待修改；验证：已验证

页面：https://echobae.com/blog?category=Buyer+Guide、https://echobae.com/blog?category=updates、https://echobae.com/products?tag=bestseller、https://echobae.com/products?tag=smart-home、https://echobae.com/products?tag=sale、https://echobae.com/products?tag=voice-control、https://echobae.com/products?tag=new、https://echobae.com/products?tag=budget（完整列表见FULL_AUDIT.md）

问题与证据：evidence/crawl.json：10个products?tag页Title相同且Canonical含tag；2个blog?category页也自引用。当前全局noindex。

操作/修复建议：运营选定独立有价值分类落地页，其余搜索/筛选保持noindex；相同内容参数使用规范URL，实质不同内容不要虚假canonical；分页用稳定可抓取href和各页正确canonical。

复现：请求products?tag=smart-home与products?tag=sale，比较Title/Canonical/robots；观察分类内容不同，不统一canonical至无关页面。

验收：发布后索引白名单清楚；搜索/低价值筛选不收录；无所有分页canonical到第一页的错误；有价值分类保留独立主题

责任：开发+运营；预计：0.5–1人日（估算）

后台对应功能：仅根据任务类型寻找商品发布/内容编辑/SEO或配置功能，实际菜单未经验证。如后台不支持该字段，将该任务交开发；修改前备份当前文本并记录正式SKU白名单，修改后读公开页复核。

## SEO-07 · P2 · 购买指南链接到404护理文章

状态：待修改；验证：已验证

页面：https://echobae.com/blog/silicone-sex-doll-buying-guide、https://echobae.com/blogs/silicone-doll-care-guide

问题与证据：crawl.json：指南链接/blogs/silicone-doll-care-guide；目标404，现有护理页/sex-doll-care返回200。

操作/修复建议：运营将该文链接改为真实相关护理内容（当前/sex-doll-care可作为候选）；若旧链接曾对外传播开发设置一对一301。

复现：打开buying-guide点击/检查护理链接/blogs/silicone-doll-care-guide，GET404；对照/sex-doll-care 200，不提交任何表单。

验收：指南内护理链接200、内容相关；无/blogs旧404，跳转最多一跳

责任：运营+开发；预计：0.25人日（估算）

后台对应功能：仅根据任务类型寻找商品发布/内容编辑/SEO或配置功能，实际菜单未经验证。如后台不支持该字段，将该任务交开发；修改前备份当前文本并记录正式SKU白名单，修改后读公开页复核。

## CONT-03 · P2 · FAQ重复问答02与03

状态：待修改；验证：已验证

页面：https://echobae.com/faq

问题与证据：page-text.json：02/03标题和回答均为removable vs fixed，完全重复。

操作/修复建议：运营删除重复条目或替换成真实不同问题并重新编号；不为SEO增加无关问题。

复现：打开/faq，对比02和03题目及回答，确认完全重复。

验收：问答不重复且编号连续；内容与商品实际配置一致

责任：运营；预计：0.25人日（估算）

后台对应功能：仅根据任务类型寻找商品发布/内容编辑/SEO或配置功能，实际菜单未经验证。如后台不支持该字段，将该任务交开发；修改前备份当前文本并记录正式SKU白名单，修改后读公开页复核。

## CONT-04 · P2 · 首页社媒图标链接到平台首页

状态：待修改；验证：已验证

页面：https://echobae.com/

问题与证据：deep.json首页7个aria标签社媒链接为linkedin.com、x.com、facebook.com、youtube.com、instagram.com、pinterest.com、tiktok.com根路径。

操作/修复建议：运营填写真实品牌主页URL；尚无账号则移除对应图标，勿造账号地址。

复现：首页Inspect七个社媒图标href与aria-label；检查URL是否只有平台根域，不发送社媒消息。

验收：每个保留图标到品牌主页，移动/桌面可读标签正确，无平台根链接

责任：运营（后台功能未验证）；预计：0.25人日（估算）

后台对应功能：仅根据任务类型寻找商品发布/内容编辑/SEO或配置功能，实际菜单未经验证。如后台不支持该字段，将该任务交开发；修改前备份当前文本并记录正式SKU白名单，修改后读公开页复核。

## SEC-01 · P2 · Demo详情HTML暴露私有HTTP图片地址

状态：待修改；验证：已验证

页面：https://echobae.com/p/demo-sh-020、https://echobae.com/p/demo-sh-030、https://echobae.com/p/demo-sh-060、https://echobae.com/p/demo-sh-100、https://echobae.com/p/demo-sh-009、https://echobae.com/p/demo-sh-011、https://echobae.com/p/demo-sh-012、https://echobae.com/p/demo-sh-095（完整列表见FULL_AUDIT.md）

问题与证据：evidence/private-image-urls.json：28个公开Demo商品页面img指向http://172.17.0.1:8093/...；不是凭此证明服务器被入侵。

操作/修复建议：随CAT-01移除Demo；开发统一媒体存储规范公网HTTPS URL并拦截内容录入内部IP/localhost引用。停止测试这些内部地址，不开展私网探测。

复现：仅检查已保存Demo HTML img/src及private-image-urls.json，不请求或探测内部地址。

验收：所有公开HTML/JSON-LD/图片候选无RFC1918/localhost/http混合图片引用；真实媒体全部HTTPS可加载

责任：开发+运营；预计：0.5–1人日（估算）

后台对应功能：仅根据任务类型寻找商品发布/内容编辑/SEO或配置功能，实际菜单未经验证。如后台不支持该字段，将该任务交开发；修改前备份当前文本并记录正式SKU白名单，修改后读公开页复核。

## TRACK-01 · P2 · GTM已嵌入，但事件与隐私承诺未验证

状态：未验证；验证：GTM公开嵌入已验证；账户/事件/同意待验证

页面：https://echobae.com/、https://echobae.com/privacy-policy

问题与证据：公开请求GTM-T2DKHJKK；请求在代理中失败。政策承诺不向外部营销/第三方分析披露成人浏览信息，并列Optional Analytics Cookies。无法读取容器/GA4/GSC账户。

操作/修复建议：运营和开发在GTM预览/GA4 DebugView验证view_item/add_to_cart/begin_checkout（purchase用测试环境）；审核数据最小化与同意管理，避免不必要成人商品/身份数据外发；按真实情况修订政策。

复现：检查公开GTM容器请求与隐私政策承诺；账户验证仅由运营在GTM Preview/GA4 DebugView完成，线上审计不提交真实purchase。

验收：账号配置、同意前后网络及事件单次触发有证据；无PII外发，政策与实际标签一致

责任：运营+开发；预计：1–2人日（估算）

后台对应功能：仅根据任务类型寻找商品发布/内容编辑/SEO或配置功能，实际菜单未经验证。如后台不支持该字段，将该任务交开发；修改前备份当前文本并记录正式SKU白名单，修改后读公开页复核。

## UX-05 · P2 · 营销弹窗在购物及结账过程中打断操作

状态：待修改；验证：已验证

页面：https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia、https://echobae.com/checkout

问题与证据：commerce-popup-attempt.json与checkout-initial-attempt.json中Get an extra discount!对话框拦截ADD TO CART/Use coupon；正常点击×可关闭，未证明按钮本身失效。

操作/修复建议：运营/开发限制营销弹窗在checkout触发，或改非阻塞提示；避免年龄验证后马上叠营销弹窗；保留可关闭、键盘可用与会话频率控制。

复现：正常成年确认后停留商品/Checkout，等待营销弹窗，检查遮挡购物或优惠入口；正常点击×恢复操作，不提交邮箱订阅。

验收：完整购物到结账过程中无非必要阻塞弹窗；年龄验证正常、优惠入口仍可见；测试不触发订阅邮件

责任：运营+开发；预计：0.5人日（估算）

后台对应功能：仅根据任务类型寻找商品发布/内容编辑/SEO或配置功能，实际菜单未经验证。如后台不支持该字段，将该任务交开发；修改前备份当前文本并记录正式SKU白名单，修改后读公开页复核。

## SEO-08 · P3 · 商品Schema基础有效但变体/图片字段仍需发布校验

状态：待优化；验证：基础语法/样本字段已验证；富结果及变体规则待验证

页面：https://echobae.com/p/demo-sh-020、https://echobae.com/p/demo-sh-030、https://echobae.com/p/demo-sh-060、https://echobae.com/p/demo-sh-080、https://echobae.com/p/demo-sh-090、https://echobae.com/p/demo-sh-100、https://echobae.com/p/robovac-x1、https://echobae.com/p/demo-sh-001（完整列表见FULL_AUDIT.md）

问题与证据：crawl.json：JSON-LD均可解析；Lydia Product name/sku QY029/Offer USD1609.99/InStock与基础页一致。Demo有相对image和评分；正式样本没有AggregateRating。

操作/修复建议：先清理Demo；确保绝对图片URL和真实库存/价格，适用时补SKU/商品变体模型，禁止无评价造评分；按Google产品与成人内容富结果规范人工复核。不优先添加FAQPage争取普通电商FAQ富结果。

复现：从代表SKU初始HTML解析Product/Offer/BreadcrumbList，比较默认USD价格、SKU、图片和库存标签；后台真实库存另验。

验收：正式商品Schema可解析且与默认配置一致；代表变体价格/库存策略明确；官方验证工具检查后保存结果，不承诺展示

责任：开发+运营；预计：0.5–1人日（估算）

后台对应功能：仅根据任务类型寻找商品发布/内容编辑/SEO或配置功能，实际菜单未经验证。如后台不支持该字段，将该任务交开发；修改前备份当前文本并记录正式SKU白名单，修改后读公开页复核。

## CONT-05 · P3 · Summer Sale 2026横幅在10月仍显示

状态：未验证；验证：文字已验证；活动有效性待运营核验

页面：https://echobae.com/

问题与证据：crawl及所有浏览样本顶部Summer Sale 2026 - Extra10% OFF · Shop now；未获活动起止和折扣规则。

操作/修复建议：运营确认实际促销有效性、代码和适用SKU；过期则撤下，仍有效则改为真实活动名并补规则。

复现：读取顶部Summer Sale2026文案；运营核对当前活动起止、优惠规则与实际有效码，不仅凭季节判定过期。

验收：横幅活动名称/期限/折扣条件与实际结账优惠一致

责任：运营；预计：0.25人日（估算）

后台对应功能：仅根据任务类型寻找商品发布/内容编辑/SEO或配置功能，实际菜单未经验证。如后台不支持该字段，将该任务交开发；修改前备份当前文本并记录正式SKU白名单，修改后读公开页复核。
