from django.db import models
import uuid

# class Contract(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)

class OfficialLink(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()

class Social(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()

class CryptoData(models.Model):
    coin = models.CharField(max_length=255)
    price = models.FloatField()
    price_change = models.FloatField()
    market_cap = models.BigIntegerField()
    market_cap_rank = models.IntegerField()
    volume = models.BigIntegerField()
    volume_rank = models.IntegerField()
    volume_change = models.FloatField()
    circulating_supply = models.BigIntegerField()
    total_supply = models.BigIntegerField()
    diluted_market_cap = models.BigIntegerField()

    official_links = models.ManyToManyField(OfficialLink)
    socials = models.ManyToManyField(Social)

    def __str__(self):
        return self.coin
class ScrapingJob(models.Model):
    job_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='PENDING')