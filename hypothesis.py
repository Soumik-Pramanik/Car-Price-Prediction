from sklearn.metrics import mean_absolute_error , mean_squared_error

MSE_Model12 = mean_squared_error(y_test1,y_pred1)
MSE_Model12
transformed_X1 = scaler.transform(data_set1)
data_set1['predection'] = linear_model.predict(transformed_X1)
data_set1['Diffrence'] = prii - data_set1['predection']
data_set1[['predection','Diffrence']].head(4)
import statsmodels.api as sm
X1 = sm.add_constant(X_train1)
model = sm.OLS(np.asarray(y_train1),np.asarray(X1))
result = model.fit()
print(result.summary())
