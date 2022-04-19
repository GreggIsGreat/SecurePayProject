from django.db import models
import uuid
from client.models import Profile


# Create your models here.

class Client(models.Model):
    owner = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    client_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    user_image = models.ImageField(null=True, blank=True, default="default.png")
    email = models.EmailField(unique=True, null=True, blank=True)
    birthday = models.DateField(auto_now=False, null=True, blank=True)
    location = models.ManyToManyField('AlphaReportTable', blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Account(models.Model):
    account_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    account_number = models.IntegerField(null=False)
    user_type = (
        ('checking', 'Checking'),
        ('business', 'Business'),
        ('savings', 'Savings'),
        ('cashpal', 'Cashpal')

    )
    account_type = models.CharField(max_length=200, choices=user_type)
    balance = models.DecimalField(decimal_places=2, max_digits=12, null=True)

    def __str__(self):
        return self.account_type


class Transaction(models.Model):
    transaction_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    transaction = models.DateTimeField(blank=False, auto_now_add=True)
    name = models.ForeignKey(Client, on_delete=models.CASCADE)
    transaction_amount = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    reason = (
        ('Checking', 'Checking'),
        ('E-wallet', 'E-wallet'),
        ('Deposit', 'Deposit'),
        ('Cashing', 'Cashing')

    )
    transaction_type = models.CharField(max_length=200, null=True, choices=reason)

    def __str__(self):
        return self.transaction_type


class AlphaReportTable(models.Model):
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.location