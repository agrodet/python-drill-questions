from importer import *

feature_df = pd.DataFrame([[1, 120.5, np.nan],
                           [3, 100, np.nan],
                           [np.nan, np.nan, np.nan],
                           [4, 200, 1.5],
                           [2, np.nan, np.nan]])

print(f"original shape: {feature_df.shape}")
# すべての要素が欠損値になっている行を削除
feature_df = feature_df.dropna(how="""①""")
print(f"shape after row removal: {feature_df.shape}")
# 欠損値の個数が2より多い列を削除
feature_df = feature_df.dropna(axis="""②""", thresh="""③""")
print(f"shape after column removal: {feature_df.shape}")
# 欠損値を列ごとの平均値で置換
feature_df = feature_df.fillna("""④""")
# StandardScalerでスケーリング
feature_df = StandardScaler()."""⑤"""(feature_df)
print(f"final df: {feature_df}")
