import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('Diabetes.csv')
print(data)
#Bar Graph (Average Glucose by Outcome) - Before Cleaning
data = pd.read_csv('Diabetes.csv')
avg_glucose = data.groupby('Outcome')['Glucose'].mean()
plt.bar(avg_glucose.index, avg_glucose.values)
plt.xlabel("Outcome (0 = Non-Diabetic, 1 = Diabetic)")
plt.ylabel("Average Glucose Level")
plt.title("Average Glucose Level by Outcome(Before Cleaning)")
plt.show()
  # Line Plot (Glucose Values Across Records)
plt.plot(data['Glucose'])
plt.xlabel("Patient Index")
plt.ylabel("Glucose Level")
plt.title("Glucose Level Distribution")
plt.show()

 # Box Plot (BMI Distribution)
plt.boxplot(data['BMI'])
plt.ylabel("BMI")
plt.title("BMI Distribution")
plt.show()

#  Scatter Plot (Glucose vs BMI)- Before Cleaning
plt.scatter(data['Glucose'], data['BMI'])
plt.xlabel("Glucose")
plt.ylabel("BMI")
plt.title("Glucose vs BMI Relationship(Before Cleaning)")
plt.show()


columns = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
data[columns] = data[columns].replace(0, np.nan)
data.fillna(data.median(), inplace=True)
print(data.isnull().sum())

#   Bar Graph (Average Glucose by Outcome) -After Cleaning
avg_glucose = data.groupby('Outcome')['Glucose'].mean()
plt.bar(avg_glucose.index, avg_glucose.values)
plt.xlabel("Outcome (0 = Non-Diabetic, 1 = Diabetic)")
plt.ylabel("Average Glucose Level")
plt.title("Average Glucose Level by Outcome(After Cleaning)")
plt.show()

# Line Plot (Glucose Variation)
plt.plot(data['Glucose'])
plt.xlabel("Patient Index")
plt.ylabel("Glucose Level")
plt.title("Glucose Level Distribution After Cleaning")
plt.show()

# Box Plot (BMI Distribution)
plt.boxplot(data['BMI'])
plt.ylabel("BMI")
plt.title("BMI Distribution After Cleaning")
plt.show()

# Scatter Plot (Glucose vs BMI)-  After Cleaning
plt.scatter(data['Glucose'], data['BMI'])
plt.xlabel("Glucose")
plt.ylabel("BMI")
plt.title("Glucose vs BMI Relationship (After Cleaning)")
plt.show()
