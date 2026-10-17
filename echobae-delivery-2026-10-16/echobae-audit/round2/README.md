# 第二轮交付说明

从 [SUMMARY.md](SUMMARY.md) 或 [FINAL_REPORT.md](FINAL_REPORT.md) 开始。当前文件仅为本地审计交付，不使用GitHub、不包含网站应用源代码或后台登录凭据。

原37 ID完整保留，新增5项，共42条追踪记录；有部分改善、合并与待核验，不能把42当当前确诊Bug总数。CSV均UTF-8 BOM。

2026-10-14当前HTTP/API/公开构建产物与文件证据在evidence/；DOM/截图及27次Lighthouse复用2026-10-13第一轮材料。浏览器因证书限制且用户不授权CA变更，本轮无新浏览器测量。

scripts/interaction_probe.py是**未执行**的开发复检采集草案，只检查语法，不保证已验证端到端流程；不绕过TLS/年龄验证，不下单/付款。其他脚本输出对应本轮真实分析和公共只读采集。

关键构建产物按当前入口BFXRDhpD和直接依赖定位，旧hash仍能下载不代表使用。所有evidence/code文件是仅格式化镜像，其行号用于报告定位；不代表原始源码文件/目录。
