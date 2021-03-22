from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('api/get-codes/', views.MorseCodesView.as_view()),
    path('api/get-words/', views.WordsFrecuencyView.as_view()),
    path('api/translate/2morse', views.Translate2Morse.as_view(), name='2morse'),
    path('api/translate/2human', views.Translate2Human.as_view(), name='2human'),
    path('api/translate/bit2morse', views.DecodeBits2Morse.as_view(), name='bit2morse'),
    path('api/translate/bit2human', views.DecodeBits2Human.as_view(), name='bit2human'),
    path('api/token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    
]
