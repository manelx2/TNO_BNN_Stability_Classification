# Probabilistic Stability Prediction of Trans-Neptunian Objects

This repository presents a study on predicting the long-term dynamical stability of Trans-Neptunian Objects (TNOs) using Bayesian Neural Networks (BNNs). The goal is to provide fast, uncertainty-aware stability estimates that complement traditional N-body simulations.

The approach formulates orbital stability as a probabilistic binary classification problem (stable vs. unstable), trained on synthetic datasets generated with REBOUND N-body integrations over 10⁶-year timescales. The trained models are then applied to real objects from the Minor Planet Center (MPC) catalog.

Two Bayesian deep-learning methods are explored and compared:
- Monte Carlo Dropout
- Bayes by Backpropagation (BBB)

Both models produce predictive probabilities as well as epistemic uncertainty estimates (mean, standard deviation, predictive entropy), making the framework suitable as a screening tool to identify borderline or high-risk objects that merit further dynamical analysis.

The method significantly reduces computational cost compared to full N-body simulations, while retaining physically meaningful trends in orbital parameter space.

Full paper available here:  
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5555072

## Main Features
- Bayesian classification of TNO stability
- Training on REBOUND-simulated orbital data
- Application to real MPC catalogs
- Uncertainty-aware predictions for catalog-level analysis
- Comparison with existing machine-learning approaches in celestial mechanics

## Tools
- Python / PyTorch
- REBOUND N-body simulations
- Bayesian Neural Networks (MC Dropout, BBB)
