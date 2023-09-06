import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

import warnings
warnings.filterwarnings("ignore")

# csv_path = "/Users/hgaje/PycharmProjects/DCA_prectice/monthly-production-data.csv"
csv_file = "input_data_quiz.csv"
df = pd.read_csv(csv_file)
# print(df.head())

# let's fill empty values with zeros
df = df.fillna(0)
print(df.describe().T)
print(df.columns)

# Ploted Average downhole Pressure and WI rate in one plot with subplot and twinx()
plt.rcParams["figure.autolayout"] = True

ax1 = plt.subplot()
l1, = ax1.plot(df.index, df["AVG_DOWNHOLE_PRESSURE"], color="green")

ax2 = ax1.twinx()
l2, = ax2.plot(df.index, df["BORE_GAS_VOL"], alpha = 0.3, color="blue")

plt.legend([l1, l2], ["AVG_DOWNHOLE_PRESSURE", "BORE_GAS_VOL"])

plt.show()


df["AVG_DOWNHOLE_PRESSURE"].replace(0, np.random.randint(240, 260), inplace=True)
df["BORE_GAS_VOL"].replace(0, np.random.randint(4500, 6000), inplace=True)
df["BORE_WAT_VOL"].replace(0, df["BORE_WAT_VOL"].median(), inplace=True)
df["BORE_OIL_VOL"].replace(0, df["BORE_OIL_VOL"].median(), inplace=True)
df.replace(0, df.median(), inplace=True)

# Create ML model to predict GLR

df["LIQ_VOL"] = df["BORE_OIL_VOL"] + df["BORE_WAT_VOL"]

sns.scatterplot(x=df["LIQ_VOL"], y=df["AVG_DOWNHOLE_PRESSURE"])
plt.show()

x_train = df[["LIQ_VOL"]][:2000]
y_train = df[["AVG_DOWNHOLE_PRESSURE"]][:2000]
x_test = df[["LIQ_VOL"]][2000:]
y_test = df[["AVG_DOWNHOLE_PRESSURE"]][2000:]


plt.scatter(x_train, y_train)
plt.scatter(x_test, y_test)
plt.show()

# Predicting the oil and water production rate using ML algorithms

fig, ax = plt.subplots(2, 1, sharex="col", sharey="row")

ax[0].plot(df.index, df["BORE_OIL_VOL"], color="orange")
ax[1].plot(df.index, df["BORE_WAT_VOL"], color="blue")
plt.show()


# split data into training and testing sets
x1_train = df[["AVG_DOWNHOLE_PRESSURE", "BORE_GAS_VOL"]][:2000]
y1_train = df[["BORE_OIL_VOL"]][:2000]
x1_test = df[["AVG_DOWNHOLE_PRESSURE", "BORE_GAS_VOL"]][2000:]
y1_test = df[["BORE_OIL_VOL"]][2000:]

model = LinearRegression()
model.fit(x1_train, y1_train)

yp_test = model.predict(x1_test)
print(yp_test)

plt.plot(df.index[2000:], yp_test, color="red", label="Predicted")
plt.plot(df.index[2000:], y1_test, color="green", label="Actual")
plt.legend()

plt.xlabel("DATEPRD", color= "blue")
plt.ylabel("Oil Production Rate", color="blue")

plt.title("Comparision between Predicted oil Prod rate and Actual Oil Prod rate", size=12, color="blue")
plt.show()

# water

x2_train = df[["AVG_DOWNHOLE_PRESSURE", "BORE_WAT_VOL"]][:2000]
y2_train = df[["BORE_WAT_VOL"]][:2000]
x2_test = df[["AVG_DOWNHOLE_PRESSURE", "BORE_WAT_VOL"]][2000:]
y2_test = df[["BORE_WAT_VOL"]][2000:]

model_2 = LinearRegression()
model_2.fit(x2_train, y2_train)

yp_test_2 = model_2.predict(x2_test)


plt.plot(df.index[2000:], yp_test_2, color="red", label="Predicted")
plt.plot(df.index[2000:], y2_test, color="green", label="Actual")
plt.legend()

plt.xlabel("DATEPRD", color="blue")
plt.ylabel("Water Production Rate", color="blue")

plt.title("Comparision between Predicted water Prod rate and Actual water Prod rate", size=12, color="blue")
plt.show()
