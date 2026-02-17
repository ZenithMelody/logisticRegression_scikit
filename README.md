# 🏘️ SG Housing size against price prediction via Logistic Regression (with Scikit-Learn)

## ✨ What does it do?
* **Problem:** Using the dataset it will predict if a flat is big (5 and above) or not (4 rooms or less)
* **Finding:** Price is a massive predictor of Size
* **Accuracy:** 80%

## 🚩 Issues & Solution
* **Reading:** My first time working with a confusion matrix so I did not know what the data meant.
* **Fix:** I wrote a guide to accompany the visuals 

## 🛠️ Tech Stack
* **Language:** Python 3.11/9
* **Library:** 
  * `scikit-learn`
  * `pandas` and `numpy` (data manipulation)
  * `matplotlib` and `seaborn` (data visualization)
* **Algorithm:** Logistic Regression

## 🩹 Future Updates
- [ ] Maybe let it factor in other variables e.g inlcude location as a feature to reduce false positives (i.e distinguishing expensive small flats in specific areas)
- [ ] Improvements on the graphs for easier readability

## 🚀 How to Run

### Prerequisites
Ensure you have Python installed. You can install the required libraries using pip:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```
  
## 📊 Visuals
*Accuaracy & Confusion Matrix*

<img width="187" height="91" alt="{56F3876B-BDA1-4A5B-B33C-8C7658758C01}" src="https://github.com/user-attachments/assets/5687ec4f-820b-42c3-b9dd-126d706b1d69" />

## 1. Confusion Matrix
| Location  | Meaning |
| ------------- | ------------- |
| Top Left (9895)  | correctly identified small flats ((3-room/4-room) |
| Bottom Right (2741)  | correctly identified big flats (5-room/Exec) |
| False Positives (930)  | expensive + small flats, model thought it was ""big" due to price (maybe it was in a prime location |
| False Negatives (2095)  | cheap + big flat, model thought it was "small" due to price (maybe non-mature estate) |
<img width="1083" height="1177" alt="{D234706F-C41E-4F7C-AAB4-5B7A2A3838C9}" src="https://github.com/user-attachments/assets/ff83dd1e-438d-4c91-82fe-37755aff8ff9" />


## 2. "S" Curve
| Location  | Meaning |
| ------------- | ------------- |
| "Floor" (left) | model is certain - if cheap = not big |
| "Ceiling" (Right) | model is certain - if expensive = big |
| "Tipping Point" (Middle) | decision boundary - if flat is $550K, model is on the fence. If $600k it decides it's big |
<img width="1088" height="1151" alt="{8439A247-F5A9-4216-BBB1-62A351AC5F0E}" src="https://github.com/user-attachments/assets/399f393b-0091-45d7-bb5c-f504c6a9701a" />
