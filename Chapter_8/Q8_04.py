from importer import *


def my_cross_val_score(model, X, y, kfold):
    result = []
    for train_index, test_index in kfold."""1"""(X):
        model.fit(X["""2"""], y["""2"""])
        predicted = model.predict(X["""3"""])
        result.append(accuracy_score(y["""3"""], predicted).round(8))
    return result


dataset = load_breast_cancer()
model = RandomForestClassifier(random_state=0)
kfold = KFold(n_splits=5, shuffle=True, random_state=0)

cv_accuracy = cross_val_score(model, dataset.data, dataset.target, cv="""4""", scoring="accuracy")
print(f"CV accuracy:\n{cv_accuracy}")
my_cv_acc = my_cross_val_score(model, dataset.data, dataset.target, kfold)
print(f"My CV accuracy: \n{my_cv_acc}")
