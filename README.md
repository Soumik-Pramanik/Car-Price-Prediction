# Car-Price-Prediction
# Introduction
It is required to model the price of cars with the available independent variables. 
It will be used by the management to understand how exactly the prices vary 
with the independent variables. They can accordingly manipulate the design of 
the cars, the business strategy etc. to meet certain price levels. Further, the 
model will be a good way for management to understand the pricing dynamics 
of a new market.
I have applied to a highly comprehensive analysis with all data cleaning, 
exploration, visualization, feature selection and model building. The data used for 
the prediction were collected from the web portal fred.stlouisfed.org using web 
scraper, written in Python/Jupyter programming language. According to a 
problem-solving approach, I have split it to 5 parts (Data understanding and 
exploration, Data cleaning, Data preparation: Feature Engineering and Scaling, 
Feature Selection using RFE and Model Building and Linear Regression 
Assumptions Validation and Outlier Removal).
# Data Description
![image](https://user-images.githubusercontent.com/96630179/193247945-c6a006ea-2050-4fe6-936e-2189a2e51040.png)
![image](https://user-images.githubusercontent.com/96630179/193248103-6179d52a-a430-42fe-a558-80af96ec4a59.png)

From above two figure the target variable price has a positive skew; however, 
majority of the cars are low priced. More than 50% of the cars (around 105-107 
out of total of 205) are priced 10,000 and close to 35% cars are priced between 
10,000 and 20,000. So around 85% of cars in US market are priced between 
5,000 to 20,000. Based on above observations and graph on right side 
(KDE/green one) it appears there are 2 distributions one for cars priced between 
5,000 and 25000 and another distribution for high priced cars 25,000 and above. 
(Notice the approximate bell curve from little less than 30000 up to 
45,000/50,000).

The below diagram shows the weight of numerical features.
![image](https://user-images.githubusercontent.com/96630179/193248783-2b331d1d-d8bf-41c1-bee8-a62ba8e859af.png)
# Correlation Matrix
![image](https://user-images.githubusercontent.com/96630179/193249025-a3f00270-a56a-476f-863d-1a13a287d832.png)

Positive correlation: price highly correlated with enginesize, curbweight, 
horsepower, carwidth (all of these variables represent the size/weight/engine 
power of the car)

Negative correlation: price negatively correlation with mpg var's citympg 
and highwaympg. This suggest that cars having high mileage may fall in the 
'economy' cars category or in other words indicates that Low priced cars 
have mostly high mpg.

Correlation among independent variables: many independent variables are 
highly correlated; wheelbase, carlength, curbweight, enginesize etc. are all 
measures of 'size/weight', and are positively correlated.
Since independent variables are highly correlated (more than 80% 
correlation among many of them) we'll have to pay attention to 
multicollinearity, which we will check in assumptions validation section 
using VIF score
# Output
After calculating the predicted price here are few values of predicted price and 
their difference from actual true price.

![image](https://user-images.githubusercontent.com/96630179/193249835-7265aee9-bcd2-4440-8ae0-3e0cb29c19cf.png)
![image](https://user-images.githubusercontent.com/96630179/193249892-bd4d6c08-b421-465e-a56d-00eb87739de1.png)
![image](https://user-images.githubusercontent.com/96630179/193250081-cb5cb62c-d0cc-4b2e-96f6-00e75db55d72.png)

And model will come out as r2 score is 0.8043634667135657
