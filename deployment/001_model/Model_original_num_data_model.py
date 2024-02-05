import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline

df = pd.read_csv('df_original_num_data_0115.csv')

#train_raw, test_raw = train_test_split(df, test_size = 0.2, shuffle=False)

features = list(df.columns)
target = 'party_label'
features.remove(target)

X_train = df[features]
y_train = df[target]

#X_test = test_raw[features]
#y_test = test_raw[target]

# Create a pipeline with XGBoost Classifier
model = Pipeline([
    ('Rescale', MinMaxScaler()),
    ('xgbc', XGBClassifier(
        learning_rate= 0.3,
        n_estimators=300,
        max_depth=20,
        random_state=42
    ))
])

# Train the pipeline
model.fit(X_train, y_train)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

