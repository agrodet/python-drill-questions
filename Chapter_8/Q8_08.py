from importer import *

dataset = load_wine()
kfold = KFold(n_splits=3, shuffle=True, random_state=0)
# K近傍法に基づいた予測モデルを作成
knn = KNeighborsClassifier()
# StandardScalerによるスケーリング後、  K近傍法を実行するパイプラインを作成
scaled_knn = Pipeline([('scaler', """①"""),
                       ('model', """②""")])
# StandardScaler→SelectKBestと適用後、  K近傍法を実行するパイプラインを作成
kbest_scaled_knn = Pipeline([('kbest', SelectKBest(mutual_info_classif, k=5)),
                             ('model', """③""")])

for name, model in [('knn', knn), ('scaled_knn', scaled_knn), ('kbest_scaled_knn', kbest_scaled_knn)]:
    accuracy = cross_val_score("""④""", dataset.data, dataset.target, cv=kfold, scoring="accuracy")
    print(f"CV accuracy of {name}: {accuracy}")
