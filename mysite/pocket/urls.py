from django.urls import path
from . import views

app_name='pocket'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:organization_id>/', views.detail, name='detail'),
    # ex: /polls/5/vote/
    path("register", views.register, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("login", views.login_request, name="login"),
]
