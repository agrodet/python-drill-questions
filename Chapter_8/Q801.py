from importer import *

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris."""1""", iris."""2""", test_size=0.33, random_state=0)
model = RandomForestClassifier(random_state=0)
model."""3"""(X_train, y_train)
predicted = model."""4"""(X_test)
print(f"Accuracy: {accuracy_score("""5""", predicted)}")
print(f"predicted: \n{predicted}")
