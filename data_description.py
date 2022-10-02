from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
data=pd.read_csv("/content/drive/MyDrive/CarPrice_Assignment.csv")
data.head().T
data=data.drop(['car_ID'],axis=1)
data['CarName'] = data['CarName'].str.split(' ',expand=True)[0]
data['CarName'] = data['CarName'].replace({'maxda': 'mazda', 'nissan': 'Nissan', 'porcshce': 'porsche', 'toyouta': 'toyota', 'vokswagen': 'volkswagen', 'vw': 'volkswagen'})
data['CarName'].unique()
data['symboling']=data['symboling'].astype('str')
cat_col = data.select_dtypes(include=['object']).columns
num_col = data.select_dtypes(exclude=['object']).columns
numeric_cols = ["wheelbase","carlength","carwidth","carheight","curbweight","enginesize","boreratio","stroke","compressionratio","horsepower","peakrpm","citympg","highwaympg"]
data[num_col].describe().T
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
cor = data[num_col].corr()
plt.figure(figsize=(14,7))
sns.heatmap(cor, annot=True);
plt.title('Correlation of the Numeric Features');
