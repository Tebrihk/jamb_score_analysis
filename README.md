# Jamb_score_analysis

#  Overview
This project analyzes JAMB (Joint Admissions and Matriculation Board) exam scores of 2022 to uncover key trends, understand contributing factors, and predict future scores using machine learning. The analysis focuses on identifying patterns in student performance and providing actionable insights to improve exam results.

# Key Questions Addressed
1 What is happening to JAMB scores and student performance?
2 Why are these trends occurring?
3 How can we predict future JAMB scores?
4 Where are changes needed to improve student outcomes?

# Tools
Excel and jupyther notebook python

# Dataset Description
The dataset contains multiple features related to student performance, study habits, school conditions, and parental involvement.
DATA TYPE: structured data

 Key Columns Used
JAMB_Score (Target Variable) – Exam scores (0 - 400).
Study_Hours_Per_Week – Weekly study hours.
Attendance_Rate – Student’s attendance percentage.
Teacher_Quality (1-5) – Quality rating of teachers.
Distance_To_School – Distance from home to school.
School_Type – Public or private.
School_Location – Urban or rural.
Extra_turorails - Yes or NOo.
Access_to_learning_materials - yes or No.
Parent_Involvement – High, medium, or low.
IT_Knowledge – Student’s tech literacy (high, medium, low).
Student_Id - Student identification number.
Age - student age.
Gender - student gender (male or female).
Socioeconomic_Status – Family’s financial background.
Parent_Education_Level – Primary, secondary, or tertiary education.
Assignment_completed - rate of assignment completion (1-5).

# Data Cleaning & Preprocessing
1 Handling Missing Values: Remove all missing or null rows.
2 Encoding Categorical Variables: Converted categorical data (e.g., School_Type, Parent_Involvement) to numerical format.
   this is to help in the analysis and visualization process.
3 Removing Irrelevant Columns: Dropped non-contributing columns like Student_ID and Gender.
  Columns that don't contribute to answering our questions.
  Columns that have too many missing values.
  columns that are redundant and/or identifiers.
4 Outlier Detection & Removal: Used boxplots to identify and remove extreme outliers.
5 Feature Scaling: Standardized numerical features for better model performance.

# Exploratory Data Analysis (EDA)
 Key Findings
1. With a correlation of 0.42 shows that study hours does not necessarily mean higher scores.
2. High attendance does not lead to higher JAMB scores with a correlation score of 0.28.
3. Private school students perform slightly better than public school students.
     with an average score of
     public schools = 171.6
     private schools = 181.2
![alt text](https://github.com/Tebrihk/jamb_score_analysis/blob/main/charts/jamb%20school_type.JPG?raw=true)
   
5. Parental involvement plays a crucial role in student success.
     with average of
     low: 167.2
     Meduim: 172.2
     High: 188.8

# Predictive Modeling
Using Linear Regression to predict JAMB scores based on key factors.

Steps for Model Training
1 Feature Selection: Used Study_Hours_Per_Week, Attendance_Rate, Teacher_Quality, and Distance_To_School.
2 Train-Test Split: 80% training data, 20% testing data.
3 Model Training: Applied Linear Regression for initial predictions.
4 Evaluation Metrics:

Mean Absolute Error (MAE) – Measures prediction error.
Mean Squared Error (MSE) – Penalizes large errors.
R² Score – Explains how well the model fits the data.

 Model Performance
MAE: ~15-20 points deviation.
R² Score: ~0.75 (Good fit, but can be improved).

# Insights & Recommendations
 Increase Study Hours: More dedicated study time improves scores.
 Improve Attendance: Students who attend school regularly perform better.
 Enhance Teacher Quality: Training programs for teachers can boost student outcomes.
 Reduce Student Travel Distance: Providing boarding or transport assistance can help.
 Encourage Parental Involvement: Higher engagement from parents leads to better student performance.
