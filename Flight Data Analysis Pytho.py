# WD Setup
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Set Working Directory
os.chdir(r"E:/2nd. 2nd Semester/STAT-2205 R programming")

# Check Current Directory
print(os.getcwd())

# Show Files
print(os.listdir())

# Load Dataset
airline = pd.read_csv("flight_data_csv.csv")

# View First Rows
print(airline.head())

# Dataset Information
print(airline.info())

# Student ID Sum + New Variable
my_id = 12310015

airline["new_miles"] = airline["miles"] + my_id
airline["new_passengers"] = airline["passengers"] + my_id
airline["new_coach_price"] = airline["coach_price"] + my_id
airline["new_firstclass_price"] = (
    airline["firstclass_price"] + my_id
)

print(airline.head())

# =========================================
# Question 1: Coach Ticket Analysis
# =========================================

# Average Price
print(airline["new_coach_price"].mean())

# Highest Price
print(airline["new_coach_price"].max())

# Lowest Price
print(airline["new_coach_price"].min())

# Median
print(airline["new_coach_price"].median())

# Standard Deviation
print(airline["new_coach_price"].std())

# Histogram
plt.hist(
    airline["new_coach_price"],
    color="skyblue",
    edgecolor="black"
)

plt.title("Histogram of Coach Ticket Price")
plt.xlabel("Coach Ticket Price")
plt.ylabel("Frequency")
plt.show()

# Boxplot
plt.boxplot(airline["new_coach_price"])

plt.title("Boxplot of Coach Ticket Price")
plt.ylabel("Coach Ticket Price")
plt.show()

# =========================================
# Question 2: 8-Hour Flight Analysis
# =========================================

flight_8_hr = airline[airline["hours"] == 8]

print(flight_8_hr["new_coach_price"].describe())
print(flight_8_hr["new_coach_price"].mean())
print(flight_8_hr["new_coach_price"].min())
print(flight_8_hr["new_coach_price"].max())

# =========================================
# Question 3: Flight Delay Distribution
# =========================================

print(airline["delay"].describe())

# Histogram
plt.hist(
    airline["delay"],
    color="orange",
    edgecolor="black"
)

plt.title("Flight Delay Distribution")
plt.xlabel("Delay Minutes")
plt.ylabel("Frequency")
plt.show()

# Boxplot
plt.boxplot(airline["delay"])

plt.title("Delay Boxplot")
plt.ylabel("Delay Minutes")
plt.show()

# =========================================
# Question 4: Correlation with Coach Price
# =========================================

print(airline["coach_price"].corr(airline["miles"]))
print(airline["coach_price"].corr(airline["passengers"]))
print(airline["coach_price"].corr(airline["delay"]))
print(airline["coach_price"].corr(airline["hours"]))

# Scatter Plot
plt.scatter(
    airline["miles"],
    airline["coach_price"],
    color="blue"
)

plt.title("Miles vs Coach Price")
plt.xlabel("Miles")
plt.ylabel("Coach Price")
plt.show()

# =========================================
# Question 5: Coach vs First-Class Price
# =========================================

print(
    airline["coach_price"].corr(
        airline["firstclass_price"]
    )
)

# Scatter Plot
plt.scatter(
    airline["coach_price"],
    airline["firstclass_price"],
    color="green"
)

plt.title("Coach vs First Class Price")
plt.xlabel("Coach Price")
plt.ylabel("First Class Price")
plt.show()

# =========================================
# Question 6: WiFi / Meal / Entertainment
# =========================================

print(
    airline.groupby("inflight_wifi")[
        "coach_price"
    ].mean()
)

print(
    airline.groupby("inflight_meal")[
        "coach_price"
    ].mean()
)

print(
    airline.groupby("inflight_entertainment")[
        "coach_price"
    ].mean()
)

# Boxplot
sns.boxplot(
    x="inflight_wifi",
    y="coach_price",
    data=airline
)

plt.title("WiFi vs Coach Price")
plt.show()

# =========================================
# Question 7: Passengers vs Flight Hours
# =========================================

print(
    airline["passengers"].corr(
        airline["hours"]
    )
)

# Scatter Plot
plt.scatter(
    airline["hours"],
    airline["passengers"],
    color="purple"
)

plt.title("Hours vs Passengers")
plt.xlabel("Flight Hours")
plt.ylabel("Passengers")
plt.show()

# =========================================
# Question 8: Weekend vs Weekday Price
# =========================================

print(
    airline.groupby("weekend")[
        "coach_price"
    ].mean()
)

# Boxplot
sns.boxplot(
    x="weekend",
    y="coach_price",
    data=airline
)

plt.title("Weekend vs Weekday Prices")
plt.show()

# =========================================
# Question 9: Redeye vs Non-Redeye
# =========================================

print(
    airline.groupby("redeye")[
        "coach_price"
    ].mean()
)

# Boxplot
sns.boxplot(
    x="redeye",
    y="coach_price",
    data=airline
)

plt.title("Redeye vs Non-Redeye")
plt.show()

# =========================================
# Question 10: Full Statistical Analysis
# =========================================

# Summary Statistics
print(airline.describe())

# Mean
print(airline["coach_price"].mean())

# Median
print(airline["coach_price"].median())

# Standard Deviation
print(airline["coach_price"].std())

# Correlation Matrix
print(
    airline[
        [
            "coach_price",
            "miles",
            "delay",
            "hours",
            "passengers"
        ]
    ].corr()
)

# Linear Regression
X = airline[
    [
        "hours",
        "miles",
        "delay"
    ]
]

y = airline["coach_price"]

# Add Constant
X = sm.add_constant(X)

# Build Model
model = sm.OLS(y, X).fit()

# Summary
print(model.summary())