from importer import *


class NanRemover():
    def fit(self, X, y=None):
        nan_count = X."""①"""().sum(axis=0)
        self.bad_columns = nan_count["""②"""].index.tolist()
        print(f"bad_columns: {self.bad_columns}")
        return self

    def transform(self, X, y=None):
        return X.drop(columns="""③""")


features = pd.DataFrame([[5, np.nan], [3, np.nan], [5, 147],
                         [1, 110], [2, 99]], columns=['a', 'b'])

target = pd.Series([True, False, True, False, False],
                   index=features.index)

X_train, X_test, y_train, y_test = \
    train_test_split(features, target, test_size=0.4, shuffle=False)

model = Pipeline([('remover', """④"""),
                  ('model', RandomForestClassifier(random_state=0))])
predicted = model.fit(X_train, y_train).predict(X_test)
print(f"accuracy: {accuracy_score(y_test, predicted)}")
