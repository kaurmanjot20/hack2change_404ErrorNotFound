from django.urls import path
from . import views

urlpatterns = [
    # path('predict/', views.predict, name='predict'),
    path('predict/', views.PredictView.as_view(), name='predict'),
    path('crop_prediction/', views.Crop_Prediction.as_view(), name='crop_prediction'),
]