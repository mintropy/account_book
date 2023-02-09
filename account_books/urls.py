from django.urls import path
from .views import AccountBookViewSet

account_book_list = AccountBookViewSet.as_view(
    {
        "post": "create",
        "get": "list",
    }
)
account_book_detail = AccountBookViewSet.as_view(
    {
        "put": "update",
        "delete": "destroy",
    }
)


urlpatterns = [
    path("", account_book_list),
    path("<int:account_book_id>/", account_book_detail),
]
