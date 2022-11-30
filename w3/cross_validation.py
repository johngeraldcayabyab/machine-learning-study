from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold, cross_val_score, StratifiedKFold, LeaveOneOut, LeavePOut, ShuffleSplit

X, y = datasets.load_iris(return_X_y=True)
clf = DecisionTreeClassifier(random_state=42)

k_folds = KFold(n_splits=5)
scores = cross_val_score(clf, X, y, cv=k_folds)
print("Cross validation scores: ", scores)
print("Average CV score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores))

sk_folds = StratifiedKFold(n_splits=5)
scores = cross_val_score(clf, X, y, cv=sk_folds)
print("Stratified Cross validation scores: ", scores)
print("Stratified Average CV score: ", scores.mean())
print("Stratified Number of CV Scores used in Average: ", len(scores))

loo = LeaveOneOut()
scores = cross_val_score(clf, X, y, cv=loo)
print("LOO Average CV score: ", scores.mean())
print("LOO Number of CV Scores used in Average: ", len(scores))

# only difference is the you can choose the number of CV from Leave one out
# lpo = LeavePOut(p=2)
# scores = cross_val_score(clf, X, y, cv=lpo)
# print("LPO Average CV score: ", scores.mean())
print("LPO Number of CV Scores used in Average: ", len(scores))

ss = ShuffleSplit(train_size=0.6, test_size=0.3, n_splits=5)
scores = cross_val_score(clf, X, y, cv=ss)
print("Shuffle Split Cross Validation Scores: ", scores)
print("Shuffle Split Average CV Score: ", scores.mean())
print("Shuffle Split Number of CV Scores used in Average: ", len(scores))
