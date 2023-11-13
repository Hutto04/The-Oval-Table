# The Oval Table - Oil Price Prediction Models (v2)

Welcome to the Oval Table's repository for our oil price prediction project. Our team has embarked on an ambitious journey into machine learning to develop models aimed at predicting future oil prices. This repository is a comprehensive suite of our models, findings, and insights.

## Key Features

1. __Data Exploration__: Dive into our datasets, we used histograms and plots to understand and visualization.

2. __Model Training__: We've trained three primary models in __Cycle 1__:
- __XGBoost__: A gradient boosting framework that uses decision trees.
- __Random Forest__: An ensemble learning method that operates by constructing multiple decision trees.
- __Polynomial Regression__: A regression algorithm that models the relationship between the input and output as an nth degree polynomial.

For __Cycle 2__ we've added 3 additional models, that was __time series__ models for future oil price forecasting:
-  __ARIMA__
- __Prophet__
- __XGBoost (Time Series)__

3. __Model Evaluation__: For each model, we've plotted:
- __Actual vs. Predicted__: See how our model's predictions compared against the actual values.
- __Learning Curve__: Understand the model's performance as more data is used for training.
- __Feature Importance__: (For models that support it) Understand which features are most influential in making predictions.

4. __Baseline Model__: We've also included a _naive forecast_ as a baseline to compare our models against.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing
To get the project running, follow these steps:

1. Clone the repo:
```bash
git clone https://github.com/Hutto04/The-Oval-Table.git
```
2. Navigate to the project directory:
```bash
cd The-Oval-Table
```

### Dependencies

Ensure you have the following dependencies installed:

- Flask
- matplotlib
- numpy
- pandas
- gunicorn
- pytest
- joblib
- scikit-learn
- statsmodels
- jupyter notebook
- A virtual environment manager like conda

### Executing Program

1. Activate your virtual environment (e.g., conda or venv).

2. Start Jupyter Notebook:
```bash
jupyter notebook
```

3. Navigate to the desired notebook and run it.

## Help

For help and support, please open an issue in the GitHub repository.

## Detailed Documentation

For an in-depth understanding of our project, methodologies, and results, please refer to our [detailed documentation](https://mariamills.github.io/Oil-Price-Prediction-Documentation/).

## Interactive Web Interface

Explore our data, models, and results interactively through our [web interface](https://oil-price-prediction.onrender.com/). Ideal for non-tech users to quickly visualize data correlations, model metrics, and predictions.

## Authors

- Maria Mills

- Jae Kim

- William (Bruce) Hutto

- Gurpreet Singh

## Version History

__Cycle 1 (v1)__: This was the first version of our project, and we aim to improve and refine our models in subsequent cycles. Initial start with Naive Forecast, Random Forest, XGBoost, and Polynomial Regression models.

__Cycle 2 (v2)__: Focused on time series models for forecasting future oil prices. Added ARIMA, Prophet, and Time Series XGBoost to our suite.

## Known Bugs/Issues

- __Overfitting__: Our models tend to overfit on the training data. We're actively researching ways to mitigate this in our next cycle.

- __Data Limitations__: Some inconsistencies in the data might affect model performance. We're looking into refining our data preprocessing steps.

- As of this writing, our time series models are not yielding the expected performance levels with the current dataset. The underlying reasons for this are not entirely clear to us yet. We are investigating potential causes, including exploring the possibility of errors in our approach.

## Notes
- __Cycle 2 Challenges__: Despite our efforts, we faced overfitting issues and found that ARIMA might not be the best fit for our data. The steep learning curve and limited time frame posed significant challenges in improving our time series models.

## License

This project is licensed under the APGL-3.0 License

## Acknowledgments

Special thanks to all contributors and supporters of this project.
