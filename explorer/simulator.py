from qiskit import transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def simulate_circuit(qc, shots=1024):
    try:
        simulator = AerSimulator()
        compiled = transpile(qc, simulator)
        result = simulator.run(compiled, shots=shots).result()
        counts = result.get_counts()
        return counts
    except Exception as e:
        raise ValueError(f"Simulation error: {e}")

def plot_counts(counts):
    fig = plot_histogram(counts)
    return fig