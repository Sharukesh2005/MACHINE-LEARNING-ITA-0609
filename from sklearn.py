from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, export_text
import pandas as pd

# Dataset
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain',
                'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny',
                'Overcast', 'Overcast', 'Rain'],

    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool',
                    'Cool', 'Mild', 'Cool', 'Mild', 'Mild',
                    'Mild', 'Hot', 'Mild'],

    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal',
                 'Normal', 'High', 'Normal', 'Normal', 'Normal',
                 'High', 'Normal', 'High'],

    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong',
             'Strong', 'Weak', 'Weak', 'Weak', 'Strong',
             'Strong', 'Weak', 'Strong'],

    'PlayTennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No',
                   'Yes', 'No', 'Yes', 'Yes', 'Yes',
                   'Yes', 'Yes', 'No']
}

# Convert into DataFrame
df = pd.DataFrame(data)

print("Training Data:\n")
print(df)

# Encode categorical values
encoder = LabelEncoder()

for column in df.columns:
    df[column] = encoder.fit_transform(df[column])

# Features and Target
X = df.drop('PlayTennis', axis=1)
y = df['PlayTennis']

# Train ID3 Decision Tree
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)

# Print Decision Tree
print("\nDecision Tree:\n")
print(export_text(model, feature_names=list(X.columns)))

# New Sample
# Outlook = Sunny
# Temperature = Cool
# Humidity = High
# Wind = Strong

new_sample = [[2, 0, 0, 0]]

prediction = model.predict(new_sample)

if prediction[0] == 1:
    print("\nPrediction: Play Tennis = Yes")
else:
    print("\nPrediction: Play Tennis = No")