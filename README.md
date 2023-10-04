
# The Oval Table - Oil Price Prediction Models (v1)

Welcome to the Oval Table's repository for oil price prediction project. Our team has delved deep into the world of machine learning to develop models that will aim to predict oil prices. This repository contains all the code, data, and results from our exploration and modeling.


## Version

__Cycle 1 (v1)__: This is the first version of our project, and we aim to improve and refine our models in subsequent cycles.
## Key Features

1. __Data Exploration__: Dive into our datasets, we used histograms and plots to understand and visualization.

2. __Model Training__: We've trained three primary models:
- __XGBoost__: A gradient boosting framework that uses decision trees.
- __Random Forest__: An ensemble learning method that operates by constructing multiple decision trees.
- __Polynomial Regression__: A regression algorithm that models the relationship between the input and output as an nth degree polynomial.

4. __Model Evaluation__: For each model, we've plotted:
- __Actual vs. Predicted__: See how our model's predictions compared against the actual values.
- __Learning Curve__: Understand the model's performance as more data is used for training.
- __Feature Importance__: (For models that support it) Understand which features are most influential in making predictions.

5. __Baseline Model__: We've also included a _naive forecast_ as a baseline to compare our models against.
## Known Bugs/Issues

- __Overfitting__: Our models tend to overfit on the training data. We're actively researching ways to mitigate this in our next cycle.

- __Data Limitations__: Some inconsistencies in the data might affect model performance. We're looking into refining our data preprocessing steps.
