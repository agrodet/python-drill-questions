from importer import *

dataset = load_iris()
# load_iris()の結果からDataFrameを作成する
df = pd.DataFrame(dataset.data, columns=dataset."""1""")
print(f"original shape: {df.shape}")
print(df.describe())

# sepal（がく）の長さが5cm以上かどうかを示す列を作成する
df["sepal is long"] = df["sepal length (cm)"] > 5

# sepalの長さが5cm以上の行のみを取得する
long_sepal = df[df["""2"""]]
print(f"long_sepal shape: {long_sepal.shape}")

# sepalの長さと幅を和を示す列を作成する
df["sepal sum"] = """3"""

# sepalが5cm以上かつpetal（花弁）が4cm以下である行のみを取得する
long_sepal_and_short_petal = df["""4"""]
print(f"long_sepal_and_short_petal shape: {long_sepal_and_short_petal.shape}")

# 「petal」で始まる列を削除する
petal_removed = df[df.columns.drop(list("""5"""))]
print(f"petal_removed: {petal_removed.shape}")
print(petal_removed.describe())
