#  二元套利计算器

用于 预测市场与博彩平台之间的二元套利计算。
支持：

PM vs PM

PM vs 博彩

博彩 vs PM

博彩 vs 博彩

输入 A 市场价格或赔率、B 市场价格或赔率，选择 A 的下注方式（Shares / 金额），即可自动计算 B 对冲下注金额与 shares，并输出理论锁定利润。

优势

全场景适用：PM vs PM / PM vs Book / Book vs PM / Book vs Book

可快速对冲：只需输入 A 投注，即可得到 B 下注金额和份额

理论利润清晰：帮助快速决策套利机会

---

## ✨ 功能特点

1. 灵活输入

A、B 市场都可以选择输入价格或赔率

自动转换概率、统一计算逻辑

支持跨市场套利场景

2. 下注方式选择

Shares：直接输入 A 的份额

金额：输入 A 的投入金额，自动计算对应份额

3. 自动计算 B 对冲

自动输出 B金额 和 B Shares

保证理论上无论 A 还是 B 胜出，都能锁定利润

4. 理论利润

自动计算 最小利润（无论哪边赢）

公式统一：

# A payout
payoutA = stakeA * oddsA if oddsA > 0 else sharesA

# B 对冲
if oddsB > 0:  # B是博彩
    stakeB = payoutA / oddsB
    sharesB = stakeB
else:  # B是PM
    sharesB = payoutA
    stakeB = sharesB * priceB

# 理论利润
payoutB = stakeB * oddsB if oddsB > 0 else sharesB
profitA = payoutA - stakeA - stakeB
profitB = payoutB - stakeA - stakeB
profit = min(profitA, profitB)
5. 套利判断

自动判断套利条件：

arb_condition = pA + pB
if arb_condition < 1:
    print("存在套利机会 ✅")
else:
    print("不存在套利 ❌")

---

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install streamlit pywebview requests

2. 运行程序
python desktop_app.py



📌 注意事项


本工具仅供学习和参考，实际交易请自行承担风险


⭐ Star 支持
如果你觉得这个工具好用，欢迎给个 Star ⭐

Made with @polymoney for 套利爱好者
