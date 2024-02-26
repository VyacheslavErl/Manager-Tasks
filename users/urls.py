from django.urls import path
from users.views import login, registration, profile, user_logout

urlpatterns = [
    path('login/', login),
    path('registration/', registration),
    path('profile/', profile),
    path('logout/', user_logout)
]