import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# --- Data ---
df = pd.read_csv('data.csv')

# --- Classification ---
# 1. Define what counts as "Big"
# HDB types are usually: '1 ROOM', '2 ROOM', '3 ROOM', '4 ROOM', '5 ROOM', 'EXECUTIVE'
big_flats = ['5 ROOM', 'EXECUTIVE', 'MULTI-GENERATION']

# 2. Create the Binary Target (The "Switch")
# If it's in the list -> 1. If not -> 0.
df['is_Big_Flat'] = df['flat_type'].apply(lambda x: 1 if x in big_flats else 0)

# 3. Now you have your X and y!
X = df[['resale_price']] # Input
y = df['is_Big_Flat']    # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# --- Train model ---
model = LogisticRegression(max_iter=1000) # max_iter prevents timeout on complex data
model.fit(X_train, y_train)

# --- Evaluation ---
y_pred = model.predict(X_test)

print("--- Model Performance ---")
print(f"Accuracy: {metrics.accuracy_score(y_test, y_pred):.2%}")
print(f"Confusion Matrix:\n {metrics.confusion_matrix(y_test, y_pred)}")
print("-" * 40)

# --- Confusion Matrix ---
plt.figure(figsize=(6, 5))
sns.heatmap(metrics.confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.title('Did the model guess right?')
plt.xlabel('Predicted (0=Not Big, 1=Big)')
plt.ylabel('Actual (0=Not Big, 1=Big)')
plt.show()

# --- Probability Curve ---
plt.figure(figsize=(8, 6))
sns.regplot(x=df['resale_price'], y=df['is_Big_Flat'], logistic=True, ci=None, scatter_kws={'color': 'black'}, line_kws={'color': 'red'})
plt.title('Probability of being a big flat vs. Price')
plt.xlabel('Price')
plt.ylabel('Probability of big flat (0 to 1)')
plt.show()