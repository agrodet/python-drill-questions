from importer import *


class NanRemover():
    def fit(self, X, y=None):
        nan_count = X."""1"""().sum(axis=0)
        self.bad_columns = nan_count["""2"""].index.tolist()
        print(f"bad_columns: {self.bad_columns}")
        return self

    def transform(self, X, y=None):
        X = X.drop(columns="""3""")
        print(f"nan removed X:\n{X}")
        return X


features = pd.DataFrame([[5, np.nan], [3, np.nan], [5, 147],
                         [1, 110], [2, 99]], columns=['a', 'b'])

target = pd.Series([True, False, True, False, False], index=features.index)

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.4, shuffle=False)

model = Pipeline([('remover', """4"""),
                  ('model', RandomForestClassifier(random_state=0))])
model.fit(X_train, y_train)
predicted = model.predict(X_test)
print(f"acuracy: {accuracy_score(y_test, predicted)}")
