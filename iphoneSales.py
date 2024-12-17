import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Reading the data file
data = pd.read_csv(r"C:\Users\rajve\Downloads\apple_products.csv")

# Data Cleaning
print(data.isnull().sum())

# Statical Analysis
print(data.describe()) # checking numeric data - statical Analysis.

# top 10 apple iphone sales analysis in india
Highest_rated =data.sort_values(by=["Star Rating"],ascending= False)
Highest_rated=Highest_rated.head(10)
print(Highest_rated['Product Name'])

# HIghest Rated iphone on flipkart - Data Visulization.
iphones = Highest_rated["Product Name"].value_counts()
labels = iphones.index
counts = Highest_rated["Number Of Ratings"]
figure = px.bar(Highest_rated,x=labels,y=counts,title="Number Of Ratings of highest rated iphones")
figure.show()

# Ploting graph according to review
iphones = Highest_rated["Product Name"].value_counts()
labels = iphones.index
counts = Highest_rated["Number Of Reviews"]
figure = px.bar(Highest_rated,x=labels,y=counts,title="Number Of Reviews of highest rated iphones")
figure.show()

# Ploting graph according to sales price
figure = px.scatter(data_frame=data,x="Number Of Ratings",y="Sale Price",size="Discount Percentage", 
trendline="ols",title="Relationship Between sale price and number of rating")
figure.show()

# Discount Percentage
figure = px.scatter(data_frame=data,x="Number Of Ratings",y="Discount Percentage",size="Sale Price", 
trendline="ols",title="Relationship Between sale price and number of rating")
figure.show()