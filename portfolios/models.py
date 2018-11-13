from django.db import models
from home.models import Company
from shipments.models import Shipment

class Sales_Contract(models.Model):
    buyers          = models.ManyToManyField(Company, related_name='as_buyers', related_query_name='as_buyer')
    sellers         = models.ManyToManyField(Company, related_name='as_sellers', related_query_name='as_seller')
    contract_type   = models.CharField(max_length=100, choices=(("SPA","Sales Purchase Agreement"),("MSPA","Master Sales Purchase Agreement"),("CN","Confirmation Notice")))
    contract_status = models.CharField(max_length=100, choices=(("DRAFT","DRAFT"),("EFFECTIVE","EFFECTIVE")))

class Transaction(models.Model):
    contract = models.ForeignKey(Sales_Contract, on_delete=models.CASCADE,)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE,)


