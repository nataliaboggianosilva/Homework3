from matplotlib import pylab as plt
import pandas as pd

df1 = pd.read_csv("AAL.csv")
print(df1.head())
df1['Date'] = pd.to_datetime(df1.Date)

df2 = pd.read_csv("JBLU.csv")
print(df2)
df2['Date'] = pd.to_datetime(df2.Date)

mean = df1["Close"].mean()
plt.figure("American Airlines Stock")
plt.plot(df1["Date"], df1["Close"], 'r-', linewidth=0.6, label="AAL Stock price, mean="+str(mean))

mean2 = df2["Close"].mean()

plt.plot(df2["Date"], df2["Close"], 'r-', linewidth=0.6, label="JBLU Stock price, mean="+str(mean2))

plt.xlabel("Dates")
plt.legend(loc="upper left")

plt.show()