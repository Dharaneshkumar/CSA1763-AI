from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
X = [[5, 80], [10, 85], [1, 60], [7, 78], [2, 50], [11, 95], [4, 65], [6, 70]]
y = [1, 1, 0, 1, 0, 1, 0, 1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Predictions:", y_pred)
print("Accuracy:", accuracy)
