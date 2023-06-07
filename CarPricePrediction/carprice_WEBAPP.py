import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

st.write("""

# CAR PRICE PREDICTION WEBAPP
""")


st.write("""
 This model will predict the cost of the car using the important variables that effect the cost of the car the most.

""")


st.write("---")

cars = pd.read_csv("C:\\Users\\Veer\\Downloads\\CarPrice_Assignment.csv")

st.write("""

### Here is the data that is provided

""")

st.write(cars.head())


cars['fuelEco'] = (0.55 * cars.citympg + 0.45 * cars.highwaympg)

cars_lr = cars
cars_lr.drop(columns=['car_ID', 'fuelsystem', 'peakrpm', 'compressionratio', 'carheight', 'doornumber', 'highwaympg', 'citympg'])

def dummies(x,df):
    temp = pd.get_dummies(df[x], drop_first = True)
    df = pd.concat([df, temp], axis = 1)
    df.drop([x], axis = 1, inplace = True)
    return df

cars_lr = dummies('fueltype',cars_lr)
cars_lr = dummies('aspiration',cars_lr)
cars_lr = dummies('carbody',cars_lr)
cars_lr = dummies('drivewheel',cars_lr)
cars_lr = dummies('enginelocation', cars_lr)
cars_lr = dummies('enginetype',cars_lr)
cars_lr = dummies('cylindernumber',cars_lr)

st.write(cars_lr.head())

from sklearn.model_selection import train_test_split

df_train, df_test = train_test_split(cars_lr, test_size = 0.5, random_state = 100)


st.write("""

#### From the heatmap, we can find out the major attributes that are affecting the price of the car""")

plt.figure(figsize = (25, 25))
fig, ax = plt.subplots()
sns.heatmap(df_train.corr(), ax = ax, cmap='YlGnBu')
st.write(fig)

y_train = df_train['price']
df_train = df_train[['wheelbase', 'carlength', 'carwidth', 'curbweight', 'enginesize', 'boreratio', 'horsepower', 'fuelEco', 'rwd', 'fwd', 'four', 'six', 'price']]

x_train = df_train.iloc[: , :12]
y_train = df_train['price']


from sklearn.linear_model import LinearRegression

mlr = LinearRegression()
mlr.fit(x_train, y_train)

st.write("---")


st.write("""

#### Important attributes are as follows: 



""")
st.write(x_train.columns)



m = mlr.coef_
c = mlr.intercept_

st.write("---")

st.write("""

#### The coeff and intercept of regression is as follows: 

""")

st.write("Coeff: ",m, " Intercept: ", c)


st.sidebar.write("---")

st.sidebar.header("Specify The Parameters")


def user_input_features():
    wheelbase = st.sidebar.slider('WHEELBASE', (x_train.wheelbase.min()), (x_train.wheelbase.max()), float(x_train.wheelbase.mean()))
    carlength = st.sidebar.slider('CARLENGTH', x_train.carlength.min(), x_train.carlength.max(), float(x_train.carlength.mean()))
    carwidth = st.sidebar.slider('CARWIDTH', x_train.carwidth.min(), x_train.carwidth.max(), float(x_train.carwidth.mean()))
    curbweight = st.sidebar.slider('CURBWEIGHT', float(x_train.curbweight.min()), float(x_train.curbweight.max()), float(x_train.curbweight.mean()))
    enginesize = st.sidebar.slider('ENGINESIZE', float(x_train.enginesize.min()), float(x_train.enginesize.max()), float(x_train.enginesize.mean()))
    boreratio = st.sidebar.slider('BORERATIO', x_train.boreratio.min(), x_train.boreratio.max(), float(x_train.boreratio.mean()))
    horsepower = st.sidebar.slider('HORSEPOWER', float(x_train.horsepower.min()), float(x_train.horsepower.max()), float(x_train.horsepower.mean()))
    fuelEco = st.sidebar.slider('FUEL ECO', x_train.fuelEco.min(), x_train.fuelEco.max(), float(x_train.fuelEco.mean()))
    rwd = st.sidebar.slider('RWD', float(x_train.rwd.min()), float(x_train.rwd.max()), float(x_train.rwd.mean()))
    fwd = st.sidebar.slider('FWD', float(x_train.fwd.min()), float(x_train.fwd.max()), float(x_train.fwd.mean()))
    four = st.sidebar.slider('FOUR', float(x_train.four.min()), float(x_train.four.max()), float(x_train.four.mean()))
    six = st.sidebar.slider('SIX', float(x_train.six.min()), float(x_train.six.max()), float(x_train.six.mean()))

    data = {'wheelbase': wheelbase,
            'carlength': carlength,
            'carwidth': carwidth,
            'curbweight': curbweight,
            'enginesize': enginesize,
            'boreratio': boreratio,
            'horsepower': horsepower,
            'fuelEco': fuelEco,
            'rwd': rwd,
            'fwd': fwd,
            'four': four,
            'six': six}
    
    features = pd.DataFrame(data, index = [0])
    return features


df1 = user_input_features()

st.write("---")
st.header("SPECIFIED INPUT PARAMETERS: ")
st.write(df1)
st.write("""

#### NOTE: rwd fwd four six take binary values
""")
st.write("---")

pred = mlr.predict(df1)

st.write("### PRICE: ", pred)
