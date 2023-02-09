from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from account_books.models import AccountBook
from account_books.serializers import AccountBookSerializer
from users.models import User

import datetime


class AccountBookViewSet(ViewSet):
    model = AccountBook
    queryset = AccountBook.objects.all()
    serializer_class = AccountBookSerializer

    def create(self, request):
        username = request.user.username
        if not username:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        user = User.objects.get(username=username)
        date = request.data.get("date", None)
        amount = request.data.get("amount", None)
        memo = request.data.get("memo", None)
        if date is None:
            today = datetime.date.today()
            date = today
        data = {
            "user": user.id,
            "date": date,
            "amount": amount,
            "memo": memo,
        }
        serializer = AccountBookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
