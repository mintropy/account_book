from django.contrib import admin
from account_books.models import AccountBook

# Register your models here.

@admin.register(AccountBook)
class AccountBookAdmin(admin.ModelAdmin):
    pass