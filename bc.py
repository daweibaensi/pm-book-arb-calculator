import streamlit as st

st.set_page_config(page_title="套利计算器", layout="centered")

st.markdown("### 二元套利计算器")

# =========================
# A 输入
# =========================
colA1, colA2 = st.columns([1,3])
with colA1:
    st.markdown("**A**")
with colA2:
    modeA = st.radio(
        "",
        ["价格", "赔率"],
        horizontal=True,
        key="modeA"
    )

if modeA == "价格":
    priceA = st.number_input("A价格", min_value=0.01, max_value=0.99, value=0.52)
    oddsA = 0
else:
    oddsA = st.number_input("A赔率", min_value=1.01, value=2.0)
    priceA = 0

# =========================
# B 输入
# =========================
colB1, colB2 = st.columns([1,3])
with colB1:
    st.markdown("**B**")
with colB2:
    modeB = st.radio(
        "",
        ["价格", "赔率"],
        horizontal=True,
        key="modeB"
    )

if modeB == "价格":
    priceB = st.number_input("B价格", min_value=0.01, max_value=0.99, value=0.48)
    oddsB = 0
else:
    oddsB = st.number_input("B赔率", min_value=1.01, value=2.3)
    priceB = 0

# =========================
# 下注方式
# =========================
colC1, colC2 = st.columns([1,3])
with colC1:
    st.markdown("**A下注方式**")
with colC2:
    bet_mode = st.radio(
        "",
        ["Shares", "金额"],
        horizontal=True
    )

if bet_mode == "Shares":
    sharesA = st.number_input("A Shares", min_value=1.0, value=100.0)
    amountA = None
else:
    amountA = st.number_input("A金额", min_value=1.0, value=100.0)
    sharesA = None

# =========================
# 计算
# =========================
if st.button("计算"):

    # -------------------------
    # 统一概率
    # -------------------------
    pA = priceA if priceA > 0 else 1 / oddsA
    pB = priceB if priceB > 0 else 1 / oddsB

    # -------------------------
    # A stake
    # -------------------------
    if bet_mode == "金额":
        if priceA > 0:  # PM
            sharesA = amountA / priceA
            stakeA = amountA
        else:  # Book
            sharesA = amountA
            stakeA = amountA
    else:
        if priceA > 0:  # PM
            stakeA = sharesA * priceA
        else:  # Book
            stakeA = sharesA

    # -------------------------
    # 计算 A payout
    # -------------------------
    payoutA = stakeA * oddsA if oddsA > 0 else sharesA

    # -------------------------
    # 计算 B 对冲
    # -------------------------
    if oddsB > 0:  # B是博彩
        stakeB = payoutA / oddsB
        sharesB = stakeB  # 博彩 shares 等于金额
    else:  # B是PM
        sharesB = payoutA
        stakeB = sharesB * priceB

    # -------------------------
    # 计算理论利润
    # -------------------------
    payoutB = stakeB * oddsB if oddsB > 0 else sharesB
    profitA = payoutA - stakeA - stakeB
    profitB = payoutB - stakeA - stakeB
    profit = min(profitA, profitB)

    # -------------------------
    # 判断套利
    # -------------------------
    arb_condition = pA + pB
    st.divider()
    if arb_condition < 1:
        st.success("存在套利机会 ✅")
    else:
        st.error("不存在套利 ❌")

    # -------------------------
    # 输出结果
    # -------------------------
    st.markdown("**B对冲下注**")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"### B金额: {round(stakeB,2)}")
    with col2:
        st.markdown(f"### B Shares: {round(sharesB,2)}")
    st.markdown(f"### 理论利润: {round(profit,2)}")