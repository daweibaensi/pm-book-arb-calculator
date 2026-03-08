# PM vs Book 套利计算器

一个简单好用的**预测市场（Polymarket） vs 博彩平台**跨平台套利计算器。

只需输入：
- Polymarket YES 价格（p）
- 博彩平台赔率（o）
- 你想买的 Polymarket 股数（s）

程序会自动计算：
- 需要在博彩平台下注多少金额
- 是否存在无风险套利
- 可以锁定的利润是多少

---

## ✨ 功能特点

- 一键启动桌面应用（无需打开浏览器）
- 简洁美观的中文界面
- 实时计算是否为正套利（p + 1/o < 1）

---

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install streamlit pywebview requests

2. 运行程序
python desktop_app.py



🧮 计算公式说明
Pythonbook_stake = s / o
locked_profit = s * (1 - p - 1/o)
is_arb = (p + 1/o) < 1

book_stake：需要在博彩平台下注的金额
locked_profit：无风险锁定利润
is_arb：True = 存在套利机会


📌 注意事项

Polymarket 价格必须在 0~1 之间
博彩赔率必须大于 1.01
本工具仅供学习和参考，实际交易请自行承担风险


⭐ Star 支持
如果你觉得这个工具好用，欢迎给个 Star ⭐

Made with @polymoney for 套利爱好者
