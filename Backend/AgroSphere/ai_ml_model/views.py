from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PredictionSerializer
import joblib
import numpy as np

# Load the trained model
model_path = "ai_ml_model/trained_data/trained_model_yield.pkl"
model = joblib.load(model_path)

# state_name_encoding = {'andhra pradesh': 0, 'arunachal pradesh': 1, 'assam': 2}  # Example
crop_type_encoding = {'rabi': 0, 'whole year': 1, 'summer': 2, 'kharif':3}  # Example
# crop_encoding = {'cotton': 0, 'horsegram': 1, 'jowar': 2}  # Example

state_names = [
    "andhra pradesh", "arunachal pradesh", "assam", "bihar", "goa", "gujarat", "haryana", 
    "jammu and kashmir", "karnataka", "kerala", "madhya pradesh", "maharashtra", "manipur", 
    "meghalaya", "mizoram", "nagaland", "odisha", "punjab", "rajasthan", "tamil nadu", 
    "telangana", "uttar pradesh", "west bengal", "chandigarh", "dadra and nagar haveli", 
    "himachal pradesh", "puducherry", "sikkim", "tripura", "andaman and nicobar islands", 
    "chhattisgarh", "uttarakhand", "jharkhand"
]

crops = [
    "cotton", "horsegram", "jowar", "maize", "moong", "ragi", "rice", "sunflower", "wheat", 
    "sesamum", "soyabean", "rapeseed", "jute", "arecanut", "onion", "potato", "sweetpotato", 
    "tapioca", "turmeric", "barley", "banana", "coriander", "garlic", "blackpepper", "cardamom", 
    "cashewnuts", "blackgram", "coffee", "ladyfinger", "brinjal", "cucumber", "grapes", "mango", 
    "orange", "papaya", "tomato", "cabbage", "bottlegourd", "pineapple", "carrot", "radish", 
    "bittergourd", "drumstick", "jackfruit", "cauliflower", "watermelon", "ashgourd", "beetroot", 
    "pomegranate", "ridgegourd", "pumpkin", "apple", "ginger"
]

state_name_encoding = {state: idx for idx, state in enumerate(state_names)}
crop_encoding = {crop: idx for idx, crop in enumerate(crops)}

# print("State Name Encoding:", state_name_encoding)
# print("Crop Encoding:", crop_encoding)

class PredictView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PredictionSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            # Encode categorical variables
            state_name = state_name_encoding.get(data['State_Name'], -1)
            crop_type = crop_type_encoding.get(data['Crop_Type'], -1)
            crop = crop_encoding.get(data['Crop'], -1)

            if state_name == -1 or crop_type == -1 or crop == -1:
                return Response({"error": "Invalid categorical input"}, status=status.HTTP_400_BAD_REQUEST)

            # Create feature array
            features = np.array([[state_name, crop_type, crop, data['N'], data['P'], data['K'],
                                  data['pH'], data['rainfall'], data['temperature'], data['Area_in_hectares']]])
            
            prediction = model.predict(features)
            result = prediction[0]
            return Response({"prediction": result}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)