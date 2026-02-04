from django.urls import path
from . import views
from django.contrib.auth import views as logout_views

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    
    #アカウント
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', logout_views.LogoutView.as_view(), name='logout'),
    path('account/', views.AccountUpdateView.as_view(), name='account'),
    path('profile/', views.ProfileUpdateView.as_view(), name='profile'),

    #店舗詳細
    path('restaurant/<int:PK>/', views.RestaurantDetailView.as_view(), name='restaurant_detail'),
]
