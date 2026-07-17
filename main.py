from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

package = joblib.load("Crop_modell.joblib")
app = FastAPI()

class CropFeatures(BaseModel):
    Crop : str
    Year : str
    Area_Hectares : float
    Season : str
    State : str
    District : str
    Latitude : float
    Longitude : float

@app.get('/')
def home():
    return{"message" : "heyyyooo"}

@app.post('/predict')
async def predictor(features:CropFeatures):
    input_data = pd.DataFrame([{
        "Area_Hectares": float(features.Area_Hectares),
        "Latitude": float(features.Latitude),
        "Longitude": float(features.Longitude),
        "Crop": str(features.Crop),
        "Year": str(features.Year),       
        "State": str(features.State),
        "District": str(features.District),
        "Season": str(features.Season)
}])
    prediction = package.predict(input_data)
    score = float(prediction[0]) if hasattr(prediction, '__len__') else float(prediction)

    if score >= 75:
        message = "The crop has excellent cropping pattern"
    elif score >= 60:
        message = "The crop has good cropping pattern"
    elif score >= 40:
        message = "The crop had average cropping pattern"
    else:
        message = "The crop has bad cropping pattern"

    return {"prediction": prediction.tolist(), "message": message}