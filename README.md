Determinants of default and probability of default in loan by survival time analysis and statistical Machine Learning algorithms in python.
In this project, I have estimated default of loan by Machine Learning algorithm such as Logistic Regression and Cox regression analysis for loans survival time by Python. As well as I used Python for estimating Pearson correlation and point biserial correlation coefficients among continuous explanatory variables and discrete variables. In addition, I have used Pandas, Numpy, Scipy.stats, seaborn and Matplotlib.pyplot for preprocessing and EDA for data which includes 58 variables and more than 5000 rows. The complete result of my work is available as PDF format.
# LoanDefaultProbability
Predicting loan default using survival time analysis and statistical machine learning.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)]()
[![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-orange.svg)]()

---

## 📌 Overview
This project explores the **determinants of loan default** and estimates the **probability of default (PD)** using:

- **Survival Time Analysis** (Cox Proportional Hazards Model using `lifelines`)
- **Statistical Machine Learning Models** (e.g., Logistic Regression)
- **Exploratory Data Analysis (EDA)** of borrower and loan-risk factors  
- **Feature engineering** for financial risk modeling  

The main goal is to understand *which borrower attributes drive default risk* and *how default probability evolves over time*.

---

## 📁 Project Structure

LoanDefaultProbability/
│
├── data/ # Loan dataset (not included in repo)
├── notebooks/
│ ├── survival_analysis.ipynb # Cox PH model, duration, event definitions
│ ├── ml_default_prediction.ipynb # ML modeling and evaluation
│ ├── eda.ipynb # EDA + data visualization
│
├── README.md # This file
└── requirements.txt # Python dependencies
This project is implemented entirely in **Python** using **Jupyter Notebooks**.

Key libraries:

| Purpose | Libraries |
|--------|-----------|
| Survival analysis | `lifelines` |
| Machine learning | `scikit-learn` |
| Data processing | `pandas`, `numpy` |
| Visualization | `matplotlib`, `seaborn` |
| Notebook environment | Jupyter |
This project is implemented entirely in **Python** using **Jupyter Notebooks**.\

Methodogy:
1. Exploratory Data Analysis (EDA)
* Distributions of loan features

* Relationship between interest rate, grade, home ownership, purpose, etc.

* Chi-square tests for categorical variables

* Correlation heatmaps

3. Survival Time Analysis
* Using the Cox Proportional Hazards Model (lifelines):

* Define duration (time until default or full payment)

* Define event (default = 1, censored = 0)

* Estimate hazard ratios of loan determinants

* Plot survival curves and hazard functions

5. Machine Learning
Models used:

* Logistic Regression

Evaluation metrics:

* Accuracy

* Precision, Recall

* Confusion matrix

Results Summary
Key insights commonly found in this type of analysis:

* Higher interest rates, DTI, and lower income significantly increase default hazard.

* Certain loan purposes (e.g., small business, debt consolidation) show higher risk.

Contributing
Pull requests are welcome!

If you plan significant changes, please open an issue first to discuss the update.

Contact
For questions or collaboration:
<f.jabbari74@gmail.com>


