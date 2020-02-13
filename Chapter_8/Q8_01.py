from importer import *

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris."""①""", iris."""②""", test_size=0.33, random_state=0)
model = RandomForestClassifier(random_state=0)
model."""③"""(X_train, y_train)
predicted = model."""④"""(X_test)
print(f"Accuracy: {accuracy_score("""⑤""", predicted)}")
print(f"predicted: \n{predicted}")
