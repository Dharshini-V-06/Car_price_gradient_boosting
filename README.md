# Car Price Prediction App 🚗

This project is a **machine learning web application** that predicts the **selling price of used cars** based on various features like year, present price, kilometers driven, fuel type, seller type, transmission, and number of previous owners. The app is built using **Python**, **Streamlit**, and **Gradient Boosting Regressor**.

---

Dataset link: [Car price prediction dataset](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho?select=car+data.csv)

App link: [Car price prediction app](https://carpricegradientboosting-sanwk2ynwlnh6nv6k6mlz8.streamlit.app/)


## Dataset

* The dataset `car data.csv` contains **301 rows and 9 columns**:

  * `Car_Name` – Name of the car
  * `Year` – Year of purchase
  * `Selling_Price` – Price at which the car is sold (target variable)
  * `Present_Price` – Current price of the car
  * `Kms_Driven` – Distance driven in kilometers
  * `Fuel_Type` – Fuel type (Petrol, Diesel, CNG)
  * `Seller_Type` – Seller type (Dealer, Individual)
  * `Transmission` – Transmission type (Manual, Automatic)
  * `Owner` – Number of previous owners

* No missing values were found in the dataset.

* Some duplicate rows were present and can be removed if needed.

---

## Data Preprocessing

1. **Dropped `Car_Name`** as it is not needed for prediction.
2. **Checked for skewness** in numeric columns:

   * `Present_Price`, `Kms_Driven`, `Selling_Price` were slightly skewed.
   * Log transformation can be applied if needed (`np.log1p`).
3. **Label Encoding** of categorical columns:

   * `Fuel_Type`, `Seller_Type`, `Transmission`

---

## Model

* **Algorithm:** Gradient Boosting Regressor

* **Hyperparameter Tuning:** GridSearchCV with 5-fold cross-validation

* **Best Parameters Found:**

  ```python
  {'learning_rate': 0.1, 'max_depth': 4, 'n_estimators': 100}
  ```

* **Model Performance on Training Data:**

  * RMSE: 0.1977
  * R²: 0.9984

* The trained model is saved as `car_price.pkl`.

---

## Streamlit Web App

* Users can input car details via sidebar:

  * Year of Purchase
  * Present Price
  * Kms Driven
  * Fuel Type
  * Seller Type
  * Transmission Type
  * Number of Previous Owners

* App predicts the **estimated selling price** of the car.

---





## File Structure

```
Car-Price-Prediction/
│
├── car data.csv         # Dataset
├── app.py               # Streamlit application
├── car_price.pkl        # Trained model and LabelEncoder
├── README.md            # Project description
└── requirements.txt     # Required Python packages
```

---

