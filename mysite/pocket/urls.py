from django.urls import path
from . import views

app_name='pocket'
urlpatterns = [
    # ex: /pocket/
    path('', views.index, name='index'),
    # ex: /pocket/5/
    path('<int:organization_id>/', views.detail, name='detail'),
    path("register/", views.register, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("login", views.login_request, name="login"),
    path("<int:user_id>/profile/",views.profile, name="profile"),
]
