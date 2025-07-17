
# 🧠 FRC-Augmented SIR Model

This repository contains the implementation of a **network-based SIR model** that integrates **Forman-Ricci Curvature (FRC)** into the disease transmission process. The approach enhances classical epidemiological modeling by incorporating **geometric features of complex networks**, enabling more accurate and topology-aware simulations.

---

## 📌 Highlights

- ✅ Curvature-aware SIR simulation on network models (Erdős–Rényi, Watts–Strogatz, Barabási–Albert, Power-law Cluster)
- ✅ **Sum-based** discrete-time dynamics
- ✅ Computation of **Forman-Ricci curvature** on undirected graphs
- ✅ Visualizations of infection spread across various topologies
- ✅ Modular Python scripts & Jupyter notebook for full reproducibility

---

## 🧪 Model Description

This model augments the classical SIR model by incorporating Forman-Ricci curvature to modulate transmission rates over a network.

For each edge `(u, v)` in the network, the transmission rate is adjusted based on curvature as follows:

```

β\_uv = β · exp(F\_uv)

```

Where:

- `β` is the base transmission rate,
- `F_uv` is the Forman-Ricci curvature of the edge `(u, v)`,
- `β_uv` is the effective (curvature-adjusted) transmission rate.


The model simulates a **discrete-time network-based SIR process**. Each node `v` updates its state over time `t` as follows:

```

S\_v(t+1) = S\_v(t) · ∑\_{u ∈ N(v)} \[1 - β\_uv · I\_u(t)]

I\_v(t+1) = S\_v(t) · \[1 - ∑\_{u ∈ N(v)} (1 - β\_uv · I\_u(t))] + (1 - γ) · I\_v(t)

R\_v(t+1) = R\_v(t) + γ · I\_v(t)

```

Where:

- `S_v(t)`, `I_v(t)`, and `R_v(t)` are the probabilities of node `v` being Susceptible, Infected, or Recovered at time `t`, respectively.
- `γ` is the recovery rate.
- `N(v)` is the set of neighboring nodes of `v`.

This formulation allows curvature to dynamically influence transmission pathways, highlighting the role of network geometry in the spread of epidemics.
```


---

## 📁 Repository Structure

```
FRC-Augmented-SIR-Model/
│
├── README.md
├── requirements.txt
├── LICENCE
│
├── frc_lib/
│   ├── forman_ricci.py          # FRC computation
│
├── notebook/
│   ├── FRC_SIR_Simulation.ipynb

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
