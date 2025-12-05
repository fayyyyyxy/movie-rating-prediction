# Movie Critic Rating Prediction

This project explores how well we can predict critic ratings for movies using basic movie metadata (runtime, MPAA rating, genres, and release/streaming dates). 
The workflow focuses on using movies released before 2010 to train models and then evaluating performance on movies released in 2010 and later.

## Data

This project uses the movies table stored on the NU MLDS PostgreSQL server (in the `everything2025` database, `public` schema).  

Access to the NU MLDS database and connection credentials are needed (not included in this repo).

All the datasets CSV used in the notebooks are also checked into this repo under `data/` (not ignored), so can run the notebooks without re-pulling from the database.

## Repository Structure

- `data/`
  -  Original CSVs pulled from database `movies_data.csv`
  -  `movies_popular_pre2010.csv` for EDA
  -  leaned and derived data files used for modeling, including:
      - `movies_clean.csv` – cleaned version of the full movie dataset  
      - `X_train_movies.csv`, `y_train_movies.csv` – training features/targets  
      - `X_test_movies.csv`, `y_test_movies.csv` – test features/targets  

- `src/`
  - `get_data.py`
    Script that connects via `psycopg` and writes the raw data to `data/`.
    
  - `cleaning_EDA/`  
    Helper code and notebooks focused on data cleaning and exploratory data analysis (EDA) for the movie data.

  - `feat_eng.ipynb`  
    Notebook for feature engineering and data preparation:
    - creates training and test splits (pre-2010 vs 2010+)  
    - builds engineered features (e.g., `kid_friendly`, `kid_family`, `days_to_stream`, `holiday_blockbuster`)  
    - constructs `X_train`, `X_test`, `y_train`, `y_test`.

  - `modeling.ipynb`
    Notebook for modeling and evaluation:
    - fits multiple linear regression models (Models 1–6) using different feature sets  
    - evaluates models using R², MAE, and RMSE on the test set  
    - inspects coefficients and p-values (via statsmodels) to understand which features help predict critic ratings.

## How to Run

1. Create and activate a Python environment (e.g., via `venv` or `conda`).
2. Install dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt


This repo is primarily intended as a final project for the Northwestern MLDS Programming for Data Science course, showing an end-to-end workflow: cleaning → feature engineering → modeling → evaluation on a movie ratings prediction task.
