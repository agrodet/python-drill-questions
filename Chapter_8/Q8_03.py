from importer import *


def eval_model(model, X, y, eval_func):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)
    model.fit(X_train, y_train)
    predicted = model.predict(X_test)
    return """①"""(y_test, predicted)


dataset = load_breast_cancer()
model = RandomForestClassifier(random_state=0)


def my_accuracy(y_true, y_pred):
    return ("""②""").sum() / y_true.shape["""③"""]


def my_recall(y_true, y_pred):
    t = y_true == y_pred
    tp = (t & """④""").sum()
    return tp / """④""".sum()


for name, eval_func in [('Accuracy', accuracy_score),
                        ('My accuracy', my_accuracy),
                        ('recall', recall_score),
                        ('My recall', my_recall)]:
    print(f"{name} score of rf: {eval_model(model, dataset.data, dataset.target, eval_func)}")
