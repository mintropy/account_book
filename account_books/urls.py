from django.urls import path
from .views import AccountBookViewSet

account_book_detail = AccountBookViewSet.as_view({"post": "create"})


urlpatterns = [path("", account_book_detail)]
