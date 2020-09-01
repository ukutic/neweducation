from django.urls import path
from . import views

app_name = 'wings'

urlpatterns = [
    path('',views.Index.as_view(),name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]