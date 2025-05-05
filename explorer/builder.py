from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT

def builder_bell_circuit():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc_for_visual = qc.copy()
    qc.measure([0, 1], [0, 1])
    return qc, qc_for_visual

def builder_ghz_circuit(qubits):
    qc = QuantumCircuit(qubits, qubits)
    qc.h(0)
    for i in range(1, qubits):
        qc.cx(0, i)
    qc_for_visual = qc.copy()
    qc.measure(range(qubits), range(qubits))
    return qc, qc_for_visual

def builder_superposition_circuit(qubits):
    qc = QuantumCircuit(qubits, qubits)
    for i in range(qubits):
        qc.h(i)
    qc_for_visual = qc.copy()
    qc.measure(range(qubits), range(qubits))
    return qc, qc_for_visual

def builder_custom_circuit(rx_angle, ry_angle, rz_angle):
    qc = QuantumCircuit(2, 2)
    qc.rx(rx_angle, 0)
    qc.ry(ry_angle, 1)
    qc.rz(rz_angle, 0)
    qc.h(0)
    qc.cx(0, 1)
    qc_for_visual = qc.copy()
    qc.measure([0, 1], [0, 1])
    return qc, qc_for_visual

def builder_quantum_teleportation():
    qc = QuantumCircuit(3, 3)
    qc.h(1)
    qc.cx(1, 2)
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [0, 1])
    qc.cx(1, 2)
    qc.cz(0, 2)
    qc_for_visual = qc.copy()
    qc.measure(2, 2)
    return qc, qc_for_visual

def builder_qft_circuit(n=3):
    qc = QuantumCircuit(n, n)
    qc.h(0)
    for i in range(1, n):
        qc.cp(3.1415 / 2**i, i, 0)
    qc.append(QFT(n), range(n))
    qc_for_visual = qc.copy()
    qc.measure(range(n), range(n))
    return qc, qc_for_visual

def builder_grover_circuit():
    qc = QuantumCircuit(2, 2)
    qc.h([0, 1])
    qc.cz(0, 1)
    qc.h([0, 1])
    qc_for_visual = qc.copy()
    qc.measure([0, 1], [0, 1])
    return qc, qc_for_visual

def builder_deutsch_jozsa():
    qc = QuantumCircuit(2, 2)
    qc.x(1)
    qc.h([0, 1])
    qc.cz(0, 1)
    qc.h(0)
    qc_for_visual = qc.copy()
    qc.measure([0, 1], [0, 1])
    return qc, qc_for_visual

def builder_qpe_circuit():
    qc = QuantumCircuit(3, 1)
    qc.h([0, 1])
    qc.cx(1, 2)
    qc.cx(0, 2)
    qc.append(QFT(2).inverse(), [0, 1])
    qc_for_visual = qc.copy()
    qc.measure(0, 0)
    return qc, qc_for_visual

def builder_coin_toss():
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc_for_visual = qc.copy()
    qc.measure(0, 0)
    return qc, qc_for_visual

def builder_bell_measurement():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc_for_visual = qc.copy()
    qc.measure([0, 1], [0, 1])
    return qc, qc_for_visual

def builder_swap_test():
    qc = QuantumCircuit(3, 1)
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(0, 2)
    qc.h(0)
    qc_for_visual = qc.copy()
    qc.measure(0, 0)
    return qc, qc_for_visual

def builder_w_state():
    qc = QuantumCircuit(3, 3)
    qc.ry(2.094, 0)
    qc.cx(0, 1)
    qc.ry(1.571, 1)
    qc.cx(1, 2)
    qc_for_visual = qc.copy()
    qc.measure([0, 1, 2], [0, 1, 2])
    return qc, qc_for_visual
