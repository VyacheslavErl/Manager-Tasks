from django.urls import path
from users.views import profile, user_logout

urlpatterns = [
    path('profile/', profile),
    path('logout/', user_logout)
]