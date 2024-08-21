Objective: Address Quality Classification

The objective of this assignment is to classify customer addresses into three categories: good, medium, and bad. I used Google Validation API to enhance the address data and perform the classification.

Project Documentation:

1. Installing Required Libraries

2. Importing Libraries
This step involves importing standard libraries like pandas and numpy for data handling, requests for API calls, and seaborn and matplotlib for data visualization, scikit-learn for model training.

3. Loading the Address Dataset
Loading the address dataset into a pandas DataFrame from Excel file using pd.read_excel.

4. Exploratory Data Analysis (EDA)
Conducted an exploratory data analysis (EDA) to understand the structure, distribution, and key characteristics of the dataset. Checked for missing values, data distributions, and identified any potential outliers or patterns in the data.

5. Data Preprocessing
Preprocessed the dataset to prepare it for model training. Handled missing values, encoded categorical variables, scaling features, and performing data balancing techniques like SMOTE (Synthetic Minority Over-sampling Technique) to address class imbalances.

6. Feature Engineering
Created new features that can enhance model performance.

7. Model Training
Split the dataset into training and testing sets using train_test_split. Train a classification model (e.g., RandomForestClassifier, GradientBoostingClassifier) to predict the quality of addresses.

8. Model Evaluation
Evaluated the trained model using metrics like accuracy, classification report, and confusion matrix. This helped in assessing how well the model performs on the test data.

9. Saving the Model
Saved the trained model, label encoder, and any other necessary objects to disk using Python’s pickle module. These saved files used later for deployment.

10. Create Flask API
Createed the Flask App for address quality classification and used saved trained model file for prediction in the flask api.

11. Create the Dockerfile
Created a Dockerfile in the project directory to containerize the Flask app. The Dockerfile contains instructions to set up the environment, copy the necessary files, install dependencies, and run the Flask app.

12. Model Deployment to GCP
Build the Docker image and Pushed the Docker image to GCP Artifact Registry.

13. Testing and Monitoring
Test the deployed API using Postman to ensure it works as expected.
Monitor the app’s performance and logs through the GCP Console.
