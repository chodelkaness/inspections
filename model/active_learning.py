# Active Learning Example
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from modAL.models import ActiveLearner

# Define initial training data
X_initial = X_train[:50]
y_initial = y_train[:50]

# Define the learner
learner = ActiveLearner(
    estimator=RandomForestRegressor(),
    X_training=X_initial, y_training=y_initial
)

# Active learning loop
n_queries = 10
for idx in range(n_queries):
    query_idx, query_instance = learner.query(X_train, n_instances=1)
    learner.teach(X_train[query_idx], y_train[query_idx])

    # Remove queried instance from the training set
    X_train = np.delete(X_train, query_idx, axis=0)
    y_train = np.delete(y_train, query_idx)

# Evaluate the updated model
y_pred = learner.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error after active learning: {mae}")
