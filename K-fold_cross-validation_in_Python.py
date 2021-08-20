import numpy as np
from sklearn.model_selection import KFold

kf = KFold(n_splits=5)

errors = []
for train_index, test_index in kf.split(data):
    train = data.iloc[train_index,:]
    test = data.iloc[test_index,:]
    
    pred = train['actual'].mean()
    test['forecast'] = pred
    error = mean_squared_error(test['actual'], test['forecast'])
    error.append(error)

print(np.mean(errors))