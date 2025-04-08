
import streamlit as st
from slot_simulator import spin_reels, evaluate_spin, display_grid, simulate, symbols

st.set_page_config(page_title="Shining Crown Simulator", layout="centered")
st.title("🎰 Shining Crown Slot Simulator (RON Version)")

# Bet slider
bet = st.slider("Set Your Bet (RON)", min_value=1, max_value=250, value=5, step=1)

if st.button("Spin Once"):
    grid = spin_reels()
    win, scatters = evaluate_spin(grid, bet)
    st.text(display_grid(grid))
    if win > 0:
        st.success(f"You won {win:.2f} RON!")
    elif scatters['$'] >= 3 or scatters['★'] >= 3:
        st.info("Scatter hit!")
    else:
        st.warning("No win this time.")

st.markdown("---")
st.subheader("Simulate Many Spins")

spins = st.slider("Number of spins", 1000, 100000, 10000, step=1000)
if st.button("Run Simulation"):
    result = simulate(spins, bet)
    st.write(f"**Spins:** {result['spins']}")
    st.write(f"**Bet per Spin:** {bet} RON")
    st.write(f"**Total Bet:** {result['total_bet']} RON")
    st.write(f"**Total Win:** {result['total_win']:.2f} RON")
    st.write(f"**Net Result:** {result['net']:.2f} RON")
    st.write(f"**RTP:** {result['rtp']:.2%}")
    st.write(f"**Hit Rate:** {result['hit_rate']:.2%}")
    st.write(f"**Scatters ($):** {result['scatters_dollar']}")
    st.write(f"**Scatters (★):** {result['scatters_star']}")
    st.write(f"**Max Single Win:** {result['max_single_win']:.2f} RON")
    st.write(f"**Avg Win per Hit:** {result['avg_win_per_hit']:.2f} RON")
    st.write(f"**Expected Win Every:** ~{result['avg_spins_per_hit']:.1f} spins")
