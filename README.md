# Diabetes Prediction and Deployment Project

## Overview

This project focuses on predicting diabetes using the Random Forest Regressor algorithm. It includes Exploratory Data Analysis (EDA) to understand the dataset, model training, and deployment of the trained model on an AWS instance.

## Table of Contents

* [Project Description](#project-description)
* [EDA](#eda)
* [Model Training](#model-training)
* [Deployment](#deployment)
* [Installation](#installation)
* [Usage](#usage)
* [Data Source](#data-source)
* [Dependencies](#dependencies)


## Project Description

The primary goal of this project is to develop a predictive model that can accurately determine the likelihood of a person having diabetes based on various health-related features.  The Random Forest Regressor model was chosen for its effectiveness in handling complex datasets and providing robust predictions.  In addition to model development, this project emphasizes the importance of EDA in gaining insights from the data and the practical aspect of deploying the model to a cloud environment (AWS) for real-world accessibility.

## EDA

Exploratory Data Analysis (EDA) was performed to gain a better understanding of the dataset. This involved:

* Analyzing the distribution of individual features.
* Identifying potential outliers.
* Examining relationships between different features.
* Visualizing the data using plots (e.g., histograms, pairplots, box plots).
* Checking for missing values and handling them appropriately.

## Model Training

The project utilizes the Random Forest Regressor model for predicting diabetes. The training process involved:

* Splitting the dataset into training and testing sets.
* Training the Random Forest Regressor model on the training data.
* Evaluating the model's performance on the testing data using appropriate metrics (e.g., Mean Squared Error, R-squared).
* Hyperparameter tuning to optimize model performance.

## Deployment

The trained Random Forest Regressor model has been deployed on an AWS instance. This allows for accessing the model through an application.  Key aspects of the deployment include:

* Creating an EC2 instance on AWS.
* Setting up the necessary environment and dependencies on the EC2 instance.
* Deploying the model using Flask.
* Configuring the application to receive input data and return predictions.
* Ensuring the application is accessible over the internet.

## Installation

To run this project, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone (https://github.com/Akshit-77/Diabetes-prediction-Deployed)
    cd Diabetes-prediction-Deployed
    ```

2.  **Set up a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Application Locally (for development/testing):

1.  Ensure you have followed the [Installation](#installation) instructions.
2.  Navigate to the project directory:
    ```bash
    cd Diabetes-prediction-Deployed
    ```
3.  Run the Flask application:
    ```bash
    python app.py
    ```
    The application will start running on a local server (e.g., `http://127.0.0.1:8080/`).
4.  You can then send a POST request to the server by clicking on Submit button with the required data to get a prediction. 

## Data Source

The dataset used in this project is the Pima Indians Diabetes Database, which is available from the UCI Machine Learning Repository.

## Dependencies

The project uses the following Python libraries:

* Python (>=3.7)
* pandas
* scikit-learn
* Flask
* Other common packages: numpy, matplotlib, seaborn
* The specific versions of the packages are listed in the `requirements.txt` file.

