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
account_book_share = AccountBookViewSet.as_view(
    {
        "get": "share",
    }
)
account_book_get_share = AccountBookViewSet.as_view(
    {
        "get": "get_share",
    }
)


urlpatterns = [
    path("", account_book_list),
    path("<int:account_book_id>/", account_book_detail),
    path("share/<int:account_book_id>/", account_book_share),
    path("share/<external_url>/", account_book_get_share),
]
