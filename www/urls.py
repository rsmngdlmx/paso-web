from django.urls import path
from www import views

urlpatterns = [
    path('', views.BioView.as_view(), name='bio'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    path('cv/', views.CVView.as_view(), name='cv')
]
