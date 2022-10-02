from sklearn.metrics import r2_score
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print (f'model : {model} and  rmse score is : {np.sqrt(mean_squared_error(y_test, y_pred))}, r2 score is {r2_score(y_test, y_pred)}')
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
print (f' rmse score is : {round(np.sqrt(mean_squared_error(y_test, y_pred)),4)}, r2 score is {round(r2_score(y_test, y_pred),4)}')
xii=[]
for i in range (1,len(final_data['predection'])+1):
  xii.append(i)
yii=final_data['predection']
plt.figure(figsize=(20, 10))

plt.xlabel("Index")
plt.ylabel("Price")
plt.title("Price : Actual vs Predction")
plt.plot(xii,prii,color="blue")  ### Actual
plt.plot(xii,yii,color="red")    ### Predicted
plt.legend(["Actual Price","Predicted Price"])
