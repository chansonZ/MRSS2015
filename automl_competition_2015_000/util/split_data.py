import numpy as np

from sklearn.cross_validation import train_test_split, StratifiedKFold


def split_data(X, Y, cv=False, shuffle=True):

    #if fold >= folds:
    #    raise ValueError((fold, folds))
    if X.shape[0] != Y.shape[0]:
        raise ValueError("The first dimension of the X and Y array must "
                         "be equal.")

    #if shuffle == True:
    #    rs = np.random.RandomState(42)
    #    indices = np.arange(X.shape[0])
    #    rs.shuffle(indices)
    #    Y = Y[indices]

    X_train, X_valid, Y_train, Y_valid = train_test_split(X, Y, test_size=0.33, random_state=42)
#     if(cv):
# #         kf = StratifiedKFold(Y_train, n_folds=folds, indices=True)
# #         for train_index, test_index in skf:
# #             X_train, X_test = X_train[train_index], X[test_index]
# #             y_train, y_test = y[train_index], y[test_index]
#
#     else:
#         return X_train, X_valid, Y_train, Y_valid
    return X_train, X_valid, Y_train, Y_valid


def get_CV_fold(X, Y, fold, folds, shuffle=True):
    fold = int(fold)
    folds = int(folds)
    if fold >= folds:
        raise ValueError((fold, folds))
    if X.shape[0] != Y.shape[0]:
        raise ValueError("The first dimension of the X and Y array must "
                         "be equal.")

    if shuffle == True:
        rs = np.random.RandomState(42)
        indices = np.arange(X.shape[0])
        rs.shuffle(indices)
        Y = Y[indices]

    kf = StratifiedKFold(Y, n_folds=folds, indices=True)
    for idx, split in enumerate(kf):
        if idx == fold:
            break

    if shuffle == True:
        return indices[split[0]], indices[split[1]]
    return split
