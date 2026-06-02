# Titanic Passenger Survival Analysis Using Python & Tableau

A beginner-friendly data analytics project that analyzes Titanic passenger survival patterns using Python, Pandas, and Tableau. The project demonstrates how raw passenger data can be cleaned, transformed, analyzed, and visualized to generate meaningful insights about survival rates, passenger demographics, ticket fares, and travel classes.

This project focuses on passenger survival analysis, fare distribution, demographic trends, and interactive dashboard creation using Tableau.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Tableau
* CSV Dataset

---

## Flow of Project

**Data Collection → Data Cleaning → Feature Engineering → Statistical Analysis → Data Visualization (Matplotlib & Seaborn) → Data Export (CSV) → Tableau Dashboard Creation → Survival Insight Reporting**

---

# Project Features

## 1. Data Extraction

Imported Titanic passenger dataset from CSV file.

Dataset includes:

* Passenger Class (Pclass)
* Gender (Sex)
* Age
* Fare
* Embarked Port
* Survival Status
* Age Group

---

## 2. Data Cleaning & Preparation

* Handled missing values in Age and Embarked columns
* Removed duplicate records
* Verified data types for all features
* Prepared dataset for analysis and visualization
* Created structured dataset for Tableau dashboarding

---

## 3. Feature Engineering

Created additional analytical features:

* Age Group Classification

  * Child
  * Teen
  * Young Adult
  * Adult
  * Senior

Performed categorical encoding and data transformation where required.

---

## 4. Statistical Analysis

Performed descriptive analysis on passenger data:

* Mean Age
* Average Fare
* Survival Rate
* Passenger Distribution by Class
* Passenger Distribution by Gender

Analyzed:

* Minimum and Maximum Fare
* Age Distribution
* Survival Trends Across Categories

---

## 5. Business (Passenger) Analytics

Conducted multiple passenger behavior analyses:

### Survival Analysis

* Passenger survival distribution
* Survival rate by class
* Survival rate by gender

### Fare Analysis

* Fare distribution across passenger classes
* Relationship between fare and survival

### Demographic Analysis

* Age-wise passenger distribution
* Age group survival trends

### Travel Analysis

* Embarkation port analysis
* Passenger class comparison

---

## 6. Data Visualization (Matplotlib & Seaborn)

Generated multiple visualizations including:

* Histogram (Age Distribution)
* Scatter Plot (Age vs Fare)
* Box Plot (Fare Distribution by Passenger Class)
* Heatmap (Survival Rate Analysis)
* Bar Charts (Gender & Survival Analysis)
* Treemap (Age Group Distribution)
* Dual Axis Chart (Survival Count & Average Fare)

Saved visualizations for reporting and dashboard development.

---

## 7. Data Export for Visualization Tools

* Exported cleaned dataset to CSV format
* Prepared dataset for Tableau integration
* Ensured compatibility for dashboard creation

---

## 8. Tableau Dashboard Integration

Imported cleaned dataset into Tableau and created interactive dashboards including:

### Age vs Fare Analysis

Examines the relationship between passenger age and ticket fare.

### Survival Count and Average Fare by Passenger Class

Compares survival counts and fare levels across classes.

### Survival Rate by Passenger Class and Embarkation Port

Visualizes survival trends using a heatmap.

### Fare Distribution by Passenger Class

Identifies fare variation and outliers through box plots.

### Passenger Distribution by Age Group and Survival Status

Highlights demographic distribution using a treemap.

### Survival Comparison by Gender

Analyzes survival differences between male and female passengers.

### Age Distribution of Passengers

Shows passenger age patterns using a histogram.

---

## 9. Insight Generation

The analysis provided several important insights:

* First-class passengers had significantly higher survival rates.
* Female passengers were more likely to survive than male passengers.
* Higher ticket fares were generally associated with better survival outcomes.
* Most passengers belonged to the young adult age group.
* Passenger class played a major role in survival probability.
* Survival rates varied across embarkation ports.
* Several fare outliers were identified, particularly among first-class passengers.

These insights help understand the factors influencing passenger survival aboard the Titanic.

---

# Project Outcome

This project demonstrates a complete data analytics workflow including data cleaning, feature engineering, statistical analysis, visualization, and dashboard development.

It showcases the ability to transform raw passenger data into meaningful insights and build interactive Tableau dashboards for data-driven analysis and decision-making.

The project highlights practical skills in Python, exploratory data analysis (EDA), data visualization, and business intelligence reporting using Tableau.
