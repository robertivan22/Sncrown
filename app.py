
import streamlit as st
from slot_simulator import spin_reels, evaluate_spin, display_grid, simulate, symbols

st.set_page_config(page_title="Shining Crown Simulator", layout="centered")
st.title("🎰 Shining Crown Slot Simulator")

if st.button("Spin Once"):
    grid = spin_reels()
    win, scatters = evaluate_spin(grid)
    st.text(display_grid(grid))
    if win > 0:
        st.success(f"You won {win} coins!")
    elif scatters >= 3:
        st.info(f"Scatter bonus hit! ({scatters} crowns)")
    else:
        st.warning("No win this time.")

st.markdown("---")
st.subheader("Simulate Many Spins")

spins = st.slider("Number of spins", 1000, 100000, 10000, step=1000)
if st.button("Run Simulation"):
    result = simulate(spins)
    st.write(f"**Spins:** {result['spins']}")
    st.write(f"**Total Win:** {result['total_win']}")
    st.write(f"**Total Bet:** {result['total_bet']}")
    st.write(f"**Net Result:** {result['net']}")
    st.write(f"**RTP:** {result['rtp']:.2%}")
    st.write(f"**Hit Rate:** {result['hit_rate']:.2%}")
    st.write(f"**Scatters Hit:** {result['scatters_hit']}")
    st.write(f"**Max Single Win:** {result['max_single_win']}")
    st.write(f"**Average Win per Hit:** {result['avg_win_per_hit']:.2f}")
    st.write(f"**Expected Win Every:** ~{result['avg_spins_per_hit']:.1f} spins")
