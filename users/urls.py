from django.urls import path
from users.views import UserViewSet


urlpatterns = [path("resister/", UserViewSet.as_view({"post": "resister"}))]
