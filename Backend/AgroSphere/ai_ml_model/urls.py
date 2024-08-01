from django.urls import path
from . import views

urlpatterns = [
    # path('predict/', views.predict, name='predict'),
    path('predict/', views.PredictView.as_view(), name='predict'),
]