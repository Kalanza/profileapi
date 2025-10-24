from django.urls import path
from apiprof.views import ProfileView

urlpatterns = [
    # Use a trailing slash for the route (Django convention)
    path('me/', ProfileView.as_view(), name='profile'),
]
