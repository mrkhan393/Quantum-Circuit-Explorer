import streamlit as st
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
from explorer.builder import *
from explorer.simulator import simulate_circuit, plot_counts
import matplotlib.pyplot as plt

st.set_page_config(page_title="Quantum Circuit Explorer", layout="centered")
st.title("🧠 Quantum Circuit Explorer")

st.write("Build and explore quantum circuits interactively using Qiskit!")

# Sidebar
st.sidebar.subheader("Custom Gate Parameters")
rx_angle = st.sidebar.number_input("Rx", -3.14, 3.14, 0.0)
ry_angle = st.sidebar.number_input("Ry", -3.14, 3.14, 0.0)
rz_angle = st.sidebar.number_input("Rz", -3.14, 3.14, 0.0)

st.sidebar.subheader("Qubits and Shots")
num_qubits = st.sidebar.slider("Qubits", 1, 5, 2)
shots = st.sidebar.slider("Shots", 100, 2048, 1024)

st.sidebar.subheader("Select Circuit")
circuit_type = st.sidebar.selectbox("Circuit Type", (
    "Bell", "GHZ", "Superposition", "Custom",
    "Quantum Teleportation", "QFT", "Grover's Algorithm", "Deutsch-Jozsa",
    "Quantum Phase Estimation", "Quantum Coin Toss", "Bell-State Measurement",
    "SWAP Test", "W-State"
))

# Build selected circuit
if circuit_type == "Bell":
    qc, qc_for_visual = builder_bell_circuit()
elif circuit_type == "GHZ":
    qc, qc_for_visual = builder_ghz_circuit(num_qubits)
elif circuit_type == "Superposition":
    qc, qc_for_visual = builder_superposition_circuit(num_qubits)
elif circuit_type == "Custom":
    qc, qc_for_visual = builder_custom_circuit(rx_angle, ry_angle, rz_angle)
elif circuit_type == "Quantum Teleportation":
    qc, qc_for_visual = builder_quantum_teleportation()
elif circuit_type == "QFT":
    qc, qc_for_visual = builder_qft_circuit(num_qubits)
elif circuit_type == "Grover's Algorithm":
    qc, qc_for_visual = builder_grover_circuit()
elif circuit_type == "Deutsch-Jozsa":
    qc, qc_for_visual = builder_deutsch_jozsa()
elif circuit_type == "Quantum Phase Estimation":
    qc, qc_for_visual = builder_qpe_circuit()
elif circuit_type == "Quantum Coin Toss":
    qc, qc_for_visual = builder_coin_toss()
elif circuit_type == "Bell-State Measurement":
    qc, qc_for_visual = builder_bell_measurement()
elif circuit_type == "SWAP Test":
    qc, qc_for_visual = builder_swap_test()
elif circuit_type == "W-State":
    qc, qc_for_visual = builder_w_state()
else:
    st.error("Unknown circuit selected.")

# Show Circuit
st.subheader(f"🔬 {circuit_type} Circuit")
st.text(qc_for_visual.draw())

# Simulate
st.subheader(f"📊 Simulation Results of {circuit_type} Circuit")
counts = simulate_circuit(qc, shots=shots)
st.pyplot(plot_counts(counts))

# Bloch Sphere (only for 1-2 qubit states)
try:
    qc_no_measure = qc_for_visual.copy()
    qc_no_measure.remove_final_measurements()
    state = Statevector.from_instruction(qc_no_measure)
    if len(state) <= 2**3:
        st.subheader(f"🌀 Bloch Sphere of {circuit_type} Circuit")
        bloch = plot_bloch_multivector(state)
        st.pyplot(bloch)
except Exception as e:
    st.warning(f"Bloch Sphere not shown: {e}")