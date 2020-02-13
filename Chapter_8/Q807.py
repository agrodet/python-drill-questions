from importer import *

dataset = load_wine()
print(f"original shape: {dataset.data.shape}")
kfold = KFold(n_splits=3, shuffle=True, random_state=0)
dim = 5
# 主成分分析(PCA）による次元削減
pca = PCA(n_components="""1""")
# 多次元尺度構成法(MDS）による次元削減
mds = MDS(n_components="""1""", random_state=0)
# 相互情報量(mutual_info_classif)の上位k個を選択
kbest = SelectKBest(mutual_info_classif, k="""1""")
model = RandomForestClassifier(random_state=0)

for name, transformer in [('pca', pca), ('mds', mds), ('kbest', kbest)]:
    transformed = transformer."""2"""(dataset.data, dataset.target)
    accuracy = cross_val_score(model, """3""", dataset.target, cv=kfold, scoring="accuracy")
    print(f"shape of {name}: {transformed.shape}")
    print(f"accuracy of {name}: {accuracy}")
    print(f"mean of {name}: {transformed.mean(axis=0)}")
