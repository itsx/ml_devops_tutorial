# From raw data that is a mixture of categoricals and numeric, featurize the categoricals using one hot encoding. Use tabular explainer to get explain object and then get raw feature importances

# Explain a model with the AML explain-model package on raw features

# 1. Train a Logistic Regression model using Scikit-learn
# 2. Run 'explain_model' with full dataset in local mode, which doesn't contact any Azure services.
# 3. Run 'explain_model' with summarized dataset in local mode, which doesn't contact any Azure services.
# 4. Visualize the global and local explanations with the visualization dashboard.

#%%
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn_pandas import DataFrameMapper

#%%
# We are using the Titanic dataset for this example
data_url = (
    "https://raw.githubusercontent.com/amueller/"
    "scipy-2017-sklearn/091d371/notebooks/datasets/titanic3.csv"
)
data = pd.read_csv(data_url)
# fill missing values - propagate backward and forward
data = data.fillna(method="ffill")
data = data.fillna(method="bfill")


#%%
# Model explainer locally with full data
from sklearn.model_selection import train_test_split

numeric_features = ["age", "fare"]
categorical_features = ["embarked", "sex", "pclass"]

y = data["survived"].values
X = data[categorical_features + numeric_features]

x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#%%
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn_pandas import DataFrameMapper

# Impute, standardize the numeric features and one-hot encode the categorical features.

transformations = [
    (
        ["age", "fare"],
        Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler()),
            ]
        ),
    ),
    (
        ["embarked"],
        Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
                ("encoder", OneHotEncoder(sparse=False)),
            ]
        ),
    ),
    (["sex", "pclass"], OneHotEncoder(sparse=False)),
]


# Append classifier to preprocessing pipeline.
# Now we have a full prediction pipeline.
clf = Pipeline(
    steps=[
        ("preprocessor", DataFrameMapper(transformations)),
        ("classifier", LogisticRegression(solver="lbfgs")),
    ]
)

#%%
#  Train a logistic regression  model, which is what we want to explain
model = clf.fit(x_train, y_train)


#%%
from azureml.explain.model.tabular_explainer import TabularExplainer

# Explain predictions on the local machine
tabular_explainer = TabularExplainer(
    clf.steps[-1][1],
    initialization_examples=x_train,
    features=x_train.columns,
    transformations=transformations,
)


#%%
# Passing in test dataset for evaluation examples - note it must be a representative sample of the original data
# x_train can be passed as well, but with more examples explanations will take longer although they may be more accurate
global_explanation = tabular_explainer.explain_global(x_test)

#%%
sorted_global_importance_values = global_explanation.get_ranked_global_values()
sorted_global_importance_names = global_explanation.get_ranked_global_names()
dict(zip(sorted_global_importance_names, sorted_global_importance_values))

#%%
# Explain overall model predictions as a collection of local (instance-level) explanations
# explain the first member of the test set
local_explanation = tabular_explainer.explain_local(x_test[:1])


#%%
# get the prediction for the first member of the test set and explain why model made that prediction
prediction_value = clf.predict(x_test)[0]

sorted_local_importance_values = local_explanation.get_ranked_local_values()[
    prediction_value
]
sorted_local_importance_names = local_explanation.get_ranked_local_names()[
    prediction_value
]

# Sorted local SHAP values
print("ranked local importance values: {}".format(sorted_local_importance_values))
# Corresponding feature names
print("ranked local importance names: {}".format(sorted_local_importance_names))

#%%
# 2. Load visualization dashboard
# Note you will need to have extensions enabled prior to jupyter kernel starting
!jupyter nbextension install --py --sys-prefix azureml.contrib.explain.model.visualize
!jupyter nbextension enable --py --sys-prefix azureml.contrib.explain.model.visualize
# Or, in Jupyter Labs, uncomment below
# jupyter labextension install @jupyter-widgets/jupyterlab-manager
# jupyter labextension install microsoft-mli-widget

#%%
from azureml.contrib.explain.model.visualize import ExplanationDashboard


#%%
ExplanationDashboard(global_explanation, model, x_test)

#%%
