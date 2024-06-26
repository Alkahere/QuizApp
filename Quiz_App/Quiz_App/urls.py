from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz.urls')),  # Include app-level URLs
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Login URL
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout URL
]
