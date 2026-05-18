#wd Setup 
getwd()
setwd("E:/2nd. 2nd Semester/STAT-2205 R programming")
getwd()
list.files()
airline_random_1000 <- read.csv("E:/2nd. 2nd Semester/STAT-2205 R programming/airline_random_1000.csv")
head(airline_random_1000)
View(airline_random_1000)
str(airline_random_1000)

#My_ID_Sum+New_variable 
my_id <- 10015
airline_random_1000$new_miles <- airline_random_1000$miles + my_id
airline_random_1000$new_passengers <- airline_random_1000$passengers + my_id
airline_random_1000$new_coach_price <- airline_random_1000$coach_price + my_id
airline_random_1000$new_firstclass_price <- airline_random_1000$firstclass_price + my_id
View(airline_random_1000)

#Q1 Solution  : mean(airline_random_1000$new_coach_price)  
max(airline_random_1000$new_coach_price)    #highest price
min(airline_random_1000$new_coach_price)    #lowest price
median(airline_random_1000$new_coach_price) #median
sd(airline_random_1000$new_coach_price)     #distribution
hist(airline_random_1000$new_coach_price, 
     main = "Histogram of Coach Ticket Price",
     xlab = "Coach Ticket Price",
     ylab = "Frequency",
     col = "skyblue",
     border = "black")
boxplot(airline_random_1000$new_coach_price,
        main = "Boxplot of Coach Ticket Price",
        ylab = "Coach Ticket Price",
        col = "red",
        border = "black")

#Q2: 8-Hour Flight Analysis
flight_8_hr <- subset(airline_random_1000, hours == 8)
summary(flight_8_hr$new_coach_price)
mean(flight_8_hr$new_coach_price)
min(flight_8_hr$new_coach_price)
max(flight_8_hr$new_coach_price)

#Q3: Flight Delay Distribution
summary(airline_random_1000$delay)
hist(airline_random_1000$delay,
     main = "Flight Delay Distribution",
     xlab = "Delay Minutes",
     ylab = "Frequency",
     col = "orange",
     border = "black")
boxplot(airline_random_1000$delay,
        main = "Delay Boxplot",
        ylab = "Delay Minutes",
        col = "yellow")
#Interpretation 
#Most flights delay 0–20 minutes
# Some flights delay over 100 minutes

#Q4: Correlation with Coach Price
cor(airline_random_1000$coach_price, airline_random_1000$new_miles)
cor(airline_random_1000$coach_price, airline_random_1000$new_passengers)
cor(airline_random_1000$coach_price, airline_random_1000$delay)
cor(airline_random_1000$coach_price, airline_random_1000$hours)
plot(airline_random_1000$new_miles, 
     airline_random_1000$new_coach_price,
     main = "New Miles vs New Coach Price",
     xlab = "Miles",
     ylab = "Coach Price",
     col = "blue")
#Interpretation 
#Longer distance flights cost more
# Hours have positive correlation with price
# Delay has weak relation

#Q5: Coach vs First-Class Price
cor(airline_random_1000$new_coach_price,
    airline_random_1000$new_firstclass_price)
plot(airline_random_1000$new_coach_price,
     airline_random_1000$new_firstclass_price,
     main = "Coach vs First Class Price",
     xlab = "Coach Price",
     ylab = "First Class Price",
     col = "darkgreen")
#Interpretation
#Strong positive correlation exists
# Higher coach prices usually mean higher first-class prices

#Question 6: WiFi / Meal / Entertainment Effect
aggregate(new_coach_price ~ inflight_wifi,
          data = airline_random_1000,
          mean)
aggregate(new_coach_price ~ inflight_meal,
          data = airline_random_1000,
          mean)
aggregate(new_coach_price ~ inflight_entertainment,
          data = airline_random_1000,
          mean)
#Interpretation 
#Flights with WiFi have higher average prices
# Entertainment and meals also increase prices

#Question 7: Passengers vs Flight Hours
cor(airline_random_1000$passengers,
    airline_random_1000$hours)
plot(airline_random_1000$hours,	
     airline_random_1000$passengers,
     main = "Hours vs Passengers",
     xlab = "Flight Hours",
     ylab = "Passengers",
     col = "purple")
#Interpretation Weak positive relation exists
# Longer flights tend to carry slightly more passengers

#Question 8: Weekend vs Weekday Price
aggregate(new_coach_price ~ weekend,
          data = airline_random_1000,
          mean)
boxplot(new_coach_price ~ weekend,
        data = airline_random_1000, 
        main = "Weekend vs Weekday Prices",
        col = "cyan")
t.test(new_coach_price ~ weekend,
       data = airline_random_1000)
# Interpretation
# Weekend flights are slightly more expensive
# If p-value < 0.05 → significant difference

#Question 9:Redeye vs Non-Redeye
aggregate(new_coach_price ~ redeye,
          data = airline_random_1000,
          mean)
boxplot(new_coach_price ~ redeye,
        data = airline_random_1000, 
        main = "Redeye vs Non-Redeye",
        col = "pink")
# Interpretation
# Redeye flights are cheaper
# Overnight travel is less preferred

# Question 10: Full Statistical Analysis
summary(airline_random_1000)
mean(airline_random_1000$new_coach_price)
median(airline_random_1000$new_coach_price)
sd(airline_random_1000$new_coach_price)
cor(airline_random_1000[,c("coach_price",
                           "miles",
                           "delay",
                           "hours",
                           "passengers")])
#Linear Regression
model <- lm(coach_price ~ hours +
              miles +
              delay,
            data = airline_random_1000)
summary(model)
# Interpretation
#Miles significantly increase coach price
#Hours also increase price
#Delay has smaller effect















