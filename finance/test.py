import xgboost as xgb
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data
data = load_iris()
X = data.data
y = data.target

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert to DMatrix, XGBoost's internal data structure
train_data = xgb.DMatrix(X_train, label=y_train)
test_data = xgb.DMatrix(X_test, label=y_test)

# Set parameters
params = {
    'objective': 'multi:softmax',
    'num_class': 3,
    'max_depth': 4,
    'eta': 0.3,
    'subsample': 0.8,
    'colsample_bytree': 0.8
}

# Train model
model = xgb.train(params, train_data, num_boost_round=100)

# Predict
predictions = model.predict(test_data)
print(f"predictions: {predictions}")
# Evaluate
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")



from sklearn.model_selection import cross_val_score
import xgboost as xgb
import numpy as np

# Load data
data = load_iris()
X = data.data
y = data.target

# Convert to DMatrix
dmatrix = xgb.DMatrix(X, label=y)

# Define parameters
params = {
    'objective': 'multi:softmax',
    'num_class': 3,
    'max_depth': 4,
    'eta': 0.3,
    'subsample': 0.8,
    'colsample_bytree': 0.8
}

# Perform cross-validation
cv_results = xgb.cv(
    params,
    dmatrix,
    num_boost_round=100,
    nfold=5,
    metrics="merror",
    as_pandas=True,
    seed=42
)

# Print mean test accuracy
print("Cross-validation mean test accuracy: ", 1 - cv_results['test-merror-mean'].iloc[-1])
