from matplotlib.offsetbox import bbox_artist
import pandas as pd
import streamlit as st
from sklearn import datasets
import shap 
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor

st.write("""
# Boston Housing Price Prediction App

This app predicts the **Boston House Price** based on the parameters set by the user

""")

st.write("---")
df = datasets.load_boston()

#X = df.iloc[:, :13]

#Y = df.MEDV

X = pd.DataFrame(df.data, columns=df.feature_names)
Y = pd.DataFrame(df.target, columns=["MEDV"])

st.sidebar.header("Parameters: ")
st.sidebar.write("""
CRIM - per capita crime rate by town

ZN - proportion of residential land zoned for lots over 25,000 sq.ft.

INDUS - proportion of non-retail business acres per town.

CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)

NOX - nitric oxides concentration (parts per 10 million)

RM - average number of rooms per dwelling

AGE - proportion of owner-occupied units built prior to 1940

DIS - weighted distances to five Boston employment centres

RAD - index of accessibility to radial highways

TAX - full-value property-tax rate per $10,000

PTRATIO - pupil-teacher ratio by town

B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town

LSTAT - % lower status of the population

MEDV - Median value of owner-occupied homes in $1000's

""")

st.sidebar.write("---")

st.sidebar.header("Specify The Parameters")

def user_input_features():
    CRIM = st.sidebar.slider('CRIM', X.CRIM.min(), X.CRIM.max(), float(X.CRIM.mean()))
    ZN = st.sidebar.slider('ZN', X.ZN.min(), X.ZN.max(), float(X.ZN.mean()))
    INDUS = st.sidebar.slider('INDUS', X.INDUS.min(), X.INDUS.max(), float(X.INDUS.mean()))
    CHAS = st.sidebar.slider('CHAS', X.CHAS.min(), X.CHAS.max(), float(X.CHAS.mean()))
    NOX = st.sidebar.slider('NOX', X.NOX.min(), X.NOX.max(), float(X.NOX.mean()))
    RM = st.sidebar.slider('RM', X.RM.min(), X.RM.max(), float(X.RM.mean()))
    AGE = st.sidebar.slider('AGE', X.AGE.min(), X.AGE.max(), float(X.AGE.mean()))
    DIS = st.sidebar.slider('DIS', X.DIS.min(), X.DIS.max(), float(X.DIS.mean()))
    RAD = st.sidebar.slider('RAD', X.RAD.min(), X.RAD.max(), float(X.RAD.mean()))
    TAX = st.sidebar.slider('TAX', X.TAX.min(), X.TAX.max(), float(X.TAX.mean()))
    PTRATIO = st.sidebar.slider('PTRATIO', X.PTRATIO.min(), X.PTRATIO.max(), float(X.PTRATIO.mean()))
    B = st.sidebar.slider('B', X.B.min(), X.B.max(), float(X.B.mean()))
    LSTAT = st.sidebar.slider('LSTAT', X.LSTAT.min(), X.LSTAT.max(), float(X.LSTAT.mean()))
    data = {'CRIM': CRIM,
            'ZN': ZN,
            'INDUS': INDUS,
            'CHAS': CHAS,
            'NOX': NOX,
            'RM': RM,
            'AGE': AGE,
            'DIS': DIS,
            'RAD': RAD,
            'TAX': TAX,
            'PTRATIO': PTRATIO,
            'B': B,
            'LSTAT': LSTAT}
    features = pd.DataFrame(data, index=[0])
    return features

df1 = user_input_features()

st.header('Specified Input parameters: ')
st.write(df1)
st.write("---")

model = RandomForestRegressor()
model.fit(X, Y)

prediction = model.predict(df1)

st.header("Prediction of MEDV")
st.write(prediction)
st.write("---")

explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(X)

st.header("Feature Importance")
st.write("Positive or negative effect on **MEDV** due to the parameter")
plt.title("feature importance based on SHAP values")
shap.summary_plot(shap_values, X)
st.pyplot(bbox_inches = 'tight')
st.write("---")

plt.title("Feature importance based on SHAP values")
shap.summary_plot(shap_values, X, plot_type = "bar")
st.pyplot(bbox_inches = "tight")