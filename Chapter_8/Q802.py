from importer import *


def time(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.today()
        result = func(*args, **kwargs)
        end = datetime.datetime.today()
        print(f"elapsed: {(end - start).microseconds / 1e6}sec")
        return """1"""
    return """2"""


@time
def eval_model("""3""", X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)
    model.fit(X_train, y_train)
    predicted = model.predict(X_test)
    return accuracy_score(y_test, predicted)


dataset = load_iris()
# デフォルトのランダムフォレスト
rf = RandomForestClassifier(random_state=0)
# ハイパーパラメータを設定したランダムフォレスト
rf_par = RandomForestClassifier(n_estimators=200, max_depth=100, random_state=0)
# K近傍法による分類器
knn_par = KNeighborsClassifier(n_neighbors=7, p=3)

for name, model in ["""4"""]:
    accuracy = eval_model(model, dataset.data, dataset.target)
    print(f"Accuracy of {name}: {accuracy}")
