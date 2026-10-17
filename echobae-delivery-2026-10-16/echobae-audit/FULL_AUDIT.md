# Echobae 上线前审计报告

结论：**不建议现在直接正式推广或开放收录。**先清理公开Demo/复制商品、核对政策与价格一致性；然后在批准发布时解除索引限制并生成Sitemap。购物流程已验证到结账展示，未付款/下单；完成公开审计不等于后台或交易链路全面验收。

## 范围与方法

只读访问线上公开页面；测试正常年龄确认与隔离匿名购物会话，未提交地址、订单、付款、订阅、联系表单或营销邮件，未修改线上配置。没有后台、源代码、GSC/GA4/GTM容器权限，也没有私网或攻击性扫描。资源采集曾对页面直接引用的2个内部媒体URL收到代理403，识别后停止，未进一步探测。

使用现有Cloud环境和之前证据，无重新初始化。发现流程先导航/Footer/分类/文章内链，后浏览器搜索与完整商品分页；清单为URL_INVENTORY.csv，参数页计为独立URL。非空Sitemap不存在，无法通过Sitemap确认全站总量。公开链接之外的孤立/未发布页面无法排除。

基础检查228/228发现URL，含189个商品URL；浏览器深度为25个唯一代表页面、58个视口记录（25桌面+25移动+8平板），另外搜索/随机404/结账/购物车有专项记录；不是189个商品都深度验收。3个正式SKU QY029/QY073/QY023及1个Demo不同图片/配置模板深查。3篇可发现正式文章全部做桌面/移动检查。性能4类页面各2设备×3次，另确认年龄后首页移动3次。

时间：2026-10-13，约14:40起（UTC+8；每个HTTP Date与Lighthouse fetchTime保存UTC）。Chrome154、Playwright1.62、Lighthouse13.5。桌面1440×900，移动390×844，平板768×1024；Lighthouse设备另有默认设置，不能把截图视口当作Lighthouse视口。浏览器补齐平台CA信任后保留TLS验证。

截图`*-settled.png`为等待初始化/正常确认后的代表首屏；早期截图可能包含加载占位/年龄弹窗，不把短暂占位宣称为最终页面损坏。evidence/previous是上次任务证据，未伪称本次重测。

## 覆盖统计

|类型|发现且基础检查URL数|
|---|---:|
|首页|1|
|分类/列表/筛选|15|
|内容/政策/支持|13|
|博客列表/筛选|3|
|账户|2|
|购物车|1|
|博客文章|4|
|商品详情|189|

详细清单：[URL_INVENTORY.csv](URL_INVENTORY.csv)。发现228、基础228、深度25唯一页面；193→227个200是扩展清单后的更新，不混用早期数量。实际打不开的链接为/blogs/silicone-doll-care-guide；www和部分第三方被代理拒绝。

## 分维度结论与已通过检查

### 抓取、索引、架构

228个发现URL中227个200、1个404（指南护理内链）；HTTP/参数/随机不存在路径/Googlebot UA专项另外保存http-checks.json。首页/正式SKU/3分类/3正式文章均返回200并有Canonical。所有200保留noindex,nofollow，robots全站Disallow与Sitemap为空均需正式发布时处理，不能当作预发布恶意配置。

允许抓取、允许索引、技术可索引和Google实际收录是四个不同结论。目前前两项未满足；后两项不能通过HTTP200推出。GSC权限缺失，不知道真实索引覆盖。Googlebot伪装UA读取首页及商品200仅证明该UA请求，没有验证Googlebot IP身份或搜索引擎可达性。

普通随机不存在URL返回404，随机商品却200空壳（SEO-03）。HTTPS non-www正常；http non-www在代理中返回200未见Location，不能确认源站是否由代理升级；www HTTPS代理返回403 tunnel，域名重定向待无代理环境/源站验证，不能宣布www坏站。用户路径点击深度至少：首页→分类→商品，首页→Blog→文章；浏览器分页商品可达，但有些分页客户端状态URL保持/products且初始链接只含当前页，需开发增加稳定href分页。未确认孤立页总数。

### Title、Meta、正文与关键词

首页Title、Meta、H1与silicone sex dolls主题一致，无必要机械改写。分类Title New Arrivals/Best Value/Best Sellers合理，应修SSR通用H1而非堆词。3篇文章覆盖最真实/材料对比/首次购买三种意图，不以相同核心词自动判断关键词蚕食；后台搜索查询/排名数据未知。产品Title重复品牌有明确改稿见SEO-05。商品核心名称/高度/SKU应保留；Siwei/Aurora混用需更正事实。图片alt属性基础检查均存在，但是否充分描述图片仍需逐图内容审核，存在alt不等于质量优秀。

### Schema

已对228页实际JSON-LD尝试解析，无语法解析异常。首页Organization/WebSite含SearchAction，搜索路由可执行；正式商品Product/Offer/BreadcrumbList样本名称、SKU、基础USD价格一致；3文章BlogPosting和BreadcrumbList有headline/image/datePublished/dateModified/publisher，未发现假定作者字段就必须缺陷。分类CollectionPage合理；普通政策WebPage合理。

Schema有效不保证富媒体展示；涉及成人内容需按Google结构化数据内容政策/SafeSearch规则复核，不能承诺产品rich result。普通电商FAQ不因添加FAQPage就能获得Google FAQ富结果；不建议优先添加。商品附加功能不自动等于独立SKU变体，ProductGroup是否适用须真实SKU建模确认。真实库存未获得后台独立验证，不把所有InStock标签等同真实可交货。

### 资源、图片与响应式

58个视口记录无documentElement级横向溢出；不代表每个组件和全部断点均已验收。正式样本图片/脚本/CSS主体能加载，第三方字体/GTM与picsum代理拒绝另列环境限制。图片原始、渲染尺寸、fit/srcset/alt均保存IMAGE_AUDIT.csv，字节未实测的明确标未单独测量。cover裁剪和伪srcset是模板问题；对裁剪是否符合特定构图仍要设计确认。首页Banner原比例contain不属于同类强制商品裁剪。

189个商品页面主图URL完成分类：73个站内主图HEAD返回200，116个第三方/内部地址未继续请求；HEAD通过不等于完整图片解码成功。深度样本另有浏览器解码与62个资源GET证据。

首页desktop三次CLS均0.456637，明显高于0.1目标；Banner缺尺寸与下方区块位移已在Lighthouse报告定位（PERF-04）。移动低CLS不能代表桌面。

### 年龄弹窗、UX及无障碍

正常首次弹窗可出现，合法成年确认后保存ecom-age-gate-verified，再刷新弹窗消失；没有绕过校验。Leave Site代码公开行为为配置leaveUrl或about:blank，未模拟未成年人。键盘焦点缺陷已实际Tab复现。Lighthouse颜色对比度/标题层级未通过项保留各报告；自动化分数不是完整屏幕阅读器/WCAG认证。首页H4和分类H3存在跳级，开发应按实际章节调整H2/H3语义，不为视觉字号选择heading标签。营销弹窗可正常关闭，但实际拦截过购物/优惠码交互；建议运营避免checkout触发促销弹窗，减少连续弹窗干扰，而不是移除年龄验证。

### 商品、搜索、购物车与结账

搜索silicone返回77项，Lydia5项，无结果关键词返回0项/无结果提示；列表标签含smart-home等Demo分类，随CAT-01清理。Next分页和price_asc排序实际操作；完整分页补查到189个商品URL。只验证公开页面发现和排序结果，未验证全部筛选组合/价格上下界。

QY029图像下一张可切换；AI升级+79.99后总价1689.98，正常ADD TO CART可添加并携带选项；购物车数量2对应3379.96，刷新/返回不丢商品，删除后空车。初次快速读取cart empty/checkout Loading经等待复测已排除，不列作功能阻断。

结账Shipping address表单有必填姓名/email/国家/地区/邮编/地址/电话，页面Stripe与PayPal选项存在。切US/Canada/Brazil地区候选可变化，Standard Free展示与政策需核对。优惠码入口展开有输入和Apply，未应用真实有效优惠码或提交订单；地址验证、精确运费、税额、支付跳转、退款/取消订单、有效优惠码计算未验证，必须在第三方开发的测试模式独立验收。未填虚构地址去触发真实订单。

### 信任、政策、内容

About/Contact/FAQ/Shipping/Returns/Privacy/Payment/Care/Wholesale/Affiliate/Reviews均读过公开内容，mail support@echobae.com公开存在；未发送邮件或联系消息，不能证明送达或客服SLA。隐私/退款占位、运费时效矛盾、型号名和五星/0评价矛盾有逐条证据。退款政策“all sales final”与瑕疵处理/法定权利关系由业务/法务核实，不作法律合规认证。Privacy的“永不向第三方分析披露”等与GTM标签需运营核实，不仅凭GTM存在宣称已经泄露。

博客3篇正文/表格/图片/相关链接实际检查，发现护理404与重复品牌；文章医疗/安全材料及“body-safe”断言无供应商测试证书，事实准确性待运营取证，不制造SEO字数目标或AI检测分数任务。

### 前端、API、安全与追踪

runtime-blocks全深度样本持续404，但公开bundle已捕获返回空列表；页面主要正文、商品和购物流程仍可运行。公开bundle仅用于解释已出现的请求，未访问后台或非公开源码；发现页面引用的内部媒体地址后停止请求，没有探测其他私有接口。Hydration49/58记录，但无未捕获pageerror；异常原因需开发验证。公开Demo包含内部HTTP图片URL，已停止相关内部地址测试，未进一步探测私网。

HTTPS访问和HSTS在200页面可见；CSP等200页缺失是公开可见配置观察，不等于已攻破/XSS漏洞。账户登录/找回页GET可访问但未登录、注册、重置密码或验证邮件。未进行支付PCI、后端权限或数据库安全认证。

公开GTM请求含容器GTM-T2DKHJKK；代理失败，GA4 ID、事件、真实采集和GSC账户都未验证。必需cookies/Consent Mode的最终行为需正常网络与账户检查。

## 问题清单与执行建议

共37项：P0 2、P1 16、P2 17、P3 2。P0含有意预发布限制的条件项；P2/P3中待验证事项不被伪称已确认故障。工期是无源码条件的粗估人日，非承诺。

### CAT-01 · P0 · 主商品列表公开展示 Demo、测试及复制商品

**类别：** 商品/内容

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 打开/products并查看首屏商品、切换Next分页；打开/pages/help的Best seller；对比正式分类new-arrival。记录智能家居Demo与copy标题，test888命名需运营确认是否测试商品。

**证据：** evidence/browser-discovery.json：/products 显示189 items，首屏 Pro Smart Scale、Video Doorbell 等；99个 /p/demo-sh-* URL；另有test888命名及4个(copy)商品，测试用途需运营核实。evidence/pagination.json 完整分页。

**影响：** 污染商品发现、品牌可信度、搜索内容和误购风险

**可能根因：** 测试数据与正式数据使用同一公开目录；发布过滤逻辑待开发验证

**修复方法：** 运营确认正式 SKU 白名单，草稿/下架 Demo 和复制商品；开发确保列表、搜索、推荐、SSR、Schema、Sitemap 仅输出发布且有效商品。不要仅靠 noindex 隐藏测试商品。

**负责人：** 运营+开发

**预计工作量：** 1–2人日（估算）

**验收标准：** 全部列表分页、搜索、Help推荐和Sitemap无测试商品；测试详情按下架策略返回404/410或有意义的301；真实商品数量与后台白名单一致

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/products
- https://echobae.com/pages/help
- https://echobae.com/p/demo-sh-020
- https://echobae.com/p/demo-sh-030
- https://echobae.com/p/demo-sh-060
- https://echobae.com/p/demo-sh-080
- https://echobae.com/p/demo-sh-090
- https://echobae.com/p/demo-sh-100
- https://echobae.com/p/demo-sh-001
- https://echobae.com/p/demo-sh-002
- https://echobae.com/p/demo-sh-003
- https://echobae.com/p/demo-sh-004
- https://echobae.com/p/demo-sh-005
- https://echobae.com/p/demo-sh-006
- https://echobae.com/p/demo-sh-007
- https://echobae.com/p/demo-sh-008
- https://echobae.com/p/demo-sh-009
- https://echobae.com/p/demo-sh-011
- https://echobae.com/p/demo-sh-012
- https://echobae.com/p/demo-sh-013
- https://echobae.com/p/demo-sh-014
- https://echobae.com/p/demo-sh-095
- https://echobae.com/p/demo-sh-071
- https://echobae.com/p/demo-sh-045
- https://echobae.com/p/demo-sh-044
- https://echobae.com/p/demo-sh-022
- https://echobae.com/p/demo-sh-021
- https://echobae.com/p/demo-sh-028
- https://echobae.com/p/demo-sh-078
- https://echobae.com/p/demo-sh-055
- https://echobae.com/p/demo-sh-084
- https://echobae.com/p/demo-sh-036
- https://echobae.com/p/demo-sh-096
- https://echobae.com/p/demo-sh-092
- https://echobae.com/p/demo-sh-085
- https://echobae.com/p/demo-sh-056
- https://echobae.com/p/demo-sh-081
- https://echobae.com/p/demo-sh-079
- https://echobae.com/p/demo-sh-054
- https://echobae.com/p/demo-sh-066
- https://echobae.com/p/demo-sh-015
- https://echobae.com/p/demo-sh-091
- https://echobae.com/p/demo-sh-088
- https://echobae.com/p/demo-sh-087
- https://echobae.com/p/demo-sh-077
- https://echobae.com/p/demo-sh-065
- https://echobae.com/p/demo-sh-063
- https://echobae.com/p/demo-sh-099
- https://echobae.com/p/demo-sh-076
- https://echobae.com/p/demo-sh-075
- https://echobae.com/p/demo-sh-046
- https://echobae.com/p/demo-sh-051
- https://echobae.com/p/demo-sh-041
- https://echobae.com/p/demo-sh-052
- https://echobae.com/p/demo-sh-037
- https://echobae.com/p/demo-sh-027
- https://echobae.com/p/demo-sh-053
- https://echobae.com/p/demo-sh-097
- https://echobae.com/p/demo-sh-072
- https://echobae.com/p/demo-sh-029
- https://echobae.com/p/demo-sh-031
- https://echobae.com/p/demo-sh-057
- https://echobae.com/p/demo-sh-083
- https://echobae.com/p/demo-sh-082
- https://echobae.com/p/demo-sh-058
- https://echobae.com/p/demo-sh-048
- https://echobae.com/p/demo-sh-059
- https://echobae.com/p/demo-sh-034
- https://echobae.com/p/demo-sh-086
- https://echobae.com/p/demo-sh-061
- https://echobae.com/p/demo-sh-064
- https://echobae.com/p/demo-sh-038
- https://echobae.com/p/demo-sh-089
- https://echobae.com/p/demo-sh-033
- https://echobae.com/p/demo-sh-050
- https://echobae.com/p/demo-sh-040
- https://echobae.com/p/demo-sh-047
- https://echobae.com/p/demo-sh-068
- https://echobae.com/p/demo-sh-094
- https://echobae.com/p/demo-sh-069
- https://echobae.com/p/demo-sh-016
- https://echobae.com/p/demo-sh-018
- https://echobae.com/p/demo-sh-024
- https://echobae.com/p/demo-sh-032
- https://echobae.com/p/demo-sh-039
- https://echobae.com/p/demo-sh-049
- https://echobae.com/p/demo-sh-074
- https://echobae.com/p/demo-sh-023
- https://echobae.com/p/demo-sh-035
- https://echobae.com/p/demo-sh-042
- https://echobae.com/p/demo-sh-043
- https://echobae.com/p/demo-sh-093
- https://echobae.com/p/demo-sh-010
- https://echobae.com/p/demo-sh-017
- https://echobae.com/p/demo-sh-019
- https://echobae.com/p/demo-sh-025
- https://echobae.com/p/demo-sh-026
- https://echobae.com/p/demo-sh-062
- https://echobae.com/p/demo-sh-067
- https://echobae.com/p/demo-sh-073
- https://echobae.com/p/demo-sh-098
- https://echobae.com/p/robovac-x1
- https://echobae.com/p/test888
- https://echobae.com/p/elva-168cm-f-cup-demo-copy-copy
- https://echobae.com/p/elva-168cm-f-cup-demo-copy-copy-copy
- https://echobae.com/p/elva-168cm-f-cup-demo-copy-copy-copy-copy
- https://echobae.com/p/elva-168cm-f-cup-demo-copy-copy-copy-copy-copy

### SEO-01 · P0 · 全站禁止抓取与索引（上线前可能有意设置）

**类别：** 上线收录条件

**验证状态：** 已验证

**问题状态：** 待发布时解除

**复现步骤：** 分别GET /robots.txt、首页、正式商品和文章；查看原始HTML meta[name=robots]及X-Robots-Tag，不用浏览器插件替代HTTP证据。

**证据：** evidence/crawl.json：227个HTTP200 URL均有noindex,nofollow；evidence/http-checks.json：robots.txt为User-agent:* / Disallow:/。

**影响：** 正式开放自然搜索前不能满足抓取和索引条件；不说明Google实际收录率

**可能根因：** 预发布全局SEO开关；是否有其他响应头/网关设置待开发确认

**修复方法：** 保留预发布限制直到正式验收。发布时仅对公开营销/商品/文章页解除noindex并开放robots；购物车、结账、账户、站内搜索继续按用途排除。先允许抓取，Google才能读取noindex变更；同步Sitemap和GSC检查。

**负责人：** 运营+开发

**预计工作量：** 0.5–1人日（估算）

**验收标准：** 正式页面200、可抓取且无meta或X-Robots-Tag noindex；私有/交易页面仍适当排除；GSC实时测试通过，实际索引另行追踪

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/
- https://echobae.com/products
- https://echobae.com/collections/new-arrival
- https://echobae.com/collections/best-value
- https://echobae.com/custom-made
- https://echobae.com/contact-us
- https://echobae.com/blog
- https://echobae.com/pages/help
- https://echobae.com/account/login
- https://echobae.com/cart
- https://echobae.com/collections/best-sellers
- https://echobae.com/customer-reviews
- https://echobae.com/blog/what-are-the-most-realistic-sex-dolls
- https://echobae.com/blog/tpe-vs-silicone-sex-doll
- https://echobae.com/blog/silicone-sex-doll-buying-guide
- https://echobae.com/payment-method
- https://echobae.com/shipping-policy
- https://echobae.com/privacy-policy
- https://echobae.com/return-refund-policy
- https://echobae.com/about-us
- https://echobae.com/wholesale
- https://echobae.com/affiliate-program
- https://echobae.com/faq
- https://echobae.com/sex-doll-care
- https://echobae.com/p/demo-sh-020
- https://echobae.com/p/demo-sh-030
- https://echobae.com/p/demo-sh-060
- https://echobae.com/p/demo-sh-080
- https://echobae.com/p/demo-sh-090
- https://echobae.com/p/demo-sh-100
- https://echobae.com/p/robovac-x1
- https://echobae.com/p/demo-sh-001
- https://echobae.com/p/demo-sh-002
- https://echobae.com/p/demo-sh-003
- https://echobae.com/p/demo-sh-004
- https://echobae.com/p/demo-sh-005
- https://echobae.com/p/demo-sh-006
- https://echobae.com/p/demo-sh-007
- https://echobae.com/p/demo-sh-008
- https://echobae.com/p/demo-sh-009
- https://echobae.com/p/demo-sh-011
- https://echobae.com/p/demo-sh-012
- https://echobae.com/p/demo-sh-013
- https://echobae.com/p/demo-sh-014
- https://echobae.com/p/149cm-christmas-silicone-love-doll-huaze
- https://echobae.com/p/170cm-realistic-silicone-sex-doll-jiachen
- https://echobae.com/p/159cm-natural-look-silicone-doll-jiachen
- https://echobae.com/p/170cm-real-skin-texture-silicone-sex-doll-jiachen
- https://echobae.com/p/169cm-silicone-realistic-sex-doll-jieman
- https://echobae.com/p/159cm-realistic-silicone-sex-doll-lanxin
- https://echobae.com/p/149cm-silicone-sex-doll-lanxin
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia
- https://echobae.com/p/149cm-silicone-doll-lydia
- https://echobae.com/p/169cm-premium-silicone-love-doll-lydia
- https://echobae.com/p/159cm-natural-look-silicone-doll-lydia
- https://echobae.com/p/169cm-anime-silicone-sex-doll-luoli
- https://echobae.com/p/169cm-realistic-silicone-sex-doll-muyao
- https://echobae.com/p/153cm-ai-companion-silicone-doll-muyao
- https://echobae.com/p/169cm-natural-look-silicone-doll-siwei
- https://echobae.com/p/169cm-teacher-fantasy-silicone-doll-ruyan
- https://echobae.com/p/159cm-anime-silicone-doll-ruyan
- https://echobae.com/p/159cm-teacher-fantasy-silicone-doll-siwei
- https://echobae.com/p/169cm-realistic-silicone-sex-doll-juaner
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-juaner
- https://echobae.com/p/149cm-slim-silicone-love-doll-juaner
- https://echobae.com/p/149cm-lifelike-silicone-sex-doll-sheena
- https://echobae.com/p/159cm-premium-silicone-love-doll-sheena
- https://echobae.com/p/169cm-natural-look-silicone-doll-sheena
- https://echobae.com/p/149cm-cosplay-silicone-doll-sheena
- https://echobae.com/p/159cm-anime-silicone-sex-doll-xiaen
- https://echobae.com/p/149cm-anime-silicone-love-doll-xiaoyu
- https://echobae.com/p/159cm-silicone-adult-love-doll-xingzi
- https://echobae.com/p/169cm-ai-silicone-companion-doll-xingzi
- https://echobae.com/blog?category=Buyer+Guide
- https://echobae.com/blog?category=updates
- https://echobae.com/account/forgot-password
- https://echobae.com/p/149cm-white-hair-silicone-doll-siwei
- https://echobae.com/p/169cm-realistic-silicone-love-doll-zhuzhu
- https://echobae.com/p/149cm-premium-silicone-love-doll-jieyi
- https://echobae.com/p/159cm-implanted-hair-silicone-sex-doll-zhiyan
- https://echobae.com/p/169cm-lifelike-silicone-sex-doll-yumeng
- https://echobae.com/p/149cm-anime-silicone-doll-yumeng
- https://echobae.com/p/159cm-cosplay-silicone-sex-doll-yumeng
- https://echobae.com/p/149cm-realistic-silicone-sex-doll-yufei
- https://echobae.com/p/169cm-silicone-adult-love-doll-yuran
- https://echobae.com/p/159cm-natural-look-silicone-doll-yinuo
- https://echobae.com/p/153cm-fantasy-silicone-sex-doll-yanke
- https://echobae.com/p/169cm-premium-silicone-love-doll-yawen
- https://echobae.com/c/silicone-sex-dolls
- https://echobae.com/products?tag=bestseller
- https://echobae.com/products?tag=smart-home
- https://echobae.com/p/demo-sh-095
- https://echobae.com/p/demo-sh-071
- https://echobae.com/p/demo-sh-045
- https://echobae.com/p/demo-sh-044
- https://echobae.com/p/demo-sh-022
- https://echobae.com/p/demo-sh-021
- https://echobae.com/products?tag=sale
- https://echobae.com/products?tag=voice-control
- https://echobae.com/p/demo-sh-028
- https://echobae.com/p/demo-sh-078
- https://echobae.com/p/demo-sh-055
- https://echobae.com/products?tag=new
- https://echobae.com/p/demo-sh-084
- https://echobae.com/p/demo-sh-036
- https://echobae.com/p/demo-sh-096
- https://echobae.com/p/demo-sh-092
- https://echobae.com/p/demo-sh-085
- https://echobae.com/p/demo-sh-056
- https://echobae.com/p/demo-sh-081
- https://echobae.com/p/demo-sh-079
- https://echobae.com/p/demo-sh-054
- https://echobae.com/p/demo-sh-066
- https://echobae.com/p/demo-sh-015
- https://echobae.com/p/demo-sh-091
- https://echobae.com/p/demo-sh-088
- https://echobae.com/p/demo-sh-087
- https://echobae.com/p/demo-sh-077
- https://echobae.com/p/demo-sh-065
- https://echobae.com/p/demo-sh-063
- https://echobae.com/products?tag=budget
- https://echobae.com/p/demo-sh-099
- https://echobae.com/p/demo-sh-076
- https://echobae.com/p/demo-sh-075
- https://echobae.com/p/demo-sh-046
- https://echobae.com/p/demo-sh-051
- https://echobae.com/p/demo-sh-041
- https://echobae.com/products?tag=wireless
- https://echobae.com/p/demo-sh-052
- https://echobae.com/p/demo-sh-037
- https://echobae.com/p/demo-sh-027
- https://echobae.com/p/demo-sh-053
- https://echobae.com/products?tag=eco-friendly
- https://echobae.com/products?tag=premium
- https://echobae.com/p/demo-sh-097
- https://echobae.com/p/demo-sh-072
- https://echobae.com/p/demo-sh-029
- https://echobae.com/p/demo-sh-031
- https://echobae.com/p/demo-sh-057
- https://echobae.com/p/demo-sh-083
- https://echobae.com/p/demo-sh-082
- https://echobae.com/p/demo-sh-058
- https://echobae.com/p/demo-sh-048
- https://echobae.com/products?tag=energy-saving
- https://echobae.com/p/demo-sh-059
- https://echobae.com/p/demo-sh-034
- https://echobae.com/p/demo-sh-086
- https://echobae.com/p/demo-sh-061
- https://echobae.com/p/demo-sh-064
- https://echobae.com/p/demo-sh-038
- https://echobae.com/p/demo-sh-089
- https://echobae.com/p/149cm-anime-silicone-doll-yawen
- https://echobae.com/p/149cm-lifelike-silicone-sex-doll-xiuyan
- https://echobae.com/p/149cm-realistic-silicone-sex-doll-xiuyan
- https://echobae.com/p/159cm-realistic-silicone-sex-doll-muyao
- https://echobae.com/p/169cm-realistic-silicone-sex-doll-nancy
- https://echobae.com/p/159cm-premium-silicone-love-doll-cailin
- https://echobae.com/p/159cm-bikini-silicone-love-doll-linda
- https://echobae.com/p/169cm-big-breast-silicone-sex-doll-xiuyan
- https://echobae.com/p/159cm-cosplay-silicone-sex-doll-cailin
- https://echobae.com/p/159cm-twin-ponytail-silicone-doll-nancy
- https://echobae.com/p/169cm-lifelike-silicone-sex-doll-jieman
- https://echobae.com/p/169cm-asian-silicone-sex-doll-xiaowu
- https://echobae.com/p/159cm-cute-silicone-love-doll-xiuyan
- https://echobae.com/p/demo-sh-033
- https://echobae.com/p/demo-sh-050
- https://echobae.com/p/demo-sh-040
- https://echobae.com/p/smart-plug-4pack
- https://echobae.com/p/demo-sh-047
- https://echobae.com/p/demo-sh-068
- https://echobae.com/p/demo-sh-094
- https://echobae.com/p/demo-sh-069
- https://echobae.com/p/demo-sh-016
- https://echobae.com/p/demo-sh-018
- https://echobae.com/p/demo-sh-024
- https://echobae.com/p/demo-sh-032
- https://echobae.com/p/demo-sh-039
- https://echobae.com/p/demo-sh-049
- https://echobae.com/p/demo-sh-074
- https://echobae.com/p/demo-sh-023
- https://echobae.com/p/demo-sh-035
- https://echobae.com/p/demo-sh-042
- https://echobae.com/p/demo-sh-043
- https://echobae.com/p/demo-sh-093
- https://echobae.com/p/demo-sh-010
- https://echobae.com/p/demo-sh-017
- https://echobae.com/p/demo-sh-019
- https://echobae.com/p/demo-sh-025
- https://echobae.com/p/demo-sh-026
- https://echobae.com/p/demo-sh-062
- https://echobae.com/p/demo-sh-067
- https://echobae.com/p/demo-sh-073
- https://echobae.com/p/demo-sh-098
- https://echobae.com/p/149cm-implanted-hair-silicone-doll-muyao
- https://echobae.com/p/149cm-lifelike-silicone-sex-doll-baoer
- https://echobae.com/p/149cm-lifelike-silicone-sex-doll-nancy
- https://echobae.com/p/149cm-natural-look-silicone-doll-nancy
- https://echobae.com/p/149cm-realistic-silicone-sex-doll-ailing
- https://echobae.com/p/149cm-realistic-silicone-sex-doll-aurora
- https://echobae.com/p/153cm-real-skin-texture-silicone-sex-doll-katelyn
- https://echobae.com/p/153cm-real-skin-texture-silicone-sex-doll-lydia
- https://echobae.com/p/159cm-blonde-silicone-love-doll-miriam
- https://echobae.com/p/159cm-cosplay-silicone-sex-doll-baoer
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-bersa
- https://echobae.com/p/159cm-premium-silicone-love-doll-qiuyu
- https://echobae.com/p/169cm-bikini-silicone-sex-doll-linda
- https://echobae.com/p/169cm-blonde-silicone-sex-doll-nancy
- https://echobae.com/p/169cm-premium-silicone-love-doll-yufei
- https://echobae.com/p/169cm-slim-silicone-sex-doll-haiyue
- https://echobae.com/p/170cm-bikini-silicone-sex-doll-perry
- https://echobae.com/p/1784262609174
- https://echobae.com/p/elva-168cm-f-cup-demo
- https://echobae.com/p/elva-168cm-f-cup-demo-copy-copy
- https://echobae.com/p/elva-168cm-f-cup-demo-copy-copy-copy
- https://echobae.com/p/elva-168cm-f-cup-demo-copy-copy-copy-copy
- https://echobae.com/p/elva-168cm-f-cup-demo-copy-copy-copy-copy-copy
- https://echobae.com/p/smart-led-strip
- https://echobae.com/p/test888
- https://echobae.com/p/169cm-silicone-large-breast-sex-doll-sheena
- https://echobae.com/p/1783396233625ff
- https://echobae.com/p/1783396905878
- https://echobae.com/p/1783397572134
- https://echobae.com/p/1783569515569
- https://echobae.com/p/1783569871599
- https://echobae.com/p/e2e-ship-heavy
- https://echobae.com/p/e2e-ship-light
- https://echobae.com/p/e2e-ship-volumetric

### SEO-02 · P1 · sitemap.xml为空索引

**类别：** Sitemap

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** GET /sitemap.xml，按XML解析sitemapindex的sitemap/loc子项；当前数量为0。

**证据：** evidence/http-checks.json：HTTP200，<sitemapindex ...></sitemapindex>，0个子Sitemap。

**影响：** GSC无有效URL清单；新站发现效率降低

**可能根因：** 内容发布状态或Sitemap生成器未接入正式目录，根因待开发验证

**修复方法：** 生成只包含已发布、200、自引用规范且允许索引页面的urlset或非空索引；剔除Demo、参数、搜索、账户、交易及失效URL；发布后提交GSC。

**负责人：** 开发+运营

**预计工作量：** 0.5–1人日（估算）

**验收标准：** XML可解析且非空，所有loc为HTTPS规范URL；覆盖正式SKU和文章清单；GSC能读取且无测试URL

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/sitemap.xml

### POL-01 · P1 · 隐私政策保留服务器国家占位符

**类别：** 隐私/内容

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 打开隐私政策，搜索[Country与Country Where Servers；核对数据存储章节与国际转移章节。

**证据：** evidence/page-text.json：[Country, e.g., United States / Germany / Singapore]、[Country Where Servers Are Located]。

**影响：** 用户无法了解真实数据存储和跨境处理位置

**可能根因：** 未完成政策模板填充；真实服务器和供应商位置没有后台证据

**修复方法：** 运营向开发/供应商核实国家、法律实体、数据处理和真实保留期限；据事实替换两处占位并审核承诺，不编造数据位置。

**负责人：** 运营（开发提供事实）

**预计工作量：** 0.5–1人日（估算）

**验收标准：** 政策无方括号占位，实际国家/供应商/联系主体准确，必要法律审核完成

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/privacy-policy

### POL-02 · P1 · 配送时效在首页和政策中矛盾

**类别：** 物流/内容

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 展开首页How Long Does It Take FAQ，读取3–7days；对照Shipping Policy的Standard/Express与production分段。

**证据：** 首页FAQ发货后3–7 days；Shipping Policy Express 10–14 business days、Standard 30–35 days after dispatch，均不含生产。

**影响：** 错误交付预期影响售前咨询与退款争议

**可能根因：** 多个内容模块分别维护未同步

**修复方法：** 运营核实真实路线和生产周期，统一所有FAQ、商品FAQ、政策和结账配送说明。建议首页改为：“Delivery time depends on your destination and shipping method. See our Shipping Policy for current estimates. Production time is additional.”

**负责人：** 运营+开发

**预计工作量：** 0.5–1人日（估算）

**验收标准：** 同一配送方式在首页/商品/政策/结账估计一致，明确工作日、生产时间和例外

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/
- https://echobae.com/shipping-policy

### POL-03 · P1 · 退款政策含缺失运费金额和未核实支付渠道

**类别：** 退款/内容

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 打开Returns政策，定位International Sex Doll Shipping的$ *与Accepted payment methods列表；对照实际结账支付选项。

**证据：** 公开文本International shipping ... starts from $ *；列Personal check/Cashier’s check/Money order/电话fax付款；结账只展示Stripe、PayPal。

**影响：** 政策不可执行且可能误导付款/运费

**可能根因：** 迁移的政策模板未结合实际业务配置

**修复方法：** 用经核实费率替换$ *；如没有最低价，改“Shipping costs are shown at checkout before payment.”；删除未提供的付款方式，明确取消、瑕疵/错发处置与法律适用例外；由运营/法务确认，勿捏造退款权利。

**负责人：** 运营

**预计工作量：** 0.5–1人日（估算）

**验收标准：** 政策无金额占位；付款渠道与实际可用方式一致；瑕疵和错发流程明确并经业务负责人审核

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/return-refund-policy

### CART-01 · P1 · 购物车及结账划线价与商品页不一致

**类别：** 购物车/价格

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 新匿名会话正常确认年龄；打开QY029 Lydia，选AI Companion Voice +79.99；记录PDP1689.98/1800；ADD TO CART后点击页头Cart，等初始化，记录1689.98/2027.98；数量2小计3379.96；进入结账只观察，不点击PLACE ORDER。

**证据：** evidence/browser/cart-verify.json：选AI后PDP $1689.98/$1800.00，购物车$1689.98/$2027.98，节省$338；无AI结账$1609.99/$1931.99。

**影响：** 虚高折扣展示影响可信度；实付单价及2件小计本次一致

**可能根因：** 可能购物车按售价×1.2回填比较价，或SKU比较价映射错误；源码待开发验证

**修复方法：** 统一PDP/cart/checkout的SKU和选项价格模型，保留真实compare_at_price，缺失原价则不展示划线价或节省金额；禁止自动虚构原价。

**负责人：** 开发（运营核对原价）

**预计工作量：** 1人日（估算）

**验收标准：** 基础价1609.99；AI后1689.98；2件3379.96；各页真实比较价/节省金额完全一致，无空原价推算

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia
- https://echobae.com/cart
- https://echobae.com/checkout

### POL-04 · P1 · 结账要求同意条款，但没有可访问的条款链接

**类别：** 结账/条款

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 从带商品购物车进入Checkout，滚动至terms checkbox；检查是否有可打开的条款a[href]并阅读页面，不提交订单。

**证据：** evidence/browser/checkout-checks.json：I have read and agree ... terms and conditions，links内无terms链接；导航也未发现条款页；猜测/terms-and-conditions返回404仅作辅助。

**影响：** 购买前不能阅读被要求同意的文本

**可能根因：** 条款URL未配置或组件未渲染链接；真实后台路径未知

**修复方法：** 运营提供适用条款正文和实际公开URL；开发把确认文案链接到200可读条款并保留购物车状态；补充Footer链接。不要假定404猜测路径即为唯一合法地址。

**负责人：** 运营+开发

**预计工作量：** 0.5–1人日（估算）

**验收标准：** 结账可打开完整条款，返回购物流程不丢数据；未同意不能提交，提交行为须在开发测试环境验收

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/checkout

### SEO-03 · P1 · 不存在的商品详情返回200空商品壳

**类别：** HTTP/软404

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 请求随机不存在/p/audit-nonexistent-20261013，检查HTTP200及空商品壳；对照普通随机路径404。

**证据：** evidence/http-checks.json与browser/search-checks.json：HTTP200，Title Product | Echobae，仅Products标题和Footer，没有商品。普通不存在路径则404。

**影响：** 无效URL可被当作软404，浪费抓取并误导用户

**可能根因：** 商品页未在服务端传播not-found错误

**修复方法：** 在SSR商品查询返回not-found时输出HTTP404/410，展示清楚提示和分类返回入口；真正重命名的商品做有意义301；不得统一跳首页。

**负责人：** 开发

**预计工作量：** 0.5–1人日（估算）

**验收标准：** 随机不存在商品URL直接GET与浏览器都返回404/410；真实商品保持200；不制造空200

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/p/audit-nonexistent-20261013

### IMG-01 · P1 · 商品图片srcset多候选指向同一个文件

**类别：** 响应式图片

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** Inspect分类第一张图和Lydia主图；读取srcset的URL/width候选，再读naturalWidth：不同w值指向同一URL。

**证据：** evidence/browser/deep.json：分类同一600×900 URL声明400w、800w；PDP同一600×900 URL声明720w、1440w，sizes=720px。

**影响：** 浏览器无法选择真正对应分辨率资源，可能放大且增加低效下载

**可能根因：** 媒体URL被直接复用为不同候选，图片优化服务未接通

**修复方法：** 开发生成实际400/800/1200等宽度变体或使用可验证图片服务；描述符对应实际固有宽度，sizes匹配断点；运营保留清晰原图，禁止把600px文件伪称1440w。

**负责人：** 开发+运营

**预计工作量：** 1–2人日（估算）

**验收标准：** 候选URL对应实际不同宽度；390/768/1440视口currentSrc选择符合布局/DPR；无伪描述符、明显糊图或额外CLS

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/collections/new-arrival
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia
- https://echobae.com/p/149cm-white-hair-silicone-doll-siwei

### IMG-02 · P1 · 主要商品图在不同模板强制裁剪

**类别：** 图片/裁剪

**验证状态：** 裁剪已验证；是否不当需设计确认

**问题状态：** 待修改

**复现步骤：** 390×844打开分类/商品，读取图像naturalWidth/Height与DOMRect和object-fit；对比原2:3照片和方形/4:5容器。

**证据：** evidence/browser/deep.json：600×900分类图340×340 cover，约裁掉原图高度1/3；Lydia主图342×427.5 cover，约裁掉1/6高度。这是CSS几何裁剪，不等于原文件损坏。

**影响：** 全身商品信息被截断，影响身材/姿态比较；裁剪能否接受需设计/运营确认

**可能根因：** 固定方形/4:5容器与2:3原图比例不同

**修复方法：** 主要商品展示优先2:3容器或contain完整展示；需方形卡片时由运营上传专用方形构图并设置焦点；不要全站盲目禁用cover。开发按图片类型区分容器。

**负责人：** 设计+开发+运营

**预计工作量：** 1–2人日（估算）

**验收标准：** 代表全身主图头部/脚部不被误裁、无拉伸，分类卡片构图一致；390/768/1440截图经运营确认

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/collections/new-arrival
- https://echobae.com/collections/best-value
- https://echobae.com/collections/best-sellers
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia

### PERF-01 · P1 · 代表页面移动端LCP持续偏慢

**类别：** 性能

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 使用performance.py指定代表URL，mobile新浏览器连续3次，保留JSON，按每指标取中位数；先核对代理资源失败与测试负载。

**证据：** evidence/lighthouse：4页×2设备×3次；首页首次mobile LCP中位5.6s，分类约5.6s，产品约5.9s，文章约4.9s；具体数字见PERFORMANCE_REPORT.md。

**影响：** 首屏内容等待明显；实验室数据不能代替CrUX

**可能根因：** 资源传输、轮播/加载遮罩渲染延迟和客户端初始化叠加；代理/并行浏览采集也增加波动

**修复方法：** 先稳定首屏与加载遮罩，优先LCP图片，高优先级只给当前首屏图；减少初始依赖/未使用CSS/JS。按报告网络链与LCP分段验证，保留年龄验证机制。

**负责人：** 开发

**预计工作量：** 2–4人日（估算）

**验收标准：** 同机同配置冷启动3次中位LCP≤2.5s、CLS≤0.1；复检第三方正常环境；上线后观察真实p75 CWV

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/
- https://echobae.com/collections/new-arrival
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia
- https://echobae.com/blog/tpe-vs-silicone-sex-doll

### PERF-02 · P1 · 主线程脚本开销与阻塞仍高

**类别：** JS/交互

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 打开home-mobile与home-accepted-mobile JSON的mainthread-work-breakdown/bootup-time和TBT；对公共builder初始化作Chrome Performance录制，勿把TBT当INP。

**证据：** home-mobile-1主线程Script Evaluation约3148ms；DNfd1SfM.js未使用估算86240B；确认年龄后的3次TBT中位2150ms，不能解释为真实INP。

**影响：** 初始化及交互可能卡顿，尤其移动设备

**可能根因：** 构建器运行时、内联初始化和大量模块预取/挂载；具体函数需开发性能剖析

**修复方法：** 对公共运行时、动态块注册、builder初始化和视口外组件做性能profile；按路由拆包、延后非首屏组件，保留交互和隐私校验。只把Lighthouse估计当诊断，不把节约量累加成收益。

**负责人：** 开发

**预计工作量：** 2–4人日（估算）

**验收标准：** 冷/保留存储场景各3次TBT中位≤200ms或提供分阶段改善证据；关键点击无明显长任务；生产INP用真实数据独立验收

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/
- https://echobae.com/collections/new-arrival
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia

### CONT-01 · P1 · 五星Reviews营销文字与0条评论展示不一致

**类别：** 信任/评论

**验证状态：** 展示矛盾已验证；真实性待运营核验

**问题状态：** 待修改

**复现步骤：** 对比首页客户引语、Customer Reviews All Reviews(0)、QY029商品⭐⭐⭐⭐⭐ Reviews和Reviews(0)；运营提供真实来源后核验，不自行认定伪造。

**证据：** 首页客户引语和星级；Customer Reviews实际All Reviews(0)；正式商品文案⭐⭐⭐⭐⭐ Reviews但Reviews(0)。无证据证明引语真假。

**影响：** 消费者无法核验“verified”来源和商品评价归属

**可能根因：** 营销富文本与评论系统脱节，或历史评论未导入

**修复方法：** 运营核验评价来源和授权；有真实来源则按SKU导入可追溯评价并显示数量；没有则删除五星/verified暗示，保留客观商品信息。不得编造评论或AggregateRating。

**负责人：** 运营+开发

**预计工作量：** 1–2人日（估算）

**验收标准：** 星级、数量、商品归属与可见真实记录一致；零评论不展示假星级；Schema评分与真实可见评论一致

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/
- https://echobae.com/customer-reviews
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia
- https://echobae.com/p/149cm-white-hair-silicone-doll-siwei

### CONT-02 · P1 · Siwei商品标题与正文名称不一致

**类别：** 商品准确性

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 打开QY073 Siwei，比较H1/Main SKU/正文Aurora及AI升级价格，运营确认名称/标配。

**证据：** 标题149cm White Hair AI Silicone Doll Siwei，Main SKU QY073，正文多次称Aurora；AI在额外升级区+$79.99。

**影响：** 用户难以确认型号及基础配置，退换争议风险

**可能根因：** 复制文案或内部别名未向买家解释

**修复方法：** 运营确认SKU QY073真实名称、头部/身体和AI是否标配；统一Siwei/Aurora或明确别名；AI为选配时标题移除暗示标配，说明基础配置和升级价。

**负责人：** 运营

**预计工作量：** 0.5人日（估算）

**验收标准：** Title/H1/正文/SKU/购物车型号一致；AI标配/选配明确；不改无问题商品

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/p/149cm-white-hair-silicone-doll-siwei

### SHIP-01 · P1 · 结账国家及免运费展示与政策范围不一致

**类别：** 配送配置

**验证状态：** 展示不一致已验证；实际运费/税费待测试环境验证

**问题状态：** 待修改

**复现步骤：** 有商品进入Checkout，不填个人信息；依次选择US、Canada、Brazil，记录国家/地区候选和Standard Free；对照Shipping Policy国家与两种路线。

**证据：** evidence/browser/checkout-checks.json：US/Canada/Brazil均可选择且显示Standard—Free，政策仅列10个配送国家、两种路线和按目的地计费；未填写地址、未提交订单。

**影响：** 可能让不支持地区的买家误认为可配送；最终服务端限制未验证

**可能根因：** 通用国家列表与实际配送分区未绑定，或政策滞后

**修复方法：** 运营确认支持国家、标准/快递费率及包税策略；开发在选择国家后明确可用路线/不可配送状态，必要时提示完整地址后报价。不能凭当前UI宣称最终订单可运巴西。

**负责人：** 运营+开发

**预计工作量：** 1–2人日（估算）

**验收标准：** 政策国家与结账可服务国家一致；非支持国家明确提示；已支持国家运费与规则一致；地址报价/税费在测试环境完成验收

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/checkout

### UX-01 · P1 · 年龄验证弹窗没有键盘焦点约束

**类别：** 年龄弹窗/无障碍

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 全新会话等待Age Verification；连续按Tab12次，第3次进入背景Shop now；正常点成年确认再刷新，确认弹窗消失。

**证据：** evidence/browser/age-keyboard.json：前2次Tab聚焦确认/离开，第3次进入背景Shop now，后续Search/Cart等背景控件。确认后刷新ageVisible=0且存储存在。

**影响：** 键盘/屏幕阅读器用户可能误操作背景，aria-modal语义与交互不符

**可能根因：** 没有focus trap和背景inert处理

**修复方法：** 在正常年龄弹窗内设初始焦点、Tab/Shift+Tab循环，背景inert；确认后还原焦点。保留确认/离开功能，不增加可绕过年龄验证的关闭方式。

**负责人：** 开发

**预计工作量：** 0.5–1人日（估算）

**验收标准：** 首次访问焦点在弹窗；连续20次Tab/Shift+Tab不进入背景；确认后正常导航且刷新记忆符合配置

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/

### PERF-04 · P1 · 首页桌面CLS三次均约0.457

**类别：** 布局稳定性

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 新浏览器以desktop preset跑首页3次，检查CLS及layout-shifts：Banner无显式尺寸，下方Find Your Perfect Doll发生主要位移。

**证据：** home-desktop-1/2/3累计布局位移均0.456637；layout-shifts将主要0.416346位移关联Find Your Perfect Doll区块，并标记Banner img Media element lacking an explicit size。

**影响：** 加载过程中内容大幅移动，增加阅读/点击误操作

**可能根因：** Banner没有预留稳定尺寸，图像到达/初始化后改变布局；实际时间线由开发复核

**修复方法：** 给Banner图片真实width/height及容器稳定aspect-ratio；同步SSR与客户端断点尺寸，确保轮播当前项变化不改父容器高度。

**负责人：** 开发

**预计工作量：** 0.5–1人日（估算）

**验收标准：** 同一desktop配置冷启动3次CLS中位≤0.1，Banner加载前后高度稳定；移动布局不退化

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/

### FE-01 · P2 · runtime-blocks在所有深度样本中返回404

**类别：** 动态模块

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 清空Network后打开首页/分类/商品，筛选runtime-blocks并观察404；在已下载公开DNfd1SfM.js定位content/runtime-blocks与!r.ok return[]。

**证据：** evidence/browser/deep.json 58个视口记录均404；evidence/public-js/DNfd1SfM.js公开函数z$在!response.ok时返回[]，W$只在列表非空时注册T$。

**影响：** 动态扩展模块无法注册并产生Console噪音；未证实哪个正式模块依赖此接口

**可能根因：** 前后端接口/部署版本不匹配或可选扩展接口不存在

**修复方法：** 开发核查公开/content/runtime-blocks路由、模块注册表和当前发布配置；功能启用则实现/恢复200数据；未使用则停请求或约定200空列表。源码路径未知，不虚构文件名。

**负责人：** 开发

**预计工作量：** 0.5–1人日（估算）

**验收标准：** 代表页无该404；现有模块、商品和购物流程不退化；若空列表则开发确认无必需模块丢失

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/
- https://echobae.com/about-us
- https://echobae.com/blog
- https://echobae.com/blog/silicone-sex-doll-buying-guide
- https://echobae.com/blog/tpe-vs-silicone-sex-doll
- https://echobae.com/blog/what-are-the-most-realistic-sex-dolls
- https://echobae.com/cart
- https://echobae.com/collections/best-sellers
- https://echobae.com/collections/best-value
- https://echobae.com/collections/new-arrival
- https://echobae.com/contact-us
- https://echobae.com/custom-made
- https://echobae.com/customer-reviews
- https://echobae.com/faq
- https://echobae.com/help
- https://echobae.com/p/149cm-white-hair-silicone-doll-siwei
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia
- https://echobae.com/p/170cm-realistic-silicone-sex-doll-jiachen
- https://echobae.com/p/demo-sh-030
- https://echobae.com/payment-method
- https://echobae.com/privacy-policy
- https://echobae.com/products
- https://echobae.com/return-refund-policy
- https://echobae.com/sex-doll-care
- https://echobae.com/shipping-policy

### FE-02 · P2 · 多模板出现Hydration mismatch

**类别：** SSR/Hydration

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 新会话加载代表模板，打开Console查Hydration mismatch；保存SSR HTML与首轮DOM，借开发调试找最小节点差异。

**证据：** evidence/browser/deep.json：49/58个记录含Hydration completed but contains mismatches，无未捕获pageerror；首始H1/DOM变化另见SEO-04。

**影响：** SSR与客户端状态不一致，可能造成重渲染/闪动，具体性能归因待验证

**可能根因：** 运行时主题、locale、页面数据或随机/时间条件渲染差异；不能凭日志确认具体代码

**修复方法：** 开发用Nuxt/Vue hydration调试定位最小差异，比较服务端数据与客户端首轮数据、tokens/locale；只把浏览器专属渲染放在正确边界，避免全页client-only。

**负责人：** 开发

**预计工作量：** 1–2人日（估算）

**验收标准：** 首页/分类/商品/文章/政策冷启动无hydration警告，初始重要文本与DOM一致，不丢SSR SEO

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/about-us
- https://echobae.com/blog
- https://echobae.com/blog/silicone-sex-doll-buying-guide
- https://echobae.com/blog/tpe-vs-silicone-sex-doll
- https://echobae.com/blog/what-are-the-most-realistic-sex-dolls
- https://echobae.com/cart
- https://echobae.com/collections/best-sellers
- https://echobae.com/collections/best-value
- https://echobae.com/collections/new-arrival
- https://echobae.com/contact-us
- https://echobae.com/custom-made
- https://echobae.com/customer-reviews
- https://echobae.com/faq
- https://echobae.com/help
- https://echobae.com/p/149cm-white-hair-silicone-doll-siwei
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia
- https://echobae.com/p/170cm-realistic-silicone-sex-doll-jiachen
- https://echobae.com/p/demo-sh-030
- https://echobae.com/payment-method
- https://echobae.com/privacy-policy
- https://echobae.com/products
- https://echobae.com/return-refund-policy
- https://echobae.com/sex-doll-care
- https://echobae.com/shipping-policy

### SEO-04 · P2 · 初始HTML与渲染DOM的主标题不一致

**类别：** SSR标题结构

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 用GET/view-source查H1，等待浏览器初始化后查询document.querySelectorAll(h1)，比较Home/Collections/Products占位与真实标题；Blog确认两个The Blog。

**证据：** evidence/crawl.json含Home/Collections/Products通用H1；deep.json中Contact变Contact Us、分类变New Arrivals、正式商品只留商品H1。/blog则渲染后仍两个The Blog H1。

**影响：** JS未完成时主题不明确、可访问结构重复；多H1本身不是自动排名惩罚

**可能根因：** 通用PageTitle在SSR输出占位，客户端再根据页面数据更新

**修复方法：** SSR直接输出真实页面名称；商品保留唯一主要商品H1，面包屑用nav/普通文本；博客列表保留一个The Blog主标题。不要机械增加正文。

**负责人：** 开发

**预计工作量：** 1人日（估算）

**验收标准：** view-source与渲染DOM的主要H1一致；分类分别New Arrivals/Best Value/Best Sellers；博客主标题无模板重复

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/products
- https://echobae.com/collections/new-arrival
- https://echobae.com/collections/best-value
- https://echobae.com/custom-made
- https://echobae.com/contact-us
- https://echobae.com/pages/help
- https://echobae.com/collections/best-sellers
- https://echobae.com/customer-reviews
- https://echobae.com/payment-method
- https://echobae.com/shipping-policy
- https://echobae.com/privacy-policy
- https://echobae.com/return-refund-policy
- https://echobae.com/about-us
- https://echobae.com/wholesale
- https://echobae.com/affiliate-program
- https://echobae.com/faq
- https://echobae.com/sex-doll-care
- https://echobae.com/p/demo-sh-020
- https://echobae.com/p/demo-sh-030
- https://echobae.com/p/demo-sh-060
- https://echobae.com/p/demo-sh-080
- https://echobae.com/p/demo-sh-090
- https://echobae.com/p/demo-sh-100
- https://echobae.com/p/robovac-x1
- https://echobae.com/p/demo-sh-001
- https://echobae.com/p/demo-sh-002
- https://echobae.com/p/demo-sh-003
- https://echobae.com/p/demo-sh-004
- https://echobae.com/p/demo-sh-005
- https://echobae.com/p/demo-sh-006
- https://echobae.com/p/demo-sh-007
- https://echobae.com/p/demo-sh-008
- https://echobae.com/p/demo-sh-009
- https://echobae.com/p/demo-sh-011
- https://echobae.com/p/demo-sh-012
- https://echobae.com/p/demo-sh-013
- https://echobae.com/p/demo-sh-014
- https://echobae.com/p/149cm-christmas-silicone-love-doll-huaze
- https://echobae.com/p/170cm-realistic-silicone-sex-doll-jiachen
- https://echobae.com/p/159cm-natural-look-silicone-doll-jiachen
- https://echobae.com/p/170cm-real-skin-texture-silicone-sex-doll-jiachen
- https://echobae.com/p/169cm-silicone-realistic-sex-doll-jieman
- https://echobae.com/p/159cm-realistic-silicone-sex-doll-lanxin
- https://echobae.com/p/149cm-silicone-sex-doll-lanxin
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia
- https://echobae.com/p/149cm-silicone-doll-lydia
- https://echobae.com/p/169cm-premium-silicone-love-doll-lydia
- https://echobae.com/p/159cm-natural-look-silicone-doll-lydia
- https://echobae.com/p/169cm-anime-silicone-sex-doll-luoli
- https://echobae.com/p/169cm-realistic-silicone-sex-doll-muyao
- https://echobae.com/p/153cm-ai-companion-silicone-doll-muyao
- https://echobae.com/p/169cm-natural-look-silicone-doll-siwei
- https://echobae.com/p/169cm-teacher-fantasy-silicone-doll-ruyan
- https://echobae.com/p/159cm-anime-silicone-doll-ruyan
- https://echobae.com/p/159cm-teacher-fantasy-silicone-doll-siwei
- https://echobae.com/p/169cm-realistic-silicone-sex-doll-juaner
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-juaner
- https://echobae.com/p/149cm-slim-silicone-love-doll-juaner
- https://echobae.com/p/149cm-lifelike-silicone-sex-doll-sheena
- https://echobae.com/p/159cm-premium-silicone-love-doll-sheena
- https://echobae.com/p/169cm-natural-look-silicone-doll-sheena
- https://echobae.com/p/149cm-cosplay-silicone-doll-sheena
- https://echobae.com/p/159cm-anime-silicone-sex-doll-xiaen
- https://echobae.com/p/149cm-anime-silicone-love-doll-xiaoyu
- https://echobae.com/p/159cm-silicone-adult-love-doll-xingzi
- https://echobae.com/p/169cm-ai-silicone-companion-doll-xingzi
- https://echobae.com/p/149cm-white-hair-silicone-doll-siwei
- https://echobae.com/p/169cm-realistic-silicone-love-doll-zhuzhu
- https://echobae.com/p/149cm-premium-silicone-love-doll-jieyi
- https://echobae.com/p/159cm-implanted-hair-silicone-sex-doll-zhiyan
- https://echobae.com/p/169cm-lifelike-silicone-sex-doll-yumeng
- https://echobae.com/p/149cm-anime-silicone-doll-yumeng
- https://echobae.com/p/159cm-cosplay-silicone-sex-doll-yumeng
- https://echobae.com/p/149cm-realistic-silicone-sex-doll-yufei
- https://echobae.com/p/169cm-silicone-adult-love-doll-yuran
- https://echobae.com/p/159cm-natural-look-silicone-doll-yinuo
- https://echobae.com/p/153cm-fantasy-silicone-sex-doll-yanke
- https://echobae.com/p/169cm-premium-silicone-love-doll-yawen
- https://echobae.com/c/silicone-sex-dolls
- https://echobae.com/products?tag=bestseller
- https://echobae.com/products?tag=smart-home
- https://echobae.com/p/demo-sh-095
- https://echobae.com/p/demo-sh-071
- https://echobae.com/p/demo-sh-045
- https://echobae.com/p/demo-sh-044
- https://echobae.com/p/demo-sh-022
- https://echobae.com/p/demo-sh-021
- https://echobae.com/products?tag=sale
- https://echobae.com/products?tag=voice-control
- https://echobae.com/p/demo-sh-028
- https://echobae.com/p/demo-sh-078
- https://echobae.com/p/demo-sh-055
- https://echobae.com/products?tag=new
- https://echobae.com/p/demo-sh-084
- https://echobae.com/p/demo-sh-036
- https://echobae.com/p/demo-sh-096
- https://echobae.com/p/demo-sh-092
- https://echobae.com/p/demo-sh-085
- https://echobae.com/p/demo-sh-056
- https://echobae.com/p/demo-sh-081
- https://echobae.com/p/demo-sh-079
- https://echobae.com/p/demo-sh-054
- https://echobae.com/p/demo-sh-066
- https://echobae.com/p/demo-sh-015
- https://echobae.com/p/demo-sh-091
- https://echobae.com/p/demo-sh-088
- https://echobae.com/p/demo-sh-087
- https://echobae.com/p/demo-sh-077
- https://echobae.com/p/demo-sh-065
- https://echobae.com/p/demo-sh-063
- https://echobae.com/products?tag=budget
- https://echobae.com/p/demo-sh-099
- https://echobae.com/p/demo-sh-076
- https://echobae.com/p/demo-sh-075
- https://echobae.com/p/demo-sh-046
- https://echobae.com/p/demo-sh-051
- https://echobae.com/p/demo-sh-041
- https://echobae.com/products?tag=wireless
- https://echobae.com/p/demo-sh-052
- https://echobae.com/p/demo-sh-037
- https://echobae.com/p/demo-sh-027
- https://echobae.com/p/demo-sh-053
- https://echobae.com/products?tag=eco-friendly
- https://echobae.com/products?tag=premium
- https://echobae.com/p/demo-sh-097
- https://echobae.com/p/demo-sh-072
- https://echobae.com/p/demo-sh-029
- https://echobae.com/p/demo-sh-031
- https://echobae.com/p/demo-sh-057
- https://echobae.com/p/demo-sh-083
- https://echobae.com/p/demo-sh-082
- https://echobae.com/p/demo-sh-058
- https://echobae.com/p/demo-sh-048
- https://echobae.com/products?tag=energy-saving
- https://echobae.com/p/demo-sh-059
- https://echobae.com/p/demo-sh-034
- https://echobae.com/p/demo-sh-086
- https://echobae.com/p/demo-sh-061
- https://echobae.com/p/demo-sh-064
- https://echobae.com/p/demo-sh-038
- https://echobae.com/p/demo-sh-089
- https://echobae.com/p/149cm-anime-silicone-doll-yawen
- https://echobae.com/p/149cm-lifelike-silicone-sex-doll-xiuyan
- https://echobae.com/p/149cm-realistic-silicone-sex-doll-xiuyan
- https://echobae.com/p/159cm-realistic-silicone-sex-doll-muyao
- https://echobae.com/p/169cm-realistic-silicone-sex-doll-nancy
- https://echobae.com/p/159cm-premium-silicone-love-doll-cailin
- https://echobae.com/p/159cm-bikini-silicone-love-doll-linda
- https://echobae.com/p/169cm-big-breast-silicone-sex-doll-xiuyan
- https://echobae.com/p/159cm-cosplay-silicone-sex-doll-cailin
- https://echobae.com/p/159cm-twin-ponytail-silicone-doll-nancy
- https://echobae.com/p/169cm-lifelike-silicone-sex-doll-jieman
- https://echobae.com/p/169cm-asian-silicone-sex-doll-xiaowu
- https://echobae.com/p/159cm-cute-silicone-love-doll-xiuyan
- https://echobae.com/p/demo-sh-033
- https://echobae.com/p/demo-sh-050
- https://echobae.com/p/demo-sh-040
- https://echobae.com/p/smart-plug-4pack
- https://echobae.com/p/demo-sh-047
- https://echobae.com/p/demo-sh-068
- https://echobae.com/p/demo-sh-094
- https://echobae.com/p/demo-sh-069
- https://echobae.com/p/demo-sh-016
- https://echobae.com/p/demo-sh-018
- https://echobae.com/p/demo-sh-024
- https://echobae.com/p/demo-sh-032
- https://echobae.com/p/demo-sh-039
- https://echobae.com/p/demo-sh-049
- https://echobae.com/p/demo-sh-074
- https://echobae.com/p/demo-sh-023
- https://echobae.com/p/demo-sh-035
- https://echobae.com/p/demo-sh-042
- https://echobae.com/p/demo-sh-043
- https://echobae.com/p/demo-sh-093
- https://echobae.com/p/demo-sh-010
- https://echobae.com/p/demo-sh-017
- https://echobae.com/p/demo-sh-019
- https://echobae.com/p/demo-sh-025
- https://echobae.com/p/demo-sh-026
- https://echobae.com/p/demo-sh-062
- https://echobae.com/p/demo-sh-067
- https://echobae.com/p/demo-sh-073
- https://echobae.com/p/demo-sh-098
- https://echobae.com/p/149cm-implanted-hair-silicone-doll-muyao
- https://echobae.com/p/149cm-lifelike-silicone-sex-doll-baoer
- https://echobae.com/p/149cm-lifelike-silicone-sex-doll-nancy
- https://echobae.com/p/149cm-natural-look-silicone-doll-nancy
- https://echobae.com/p/149cm-realistic-silicone-sex-doll-ailing
- https://echobae.com/p/149cm-realistic-silicone-sex-doll-aurora
- https://echobae.com/p/153cm-real-skin-texture-silicone-sex-doll-katelyn
- https://echobae.com/p/153cm-real-skin-texture-silicone-sex-doll-lydia
- https://echobae.com/p/159cm-blonde-silicone-love-doll-miriam
- https://echobae.com/p/159cm-cosplay-silicone-sex-doll-baoer
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-bersa
- https://echobae.com/p/159cm-premium-silicone-love-doll-qiuyu
- https://echobae.com/p/169cm-bikini-silicone-sex-doll-linda
- https://echobae.com/p/169cm-blonde-silicone-sex-doll-nancy
- https://echobae.com/p/169cm-premium-silicone-love-doll-yufei
- https://echobae.com/p/169cm-slim-silicone-sex-doll-haiyue
- https://echobae.com/p/170cm-bikini-silicone-sex-doll-perry
- https://echobae.com/p/1784262609174
- https://echobae.com/p/elva-168cm-f-cup-demo
- https://echobae.com/p/elva-168cm-f-cup-demo-copy-copy
- https://echobae.com/p/elva-168cm-f-cup-demo-copy-copy-copy
- https://echobae.com/p/elva-168cm-f-cup-demo-copy-copy-copy-copy
- https://echobae.com/p/elva-168cm-f-cup-demo-copy-copy-copy-copy-copy
- https://echobae.com/p/smart-led-strip
- https://echobae.com/p/test888
- https://echobae.com/p/169cm-silicone-large-breast-sex-doll-sheena
- https://echobae.com/p/1783396233625ff
- https://echobae.com/p/1783396905878
- https://echobae.com/p/1783397572134
- https://echobae.com/p/1783569515569
- https://echobae.com/p/1783569871599
- https://echobae.com/p/e2e-ship-heavy
- https://echobae.com/p/e2e-ship-light
- https://echobae.com/p/e2e-ship-volumetric

### SEO-05 · P2 · Title品牌后缀重复

**类别：** Title

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 查看URL_INVENTORY中Title含两次Echobae的76页；以Lydia和buying-guide直接view-source验证。

**证据：** evidence/crawl.json：76个页面Title出现多次Echobae，如Lydia ... | Echobae | Echobae、buying guide ... | Echobae | Echobae。

**影响：** 搜索标题冗余和可读性下降

**可能根因：** 后台内容已含品牌，前端titleTemplate再次拼接

**修复方法：** 优先统一titleTemplate去重或明确后台填写规范。Lydia推荐“159cm Lifelike Silicone Sex Doll Lydia | Echobae”，核心主题保留；购买指南只保留一个品牌。

**负责人：** 开发+运营

**预计工作量：** 0.5人日（估算）

**验收标准：** 所有公开Title只保留一个品牌，产品名称/尺寸和文章意图不变；首页当前Title无需改写

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/blog
- https://echobae.com/blog/silicone-sex-doll-buying-guide
- https://echobae.com/p/149cm-christmas-silicone-love-doll-huaze
- https://echobae.com/p/170cm-realistic-silicone-sex-doll-jiachen
- https://echobae.com/p/159cm-natural-look-silicone-doll-jiachen
- https://echobae.com/p/170cm-real-skin-texture-silicone-sex-doll-jiachen
- https://echobae.com/p/169cm-silicone-realistic-sex-doll-jieman
- https://echobae.com/p/159cm-realistic-silicone-sex-doll-lanxin
- https://echobae.com/p/149cm-silicone-sex-doll-lanxin
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia
- https://echobae.com/p/149cm-silicone-doll-lydia
- https://echobae.com/p/169cm-premium-silicone-love-doll-lydia
- https://echobae.com/p/159cm-natural-look-silicone-doll-lydia
- https://echobae.com/p/169cm-anime-silicone-sex-doll-luoli
- https://echobae.com/p/169cm-realistic-silicone-sex-doll-muyao
- https://echobae.com/p/153cm-ai-companion-silicone-doll-muyao
- https://echobae.com/p/169cm-natural-look-silicone-doll-siwei
- https://echobae.com/p/169cm-teacher-fantasy-silicone-doll-ruyan
- https://echobae.com/p/159cm-anime-silicone-doll-ruyan
- https://echobae.com/p/159cm-teacher-fantasy-silicone-doll-siwei
- https://echobae.com/p/169cm-realistic-silicone-sex-doll-juaner
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-juaner
- https://echobae.com/p/149cm-slim-silicone-love-doll-juaner
- https://echobae.com/p/149cm-lifelike-silicone-sex-doll-sheena
- https://echobae.com/p/159cm-premium-silicone-love-doll-sheena
- https://echobae.com/p/169cm-natural-look-silicone-doll-sheena
- https://echobae.com/p/149cm-cosplay-silicone-doll-sheena
- https://echobae.com/p/159cm-anime-silicone-sex-doll-xiaen
- https://echobae.com/p/149cm-anime-silicone-love-doll-xiaoyu
- https://echobae.com/p/159cm-silicone-adult-love-doll-xingzi
- https://echobae.com/p/169cm-ai-silicone-companion-doll-xingzi
- https://echobae.com/blog?category=Buyer+Guide
- https://echobae.com/blog?category=updates
- https://echobae.com/p/149cm-white-hair-silicone-doll-siwei
- https://echobae.com/p/169cm-realistic-silicone-love-doll-zhuzhu
- https://echobae.com/p/149cm-premium-silicone-love-doll-jieyi
- https://echobae.com/p/159cm-implanted-hair-silicone-sex-doll-zhiyan
- https://echobae.com/p/169cm-lifelike-silicone-sex-doll-yumeng
- https://echobae.com/p/149cm-anime-silicone-doll-yumeng
- https://echobae.com/p/159cm-cosplay-silicone-sex-doll-yumeng
- https://echobae.com/p/149cm-realistic-silicone-sex-doll-yufei
- https://echobae.com/p/169cm-silicone-adult-love-doll-yuran
- https://echobae.com/p/159cm-natural-look-silicone-doll-yinuo
- https://echobae.com/p/153cm-fantasy-silicone-sex-doll-yanke
- https://echobae.com/p/169cm-premium-silicone-love-doll-yawen
- https://echobae.com/p/149cm-anime-silicone-doll-yawen
- https://echobae.com/p/149cm-lifelike-silicone-sex-doll-xiuyan
- https://echobae.com/p/149cm-realistic-silicone-sex-doll-xiuyan
- https://echobae.com/p/159cm-realistic-silicone-sex-doll-muyao
- https://echobae.com/p/169cm-realistic-silicone-sex-doll-nancy
- https://echobae.com/p/159cm-premium-silicone-love-doll-cailin
- https://echobae.com/p/159cm-bikini-silicone-love-doll-linda
- https://echobae.com/p/169cm-big-breast-silicone-sex-doll-xiuyan
- https://echobae.com/p/159cm-cosplay-silicone-sex-doll-cailin
- https://echobae.com/p/159cm-twin-ponytail-silicone-doll-nancy
- https://echobae.com/p/169cm-lifelike-silicone-sex-doll-jieman
- https://echobae.com/p/169cm-asian-silicone-sex-doll-xiaowu
- https://echobae.com/p/159cm-cute-silicone-love-doll-xiuyan
- https://echobae.com/p/149cm-implanted-hair-silicone-doll-muyao
- https://echobae.com/p/149cm-lifelike-silicone-sex-doll-baoer
- https://echobae.com/p/149cm-lifelike-silicone-sex-doll-nancy
- https://echobae.com/p/149cm-natural-look-silicone-doll-nancy
- https://echobae.com/p/149cm-realistic-silicone-sex-doll-ailing
- https://echobae.com/p/149cm-realistic-silicone-sex-doll-aurora
- https://echobae.com/p/153cm-real-skin-texture-silicone-sex-doll-katelyn
- https://echobae.com/p/153cm-real-skin-texture-silicone-sex-doll-lydia
- https://echobae.com/p/159cm-blonde-silicone-love-doll-miriam
- https://echobae.com/p/159cm-cosplay-silicone-sex-doll-baoer
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-bersa
- https://echobae.com/p/159cm-premium-silicone-love-doll-qiuyu
- https://echobae.com/p/169cm-bikini-silicone-sex-doll-linda
- https://echobae.com/p/169cm-blonde-silicone-sex-doll-nancy
- https://echobae.com/p/169cm-premium-silicone-love-doll-yufei
- https://echobae.com/p/169cm-slim-silicone-sex-doll-haiyue
- https://echobae.com/p/170cm-bikini-silicone-sex-doll-perry
- https://echobae.com/p/169cm-silicone-large-breast-sex-doll-sheena

### SEO-06 · P2 · 参数页重复标题并自引用Canonical

**类别：** 筛选/规范化

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 请求products?tag=smart-home与products?tag=sale，比较Title/Canonical/robots；观察分类内容不同，不统一canonical至无关页面。

**证据：** evidence/crawl.json：10个products?tag页Title相同且Canonical含tag；2个blog?category页也自引用。当前全局noindex。

**影响：** 解除全局noindex时可能形成低价值筛选索引与主题重复；不同结果不必一律canonical首页

**可能根因：** 通用按当前URL生成canonical，没有显式筛选索引策略

**修复方法：** 运营选定独立有价值分类落地页，其余搜索/筛选保持noindex；相同内容参数使用规范URL，实质不同内容不要虚假canonical；分页用稳定可抓取href和各页正确canonical。

**负责人：** 开发+运营

**预计工作量：** 0.5–1人日（估算）

**验收标准：** 发布后索引白名单清楚；搜索/低价值筛选不收录；无所有分页canonical到第一页的错误；有价值分类保留独立主题

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/blog?category=Buyer+Guide
- https://echobae.com/blog?category=updates
- https://echobae.com/products?tag=bestseller
- https://echobae.com/products?tag=smart-home
- https://echobae.com/products?tag=sale
- https://echobae.com/products?tag=voice-control
- https://echobae.com/products?tag=new
- https://echobae.com/products?tag=budget
- https://echobae.com/products?tag=wireless
- https://echobae.com/products?tag=eco-friendly
- https://echobae.com/products?tag=premium
- https://echobae.com/products?tag=energy-saving

### SEO-07 · P2 · 购买指南链接到404护理文章

**类别：** 站内链接

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 打开buying-guide点击/检查护理链接/blogs/silicone-doll-care-guide，GET404；对照/sex-doll-care 200，不提交任何表单。

**证据：** crawl.json：指南链接/blogs/silicone-doll-care-guide；目标404，现有护理页/sex-doll-care返回200。

**影响：** 用户阅读路径中断

**可能根因：** 博客路由/blog与旧/blogs链接混用

**修复方法：** 运营将该文链接改为真实相关护理内容（当前/sex-doll-care可作为候选）；若旧链接曾对外传播开发设置一对一301。

**负责人：** 运营+开发

**预计工作量：** 0.25人日（估算）

**验收标准：** 指南内护理链接200、内容相关；无/blogs旧404，跳转最多一跳

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/blog/silicone-sex-doll-buying-guide
- https://echobae.com/blogs/silicone-doll-care-guide

### UX-02 · P2 · 移动端轮播箭头覆盖正文区域

**类别：** 移动首屏

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 390×844查看首页首屏，比较轮播圆箭头与A private space正文的边界；切换滑块再次检查，截图留证。

**证据：** evidence/previous/mobile-viewport.png（390×844）：左右白色圆箭头叠在“A private space...”文字所在高度；本次settled截图供复核。

**影响：** 文字与控制争夺触摸/阅读区域

**可能根因：** 桌面轮播控件沿用绝对定位，未预留移动文本安全区

**修复方法：** 设计/开发将移动箭头移至底部独立区域或使用明确分页控制，保留触摸切换；正文不能被控件覆盖。

**负责人：** 设计+开发

**预计工作量：** 0.5人日（估算）

**验收标准：** 390/412/768首屏正文与控制无重叠，CTA可点击，按钮触摸区域清晰

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/

### UX-03 · P2 · Footer暴露翻译键footer.poweredBy

**类别：** 国际化

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 正常购物车与Checkout等待初始化后搜索正文footer.poweredBy，比较首页正常Footer。

**证据：** cart-verify.json和checkout-checks.json可见footer.poweredBy；某些初始HTML/其他页正常Powered by wiipoo。

**影响：** 界面出现实现细节破坏可信度

**可能根因：** locale字典缺项或客户端上下文丢失

**修复方法：** 开发统一加载语言字典，补缺项/安全fallback；检查前后端locale初始化。

**负责人：** 开发

**预计工作量：** 0.25–0.5人日（估算）

**验收标准：** 所有模板初始与渲染页面都不显示翻译key、undefined或占位文本

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/cart
- https://echobae.com/checkout

### CONT-03 · P2 · FAQ重复问答02与03

**类别：** FAQ

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 打开/faq，对比02和03题目及回答，确认完全重复。

**证据：** page-text.json：02/03标题和回答均为removable vs fixed，完全重复。

**影响：** 降低内容清晰度和帮助信息密度

**可能根因：** 内容录入重复

**修复方法：** 运营删除重复条目或替换成真实不同问题并重新编号；不为SEO增加无关问题。

**负责人：** 运营

**预计工作量：** 0.25人日（估算）

**验收标准：** 问答不重复且编号连续；内容与商品实际配置一致

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/faq

### CONT-04 · P2 · 首页社媒图标链接到平台首页

**类别：** 外链

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 首页Inspect七个社媒图标href与aria-label；检查URL是否只有平台根域，不发送社媒消息。

**证据：** deep.json首页7个aria标签社媒链接为linkedin.com、x.com、facebook.com、youtube.com、instagram.com、pinterest.com、tiktok.com根路径。

**影响：** 不能找到品牌账号，可能分流访客

**可能根因：** 社媒模板默认URL未填真实账号

**修复方法：** 运营填写真实品牌主页URL；尚无账号则移除对应图标，勿造账号地址。

**负责人：** 运营（后台功能未验证）

**预计工作量：** 0.25人日（估算）

**验收标准：** 每个保留图标到品牌主页，移动/桌面可读标签正确，无平台根链接

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/

### SEC-01 · P2 · Demo详情HTML暴露私有HTTP图片地址

**类别：** 公开图片配置

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 仅检查已保存Demo HTML img/src及private-image-urls.json，不请求或探测内部地址。

**证据：** evidence/private-image-urls.json：28个公开Demo商品页面img指向http://172.17.0.1:8093/...；不是凭此证明服务器被入侵。

**影响：** 公网浏览器不可正常加载内部地址并有混合内容/内部拓扑暴露

**可能根因：** 媒体迁移时保存了容器内部绝对URL

**修复方法：** 随CAT-01移除Demo；开发统一媒体存储规范公网HTTPS URL并拦截内容录入内部IP/localhost引用。停止测试这些内部地址，不开展私网探测。

**负责人：** 开发+运营

**预计工作量：** 0.5–1人日（估算）

**验收标准：** 所有公开HTML/JSON-LD/图片候选无RFC1918/localhost/http混合图片引用；真实媒体全部HTTPS可加载

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/p/demo-sh-020
- https://echobae.com/p/demo-sh-030
- https://echobae.com/p/demo-sh-060
- https://echobae.com/p/demo-sh-100
- https://echobae.com/p/demo-sh-009
- https://echobae.com/p/demo-sh-011
- https://echobae.com/p/demo-sh-012
- https://echobae.com/p/demo-sh-095
- https://echobae.com/p/demo-sh-071
- https://echobae.com/p/demo-sh-022
- https://echobae.com/p/demo-sh-021
- https://echobae.com/p/demo-sh-084
- https://echobae.com/p/demo-sh-036
- https://echobae.com/p/demo-sh-096
- https://echobae.com/p/demo-sh-085
- https://echobae.com/p/demo-sh-046
- https://echobae.com/p/demo-sh-052
- https://echobae.com/p/demo-sh-072
- https://echobae.com/p/demo-sh-059
- https://echobae.com/p/demo-sh-086
- https://echobae.com/p/demo-sh-061
- https://echobae.com/p/demo-sh-094
- https://echobae.com/p/demo-sh-035
- https://echobae.com/p/demo-sh-042
- https://echobae.com/p/demo-sh-010
- https://echobae.com/p/demo-sh-017
- https://echobae.com/p/demo-sh-019
- https://echobae.com/p/demo-sh-067

### SEC-02 · P2 · 公开200页面缺少统一安全响应头

**类别：** 安全响应头

**验证状态：** 环境所见已验证；源站头待开发复核

**问题状态：** 待修改

**复现步骤：** 读取已保存200与404响应头，比较HSTS/CSP/nosniff/frame/referrer；开发从源站与正常公网重复GET确认代理是否改写。

**证据：** crawl.json：227个200均有HSTS；未见CSP/X-Content-Type-Options/X-Frame-Options/Referrer-Policy，404页反而带nosniff/DENY/no-referrer。代理可能影响响应头可见性。

**影响：** 减少纵深防护；没有实际XSS/点击劫持攻击证据

**可能根因：** 主应用与错误页网关配置不一致，源站需开发复核

**修复方法：** 开发核查源站与CDN实测头；对HTML启用nosniff和适当Referrer-Policy，设计frame-ancestors；CSP先Report-Only并兼容支付/必要外域，再收紧。勿盲目DENY导致支付集成故障。

**负责人：** 开发

**预计工作量：** 0.5–1人日（估算）

**验收标准：** 外网正常浏览确认各模板头一致，CSP不破坏支付/图片/脚本；不以缺头宣称漏洞利用成功

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/
- https://echobae.com/products
- https://echobae.com/collections/new-arrival
- https://echobae.com/collections/best-value
- https://echobae.com/custom-made
- https://echobae.com/contact-us
- https://echobae.com/blog
- https://echobae.com/pages/help
- https://echobae.com/account/login
- https://echobae.com/cart
- https://echobae.com/collections/best-sellers
- https://echobae.com/customer-reviews
- https://echobae.com/blog/what-are-the-most-realistic-sex-dolls
- https://echobae.com/blog/tpe-vs-silicone-sex-doll
- https://echobae.com/blog/silicone-sex-doll-buying-guide
- https://echobae.com/payment-method
- https://echobae.com/shipping-policy
- https://echobae.com/privacy-policy
- https://echobae.com/return-refund-policy
- https://echobae.com/about-us
- https://echobae.com/wholesale
- https://echobae.com/affiliate-program
- https://echobae.com/faq
- https://echobae.com/sex-doll-care
- https://echobae.com/p/demo-sh-020
- https://echobae.com/p/demo-sh-030
- https://echobae.com/p/demo-sh-060
- https://echobae.com/p/demo-sh-080
- https://echobae.com/p/demo-sh-090
- https://echobae.com/p/demo-sh-100
- https://echobae.com/p/robovac-x1
- https://echobae.com/p/demo-sh-001
- https://echobae.com/p/demo-sh-002
- https://echobae.com/p/demo-sh-003
- https://echobae.com/p/demo-sh-004
- https://echobae.com/p/demo-sh-005
- https://echobae.com/p/demo-sh-006
- https://echobae.com/p/demo-sh-007
- https://echobae.com/p/demo-sh-008
- https://echobae.com/p/demo-sh-009
- https://echobae.com/p/demo-sh-011
- https://echobae.com/p/demo-sh-012
- https://echobae.com/p/demo-sh-013
- https://echobae.com/p/demo-sh-014
- https://echobae.com/p/149cm-christmas-silicone-love-doll-huaze
- https://echobae.com/p/170cm-realistic-silicone-sex-doll-jiachen
- https://echobae.com/p/159cm-natural-look-silicone-doll-jiachen
- https://echobae.com/p/170cm-real-skin-texture-silicone-sex-doll-jiachen
- https://echobae.com/p/169cm-silicone-realistic-sex-doll-jieman
- https://echobae.com/p/159cm-realistic-silicone-sex-doll-lanxin
- https://echobae.com/p/149cm-silicone-sex-doll-lanxin
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia
- https://echobae.com/p/149cm-silicone-doll-lydia
- https://echobae.com/p/169cm-premium-silicone-love-doll-lydia
- https://echobae.com/p/159cm-natural-look-silicone-doll-lydia
- https://echobae.com/p/169cm-anime-silicone-sex-doll-luoli
- https://echobae.com/p/169cm-realistic-silicone-sex-doll-muyao
- https://echobae.com/p/153cm-ai-companion-silicone-doll-muyao
- https://echobae.com/p/169cm-natural-look-silicone-doll-siwei
- https://echobae.com/p/169cm-teacher-fantasy-silicone-doll-ruyan
- https://echobae.com/p/159cm-anime-silicone-doll-ruyan
- https://echobae.com/p/159cm-teacher-fantasy-silicone-doll-siwei
- https://echobae.com/p/169cm-realistic-silicone-sex-doll-juaner
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-juaner
- https://echobae.com/p/149cm-slim-silicone-love-doll-juaner
- https://echobae.com/p/149cm-lifelike-silicone-sex-doll-sheena
- https://echobae.com/p/159cm-premium-silicone-love-doll-sheena
- https://echobae.com/p/169cm-natural-look-silicone-doll-sheena
- https://echobae.com/p/149cm-cosplay-silicone-doll-sheena
- https://echobae.com/p/159cm-anime-silicone-sex-doll-xiaen
- https://echobae.com/p/149cm-anime-silicone-love-doll-xiaoyu
- https://echobae.com/p/159cm-silicone-adult-love-doll-xingzi
- https://echobae.com/p/169cm-ai-silicone-companion-doll-xingzi
- https://echobae.com/blog?category=Buyer+Guide
- https://echobae.com/blog?category=updates
- https://echobae.com/account/forgot-password
- https://echobae.com/p/149cm-white-hair-silicone-doll-siwei
- https://echobae.com/p/169cm-realistic-silicone-love-doll-zhuzhu
- https://echobae.com/p/149cm-premium-silicone-love-doll-jieyi
- https://echobae.com/p/159cm-implanted-hair-silicone-sex-doll-zhiyan
- https://echobae.com/p/169cm-lifelike-silicone-sex-doll-yumeng
- https://echobae.com/p/149cm-anime-silicone-doll-yumeng
- https://echobae.com/p/159cm-cosplay-silicone-sex-doll-yumeng
- https://echobae.com/p/149cm-realistic-silicone-sex-doll-yufei
- https://echobae.com/p/169cm-silicone-adult-love-doll-yuran
- https://echobae.com/p/159cm-natural-look-silicone-doll-yinuo
- https://echobae.com/p/153cm-fantasy-silicone-sex-doll-yanke
- https://echobae.com/p/169cm-premium-silicone-love-doll-yawen
- https://echobae.com/c/silicone-sex-dolls
- https://echobae.com/products?tag=bestseller
- https://echobae.com/products?tag=smart-home
- https://echobae.com/p/demo-sh-095
- https://echobae.com/p/demo-sh-071
- https://echobae.com/p/demo-sh-045
- https://echobae.com/p/demo-sh-044
- https://echobae.com/p/demo-sh-022
- https://echobae.com/p/demo-sh-021
- https://echobae.com/products?tag=sale
- https://echobae.com/products?tag=voice-control
- https://echobae.com/p/demo-sh-028
- https://echobae.com/p/demo-sh-078
- https://echobae.com/p/demo-sh-055
- https://echobae.com/products?tag=new
- https://echobae.com/p/demo-sh-084
- https://echobae.com/p/demo-sh-036
- https://echobae.com/p/demo-sh-096
- https://echobae.com/p/demo-sh-092
- https://echobae.com/p/demo-sh-085
- https://echobae.com/p/demo-sh-056
- https://echobae.com/p/demo-sh-081
- https://echobae.com/p/demo-sh-079
- https://echobae.com/p/demo-sh-054
- https://echobae.com/p/demo-sh-066
- https://echobae.com/p/demo-sh-015
- https://echobae.com/p/demo-sh-091
- https://echobae.com/p/demo-sh-088
- https://echobae.com/p/demo-sh-087
- https://echobae.com/p/demo-sh-077
- https://echobae.com/p/demo-sh-065
- https://echobae.com/p/demo-sh-063
- https://echobae.com/products?tag=budget
- https://echobae.com/p/demo-sh-099
- https://echobae.com/p/demo-sh-076
- https://echobae.com/p/demo-sh-075
- https://echobae.com/p/demo-sh-046
- https://echobae.com/p/demo-sh-051
- https://echobae.com/p/demo-sh-041
- https://echobae.com/products?tag=wireless
- https://echobae.com/p/demo-sh-052
- https://echobae.com/p/demo-sh-037
- https://echobae.com/p/demo-sh-027
- https://echobae.com/p/demo-sh-053
- https://echobae.com/products?tag=eco-friendly
- https://echobae.com/products?tag=premium
- https://echobae.com/p/demo-sh-097
- https://echobae.com/p/demo-sh-072
- https://echobae.com/p/demo-sh-029
- https://echobae.com/p/demo-sh-031
- https://echobae.com/p/demo-sh-057
- https://echobae.com/p/demo-sh-083
- https://echobae.com/p/demo-sh-082
- https://echobae.com/p/demo-sh-058
- https://echobae.com/p/demo-sh-048
- https://echobae.com/products?tag=energy-saving
- https://echobae.com/p/demo-sh-059
- https://echobae.com/p/demo-sh-034
- https://echobae.com/p/demo-sh-086
- https://echobae.com/p/demo-sh-061
- https://echobae.com/p/demo-sh-064
- https://echobae.com/p/demo-sh-038
- https://echobae.com/p/demo-sh-089
- https://echobae.com/p/149cm-anime-silicone-doll-yawen
- https://echobae.com/p/149cm-lifelike-silicone-sex-doll-xiuyan
- https://echobae.com/p/149cm-realistic-silicone-sex-doll-xiuyan
- https://echobae.com/p/159cm-realistic-silicone-sex-doll-muyao
- https://echobae.com/p/169cm-realistic-silicone-sex-doll-nancy
- https://echobae.com/p/159cm-premium-silicone-love-doll-cailin
- https://echobae.com/p/159cm-bikini-silicone-love-doll-linda
- https://echobae.com/p/169cm-big-breast-silicone-sex-doll-xiuyan
- https://echobae.com/p/159cm-cosplay-silicone-sex-doll-cailin
- https://echobae.com/p/159cm-twin-ponytail-silicone-doll-nancy
- https://echobae.com/p/169cm-lifelike-silicone-sex-doll-jieman
- https://echobae.com/p/169cm-asian-silicone-sex-doll-xiaowu
- https://echobae.com/p/159cm-cute-silicone-love-doll-xiuyan
- https://echobae.com/p/demo-sh-033
- https://echobae.com/p/demo-sh-050
- https://echobae.com/p/demo-sh-040
- https://echobae.com/p/smart-plug-4pack
- https://echobae.com/p/demo-sh-047
- https://echobae.com/p/demo-sh-068
- https://echobae.com/p/demo-sh-094
- https://echobae.com/p/demo-sh-069
- https://echobae.com/p/demo-sh-016
- https://echobae.com/p/demo-sh-018
- https://echobae.com/p/demo-sh-024
- https://echobae.com/p/demo-sh-032
- https://echobae.com/p/demo-sh-039
- https://echobae.com/p/demo-sh-049
- https://echobae.com/p/demo-sh-074
- https://echobae.com/p/demo-sh-023
- https://echobae.com/p/demo-sh-035
- https://echobae.com/p/demo-sh-042
- https://echobae.com/p/demo-sh-043
- https://echobae.com/p/demo-sh-093
- https://echobae.com/p/demo-sh-010
- https://echobae.com/p/demo-sh-017
- https://echobae.com/p/demo-sh-019
- https://echobae.com/p/demo-sh-025
- https://echobae.com/p/demo-sh-026
- https://echobae.com/p/demo-sh-062
- https://echobae.com/p/demo-sh-067
- https://echobae.com/p/demo-sh-073
- https://echobae.com/p/demo-sh-098
- https://echobae.com/p/149cm-implanted-hair-silicone-doll-muyao
- https://echobae.com/p/149cm-lifelike-silicone-sex-doll-baoer
- https://echobae.com/p/149cm-lifelike-silicone-sex-doll-nancy
- https://echobae.com/p/149cm-natural-look-silicone-doll-nancy
- https://echobae.com/p/149cm-realistic-silicone-sex-doll-ailing
- https://echobae.com/p/149cm-realistic-silicone-sex-doll-aurora
- https://echobae.com/p/153cm-real-skin-texture-silicone-sex-doll-katelyn
- https://echobae.com/p/153cm-real-skin-texture-silicone-sex-doll-lydia
- https://echobae.com/p/159cm-blonde-silicone-love-doll-miriam
- https://echobae.com/p/159cm-cosplay-silicone-sex-doll-baoer
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-bersa
- https://echobae.com/p/159cm-premium-silicone-love-doll-qiuyu
- https://echobae.com/p/169cm-bikini-silicone-sex-doll-linda
- https://echobae.com/p/169cm-blonde-silicone-sex-doll-nancy
- https://echobae.com/p/169cm-premium-silicone-love-doll-yufei
- https://echobae.com/p/169cm-slim-silicone-sex-doll-haiyue
- https://echobae.com/p/170cm-bikini-silicone-sex-doll-perry
- https://echobae.com/p/1784262609174
- https://echobae.com/p/elva-168cm-f-cup-demo
- https://echobae.com/p/elva-168cm-f-cup-demo-copy-copy
- https://echobae.com/p/elva-168cm-f-cup-demo-copy-copy-copy
- https://echobae.com/p/elva-168cm-f-cup-demo-copy-copy-copy-copy
- https://echobae.com/p/elva-168cm-f-cup-demo-copy-copy-copy-copy-copy
- https://echobae.com/p/smart-led-strip
- https://echobae.com/p/test888
- https://echobae.com/p/169cm-silicone-large-breast-sex-doll-sheena
- https://echobae.com/p/1783396233625ff
- https://echobae.com/p/1783396905878
- https://echobae.com/p/1783397572134
- https://echobae.com/p/1783569515569
- https://echobae.com/p/1783569871599
- https://echobae.com/p/e2e-ship-heavy
- https://echobae.com/p/e2e-ship-light
- https://echobae.com/p/e2e-ship-volumetric

### TRACK-01 · P2 · GTM已嵌入，但事件与隐私承诺未验证

**类别：** 追踪/隐私

**验证状态：** GTM公开嵌入已验证；账户/事件/同意待验证

**问题状态：** 未验证

**复现步骤：** 检查公开GTM容器请求与隐私政策承诺；账户验证仅由运营在GTM Preview/GA4 DebugView完成，线上审计不提交真实purchase。

**证据：** 公开请求GTM-T2DKHJKK；请求在代理中失败。政策承诺不向外部营销/第三方分析披露成人浏览信息，并列Optional Analytics Cookies。无法读取容器/GA4/GSC账户。

**影响：** 不能证明电商追踪或同意管理正确；潜在承诺与实际配置不符

**可能根因：** 真实容器标签、Consent Mode和数据层规则未知

**修复方法：** 运营和开发在GTM预览/GA4 DebugView验证view_item/add_to_cart/begin_checkout（purchase用测试环境）；审核数据最小化与同意管理，避免不必要成人商品/身份数据外发；按真实情况修订政策。

**负责人：** 运营+开发

**预计工作量：** 1–2人日（估算）

**验收标准：** 账号配置、同意前后网络及事件单次触发有证据；无PII外发，政策与实际标签一致

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/
- https://echobae.com/privacy-policy

### PERF-03 · P2 · 首屏存在可减小的公共CSS/JS负载

**类别：** 首屏CSS

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 查看home-mobile-1 unused-css-rules/unused-javascript/render-blocking-insight与network-requests；核对公共CSS/JS资源字节。

**证据：** home-mobile-1：blocks-built.css 26251B，unused估计22227B；StoreFooter CSS约10016B阻塞；DNfd1SfM.js传输约243593B、未使用估计86240B。

**影响：** 增加首屏下载/解析及阻塞链

**可能根因：** 共享构建器样式全量输出

**修复方法：** 按当前页面block拆分样式，保留关键CSS并延后非关键样式；按路由拆分公共JS。避免purge动态类后破坏builder；实测而非累加Lighthouse估算收益。

**负责人：** 开发

**预计工作量：** 1–2人日（估算）

**验收标准：** 相同功能截图不退化，初始CSS/JS传输量和未使用字节下降，LCP/FCP重复测试改善

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/

### IMG-03 · P2 · 移动Banner复用大图且无srcset

**类别：** Banner资源

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 读取390px首页Banner的natural/render/srcset/fetchPriority与loading；对照LCP节点和首图请求时间。

**证据：** deep.json：Banner固有1672×941，移动390×219.48，无srcset/sizes，首图fetchPriority auto、两张eager；LCP诊断优先级提示未满足。

**影响：** 移动下载无法按布局选图，多轮播图片争用首屏资源

**可能根因：** Banner组件只用单src、全轮播eager

**修复方法：** 生成符合真实构图的移动/桌面候选，当前首屏图fetchpriority=high且eager，其他轮播按交互/预加载窗口延后；不延迟真实LCP图。

**负责人：** 开发+设计

**预计工作量：** 0.5–1人日（估算）

**验收标准：** 移动选择更小候选且清晰，首屏图提前请求；切换不出现空白，LCP和总图片字节改善

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/

### UX-04 · P2 · CTA和比较价文字对比度未达到自动化阈值

**类别：** 颜色对比度

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 打开home-mobile-1/product-mobile-1 color-contrast失败节点；核对Explore/比较价CSS色值及16px字体。

**证据：** home-mobile-1 color-contrast：Explore #ff2929/白色比3.74:1；product-mobile-1 比较价#9ca3af/白色2.53:1，16px普通文本预期4.5:1。

**影响：** 低视力用户阅读价格与操作困难

**可能根因：** 主题accent与muted颜色未按实际背景配对

**修复方法：** 设计/开发调整CTA文字或背景、比较价灰色，普通文本至少4.5:1，大文本至少3:1；保留品牌色用于适合的非文字装饰。

**负责人：** 设计+开发

**预计工作量：** 0.5人日（估算）

**验收标准：** 对应CSS节点对比度复测通过；各hover/focus/disabled状态分别检查，不以总分代替具体节点

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia

### UX-05 · P2 · 营销弹窗在购物及结账过程中打断操作

**类别：** 结账干扰

**验证状态：** 已验证

**问题状态：** 待修改

**复现步骤：** 正常成年确认后停留商品/Checkout，等待营销弹窗，检查遮挡购物或优惠入口；正常点击×恢复操作，不提交邮箱订阅。

**证据：** commerce-popup-attempt.json与checkout-initial-attempt.json中Get an extra discount!对话框拦截ADD TO CART/Use coupon；正常点击×可关闭，未证明按钮本身失效。

**影响：** 用户正在决策/输入时被打断；属于转化体验风险而非购物流程不可用

**可能根因：** 营销弹窗触发规则包含商品及checkout，未考虑年龄弹窗和购买步骤

**修复方法：** 运营/开发限制营销弹窗在checkout触发，或改非阻塞提示；避免年龄验证后马上叠营销弹窗；保留可关闭、键盘可用与会话频率控制。

**负责人：** 运营+开发

**预计工作量：** 0.5人日（估算）

**验收标准：** 完整购物到结账过程中无非必要阻塞弹窗；年龄验证正常、优惠入口仍可见；测试不触发订阅邮件

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia
- https://echobae.com/checkout

### SEO-08 · P3 · 商品Schema基础有效但变体/图片字段仍需发布校验

**类别：** 结构化数据

**验证状态：** 基础语法/样本字段已验证；富结果及变体规则待验证

**问题状态：** 待优化

**复现步骤：** 从代表SKU初始HTML解析Product/Offer/BreadcrumbList，比较默认USD价格、SKU、图片和库存标签；后台真实库存另验。

**证据：** crawl.json：JSON-LD均可解析；Lydia Product name/sku QY029/Offer USD1609.99/InStock与基础页一致。Demo有相对image和评分；正式样本没有AggregateRating。

**影响：** 语法正确不等于Google富结果资格或实际展示

**可能根因：** Schema模型主要输出默认Offer，额外升级/库存映射需开发确认

**修复方法：** 先清理Demo；确保绝对图片URL和真实库存/价格，适用时补SKU/商品变体模型，禁止无评价造评分；按Google产品与成人内容富结果规范人工复核。不优先添加FAQPage争取普通电商FAQ富结果。

**负责人：** 开发+运营

**预计工作量：** 0.5–1人日（估算）

**验收标准：** 正式商品Schema可解析且与默认配置一致；代表变体价格/库存策略明确；官方验证工具检查后保存结果，不承诺展示

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/p/demo-sh-020
- https://echobae.com/p/demo-sh-030
- https://echobae.com/p/demo-sh-060
- https://echobae.com/p/demo-sh-080
- https://echobae.com/p/demo-sh-090
- https://echobae.com/p/demo-sh-100
- https://echobae.com/p/robovac-x1
- https://echobae.com/p/demo-sh-001
- https://echobae.com/p/demo-sh-002
- https://echobae.com/p/demo-sh-003
- https://echobae.com/p/demo-sh-004
- https://echobae.com/p/demo-sh-005
- https://echobae.com/p/demo-sh-006
- https://echobae.com/p/demo-sh-007
- https://echobae.com/p/demo-sh-008
- https://echobae.com/p/demo-sh-009
- https://echobae.com/p/demo-sh-011
- https://echobae.com/p/demo-sh-012
- https://echobae.com/p/demo-sh-013
- https://echobae.com/p/demo-sh-014
- https://echobae.com/p/149cm-christmas-silicone-love-doll-huaze
- https://echobae.com/p/170cm-realistic-silicone-sex-doll-jiachen
- https://echobae.com/p/159cm-natural-look-silicone-doll-jiachen
- https://echobae.com/p/170cm-real-skin-texture-silicone-sex-doll-jiachen
- https://echobae.com/p/169cm-silicone-realistic-sex-doll-jieman
- https://echobae.com/p/159cm-realistic-silicone-sex-doll-lanxin
- https://echobae.com/p/149cm-silicone-sex-doll-lanxin
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-lydia
- https://echobae.com/p/149cm-silicone-doll-lydia
- https://echobae.com/p/169cm-premium-silicone-love-doll-lydia
- https://echobae.com/p/159cm-natural-look-silicone-doll-lydia
- https://echobae.com/p/169cm-anime-silicone-sex-doll-luoli
- https://echobae.com/p/169cm-realistic-silicone-sex-doll-muyao
- https://echobae.com/p/153cm-ai-companion-silicone-doll-muyao
- https://echobae.com/p/169cm-natural-look-silicone-doll-siwei
- https://echobae.com/p/169cm-teacher-fantasy-silicone-doll-ruyan
- https://echobae.com/p/159cm-anime-silicone-doll-ruyan
- https://echobae.com/p/159cm-teacher-fantasy-silicone-doll-siwei
- https://echobae.com/p/169cm-realistic-silicone-sex-doll-juaner
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-juaner
- https://echobae.com/p/149cm-slim-silicone-love-doll-juaner
- https://echobae.com/p/149cm-lifelike-silicone-sex-doll-sheena
- https://echobae.com/p/159cm-premium-silicone-love-doll-sheena
- https://echobae.com/p/169cm-natural-look-silicone-doll-sheena
- https://echobae.com/p/149cm-cosplay-silicone-doll-sheena
- https://echobae.com/p/159cm-anime-silicone-sex-doll-xiaen
- https://echobae.com/p/149cm-anime-silicone-love-doll-xiaoyu
- https://echobae.com/p/159cm-silicone-adult-love-doll-xingzi
- https://echobae.com/p/169cm-ai-silicone-companion-doll-xingzi
- https://echobae.com/p/149cm-white-hair-silicone-doll-siwei
- https://echobae.com/p/169cm-realistic-silicone-love-doll-zhuzhu
- https://echobae.com/p/149cm-premium-silicone-love-doll-jieyi
- https://echobae.com/p/159cm-implanted-hair-silicone-sex-doll-zhiyan
- https://echobae.com/p/169cm-lifelike-silicone-sex-doll-yumeng
- https://echobae.com/p/149cm-anime-silicone-doll-yumeng
- https://echobae.com/p/159cm-cosplay-silicone-sex-doll-yumeng
- https://echobae.com/p/149cm-realistic-silicone-sex-doll-yufei
- https://echobae.com/p/169cm-silicone-adult-love-doll-yuran
- https://echobae.com/p/159cm-natural-look-silicone-doll-yinuo
- https://echobae.com/p/153cm-fantasy-silicone-sex-doll-yanke
- https://echobae.com/p/169cm-premium-silicone-love-doll-yawen
- https://echobae.com/p/demo-sh-095
- https://echobae.com/p/demo-sh-071
- https://echobae.com/p/demo-sh-045
- https://echobae.com/p/demo-sh-044
- https://echobae.com/p/demo-sh-022
- https://echobae.com/p/demo-sh-021
- https://echobae.com/p/demo-sh-028
- https://echobae.com/p/demo-sh-078
- https://echobae.com/p/demo-sh-055
- https://echobae.com/p/demo-sh-084
- https://echobae.com/p/demo-sh-036
- https://echobae.com/p/demo-sh-096
- https://echobae.com/p/demo-sh-092
- https://echobae.com/p/demo-sh-085
- https://echobae.com/p/demo-sh-056
- https://echobae.com/p/demo-sh-081
- https://echobae.com/p/demo-sh-079
- https://echobae.com/p/demo-sh-054
- https://echobae.com/p/demo-sh-066
- https://echobae.com/p/demo-sh-015
- https://echobae.com/p/demo-sh-091
- https://echobae.com/p/demo-sh-088
- https://echobae.com/p/demo-sh-087
- https://echobae.com/p/demo-sh-077
- https://echobae.com/p/demo-sh-065
- https://echobae.com/p/demo-sh-063
- https://echobae.com/p/demo-sh-099
- https://echobae.com/p/demo-sh-076
- https://echobae.com/p/demo-sh-075
- https://echobae.com/p/demo-sh-046
- https://echobae.com/p/demo-sh-051
- https://echobae.com/p/demo-sh-041
- https://echobae.com/p/demo-sh-052
- https://echobae.com/p/demo-sh-037
- https://echobae.com/p/demo-sh-027
- https://echobae.com/p/demo-sh-053
- https://echobae.com/p/demo-sh-097
- https://echobae.com/p/demo-sh-072
- https://echobae.com/p/demo-sh-029
- https://echobae.com/p/demo-sh-031
- https://echobae.com/p/demo-sh-057
- https://echobae.com/p/demo-sh-083
- https://echobae.com/p/demo-sh-082
- https://echobae.com/p/demo-sh-058
- https://echobae.com/p/demo-sh-048
- https://echobae.com/p/demo-sh-059
- https://echobae.com/p/demo-sh-034
- https://echobae.com/p/demo-sh-086
- https://echobae.com/p/demo-sh-061
- https://echobae.com/p/demo-sh-064
- https://echobae.com/p/demo-sh-038
- https://echobae.com/p/demo-sh-089
- https://echobae.com/p/149cm-anime-silicone-doll-yawen
- https://echobae.com/p/149cm-lifelike-silicone-sex-doll-xiuyan
- https://echobae.com/p/149cm-realistic-silicone-sex-doll-xiuyan
- https://echobae.com/p/159cm-realistic-silicone-sex-doll-muyao
- https://echobae.com/p/169cm-realistic-silicone-sex-doll-nancy
- https://echobae.com/p/159cm-premium-silicone-love-doll-cailin
- https://echobae.com/p/159cm-bikini-silicone-love-doll-linda
- https://echobae.com/p/169cm-big-breast-silicone-sex-doll-xiuyan
- https://echobae.com/p/159cm-cosplay-silicone-sex-doll-cailin
- https://echobae.com/p/159cm-twin-ponytail-silicone-doll-nancy
- https://echobae.com/p/169cm-lifelike-silicone-sex-doll-jieman
- https://echobae.com/p/169cm-asian-silicone-sex-doll-xiaowu
- https://echobae.com/p/159cm-cute-silicone-love-doll-xiuyan
- https://echobae.com/p/demo-sh-033
- https://echobae.com/p/demo-sh-050
- https://echobae.com/p/demo-sh-040
- https://echobae.com/p/smart-plug-4pack
- https://echobae.com/p/demo-sh-047
- https://echobae.com/p/demo-sh-068
- https://echobae.com/p/demo-sh-094
- https://echobae.com/p/demo-sh-069
- https://echobae.com/p/demo-sh-016
- https://echobae.com/p/demo-sh-018
- https://echobae.com/p/demo-sh-024
- https://echobae.com/p/demo-sh-032
- https://echobae.com/p/demo-sh-039
- https://echobae.com/p/demo-sh-049
- https://echobae.com/p/demo-sh-074
- https://echobae.com/p/demo-sh-023
- https://echobae.com/p/demo-sh-035
- https://echobae.com/p/demo-sh-042
- https://echobae.com/p/demo-sh-043
- https://echobae.com/p/demo-sh-093
- https://echobae.com/p/demo-sh-010
- https://echobae.com/p/demo-sh-017
- https://echobae.com/p/demo-sh-019
- https://echobae.com/p/demo-sh-025
- https://echobae.com/p/demo-sh-026
- https://echobae.com/p/demo-sh-062
- https://echobae.com/p/demo-sh-067
- https://echobae.com/p/demo-sh-073
- https://echobae.com/p/demo-sh-098
- https://echobae.com/p/149cm-implanted-hair-silicone-doll-muyao
- https://echobae.com/p/149cm-lifelike-silicone-sex-doll-baoer
- https://echobae.com/p/149cm-lifelike-silicone-sex-doll-nancy
- https://echobae.com/p/149cm-natural-look-silicone-doll-nancy
- https://echobae.com/p/149cm-realistic-silicone-sex-doll-ailing
- https://echobae.com/p/149cm-realistic-silicone-sex-doll-aurora
- https://echobae.com/p/153cm-real-skin-texture-silicone-sex-doll-katelyn
- https://echobae.com/p/153cm-real-skin-texture-silicone-sex-doll-lydia
- https://echobae.com/p/159cm-blonde-silicone-love-doll-miriam
- https://echobae.com/p/159cm-cosplay-silicone-sex-doll-baoer
- https://echobae.com/p/159cm-lifelike-silicone-sex-doll-bersa
- https://echobae.com/p/159cm-premium-silicone-love-doll-qiuyu
- https://echobae.com/p/169cm-bikini-silicone-sex-doll-linda
- https://echobae.com/p/169cm-blonde-silicone-sex-doll-nancy
- https://echobae.com/p/169cm-premium-silicone-love-doll-yufei
- https://echobae.com/p/169cm-slim-silicone-sex-doll-haiyue
- https://echobae.com/p/170cm-bikini-silicone-sex-doll-perry
- https://echobae.com/p/1784262609174
- https://echobae.com/p/elva-168cm-f-cup-demo
- https://echobae.com/p/elva-168cm-f-cup-demo-copy-copy
- https://echobae.com/p/elva-168cm-f-cup-demo-copy-copy-copy
- https://echobae.com/p/elva-168cm-f-cup-demo-copy-copy-copy-copy
- https://echobae.com/p/elva-168cm-f-cup-demo-copy-copy-copy-copy-copy
- https://echobae.com/p/smart-led-strip
- https://echobae.com/p/test888
- https://echobae.com/p/169cm-silicone-large-breast-sex-doll-sheena
- https://echobae.com/p/1783396233625ff
- https://echobae.com/p/1783396905878
- https://echobae.com/p/1783397572134
- https://echobae.com/p/1783569515569
- https://echobae.com/p/1783569871599
- https://echobae.com/p/e2e-ship-heavy
- https://echobae.com/p/e2e-ship-light
- https://echobae.com/p/e2e-ship-volumetric

### CONT-05 · P3 · Summer Sale 2026横幅在10月仍显示

**类别：** 促销内容

**验证状态：** 文字已验证；活动有效性待运营核验

**问题状态：** 未验证

**复现步骤：** 读取顶部Summer Sale2026文案；运营核对当前活动起止、优惠规则与实际有效码，不仅凭季节判定过期。

**证据：** crawl及所有浏览样本顶部Summer Sale 2026 - Extra10% OFF · Shop now；未获活动起止和折扣规则。

**影响：** 活动时效不清；不能据季节单独认定优惠失效

**可能根因：** 活动未设置结束时间或活动名称有意保留

**修复方法：** 运营确认实际促销有效性、代码和适用SKU；过期则撤下，仍有效则改为真实活动名并补规则。

**负责人：** 运营

**预计工作量：** 0.25人日（估算）

**验收标准：** 横幅活动名称/期限/折扣条件与实际结账优惠一致

**受影响URL（已观察范围，非未查全站推断）：**

- https://echobae.com/

## 未完成/外部验证项（不得标为已通过）

- 后台正式SKU/库存/生产能力、真实政策事实、评价授权、物流分区和税费规则：需运营与第三方开发。
- GSC真实索引、域名验证和Sitemap提交；CrUX/真实INP；GA4/GTM容器事件、Consent Mode：无账户权限。
- 有效/无效优惠码计算、地址校验错误、完整运费/税率、支付跳转和测试purchase：仅展开表单，须开发沙盒，不提交真实订单。
- www和HTTP源站跳转；Google官方文档实时正文；Google字体、loli字体、GTM、picsum正常公网加载：当前代理拒绝，不作源站故障结论。
- 全部SKU选项兼容性、全部图片Zoom/键盘、全部筛选/价格区间/页面断点、辅助技术完整测试和未公开孤立页面：本次抽样未覆盖。
- 没有攻击性扫描/后端代码/服务器日志；未获正式订单/邮件或支付通知端到端结果。

### 官方技术参考

Google Search Central官方参考链接：

- https://developers.google.com/search/docs/crawling-indexing/robots/intro
- https://developers.google.com/search/docs/crawling-indexing/block-indexing
- https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- https://developers.google.com/search/docs/appearance/structured-data/product
- https://developers.google.com/search/docs/appearance/structured-data/faqpage
- https://developers.google.com/search/docs/crawling-indexing/safesearch

本环境实际请求这些文档均被代理403拒绝，见official-reference-access.json。因此没有声称读取当前在线正文；使用稳定技术规则提出修复，发布前由开发在可访问网络核对最新适用规范与官方验证工具。没有伪造Rich Results Test/GSC通过截图。

## 修复依赖与发布顺序

1. 运营锁定正式SKU与业务政策、评论来源；开发同步发布白名单和价格模型。
2. 修复软404、条款链接、图片候选/主要裁剪、SSR/hydration/必需API。
3. 优化首屏/主线程，并在正常第三方网络重复性能与购买沙盒测试。
4. 通过政策、配送/税费/有效优惠码、测试支付和数据追踪验收。
5. 最后在正式发布窗口解除公开页面noindex/robots、发布非空Sitemap、提交GSC；继续排除交易与账户页。
6. P2/P3视觉/FAQ/社媒/变体Schema及内容按影响范围短期排程，不让细节阻碍必要修复。
