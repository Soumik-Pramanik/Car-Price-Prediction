from sklearn.model_selection import train_test_split

y_col = 'target'

feature_cols = [x for x in final_data.columns if x != y_col]
X_final_data = final_data[feature_cols]
y_final_data = final_data[y_col]

X_final_train, X_final_test, y_final_train, y_final_test = train_test_split(X_final_data, y_final_data, test_size=0.3, random_state=42)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

LR = LinearRegression()

# Storage for error values
error_df = list()

LR = LR.fit(X_final_train, y_final_train)
y_final_train_pred = LR.predict(X_final_train)
y_final_test_pred = LR.predict(X_final_test)

error_df.append(pd.Series({'train': mean_squared_error(y_final_train, y_final_train_pred),'test' : mean_squared_error(y_final_test, y_final_test_pred)},name='one-hot enc'))

error_df
final_data.corr()['target'].abs().sort_values()
# take 1 feature, 2 feature
len_features = list()
train_error = list()
test_error= list()

x = final_data.corr().target.abs().sort_values(ascending = False)
x = x.drop(labels=['target'])

for i in range(1,13):
    features = list()
    features = x.index[range(0,i)]
    X = final_data[features]
    y = final_data['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    LR = LR.fit(X_train, y_train)
    y_train_pred = LR.predict(X_train)
    y_test_pred = LR.predict(X_test)
    
    len_features.append(len(features))
    train_error.append(mean_squared_error(y_train, y_train_pred))
    test_error.append(mean_squared_error(y_test,  y_test_pred))
    
    df_error = pd.DataFrame(list(zip(len_features,train_error,test_error)),columns = ['len_features','train_error','test_error'])
    df_error
    plt.figure(figsize = (20,8))
plt.plot('len_features', 'train_error', data = df_error, marker = "o", linestyle = "-", label = "Train Error", color = "black")
plt.plot('len_features', 'test_error', data = df_error, marker = "o", linestyle = "-", label = "Test Error")
