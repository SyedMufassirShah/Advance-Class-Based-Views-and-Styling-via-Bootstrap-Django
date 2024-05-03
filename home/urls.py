from django.urls import path
from . import views

urlpatterns = [
    # General URL configured for Function Based Views
    # path('greeting/', views.home),
    # path('authorized/', views.authorized),

    # URLs Configured for Class Based Views
    path('greeting/', views.HomeView.as_view()),
    path('authorized/', views.AuthorizedView.as_view()),
    path('register/', views.VisitorRegisterationForm.as_view()),
    path('register-success/', views.UserRegisterationSuccess.as_view())
]
