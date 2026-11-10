# Machine Learning Model Lab

*Currently Incomplete*

The goal of this project is to simplify user's workflow by directly uploading a CSV and finding correlations and to what extent.

## Technologies Used
| Technology | Purpose |
|---|---|
| Streamlit | Interactive frontend |
| pandas | Data analysis |
| NumPy | Computations and Arrays |
| scikit-learn | Machine learning and preprocessing |
| Plotly | Data visualizations |
| joblib | Saving a model |
| pytest | Testing |

*This entire project will be done in Python*

*This may be edited!*
## Final Result 

### 1. Dataset Upload & Validation
- Upload CSV datasets.
- Identify duplicate rows and potentially problematic columns.
- Organize rows and columns.

### 2. Exploratory Data Analysis
- Visualize quantative and categorical variables.
- Generate correlation graphs.
- Identify missing values and potential outliers.
- Generate downloadable dataset summaries.

### 3. Data Preprocessing
- Missing-value imputation.
- Feature scaling and categorical encoding.
- Configurable training, validation, and testing splits.

### 4. Model Training
Support for multiple regression and classification algorithms.

**Regression**
- Linear Regression
- Ridge Regression
- Random Forest Regressor

**Tree Models**
- Gradient Boosting Regressor
- Random Forest Classifier
- XGB Regressor
  
### 5. Model Evaluation & Comparison
Compare models using proper evaluations metrics.

**Regression metrics**
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

### 6. Hyperparameter Optimization
- RandomizedSearchCV
- GridSearchCV
- Comparison of baseline and optimized performance.

### 7. Model Export
- Export trained models using joblib.
- Download experiment summaries.
- Export prediction results.

## Project Architecture
*Will be determined as project approaches final structure*

## Checklist

- [x] Initial project planning and architecture
- [X] CSV upload and dataset validation
- [ ] Exploratory data analysis
- [ ] Data preprocessing pipelines
- [ ] Baseline model implementation
- [ ] Model training and comparison
- [ ] Cross-validation and evaluation
- [ ] Hyperparameter optimization
- [ ] Model explainability
- [ ] Model and report exports
- [ ] Automated testing
- [ ] Deployment
