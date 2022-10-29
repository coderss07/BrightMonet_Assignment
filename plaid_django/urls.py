"""plaid_django URL Configuration """

from django.contrib import admin
from django.urls import path, include

from knox import views as knox_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('register/', user_views.register_view, name='register'),
    # path('login/', user_views.login_view, name='login'),
    # path('logout/', user_views.logout_view, name='logout'),

    path('api/register/', user_views.UserRegisterAPIView.as_view()),
    path('api/login/', user_views.UserLoginAPIView.as_view()),
    path('api/logout/', user_views.UserLogoutAPIView.as_view()),
    path('api/logoutall/', knox_views.LogoutAllView.as_view()),
    path('', include('finance_app.urls'))
]
