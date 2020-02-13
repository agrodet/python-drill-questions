from importer import *

dataset = load_wine()
# 1 ≦ k ≦ 9、3 ≦ n_neighbors ≦ 7の探索空間を定義
search_space = {"kbest__k": """①""",
                " """②""" ": range(3, 8)}
kbest_knn = Pipeline([("kbest", SelectKBest(mutual_info_classif)),
                      ("model", KNeighborsClassifier())])

X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.33, random_state=0)

# search_space内をGridSearchCV関数で探索
grid_cv = GridSearchCV(kbest_knn, param_grid=search_space, cv=4)
grid_cv."""③"""(X_train, y_train)
# 最も優秀だったパラメータの条件を表示
print(f"best parameters: {grid_cv."""④"""}")
print(f"best scores: {grid_cv.best_score_}")
# 探索したパラメータの条件でテストデータを予測
predicted = """⑤""".predict(X_test)
print(f"score for test_data: {accuracy_score(y_test, predicted)}")
