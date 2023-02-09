from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from account_books.models import AccountBook
from account_books.serializers import AccountBookSerializer
from users.models import User

import datetime
import uuid


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
        amount = request.data.get("amount", 0)
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
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        user = User.objects.get(username=request.user.username)
        account_books = AccountBook.objects.filter(user=user.id)
        serializer = AccountBookSerializer(account_books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def detail(self, request, account_book_id):
        user = User.objects.get(username=request.user.username)
        account_book = AccountBook.objects.filter(id=account_book_id)[0]
        if account_book.user != user.id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = AccountBookSerializer(account_book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, account_book_id):
        account_book = AccountBook.objects.filter(id=account_book_id)[0]
        user = User.objects.get(username=request.user.username)
        if account_book.user != user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        amount = request.data.get("amount", None)
        memo = request.data.get("memo", None)
        data = {
            "user": user.id,
            "date": account_book.date,
            "amount": amount if amount is not None else account_book.amount,
            "memo": memo if memo is not None else account_book.memo,
        }
        serializer = AccountBookSerializer(account_book, data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(dstatus=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, account_book_id):
        account_book = AccountBook.objects.filter(id=account_book_id)[0]
        account_book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def share(self, request, account_book_id):
        user = get_object_or_404(User, username=request.user.username)
        account_book = get_object_or_404(AccountBook, id=account_book_id, user=user.id)
        url_id = uuid.uuid4()
        expire_date = datetime.datetime.now() + datetime.timedelta(hours=3)
        data = {
            **account_book.__dict__,
            "user": user.id,
            "external_url": url_id,
            "external_url_expire": expire_date,
        }
        serializer = AccountBookSerializer(account_book, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def get_share(self, request, external_url):
        account_book = get_object_or_404(AccountBook, external_url=external_url)
        expire_date = account_book.external_url_expire.replace(
            tzinfo=datetime.timezone.utc
        )
        if expire_date < datetime.datetime.now(tz=datetime.timezone.utc):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = AccountBookSerializer(account_book)
        return Response(serializer.data, status=status.HTTP_200_OK)
