# Machine Learning Problem Framing Guide

## Overview

Framing a machine learning (ML) problem is the most critical step in any ML project. It involves clearly defining the problem, understanding the data, and deciding the appropriate approach before building any model.

A well-framed problem ensures:

* Correct model selection
* Better performance
* Efficient use of time and resources

---

## Step 1: Understand the Business Problem

Start by clearly defining the objective.

### Ask:

* What problem are we solving?
* Why is it important?
* What is the expected outcome?

### Example:

* Predict house prices
* Detect spam emails
* Classify whether a student will be placed or not

---

## Step 2: Define Input and Output

Identify:

* **Input (Features / Independent Variables)** → What data you have
* **Output (Target / Dependent Variable)** → What you want to predict

### Example:

| Feature (X)               | Target (Y)         |
| ------------------------- | ------------------ |
| CGPA, Skills, Internships | Placement (Yes/No) |

---

## Step 3: Identify the Type of Problem

### 1️⃣ Classification

* Output is **categorical**
* Example: Yes/No, Spam/Not Spam

### 2️⃣ Regression

* Output is **continuous**
* Example: Salary prediction, house price

### 3️⃣ Clustering (Unsupervised)

* No labeled output
* Example: Customer segmentation

---

## Step 4: Check Data Availability

Ensure:

* Sufficient data is available
* Data is relevant and clean

### Consider:

* Missing values
* Data imbalance
* Noise in data

---

## Step 5: Define Evaluation Metrics

Choose how you will measure success.

### For Classification:

* Accuracy
* Precision
* Recall
* F1 Score

### For Regression:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

---

## Step 6: Understand Constraints

Identify limitations such as:

* Time constraints
* Computational power
* Real-time vs batch prediction
* Data privacy issues

---

## Step 7: Baseline Approach

Start with a simple model:

* Linear Regression
* Logistic Regression
* Decision Tree

This helps to:

* Set a benchmark
* Understand model performance

---

## Step 8: Feature Engineering Strategy

Think about:

* Which features are important?
* Can you create new features?
* Should you scale or normalize data?

---

## Step 9: Data Splitting Strategy

Split data into:

* Training set
* Testing set

Example (Python):

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

---

## Step 10: Iterate and Improve

Machine learning is iterative:

* Train → Evaluate → Improve → Repeat

---

## Example Problem Framing

### Problem:

Predict whether a student will be placed.

### Framing:

* Type: Classification
* Input: CGPA, Skills, Projects
* Output: Placed (Yes/No)
* Metric: Accuracy / F1 Score
* Model: Logistic Regression (baseline)

---

## Common Mistakes to Avoid

* ❌ Jumping to model building without understanding the problem
* ❌ Using wrong evaluation metrics
* ❌ Ignoring data quality issues
* ❌ Not defining a clear objective

---

