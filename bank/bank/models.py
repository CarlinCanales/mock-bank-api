from django.db import models


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Accounts(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Transactions(models.Model):
    type = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Deposits(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()


class Withdrawals(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
