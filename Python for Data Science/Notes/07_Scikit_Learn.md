# Scikit-Learn – Machine Learning Workflow, Internals & Interview-Level Notes

Scikit-learn is not just a modeling library.

It provides a structured, consistent framework for:

* Data preprocessing
* Model training
* Evaluation
* Validation
* Pipeline construction

Understanding Scikit-learn deeply means understanding the full ML lifecycle.

---

# 1. Philosophy of Scikit-Learn

Core design principles:

* Consistent API (fit, predict, transform)
* Estimator abstraction
* Separation of training and inference
* Composability via Pipelines

Every estimator follows this pattern:

model = Model()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

This consistency is one of the biggest strengths of scikit-learn.

---

# 2. Types of Problems

## Supervised Learning

* Regression (continuous target)
* Classification (categorical target)

## Unsupervised Learning

* Clustering
* Dimensionality reduction

Interview insight:

Always identify problem type before choosing algorithm.

---

# 3. Train-Test Split

Purpose:

* Evaluate generalization
* Prevent overfitting illusion

Correct order:

1. Split data
2. Fit preprocessing on training set
3. Transform test set using training parameters

Never preprocess before splitting.

---

# 4. Core Workflow

1. Data cleaning
2. Feature engineering
3. Train-test split
4. Model selection
5. Model training
6. Evaluation
7. Hyperparameter tuning
8. Cross-validation

Interview tip:

Explain the workflow before naming algorithms.

---

# 5. Regression Models

Common algorithms:

* Linear Regression
* Ridge (L2 regularization)
* Lasso (L1 regularization)
* Decision Tree Regressor
* Random Forest Regressor

Interview depth:

## Regularization

Purpose:

* Prevent overfitting
* Penalize large coefficients

L1 → feature selection effect
L2 → coefficient shrinkage

---

# 6. Classification Models

Common algorithms:

* Logistic Regression
* K-Nearest Neighbors
* Decision Tree
* Random Forest
* Support Vector Machine
* Gradient Boosting

Interview insight:

Know bias-variance behavior of each model.

---

# 7. Model Evaluation – Regression

Common metrics:

* MAE
* MSE
* RMSE
* R²

Interview insight:

RMSE penalizes large errors more heavily.

R² explains variance captured by model.

---

# 8. Model Evaluation – Classification

Metrics:

* Accuracy
* Precision
* Recall
* F1-score
* ROC-AUC
* Confusion Matrix

Interview depth:

Accuracy is misleading for imbalanced data.

Precision vs Recall tradeoff depends on business context.

Example:

Fraud detection → prioritize recall.
Spam detection → balance precision and recall.

---

# 9. Cross-Validation

Purpose:

* More reliable performance estimate
* Reduce variance of evaluation

Types:

* K-Fold
* Stratified K-Fold
* Leave-One-Out

Interview insight:

Stratified K-Fold preferred for classification problems.

---

# 10. Hyperparameter Tuning

Methods:

* GridSearchCV
* RandomizedSearchCV

Key idea:

Hyperparameters are not learned from data directly.

They control learning behavior.

Interview tip:

Explain difference between parameter and hyperparameter.

---

# 11. Pipelines

Pipeline ensures:

* Clean workflow
* No data leakage
* Reproducibility

Example steps:

* Scaling
* Encoding
* Model training

Interview insight:

Pipelines prevent fitting transformations on test data.

---

# 12. Feature Scaling in Scikit-Learn

Common scalers:

* StandardScaler
* MinMaxScaler

Important:

Tree-based models do not require scaling.

Distance-based models do.

---

# 13. Handling Categorical Variables

Tools:

* OneHotEncoder
* LabelEncoder

Interview insight:

Never use LabelEncoder on input categorical features in most cases.

It creates artificial ordinal relationships.

---

# 14. Bias-Variance Tradeoff

High bias:

* Underfitting
* Model too simple

High variance:

* Overfitting
* Model too complex

Goal:

Balance bias and variance.

Interview answer should include:

Cross-validation and regularization.

---

# 15. Overfitting & Underfitting

Detect via:

* Train vs test performance comparison

High train accuracy + low test accuracy → overfitting

Low train + low test → underfitting

---

# 16. Feature Importance

Available in:

* Tree-based models
* Permutation importance

Used for:

* Model interpretability
* Feature selection

Interview insight:

Correlation does not imply importance.

---

# 17. Data Leakage (Critical)

Occurs when:

* Future information used in training
* Target-related transformation applied before split

Always use pipelines.

---

# 18. Common Interview Questions

1. Difference between L1 and L2 regularization?
2. When would you use ROC-AUC?
3. How do you handle imbalanced datasets?
4. What is cross-validation?
5. How do you detect overfitting?
6. Why use pipelines?
7. How do you select features?

Answers must include reasoning and real scenarios.

---

# Final Takeaway

Scikit-learn is not about memorizing algorithms.

It is about understanding:

* Problem framing
* Evaluation strategy
* Bias-variance tradeoff
* Reproducibility
* Leakage prevention

Strong ML understanding = structured thinking, not tool memorization.

