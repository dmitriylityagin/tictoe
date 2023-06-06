import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)



path = "../data_files/melb_data.csv"
file = pd.read_csv(path)
file.describe()

print(file.columns)

y = file.Price
# print(y)

features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = file[features]
# X.describe()
# X.head()
#
model = DecisionTreeRegressor(random_state=1)
model.fit(X, y)
# print(X.head())
# print("---------")
# print(model.predict(X.head()))

predicted_home_prices = model.predict(X)
# print(mean_absolute_error(y, predicted_home_prices))

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
melbourne_model = DecisionTreeRegressor()
melbourne_model.fit(train_X, train_y)

# print("Predicted values for homes: ", melbourne_model.predict(val_X.head()))
# print("Actual target values for those homes:", val_y.head().tolist())
# get predicted prices on validation data

val_predictions = melbourne_model.predict(val_X)
val_mae = mean_absolute_error(val_y, val_predictions)


# print(val_mae)


for max_leaf_nodes in [5, 50, 500, 1000, 5000, 10000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))
