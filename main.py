import pandas as pd
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load sample dataset (replace with your CSV path)
df = pd.read_csv('data/sample_traffic.csv')

# Basic preprocessing
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
# For demo: assume feature set exists; adjust to your dataset columns
X = df[numeric_cols[:-1]]
y = df['label']

# Train / test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Isolation Forest (unsupervised anomaly detection)
iso = IsolationForest(contamination=0.1, random_state=42)
iso.fit(X_train)

# Random Forest (supervised classification)
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Predictions
y_pred = rf.predict(X_test)

# Metrics
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average='weighted', zero_division=0))
print("Recall:", recall_score(y_test, y_pred, average='weighted', zero_division=0))
print("F1:", f1_score(y_test, y_pred, average='weighted', zero_division=0))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred, labels=sorted(y.unique()))
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.tight_layout()
plt.savefig('outputs/confusion_matrix.png')
plt.close()

# Anomaly plot (top outliers)
scores = iso.decision_function(X)
plt.figure(figsize=(8, 4))
plt.hist(scores, bins=30, color='steelblue', edgecolor='black')
plt.title('Isolation Forest Anomaly Scores')
plt.xlabel('Score')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('outputs/anomaly_plot.png')
plt.close()

# Save predictions
pred_df = pd.DataFrame({'actual': y_test, 'predicted': y_pred, 'anomaly_score': scores[-len(y_test):]})
pred_df.to_csv('outputs/alerts.csv', index=False)
print("Pipeline complete. Outputs saved to outputs/")
