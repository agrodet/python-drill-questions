from importer import *

dataset = load_iris()
# load_iris()の結果からDataFrameを作成する
df = pd.DataFrame(dataset.data, columns=dataset."""①""")
print(f"original shape: {df.shape}")
print(df.describe())

# sepal（がく）の長さが5cm以上かどうかを示す列を作成する
df["sepal is long"] = df["sepal length (cm)"] > 5

# sepalの長さが5cm以上の行のみを取得する
long_sepal = df[df["""②"""]]
print(f"long_sepal shape: {long_sepal.shape}")

# sepalの長さと幅を和を示す列を作成する
df["sepal sum"] = """③"""

# sepalが5cm以上かつpetal（花弁）が4cm以下である行のみを取得する
long_sepal_and_short_petal = df["""④"""]
print(f"long_sepal_and_short_petal shape: {long_sepal_and_short_petal.shape}")

# 「petal」で始まる列を削除する
petal_removed = df[df.columns.drop(list("""⑤"""))]
print(f"petal_removed: {petal_removed.shape}")
print(petal_removed.describe())
