import streamlit as st


def pm_book_arb(p, o, s):
    if o <= 1:
        return None, None, None
    if not (0 < p < 1):
        return None, None, None

    book_stake = s / o
    locked_profit = s * (1 - p - 1 / o)
    is_arb = (p + 1 / o) < 1

    return book_stake, is_arb, locked_profit


st.title("PM vs Book 套利计算器")

p = st.number_input("PM A YES 价格", min_value=0.01, max_value=0.99, value=0.52)
o = st.number_input("Book B 赔率", min_value=1.01, value=2.3)
s = st.number_input("PM Shares", min_value=1.0, value=100.0)

if st.button("计算套利"):
    stake, arb, profit = pm_book_arb(p, o, s)

    if arb:
        st.success("存在套利机会 ✅")
    else:
        st.error("不存在套利 ❌")

    st.write(f"Book下注金额: {round(stake,2)}")
    st.write(f"锁定利润: {round(profit,2)}")
