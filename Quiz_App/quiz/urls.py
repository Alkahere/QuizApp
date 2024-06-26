from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('quizzes/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz_detail/', views.quiz_detail, name='quiz_detail_html'),  # URL for quiz_detail.html
    path('logout/', views.logout_view, name='logout'),
]
