from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PredictionSerializer, Crop_Prediction_Serializer
import joblib
import numpy as np

# Load the trained model
model_path_1 = "ai_ml_model/trained_data/trained_model_yield.pkl"
model_1 = joblib.load(model_path_1)
model_path_2 = "ai_ml_model/trained_data/trained_model_crop_recommendation_2.pkl"
model_2 = joblib.load(model_path_2)
model_path_3 = "ai_ml_model/trained_data/trained_model_fertilizer.pkl"
model_3 = joblib.load(model_path_3)

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
            
            prediction = model_1.predict(features)
            result = prediction[0]
            return Response({"prediction": result}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score
# import joblib

# # Step 1: Load the Data
# data = pd.read_csv('ai_ml_model/csv_data/crop_recommendation.csv')

# # Step 2: Preprocess the Data
# X = data.drop('label', axis=1)
# y = data['label']

# # Step 3: Train-Test Split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Step 4: Model Selection
# model = RandomForestClassifier(n_estimators=100, random_state=42)

# # Step 5: Train the Model
# model.fit(X_train, y_train)

# # Step 6: Evaluate the Model
# y_pred = model.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# print(f'Accuracy: {accuracy}')

# # Save the model
# joblib.dump(model, 'ai_ml_model/trained_data/trained_model_yield_2.pkl')

class Crop_Prediction(APIView):
    def post(self, request, *args, **kwargs):
        serializer = Crop_Prediction_Serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            # Create feature array
            features = np.array([[data['N'], data['P'], data['K'], data['temperature'], data['humidity'], data['ph'], data['rainfall']]])
            
            # Predict using the model
            prediction = model_2.predict(features)
            result = prediction[0]

            return Response({"prediction": result}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score

# # Step 1: Load the Data
# data = pd.read_csv('ai_ml_model/csv_data/crop_recommendation.csv')

# # Step 2: Preprocess the Data
# X = data.drop('label', axis=1)
# y = data['label']

# # Step 3: Train-Test Split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Step 4: Model Selection
# model = RandomForestClassifier(n_estimators=100, random_state=42)

# # Step 5: Train the Model
# model.fit(X_train, y_train)

# # Step 6: Evaluate the Model
# y_pred = model.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# print(f'Accuracy: {accuracy}')

# # Step 7: Predict
# sample_data = [[90, 42, 43, 20.87974371, 82.00274423, 6.502985292000001, 202.9355362]]
# prediction = model.predict(sample_data)
# print(f'Predicted Crop: {prediction[0]}')