from importer import *


def my_cross_val_score(model, X, y, kfold):
    result = []
    for train_index, test_index in kfold."""①"""(X):
        model.fit(X["""②"""], y["""②"""])
        predicted = model.predict(X["""③"""])
        result.append(accuracy_score(y["""③"""], predicted).round(8))
    return result


dataset = load_breast_cancer()
model = RandomForestClassifier(random_state=0)
kfold = KFold(n_splits=3, shuffle=True, random_state=0)

cv_accuracy = cross_val_score(model, dataset.data, dataset.target, cv="""④""", scoring="accuracy")
my_cv_acc = my_cross_val_score(model, dataset.data, dataset.target, """④""")
print(f"CV accuracy: {cv_accuracy}\nMy CV accuracy: {my_cv_acc}")
