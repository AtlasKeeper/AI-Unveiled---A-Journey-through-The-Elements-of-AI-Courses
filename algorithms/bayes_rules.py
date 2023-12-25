import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.impute import SimpleImputer
from sklearn import metrics

# Load Titanic training dataset
# Use raw strings (r'') to avoid escape sequence issues
train_data = pd.read_csv(r'A:\Code\Projects\elements-of-a.i\algorithms\train.csv')

# Preprocess the training data (feature selection, handling missing values, encoding categorical variables, etc.)
# For simplicity, let's use a subset of features. You may need to customize this based on your analysis.
selected_features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Survived']
train_data = train_data[selected_features].dropna()

# Convert categorical variables to numerical using one-hot encoding
train_data = pd.get_dummies(train_data, columns=['Sex'], drop_first=True)

# Define features (X) and target variable (y) for training
X_train = train_data.drop('Survived', axis=1)
y_train = train_data['Survived']

# Load Titanic testing dataset
# Use raw strings (r'') to avoid escape sequence issues
test_data = pd.read_csv(r'A:\Code\Projects\elements-of-a.i\algorithms\test.csv')

# Preprocess the testing data (similar to the training data)
# Exclude non-numeric columns before imputing missing values
numeric_columns = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
test_data_numeric = test_data[numeric_columns]

# Impute missing values using the mean (you can choose a different strategy)
imputer = SimpleImputer(strategy='mean')
X_test_imputed = pd.DataFrame(imputer.fit_transform(test_data_numeric), columns=test_data_numeric.columns)

# Convert categorical variables to numerical using one-hot encoding
test_data_categorical = pd.get_dummies(test_data[['Sex']], columns=['Sex'], drop_first=True)

# Combine the imputed numeric features with the one-hot encoded categorical features
X_test = pd.concat([X_test_imputed, test_data_categorical], axis=1)

# Ensure that the selected features match the features used during training
# Exclude 'Survived' since it's not in the test set
X_test = X_test[X_train.columns]

# Initialize Gaussian Naive Bayes classifier
gnb = GaussianNB()

# Train the classifier using the training data
gnb.fit(X_train, y_train)

# Make predictions on the test set
y_pred = gnb.predict(X_test)

# Calculate the percentage of positive predictions
percentage_positive = (sum(y_pred) / len(y_pred)) * 100

# Display the percentage of positive predictions
print(f"Percentage of positive predictions: {percentage_positive:.2f}%")
