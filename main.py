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
    return{"message" : "heyyyo000"}

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
    return {"prediction" : prediction.tolist()}