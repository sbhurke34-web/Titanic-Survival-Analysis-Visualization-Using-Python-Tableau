# ================== IMPORT LIBRARIES ==================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ================== SET OUTPUT FOLDER ==================
output_folder = "titanic_visualization"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# ================== LOAD DATA ==================
df = pd.read_csv("Titanic-Dataset.csv")

print("First 5 rows:\n", df.head())
print("\nShape:", df.shape)
print("\nColumns:", df.columns)
print("\nData Types:\n", df.dtypes)

# ================== DATA CLEANING ==================

# Missing values
print("\nMissing Values:\n", df.isnull().sum())

# Fill missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Drop Cabin (too many missing values)
if 'Cabin' in df.columns:
    df = df.drop(columns=['Cabin'])

# Remove duplicates
print("\nDuplicate Rows:", df.duplicated().sum())
df = df.drop_duplicates()

# Convert categorical to numeric
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

print("\nAfter Cleaning:\n", df.isnull().sum())

# ================== FEATURE ENGINEERING ==================

# Create Age Group
df['Age_Group'] = pd.cut(df['Age'],
                        bins=[0,12,18,35,60,100],
                        labels=['Child','Teen','Young Adult','Adult','Senior'])

# ================== DESCRIPTIVE STATS ==================
print("\nFare Stats:\n", df['Fare'].describe())
print("\nSurvival Count:\n", df['Survived'].value_counts())

# ================== GROUPBY ANALYSIS ==================
print("\nSurvival by Gender:\n", df.groupby('Sex')['Survived'].mean())
print("\nSurvival by Class:\n", df.groupby('Pclass')['Survived'].mean())

# ================== VISUALIZATION ==================

# 1. Pie Chart - Survival
plt.figure()
df['Survived'].value_counts().plot(kind='pie', autopct='%1.1f%%',
                                   labels=['Not Survived', 'Survived'])
plt.title("Survival Distribution")
plt.ylabel("")
plt.savefig(f"{output_folder}/pie_survival.png")
plt.close()

# 2. Survival by Gender
plt.figure()
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival by Gender")
plt.savefig(f"{output_folder}/survival_gender.png")
plt.close()

# 3. Survival by Class
plt.figure()
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Survival by Class")
plt.savefig(f"{output_folder}/survival_class.png")
plt.close()

# 4. Age Distribution
plt.figure()
plt.hist(df['Age'], bins=20)
plt.title("Age Distribution")
plt.savefig(f"{output_folder}/age_distribution.png")
plt.close()

# 5. Fare Distribution
plt.figure()
sns.histplot(df['Fare'], bins=20, kde=True)
plt.title("Fare Distribution")
plt.savefig(f"{output_folder}/fare_distribution.png")
plt.close()

# 6. Boxplot - Age vs Survival
plt.figure()
sns.boxplot(x='Survived', y='Age', data=df)
plt.title("Age vs Survival")
plt.savefig(f"{output_folder}/box_age_survival.png")
plt.close()

# 7. Scatter Plot - Age vs Fare
plt.figure()
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df)
plt.title("Age vs Fare")
plt.savefig(f"{output_folder}/scatter_age_fare.png")
plt.close()

# 8. Heatmap
plt.figure()
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.savefig(f"{output_folder}/heatmap.png")
plt.close()

# 9. Violin Plot - Fare by Class
plt.figure()
sns.violinplot(x='Pclass', y='Fare', data=df)
plt.title("Fare by Class")
plt.savefig(f"{output_folder}/violin_fare_class.png")
plt.close()

# 10. Age Group vs Survival
plt.figure()
sns.countplot(x='Age_Group', hue='Survived', data=df)
plt.title("Survival by Age Group")
plt.savefig(f"{output_folder}/agegroup_survival.png")
plt.close()

# ================== SAVE CLEANED DATA ==================
df.to_csv("cleaned_titanic_data.csv", index=False)

print("\n✅ All graphs saved in 'titanic_visualization' folder")
print("✅ Cleaned dataset saved as 'cleaned_titanic_data.csv'")