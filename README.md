# 🌾 Crop Yield Predictor API

A FastAPI-based Machine Learning API that predicts the expected **Crop Yield (Tonnes per Hectare)** using a trained **XGBoost Regression** model integrated with a Scikit-learn preprocessing pipeline.

The API accepts agricultural and geographical information as input and returns the predicted crop yield.

---

# 🚀 Features

- Predicts Crop Yield (Tonnes per Hectare)
- RESTful API built with FastAPI
- Automatic preprocessing using Scikit-learn Pipeline
- Supports unknown categorical values safely
- JSON-based requests and responses
- Interactive Swagger Documentation
- Single trained model (`crop_model.joblib`)

---

# 🛠️ Technologies Used

- Python
- FastAPI
- Scikit-learn
- XGBoost
- Pandas
- NumPy
- Joblib
- Uvicorn

---

# 📂 Project Structure

```
predictor/
│
├── app.py
├── crop_model.joblib
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📥 Input Features

The API expects the following information:

| Feature | Type | Description |
|----------|------|-------------|
| Crop | String | Name of the crop |
| Year | String | Cultivation year |
| Area_Hectares | Float | Cultivated land area in hectares |
| Season | String | Growing season |
| State | String | State name |
| District | String | District name |
| Latitude | Float | Latitude of the location |
| Longitude | Float | Longitude of the location |

---

# 📤 Output

The API returns the predicted crop yield in tonnes per hectare.

Example Response

```json
{
    "prediction": [
        2.87
    ]
}
```

---

# ▶️ Running the API

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start the Server

```bash
uvicorn app:app --reload
```

The API will be available at

```
http://127.0.0.1:8000
```

---

# 📚 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 📩 Prediction Endpoint

### POST

```
/predict
```

---

## Sample Request

```json
{
    "Crop": "Rice",
    "Year": "2023",
    "Area_Hectares": 5.2,
    "Season": "Kharif",
    "State": "Tamil Nadu",
    "District": "Thanjavur",
    "Latitude": 10.79,
    "Longitude": 79.13
}
```

---

## Sample Response

```json
{
    "prediction": [
        2.84
    ]
}
```

---

# 🧠 Prediction Workflow

```
Client Request
      │
      ▼
FastAPI Endpoint
      │
      ▼
Input Validation (Pydantic)
      │
      ▼
Scikit-learn Pipeline
      │
      ├── Numerical Feature Processing
      ├── One-Hot Encoding
      ▼
XGBoost Regression Model
      │
      ▼
Predicted Crop Yield
      │
      ▼
JSON Response
```

---

# 📈 Model Information

| Model | XGBoost Regressor |
|--------|-------------------|
| Target | Yield_Tonnes_per_Hectare |
| Pipeline | Scikit-learn Pipeline |
| Encoding | OneHotEncoder |
| Numerical Processing | ColumnTransformer |

---

# 📌 Example Use Cases

- Agricultural Yield Prediction
- Crop Production Analysis
- Decision Support Systems
- Smart Farming Applications
- Agricultural Research
- Educational Demonstrations

---

# 👩‍💻 Author

**Snow Varshini V**

Artificial Intelligence & Machine Learning Engineer

---

# 📄 License

This project is intended for educational and research purposes.
