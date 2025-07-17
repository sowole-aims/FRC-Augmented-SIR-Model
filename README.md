
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

For each edge \((u, v)\) in the network, transmission rate is modulated by the curvature:
\[
\beta_{uv} = \beta \cdot \exp(F_{uv}),
\]
where \(F_{uv}\) is the Forman-Ricci curvature of edge \((u,v)\).

Node states are updated using the discrete-time SIR formulation:
\[
S_v(t+1) = S_v(t) \sum_{u \in \mathcal{N}(v)} \left(1 - \beta_{uv} I_u(t) \right)
\]
\[
I_v(t+1) = S_v(t) \left[1 - \sum_{u \in \mathcal{N}(v)} \left(1 - \beta_{uv} I_u(t) \right) \right] + (1 - \gamma) I_v(t)
\]
\[
R_v(t+1) = R_v(t) + \gamma I_v(t)
\]

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
