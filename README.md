# 🧠 Quantum Circuit Explorer

An interactive **Streamlit** web app for building, simulating, and visualizing quantum circuits using **Qiskit**. Pick from a library of classic quantum algorithms and demonstrations, tune parameters live, and instantly see the circuit diagram, measurement histogram, and Bloch sphere representation.

---

## Visit

- 🔗 **Live App:** https://huggingface.co/spaces/mrkhan393/Quantum_Circuit_Explorer_App
- 📦 **Repository:** https://github.com/mrkhan393/Quantum-Circuit-Explorer

---

## ✨ Features

- **12 built-in quantum circuits**, including:
  - Bell State
  - GHZ State
  - Superposition
  - Custom Circuit (adjustable Rx / Ry / Rz gates)
  - Quantum Teleportation
  - Quantum Fourier Transform (QFT)
  - Grover's Algorithm
  - Deutsch–Jozsa Algorithm
  - Quantum Phase Estimation (QPE)
  - Quantum Coin Toss
  - Bell-State Measurement
  - SWAP Test
  - W-State
- **Adjustable parameters** — number of qubits, shot count, and custom rotation gate angles (Rx, Ry, Rz) via the sidebar
- **Live circuit diagram** rendering
- **Measurement histogram** from a simulated run (via Qiskit Aer)
- **Bloch sphere visualization** for circuits with up to 3 qubits
- Clean, single-page interactive UI powered by Streamlit

---

## 🖥️ Tech Stack

| Component        | Technology                     |
|-------------------|--------------------------------|
| UI Framework      | [Streamlit](https://streamlit.io/) |
| Quantum Computing  | [Qiskit](https://www.ibm.com/quantum/qiskit) |
| Simulation Backend | [Qiskit Aer](https://qiskit.github.io/qiskit-aer/) |
| Visualization      | Matplotlib, Qiskit Visualization |
| Deployment         | Hugging Face Spaces |

---

## 📂 Project Structure

```
Quantum-Circuit-Explorer/
├── app.py                     # Main Streamlit application
├── explorer/
│   ├── builder.py             # Functions that build each quantum circuit
│   └── simulator.py           # Circuit simulation and histogram plotting
├── requirements.txt           # Python dependencies
└── .huggingface.yaml          # Hugging Face Spaces configuration
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/mrkhan393/Quantum-Circuit-Explorer.git
cd Quantum-Circuit-Explorer

# (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run locally

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 🎛️ How to Use

1. Choose a **Circuit Type** from the sidebar (Bell, GHZ, QFT, Grover's, etc.).
2. Adjust **Qubits** and **Shots** using the sliders.
3. For the **Custom** circuit, tune the **Rx**, **Ry**, and **Rz** rotation angles.
4. View the generated **circuit diagram**, the **measurement result histogram**, and (for small circuits) the **Bloch sphere**.

---

## 🧩 Available Circuits

| Circuit | Description |
|---|---|
| Bell | Creates a 2-qubit maximally entangled Bell pair |
| GHZ | Generalized multi-qubit entangled GHZ state |
| Superposition | Puts all qubits into equal superposition with Hadamard gates |
| Custom | User-defined Rx/Ry/Rz rotations followed by entanglement |
| Quantum Teleportation | Demonstrates teleporting a qubit's state using entanglement and classical communication |
| QFT | Quantum Fourier Transform circuit |
| Grover's Algorithm | Simplified 2-qubit Grover search demonstration |
| Deutsch–Jozsa | Classic algorithm distinguishing constant vs. balanced functions |
| Quantum Phase Estimation | Estimates the phase of a unitary operator |
| Quantum Coin Toss | Single-qubit Hadamard-based random bit generator |
| Bell-State Measurement | Bell state with explicit measurement demonstration |
| SWAP Test | Tests similarity between two quantum states |
| W-State | Generates a 3-qubit W entangled state |

---

## 🌐 Deployment

This app is deployed on **Hugging Face Spaces** using the Streamlit SDK. Configuration lives in `.huggingface.yaml`:

```yaml
sdk: streamlit
app_file: app.py
```

To deploy your own copy, push this repository to a new Hugging Face Space (Streamlit SDK) or connect your GitHub repo directly to a Space.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source. Add your preferred license (e.g., MIT) here.

---

## 🙏 Acknowledgments

- Built with [Qiskit](https://www.ibm.com/quantum/qiskit) by IBM Quantum
- UI powered by [Streamlit](https://streamlit.io/)
- Hosted on [Hugging Face Spaces](https://huggingface.co/spaces)
