# 🧠 FRC-Augmented SIR Model

A network-based epidemic modelling framework that incorporates **Forman–Ricci curvature (FRC)** into edge-level transmission dynamics.

The repository contains the computational implementation and experimental notebooks used to investigate how local network structure and curvature-dependent transmission heterogeneity affect epidemic dynamics across synthetic and empirical contact networks.

---

## 🔬 Overview

Traditional network-SIR models represent transmission primarily through network connectivity and edge weights. This project extends that formulation by using **Forman–Ricci curvature** as a structural descriptor of individual edges.

The framework separates the baseline transmission scale from curvature-driven heterogeneity. For an edge \((i,j)\),

```text
βᵢⱼ = β₀ wᵢⱼ ĝα(F̃ᵢⱼ)
```

where:

- `β₀` is the baseline transmission parameter;
- `wᵢⱼ` is the normalized edge weight;
- `F̃ᵢⱼ` is standardized Forman–Ricci curvature;
- `α` controls the strength of curvature-dependent heterogeneity;
- `ĝα(·)` is a mean-normalized curvature-to-transmission mapping.

The normalization is designed so that the curvature modulation changes the **distribution of transmission across edges without unintentionally changing the weighted baseline transmission scale**.

---

## ✨ Key Features

- 🕸️ **Network-based SIR modelling**
- 📐 **Forman–Ricci curvature** computation on network edges
- 🔗 Support for weighted and unweighted networks
- 🧮 Standardization of edge-level curvature
- 🔄 Multiple curvature-to-transmission mappings:
  - Uniform
  - Linear
  - Exponential
  - Saturating
- 🎚️ Curvature-strength sensitivity analysis through `α`
- 📈 Baseline transmission sensitivity analysis through `β₀`
- 🎲 Repeated stochastic simulations with matched random seeds
- 📊 Epidemic outcome analysis using:
  - Peak infected
  - Peak time
  - Final epidemic size
  - Epidemic duration
- 📉 Uncertainty analysis and confidence intervals
- 🧪 Validation across multiple synthetic network topologies
- 🏫 Evaluation on an empirical high-school contact network
- 📦 Export of experiment summaries and figures for reproducibility

---

## 🕸️ Network Topologies

The synthetic experiments use four structurally distinct network families:

| Network | Structural role |
|---|---|
| **Erdős–Rényi (ER)** | Random, relatively homogeneous connectivity |
| **Watts–Strogatz (WS)** | Small-world structure and local clustering |
| **Barabási–Albert (BA)** | Hub-dominated scale-free connectivity |
| **Power-Law Cluster (PLC)** | Scale-free structure with enhanced clustering |

The synthetic experiments use approximately 1,000 nodes per network and compare the same network realization across competing model conditions.

---

## 🏫 Empirical Contact Network

The repository also contains an empirical-network experiment based on the **SocioPatterns high-school contact dataset**.

The aggregated contact network contains:

- **327 individuals**
- **5,818 undirected edges**
- **20-second temporal resolution** in the original contact records
- Contact duration as the primary edge-weight measure
- Maximum-weight normalization of edge weights

Because contact duration is directly proportional to the number of recorded 20-second contact intervals, duration and contact count are not treated as independent weighting sensitivities.

The empirical experiment is used as a **structural validation of the modelling mechanism**, not as predictive validation against an observed epidemic trajectory.

---

## 🧮 Model Formulation

### Standardized Forman–Ricci curvature

For an edge \(e=(i,j)\), the computed curvature is standardized before it is used to modulate transmission:

```text
F̃ᵢⱼ = (Fᵢⱼ − μF) / σF
```

This places curvature values on a common scale across network realizations.

### Curvature-to-transmission mappings

The framework evaluates several mappings.

#### 1. Uniform mapping

```text
g(x) = 1
```

This corresponds to the weighted Network-SIR baseline.

#### 2. Linear mapping

```text
g(x) = max(ε, 1 + αx)
```

A small positivity floor `ε` prevents non-positive transmission modifiers.

#### 3. Exponential mapping

```text
g(x) = exp(αx)
```

The exponential mapping provides a smooth multiplicative transformation of standardized curvature.

#### 4. Saturating mapping

```text
g(x) = 1 + tanh(αx)
```

This limits the magnitude of curvature-induced modulation.

### Mean-normalized modulation

For each mapping, the raw modifier is normalized so that its **edge-weighted mean equals one**:

```text
ĝα(Fᵢⱼ) =
    gα(F̃ᵢⱼ)
    ─────────────────────────────────────────────
    Σ₍ₖ,ₗ₎ wₖₗ gα(F̃ₖₗ) / Σ₍ₖ,ₗ₎ wₖ
```

The resulting transmission coefficient is therefore:

```text
βᵢⱼ = β₀ wᵢⱼ ĝα(F̃ᵢⱼ)
```

At `α = 0`, the modulation is exactly one and the model reduces to the weighted Network-SIR baseline:

```text
βᵢⱼ = β₀ wᵢⱼ
```

This makes `α` a direct control on curvature-driven transmission heterogeneity.

---

## 🧪 Experimental Design

The revised experimental workflow is organized into six experiments.

### Experiment 1: Structural characterization

Characterizes the four synthetic networks using:

- network size and edge count;
- degree;
- clustering;
- edge-level Forman–Ricci curvature;
- curvature distributions;
- relationships between curvature and classical network descriptors.

### Experiment 2: Network-SIR vs Curvature-SIR

Compares the weighted Network-SIR baseline with the curvature-aware formulation using the same network realization and stochastic simulation protocol.

### Experiment 3: Mapping robustness

Tests whether the observed epidemic response depends specifically on the exponential mapping by comparing:

- Uniform
- Linear
- Exponential
- Saturating

mappings under otherwise matched conditions.

### Experiment 4: Parameter sensitivity

Investigates:

- curvature strength `α`;
- baseline transmission `β₀`.

The current synthetic sensitivity grid includes:

```text
α = {0, 0.25, 0.5, 0.75, 1, 1.5, 2}
```

and:

```text
β₀ = {0.2, 0.3, 0.4, 0.5, 0.6}
```

### Experiment 5: tochastic variability

Uses repeated stochastic simulations to quantify variability in epidemic outcomes rather than relying on a single epidemic trajectory.

The revised synthetic experiments use **200 stochastic realisations** for the principal comparisons.

### Experiment 6: Empirical network validation

Applies the framework to the aggregated high-school contact network and evaluates:

- weighted Network-SIR vs Curvature-SIR;
- mapping robustness;
- curvature-strength sensitivity;
- stochastic outcome distributions;
- the operating behaviour of the positivity-constrained linear mapping.

---

## 📊 Main Epidemic Metrics

The experiments report four principal outcomes:

| Metric | Description |
|---|---|
| **Peak infected** | Maximum number of simultaneously infected individuals |
| **Peak time** | Time at which peak infection occurs |
| **Final epidemic size** | Total number of individuals infected by the end of the simulation |
| **Epidemic duration** | Time until the epidemic reaches extinction |

For stochastic experiments, distributions, standard deviations, and confidence intervals are also reported where appropriate.

---

## 📁 Repository Structure

The repository is organized around the curvature computation library and the experimental notebooks.

```text
FRC-Augmented-SIR-Model/
│
├── README.md
├── requirements.txt
├── LICENSE
│
├── frc_lib/
│   └── forman_ricci.py
│
├── notebook/
│   ├── FRC_SIR_Simulation.ipynb
│   └── aggregated_weighted_network_complete_revised.ipynb
│
└── data/
    ├── High-School_data_2013.csv
│   └── metadata_2013.txt
```

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/sowole-aims/FRC-Augmented-SIR-Model.git
cd FRC-Augmented-SIR-Model
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

For notebook-based execution, ensure that Jupyter is installed:

```bash
pip install jupyter
```

---

## ▶️ Usage

Launch Jupyter:

```bash
jupyter notebook
```

Then open the relevant notebook from the `notebook/` directory.

For the synthetic-network experiments, use the `FRC_SIR_Simulation` notebook.

For the empirical high-school contact-network experiment, use the `aggregated_weighted_network_complete_revised` notebook.

Before reproducing the manuscript results, run the notebook from the beginning so that the network realizations, random seeds, model configuration, and exported results remain internally consistent.

---

## 🔁 Reproducibility

The experiments use explicit random seeds and matched stochastic replicates for direct model comparisons.

Important reproducibility principles include:

1. **Freeze the network realization** before comparing model conditions.
2. Use the **same initialisation protocol** for competing models.
3. Use **matched random seeds** for paired comparisons where appropriate.
4. Keep the epidemiological parameters fixed when evaluating mapping robustness.
5. Record the curvature mapping and normalization used for every experiment.
6. Verify that `α = 0` reproduces the weighted Network-SIR baseline.
7. Export experiment configuration and summary results alongside figures.

These controls are intended to distinguish structural model effects from differences caused by network generation or Monte Carlo variability.

---

## 📈 Outputs

The analysis produces figures and tables for:

- synthetic-network structural characterisation;
- baseline vs curvature-aware epidemic dynamics;
- mapping robustness;
- curvature-strength sensitivity;
- baseline-transmission sensitivity;
- stochastic outcome distributions;
- uncertainty bands;
- empirical-network validation.

Representative output files include:

```text
experiment2_baseline_vs_curvature.png
experiment3_mapping_comparison.png
experiment4_alpha_peak.png
experiment4_alpha_final_size.png
experiment4_alpha_peak_time.png
experiment4_beta_peak.png
experiment5_peak_distributions.png
experiment5_uncertainty_bands.png

Figure_E6_Baseline_vs_Curvature_CI.png
Figure_E6_Alpha_Sensitivity.png
Figure_E6_Mapping_Robustness.png
Figure_E6_Boxplots.png
```

CSV exports contain the corresponding numerical experiment summaries.

---

## ⚠️ Scope and Limitations

The framework is intended to study the **structural role of network curvature in epidemic dynamics**.

The current experiments do **not** establish:

- predictive superiority over conventional epidemic models;
- an empirically validated universal curvature-to-transmission law;
- a universal epidemiological threshold;
- direct effectiveness of vaccination, contact tracing, mobility restrictions, or other interventions;
- real-time epidemic forecasting capability.

The empirical high-school experiment uses one aggregated contact network and does not calibrate the model against an observed epidemic trajectory.

The curvature-to-transmission mappings remain phenomenological. The mapping-robustness experiments show that the qualitative effect is not restricted to the exponential mapping, but they do not determine which mapping is epidemiologically correct.

---

## 📚 Publications

### Published work

The curvature-based epidemic modelling work has been published in *Mathematics*:

**Sowole, O. S., Bragazzi, N. L., & Lyakurwa, G. A. (2025).**  
*Analysing Disease Spread on Complex Networks Using Forman–Ricci Curvature.*  
**Mathematics, 13(23), 3742.**

DOI:

https://doi.org/10.3390/math13233742

The computational framework in this repository extends the earlier work with additional stochastic validation, alternative curvature-to-transmission mappings, parameter sensitivity analyses, and empirical contact-network experiments.

---

## 📖 Related Dataset

The empirical contact-network experiment uses the SocioPatterns high-school contact data described by:

> Fournet, J., & Barrat, A. (2014). Contact patterns among high school students. *PLoS ONE, 9*(9), e107878.

DOI:

https://doi.org/10.1371/journal.pone.0107878

The dataset is used for research purposes in accordance with its original distribution and licensing conditions.

---

## 📜 Citation

If you use this repository or the associated computational framework in your
research, please cite the following manuscript:

```bibtex
@article{Sowole2026CurvatureAwareSIR,
  author  = {Sowole, Oladimeji Samuel and Bragazzi, Nicola Luigi and Lyakurwa, Geminpeter A.},
  title   = {Integrating Network Curvature into Epidemic Dynamics: A Curvature-Aware SIR Model Framework},
  journal = {Complex Systems},
  year    = {2026},
  note    = {Manuscript submitted for publication}
}

For work specifically using the experimental implementation, please also cite this repository:

```bibtex
@misc{Sowole2026FRCRepository,
  author       = {Sowole, Oladimeji Samuel},
  title        = {FRC-Augmented-SIR-Model},
  year         = {2026},
  howpublished = {GitHub repository},
  url          = {https://github.com/sowole-aims/FRC-Augmented-SIR-Model}
}
```

---

## 📬 Contact

**Oladimeji Samuel Sowole**

- Email: `osowole@aimsric.org`
---

## 📄 License

This project is licensed under the **Apache License 2.0**.

See [`LICENSE`](LICENSE) for the full license text.
