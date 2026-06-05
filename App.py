import streamlit as st
import pandas as pd
import numpy as np

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Liquidity Incentive Simulator",
    layout="wide"
)

st.title("📊 Market Maker Performance & Incentive Simulator")

st.markdown("""
Simulated liquidity operations dashboard for evaluating market makers, 
monitoring performance, and allocating incentive rewards.
""")

# =========================
# SIDEBAR CONTROLS
# =========================

st.sidebar.header("⚙️ Incentive Parameters")

reward_pool = st.sidebar.number_input(
    "Reward Pool ($)",
    min_value=1000,
    max_value=1000000,
    value=50000,
    step=5000
)

volume_weight = st.sidebar.slider("Volume Weight", 0.0, 1.0, 0.40)
order_weight = st.sidebar.slider("Order Weight", 0.0, 1.0, 0.25)
uptime_weight = st.sidebar.slider("Uptime Weight", 0.0, 1.0, 0.20)
spread_weight = st.sidebar.slider("Spread Weight", 0.0, 1.0, 0.15)

weight_sum = volume_weight + order_weight + uptime_weight + spread_weight

if abs(weight_sum - 1.0) > 0.001:
    st.sidebar.error("Weights must sum to 1.0")

# =========================
# SYNTHETIC DATA GENERATION
# =========================

np.random.seed(42)

market_makers = [f"MM_{c}" for c in list("ABCDEFGH")]

df = pd.DataFrame({
    "Market Maker": market_makers,
    "Volume_USD_M": np.random.randint(50, 500, len(market_makers)),
    "Orders": np.random.randint(1000, 10000, len(market_makers)),
    "Spread_BPS": np.random.uniform(2, 20, len(market_makers)).round(2),
    "Uptime_Percent": np.random.uniform(90, 100, len(market_makers)).round(2)
})

# =========================
# SCORE COMPONENTS
# =========================

df["Volume_Score"] = df["Volume_USD_M"] / df["Volume_USD_M"].max()
df["Order_Score"] = df["Orders"] / df["Orders"].max()
df["Uptime_Score"] = df["Uptime_Percent"] / 100
df["Spread_Score"] = 1 - (df["Spread_BPS"] / df["Spread_BPS"].max())

# =========================
# LIQUIDITY SCORE ENGINE
# =========================

df["Liquidity_Score"] = (
    volume_weight * df["Volume_Score"] +
    order_weight * df["Order_Score"] +
    uptime_weight * df["Uptime_Score"] +
    spread_weight * df["Spread_Score"]
)

# =========================
# ALERTS
# =========================

df["Spread_Alert"] = df["Spread_BPS"] > 15
df["Uptime_Alert"] = df["Uptime_Percent"] < 95

df["Previous_Volume"] = (
    df["Volume_USD_M"] * np.random.uniform(0.7, 1.3, len(df))
).round(0)

df["Volume_Change_Pct"] = (
    (df["Volume_USD_M"] - df["Previous_Volume"])
    / df["Previous_Volume"]
) * 100

df["Volume_Alert"] = df["Volume_Change_Pct"] < -20

alert_df = df[
    df["Spread_Alert"] |
    df["Uptime_Alert"] |
    df["Volume_Alert"]
]

# =========================
# REWARD ALLOCATION ENGINE
# =========================

total_score = df["Liquidity_Score"].sum()

df["Reward_USD"] = (
    df["Liquidity_Score"] / total_score
) * reward_pool

# =========================
# TOP METRICS
# =========================

st.subheader("📌 Liquidity Operations Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Market Makers", len(df))
col2.metric("Reward Pool", f"${reward_pool:,.0f}")
col3.metric("Avg Liquidity Score", f"{df['Liquidity_Score'].mean():.3f}")
col4.metric("Active Alerts", len(alert_df))

# =========================
# LEADERBOARD
# =========================

st.subheader("🏆 Liquidity Leaderboard")

leaderboard = df.sort_values("Liquidity_Score", ascending=False)

st.dataframe(
    leaderboard[["Market Maker", "Liquidity_Score"]],
    use_container_width=True
)

st.bar_chart(
    leaderboard.set_index("Market Maker")["Liquidity_Score"]
)

# =========================
# INCENTIVE DISTRIBUTION
# =========================

st.subheader("💰 Incentive Allocation")

st.dataframe(
    leaderboard[["Market Maker", "Reward_USD"]],
    use_container_width=True
)

st.bar_chart(
    leaderboard.set_index("Market Maker")["Reward_USD"]
)

# =========================
# ALERT CENTER
# =========================

st.subheader("🚨 Alert Center")

if len(alert_df) > 0:
    st.warning("Operational alerts detected")

    st.dataframe(
        alert_df[[
            "Market Maker",
            "Spread_BPS",
            "Uptime_Percent",
            "Volume_Change_Pct"
        ]],
        use_container_width=True
    )
else:
    st.success("No critical alerts detected")

# =========================
# EXECUTIVE SUMMARY
# =========================

st.subheader("🧠 Executive Summary")

best_mm = leaderboard.iloc[0]

summary = f"""
{best_mm['Market Maker']} is currently the top-performing market maker 
with a liquidity score of {best_mm['Liquidity_Score']:.3f}. 

Based on the current incentive configuration, this participant receives 
${best_mm['Reward_USD']:,.0f} from the reward pool of ${reward_pool:,.0f}.

There are {len(alert_df)} active operational alerts requiring review, 
primarily driven by spread deviations, uptime drops, and volume fluctuations.

The current weighting model places {'volume' if volume_weight > 0.3 else 'balanced liquidity factors'} as the dominant driver of performance.
"""

st.info(summary)
