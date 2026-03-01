# Data Cleaning & Preprocessing – Interview-Level Deep Notes

(Data Cleaning is 70–80% of real Data Science work.)

If you cannot clean data properly, model performance does not matter.

This document covers deep, interview-focused concepts required before moving to modeling.

---

# 1. What is Data Cleaning?

Data Cleaning is the process of:

* Identifying incorrect, inconsistent, incomplete, or irrelevant data
* Fixing structural issues
* Making the dataset analysis-ready

Goal:

Transform raw, messy data → structured, reliable input for analysis or modeling.

---

# 2. Types of Data Quality Issues

In interviews, you must know common categories of data problems:

1. Missing values
2. Duplicate records
3. Inconsistent formatting
4. Incorrect data types
5. Outliers
6. Invalid entries
7. Inconsistent categorical labels
8. Structural errors

You should always ask:

* Is the dataset reliable?
* Are there hidden inconsistencies?

---

# 3. Missing Values (Most Common Problem)

## Types of Missingness

Interview-level concept:

1. MCAR – Missing Completely At Random
   Missingness independent of data

2. MAR – Missing At Random
   Missingness related to other features

3. MNAR – Missing Not At Random
   Missingness depends on the value itself

Understanding missing type impacts imputation strategy.

---

## Identifying Missing Values

In Pandas:

* df.isnull()
* df.isna()
* df.info()

Important:

Missing values may appear as:

* NaN
* None
* Empty strings
* Placeholder values ("NA", "-999")

Always standardize them first.

---

## Handling Missing Data

### 1. Deletion

* Row deletion (dropna)
* Column deletion

Use when:

* Missing % is very small
* Feature not important

Risk:

Losing important information.

---

### 2. Imputation

Common methods:

* Mean
* Median
* Mode
* Forward fill
* Backward fill

Interview Insight:

Median preferred when outliers exist.

---

### 3. Model-Based Imputation

* KNN imputation
* Regression-based filling

Used when:

* Feature important
* Missingness is significant

---

# 4. Duplicate Handling

Duplicates cause:

* Inflated counts
* Biased statistics

Types:

* Exact duplicates
* Partial duplicates

In Pandas:

* df.duplicated()
* df.drop_duplicates()

Interview Tip:

Always verify business logic before removing duplicates.

---

# 5. Data Type Correction

Incorrect data types cause silent bugs.

Examples:

* Numbers stored as strings
* Dates stored as objects

Common conversions:

* astype()
* to_datetime()
* to_numeric()

Interview Question Example:

"Why is object dtype dangerous?"

Because it prevents vectorized numerical operations and increases memory usage.

---

# 6. Handling Outliers

Outliers can distort:

* Mean
* Standard deviation
* Model training

## Detection Methods

1. IQR Method
   Q1 - 1.5*IQR
   Q3 + 1.5*IQR

2. Z-score method

3. Domain-based rules

Interview Insight:

Do not blindly remove outliers. Understand domain context.

---

# 7. Inconsistent Categorical Labels

Example:

* "India"
* "india"
* "IND"

Fix by:

* Lowercasing
* Stripping whitespace
* Mapping standardized values

Interview Tip:

Category inconsistency leads to incorrect grouping results.

---

# 8. Feature Scaling (Preprocessing for Models)

Important for:

* Distance-based algorithms
* Gradient descent optimization

Methods:

1. Standardization (Z-score)
2. Min-Max Scaling

Interview Insight:

Tree-based models do not require scaling.

---

# 9. Encoding Categorical Variables

Models cannot understand text.

Common techniques:

1. Label Encoding
2. One-Hot Encoding
3. Target Encoding

Interview Insight:

* Avoid label encoding for nominal categories.
* One-hot can cause dimensional explosion.

---

# 10. Handling Imbalanced Data

In classification problems:

* One class may dominate

Solutions:

* Oversampling
* Undersampling
* SMOTE
* Class weighting

Interview Insight:

Accuracy is misleading for imbalanced datasets.

---

# 11. Data Leakage (Critical Interview Topic)

Definition:

Using information during training that would not be available at prediction time.

Examples:

* Using target variable for imputation
* Scaling entire dataset before train-test split

Interview Insight:

Always split before preprocessing.

---

# 12. Train-Test Split Order

Correct order:

1. Split data
2. Fit preprocessing on training set
3. Apply same transformation to test set

Never fit on full dataset.

---

# 13. Pipeline Thinking

Professional workflow:

* Cleaning
* Transformation
* Scaling
* Encoding
* Model training

Use pipelines to:

* Ensure reproducibility
* Prevent leakage
* Maintain consistency

---

# 14. Real-World Data Cleaning Mindset

Ask these in interview:

* What assumptions does this dataset violate?
* Are missing values random?
* Are there hidden duplicates?
* Are there data entry inconsistencies?
* Is there leakage?

Data cleaning is not mechanical.
It is investigative.

---

# 15. Common Interview Questions

1. How do you handle missing values?
2. What is data leakage?
3. When would you remove outliers?
4. How do you treat categorical variables?
5. How do you detect duplicates?
6. What is the difference between scaling and normalization?
7. Why split before preprocessing?

You must answer with reasoning, not just definitions.

---

# Final Takeaway

Data Cleaning determines:

* Model reliability
* Generalization
* Interpretability
* Business trust

Advanced models cannot fix bad data.

Strong data cleaning skills separate beginners from real Data Scientists.

