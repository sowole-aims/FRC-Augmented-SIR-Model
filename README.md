# 🧠 FRC-Augmented SIR Model

This repository contains the implementation of a **network-based SIR epidemic model** that incorporates **Forman-Ricci Curvature (FRC)** to modulate transmission rates over edges. It explores how network geometry influences disease spread dynamics.

---

## 📌 Key Features

- 📊 Simulates disease dynamics on multiple network topologies:
  - Erdős–Rényi
  - Watts–Strogatz
  - Barabási–Albert
  - Power-law Cluster
- 🌐 Integrates Forman-Ricci curvature to modulate edge-based transmission
- 📈 Visualizes SIR dynamics and infection curves over time
- 🧪 Supports both **sum-based** and **product-based** discrete SIR formulations

---

## 🧪 Model Description

For each edge \((u, v)\) in the network, transmission rate is modulated by the curvature:

```
β_{uv} = β ⋅ exp(F_{uv})
```

where `F_{uv}` is the Forman-Ricci curvature of edge \((u,v)\).

Node states are updated using the discrete-time SIR formulation:

```
S_v(t+1) = S_v(t) ⋅ ∑_{u ∈ N(v)} (1 - β_{uv} ⋅ I_u(t))
I_v(t+1) = S_v(t) ⋅ [1 - ∑_{u ∈ N(v)} (1 - β_{uv} ⋅ I_u(t))] + (1 - γ) ⋅ I_v(t)
R_v(t+1) = R_v(t) + γ ⋅ I_v(t)
```

---

## 📁 Repository Structure

```text
FRC-Augmented-SIR-Model/
│
├── README.md                  # Project documentation
├── requirements.txt           # Required dependencies
├── LICENSE                    # Project license
│
├── frc_lib/
│   ├── forman_ricci.py        # FRC computation module
│
├── notebook/
│   ├── FRC_SIR_Simulation.ipynb  # Simulation and visualization notebook
```

---

## 🛠️ Installation

```bash
git clone https://github.com/sowole-aims/FRC-Augmented-SIR-Model.git
cd FRC-Augmented-SIR-Model
pip install -r requirements.txt
```

---

## 📊 Usage

Run Jupyter notebooks to simulate the models:

```bash
cd notebook/
jupyter notebook FRC_SIR_Simulation.ipynb
```

---

## 📚 Citation

If you use this code, please cite the paper:

```
@inproceedings{Sowole2025,
  author    = {Oladimeji Samuel Sowole, Nicola Luigi Bragazzi and Geminpeter A. Lyakurwa},
  title     = {Integrating Network Curvature into Epidemic Dynamics: A Curvature-Aware SIR Model Framework},
  booktitle = {Deep Learning Indaba, 2025},
  year      = {2025}
}
```

---

## 🤝 Acknowledgements

This work will be presented at the **Deep Learning Indaba 2025** conference. We acknowledge the AIMS Research Innovation Centre, Kigali, Rwanda for supporting this study.

---

## 📬 Contact

- 📧 Oladimeji Samuel Sowole — `osowole@aimsric.org`
- 🌍 [Website](https://aimsric.org)

---

## 📄 License

This project is licensed under the Apache 2.0 License.
