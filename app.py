import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Market Power Simulator")
st.title("🧠 Market Power Simulator: Monopoly vs Monopsony")

st.markdown("""
Welcome to the **Market Power Simulator**! Use the sliders to adjust market parameters and compare outcomes under:
- **Perfect Competition**
- **Monopoly** (single seller)
- **Monopsony** (single buyer)
""")

st.sidebar.header("Market Parameters")
demand_intercept = st.sidebar.slider("Demand Intercept (a)", 10, 100, 60)
demand_slope = st.sidebar.slider("Demand Slope (b)", 1, 10, 2)
supply_intercept = st.sidebar.slider("Supply Intercept (c)", 0, 50, 20)
supply_slope = st.sidebar.slider("Supply Slope (d)", 1, 10, 3)

quantity = np.linspace(0, 50, 100)

def demand(q):
    return demand_intercept - demand_slope * q

def supply(q):
    return supply_intercept + supply_slope * q

def marginal_revenue(q):
    return demand_intercept - 2 * demand_slope * q

def marginal_cost(q):
    return supply(q)

def marginal_expenditure(q):
    return supply_intercept + 2 * supply_slope * q

# Compute intersections
q_comp = (demand_intercept - supply_intercept) / (demand_slope + supply_slope)
p_comp = demand(q_comp)

q_mono = (demand_intercept - supply_intercept) / (2 * demand_slope + supply_slope)
p_mono = demand(q_mono)

q_monop = (demand_intercept - supply_intercept) / (demand_slope + 2 * supply_slope)
p_monop = supply(q_monop)

# Plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(quantity, demand(quantity), label="Demand (D)")
ax.plot(quantity, supply(quantity), label="Supply (S)")
ax.plot(quantity, marginal_revenue(quantity), linestyle='--', label="Marginal Revenue (MR)")
ax.plot(quantity, marginal_expenditure(quantity), linestyle='--', label="Marginal Expenditure (ME)")
ax.axvline(q_comp, color='green', linestyle=':', label="Q Competitive")
ax.axvline(q_mono, color='red', linestyle=':', label="Q Monopoly")
ax.axvline(q_monop, color='blue', linestyle=':', label="Q Monopsony")

ax.set_xlabel("Quantity")
ax.set_ylabel("Price / Cost")
ax.set_title("Market Outcomes")
ax.legend()
ax.grid(True)

st.pyplot(fig)

st.markdown("""
### 🧮 Key Results
- **Competitive Market**: Q = {:.2f}, P = {:.2f}
- **Monopoly Outcome**: Q = {:.2f}, P = {:.2f}
- **Monopsony Outcome**: Q = {:.2f}, P = {:.2f}
""".format(q_comp, p_comp, q_mono, p_mono, q_monop, p_monop))

st.markdown("""
Try tweaking the parameters to see how **market power** affects prices and efficiency!

- Monopoly: ↓ Q, ↑ P (bad for consumers)
- Monopsony: ↓ Q, ↓ P (bad for suppliers/workers)

🔍 Use this tool to explore **deadweight loss**, **surplus redistribution**, and real-world policy ideas!
""")
