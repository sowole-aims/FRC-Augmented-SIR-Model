# FRC-Augmented SIR Model

A stochastic network-based epidemic modelling framework that incorporates **Forman–Ricci curvature (FRC)** into edge-level transmission dynamics.

This repository contains the computational implementation and experimental notebooks used to study how local network structure and curvature-dependent transmission heterogeneity affect epidemic dynamics across synthetic and empirical contact networks.

---

## Overview

Traditional network-SIR models represent transmission through network connectivity and, where available, edge weights. This framework extends the weighted Network-SIR formulation by using **Forman–Ricci curvature** as an edge-level structural descriptor.

For an edge $e_{ij}=(i,j)$, the curvature-aware transmission coefficient is

$$
\beta_{ij}
=
\beta_0\,w_{ij}\,
\widehat{g}_{\alpha}\!\left(\widetilde{F}_{ij}\right),
$$

where

- $\beta_0$ is the baseline transmission parameter;
- $w_{ij}$ is the normalized edge weight;
- $\widetilde{F}_{ij}$ is the standardized Forman–Ricci curvature;
- $\alpha$ controls the strength of curvature-dependent heterogeneity; and
- $\widehat{g}_{\alpha}(\cdot)$ is a mean-normalized curvature-to-transmission mapping.

The normalization is constructed so that curvature changes the **distribution of transmission intensity across edges without unintentionally changing the mean weighted transmission scale**.

---

## Key Features

- Network-based stochastic SIR modelling
- Edge-level Forman–Ricci curvature computation
- Weighted and unweighted network support
- Standardization of edge curvature
- Four curvature-to-transmission mappings:
  - Uniform
  - Linear
  - Exponential
  - Saturating
- Curvature-strength sensitivity through $\alpha$
- Baseline-transmission sensitivity through $\beta_0$
- Repeated stochastic simulations with matched random seeds
- Fixed-network and across-network-realisation uncertainty analysis
- Epidemic outcome analysis using peak prevalence, peak time, final epidemic size, and epidemic duration
- Evaluation on four synthetic network families
- Structural validation on an empirical high-school contact network
- Export of numerical summaries and figures for reproducibility

---

## Network Topologies

The synthetic experiments use four structurally distinct network families:

| Network | Structural role |
| --- | --- |
| **Erdős–Rényi (ER)** | Random, relatively homogeneous connectivity |
| **Watts–Strogatz (WS)** | Small-world structure with local clustering |
| **Barabási–Albert (BA)** | Hub-dominated scale-free connectivity |
| **Power-Law Cluster (PLC)** | Scale-free structure with enhanced triadic closure |

The principal synthetic experiments use approximately 1,000 nodes per network. Competing model conditions are evaluated on the same fixed network realisation. A separate experiment uses independent network realisations to quantify structural variability.

---

## Empirical Contact Network

The empirical analysis uses the **SocioPatterns high-school contact dataset**. After aggregating the temporal contacts, the resulting weighted network contains:

- **327 individuals**
- **5,818 undirected edges**
- contacts originally recorded at **20-second resolution**
- cumulative contact duration as the edge-weight measure
- edge weights normalized by the maximum observed contact duration

Because cumulative duration is directly proportional to the number of recorded 20-second contact intervals, contact duration and contact count are not treated as independent weighting sensitivities.

The empirical experiment is used as a **structural validation of the modelling mechanism**, not as predictive validation against an observed epidemic trajectory.

---

## Model Formulation

### 1. Standardized Forman–Ricci curvature

For each edge $e_{ij}$, the computed curvature $F_{ij}$ is standardized before being used to modulate transmission:


$$
\widetilde{F}_{ij}
=
\frac{F_{ij}-\mu_F}{\sigma_F},
$$

where $\mu_F$ and $\sigma_F$ are the mean and standard deviation of the edge-curvature distribution, respectively.

This transformation places curvature values on a common standardized scale.

### 2. Curvature-to-transmission mappings

Let

$$
x_{ij}=\widetilde{F}_{ij}.
$$

The framework evaluates four mappings.

#### Uniform

$$
g_{\alpha}(x)=1.
$$

This is the curvature-free weighted Network-SIR reference.

#### Linear

$$
g_{\alpha}(x)
=
\max\!\left(\varepsilon,\,1+\alpha x\right),
$$

where $\varepsilon>0$ is a small positivity floor that prevents non-positive transmission modifiers.

#### Exponential

$$
g_{\alpha}(x)
=
\exp(\alpha x).
$$

#### Saturating

$$
g_{\alpha}(x)
=
1+\tanh(\alpha x).
$$

The alternative mappings are used to assess whether the observed epidemic response depends critically on a particular curvature-to-transmission transformation.

### 3. Mean-normalized modulation

For weighted networks, the raw modifier is normalized by its edge-weighted mean:

$$
\widehat{g}_{\alpha}(x_{ij})
=
\frac{
g_{\alpha}(x_{ij})
}{
\displaystyle
\frac{
\sum_{(k,l)\in E} w_{kl}\,g_{\alpha}(x_{kl})
}{
\sum_{(k,l)\in E} w_{kl}
}
}.
$$

Equivalently,

$$
\frac{
\sum_{(i,j)\in E}
w_{ij}\widehat{g}_{\alpha}(x_{ij})
}{
\sum_{(i,j)\in E}w_{ij}
}
=1.
$$

For the unweighted synthetic networks, $w_{ij}=1$, so this reduces to ordinary arithmetic-mean normalization.

The edge-level transmission coefficient is then


$$
\boxed{
\beta_{ij}
=
\beta_0 w_{ij}
\widehat{g}_{\alpha}\!\left(\widetilde{F}_{ij}\right)
}.
$$

At \(\alpha=0\),

$$
\widehat{g}_{0}\!\left(\widetilde{F}_{ij}\right)=1,
$$

and therefore

$$
\beta_{ij}=\beta_0w_{ij},
$$

so the curvature-aware model is nested within the weighted Network-SIR baseline.

### 4. Infection probability

For a susceptible node $i$ connected to an infectious neighbour $j$, the one-step transmission probability is


$$
p_{ij}^{\mathrm{inf}}
=
1-\exp\!\left[
-\beta_0 w_{ij}
\widehat{g}_{\alpha}\!\left(\widetilde{F}_{ij}\right)
\Delta t
\right].
$$

For all infectious neighbours of $i$, the infection probability becomes


$$
p_i^{\mathrm{inf}}(t)
=
1-
\prod_{j\in\mathcal{N}(i)}
\left(1-p_{ij}^{\mathrm{inf}}\right)^{I_j(t)}.
$$

The stochastic implementation samples infection and recovery transitions as Bernoulli events.

---

## Experimental Design

The computational workflow is organized into six experiments.

### Experiment 1 — Structural Characterisation

Characterises the four synthetic network families using network size, edge count, degree, clustering, edge-level Forman–Ricci curvature, curvature distributions, and relationships between curvature and conventional network descriptors.

### Experiment 2 — Network-SIR vs Curvature-SIR

Compares the weighted Network-SIR baseline with the curvature-aware formulation under matched network structure, initialisation, epidemiological parameters, and stochastic seeds.

### Experiment 3 — Mapping Robustness

Compares the **uniform**, **linear**, **exponential**, and **saturating** mappings under otherwise matched conditions.

### Experiment 4 — Parameter Sensitivity

Curvature strength is evaluated over

$$
\alpha\in\{0,\;0.25,\;0.5,\;0.75,\;1,\;1.5,\;2\},
$$

and the synthetic baseline transmission parameter over

$$
\beta_0\in\{0.2,\;0.3,\;0.4,\;0.5,\;0.6\}.
$$

### Experiment 5 — Stochastic and Network-Realisation Variability

Two sources of uncertainty are evaluated separately:

1. **Within-network stochastic variability:** 200 stochastic epidemic realisations on each fixed synthetic network for the principal comparisons.
2. **Across-network-realisation variability:** 20 independent network realisations per topology, with 20 paired epidemic simulations on each network realisation.

This separation distinguishes epidemic-event variability conditional on a fixed network from variability caused by the generated network structure itself.

### Experiment 6 — Empirical High-School Network Validation

The empirical analysis evaluates:

- weighted Network-SIR versus Curvature-SIR;
- endpoint-strength control;
- endpoint-degree control;
- shuffled-FRC control;
- mapping robustness;
- curvature-strength sensitivity;
- stochastic outcome distributions; and
- clipping behaviour of the positivity-constrained linear mapping.

For each empirical model condition, the principal analysis uses **200 paired stochastic realisations**.

---

## Epidemic Outcome Metrics

The experiments report four principal outcomes:

| Metric | Definition |
| --- | --- |
| **Peak infected** | Maximum number of simultaneously infected individuals |
| **Peak time** | Time at which the infection peak occurs |
| **Final epidemic size** | Total number infected by the end of the simulation |
| **Epidemic duration** | Time from epidemic initiation until extinction |

For stochastic experiments, the analysis also reports uncertainty summaries such as means, standard deviations, distributions, and confidence intervals where appropriate.

---

## Repository Structure

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
    └── metadata_2013.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/sowole-aims/FRC-Augmented-SIR-Model.git
cd FRC-Augmented-SIR-Model
```

Install the required packages:

```bash
pip install -r requirements.txt
```

For notebook-based execution, install Jupyter if needed:

```bash
pip install jupyter
```

---

## Usage

Launch Jupyter:

```bash
jupyter notebook
```

Then open the appropriate notebook from `notebook/`:

- `FRC_SIR_Simulation.ipynb` — synthetic-network experiments
- `aggregated_weighted_network_complete_revised.ipynb` — empirical high-school contact-network experiments

For reproducibility, run the selected notebook from the beginning so that network generation, random seeds, model configuration, simulations, and exported outputs remain internally consistent.

---

## Reproducibility

The experiments use explicit random seeds and matched stochastic replicates where direct model comparisons are required.

Important reproducibility principles are:

1. Freeze the network realisation before comparing model conditions in fixed-network experiments.
2. Use the same initialisation protocol across competing models.
3. Use matched random seeds for paired comparisons.
4. Keep epidemiological parameters fixed when evaluating mapping robustness.
5. Record the curvature mapping and normalization used in each experiment.
6. Verify that \(\alpha=0\) reproduces the weighted Network-SIR baseline.
7. Treat fixed-network stochastic variability separately from across-network-realisation variability.
8. Export experiment configuration and numerical summaries alongside figures.

These controls help distinguish curvature-dependent structural effects from differences caused by network generation or Monte Carlo variability.


---

## Scope and Limitations

This framework is designed to investigate the **structural role of network curvature in epidemic dynamics**.

The current experiments do **not** establish:

- predictive superiority over conventional epidemic models;
- a universally valid curvature-to-transmission relationship;
- independence of Forman–Ricci curvature from conventional network statistics;
- a universal epidemiological threshold;
- the effectiveness of specific interventions such as vaccination or contact tracing; or
- real-time epidemic forecasting capability.

For the unweighted synthetic networks, Forman–Ricci curvature is deterministically related to endpoint degree. The synthetic experiments should therefore be interpreted as analyses of the curvature-based transmission construction across different network architectures, rather than evidence that curvature provides information independent of degree.

The empirical analysis uses one aggregated high-school contact network and does not calibrate the model against an observed epidemic trajectory. It is therefore interpreted as a structural sensitivity analysis rather than predictive validation.

The curvature-to-transmission mappings are phenomenological. Mapping-robustness experiments test sensitivity to the assumed functional form but do not determine which mapping is epidemiologically correct.

---

## Publications

### Published Work

**Sowole, O. S., Bragazzi, N. L., & Lyakurwa, G. A. (2025).**  
*Analysing Disease Spread on Complex Networks Using Forman–Ricci Curvature.*  
**Mathematics, 13**(23), 3742.  
DOI: https://doi.org/10.3390/math13233742

The computational framework in this repository extends the earlier work through additional stochastic validation, alternative curvature-to-transmission mappings, parameter-sensitivity analyses, and empirical contact-network experiments.

---

## Related Dataset

The empirical contact-network experiment uses the SocioPatterns high-school contact data described by:

> Fournet, J., & Barrat, A. (2014). Contact patterns among high school students. *PLoS ONE, 9*(9), e107878. https://doi.org/10.1371/journal.pone.0107878

The dataset is used for research purposes in accordance with its original distribution and licensing conditions.

---

## Citation

If you use this repository or the associated computational framework in your research, please cite the manuscript:

```bibtex
@article{Sowole2026CurvatureAwareSIR,
  author  = {Sowole, Oladimeji Samuel and Bragazzi, Nicola Luigi and Lyakurwa, Geminpeter A.},
  title   = {Integrating Network Curvature into Epidemic Dynamics: A Curvature-Aware SIR Model Framework},
  journal = {Complex Systems},
  year    = {2026},
  note    = {Manuscript submitted for publication}
}
```

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

## Contact

**Oladimeji Samuel Sowole**  
Email: `osowole@aimsric.org`

---

## License

This project is licensed under the **Apache License 2.0**. See [`LICENSE`](LICENSE) for the full license text.
