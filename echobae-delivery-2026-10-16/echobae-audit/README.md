# Echobae 线上审计

本仓库分支 `audit/prelaunch-2026-10-13` 保存2026-10-13只读审计。网站由第三方开发管理，本仓库没有网站应用源代码。

从 [AUDIT_SUMMARY.md](AUDIT_SUMMARY.md) 开始；详报 [FULL_AUDIT.md](FULL_AUDIT.md)，问题表 [ISSUES.csv](ISSUES.csv)，证据 [evidence/INDEX.md](evidence/INDEX.md)。CSV采用UTF-8 BOM。

覆盖228个公开发现URL、25个深度代表页面、58个视口记录，27次Lighthouse；不能把抽样视为全SKU、后台、支付及真实Google索引认证。

## 脚本与复检

已有Cloud环境包含Python、Playwright、Pillow、Chromium。Lighthouse位于 `/workspace/echobae-audit/tools/node_modules/.bin/lighthouse`；新环境可在仓库外目录用 npm install lighthouse@13.5.0 重新安装（TLS/校验必须开启），或改脚本的BIN变量为实际安装路径。

从仓库根目录执行对应scripts/*.py。爬虫支持从当前证据恢复，因此复检应另建证据目录或备份当前文件，并更新脚本D路径；不要覆盖原始基线。该任务环境已经隔离，不需要另建Git worktree。

`crawl.py` / `pagination.py` 做公开链接发现与基础检查；`deep_browser.py` 做代表视口采集；`cart_verify.py` / `checkout_checks.py` 做正常匿名购物展示；`performance.py` 做顺序重复Lighthouse；`accepted_performance.py` 使用正常年龄确认保留存储作对照；`build_reports.py` 根据本次数据生成报告，问题判断是本次审计结论，不能盲目套用新站点。

所有商品/购物测试仅在隔离浏览器会话。不要执行PLACE ORDER、支付、订阅或联系表单；不要输入真实个人信息。脚本不测试真实付款或订单创建；checkout展示通过不等于交易链通过。资源脚本只允许站内HTTPS；页面中的内部IP/第三方URL记录后跳过，不探测私网。

云环境代理证书可能随连接更新。curl可信但Chromium证书失败时，应将平台提供CA导入用户Chromium信任库并重测，不能用ignore_https_errors或关闭证书验证。字体/GTM/www等代理拒绝应单列环境限制，不能认定源站故障。

源站、后台、GSC/GA4/GTM和支付测试模式都未提供凭据。未修改线上站点，本分支只交付审计和修复计划。
