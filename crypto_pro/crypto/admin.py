from django.contrib import admin
from .models import CryptoData,ScrapingJob

# Register your models here.
admin.site.register(CryptoData)
admin.site.register(ScrapingJob)
class CryptoDataAdmin(admin.ModelAdmin):
    list_display=('coin','price','price_change','market_cap','market_cap_rank','volume','volume_rank','volume_change','circulating_supply','total_supply','diluted_market_cap')

class ScrapingJob(admin.ModelAdmin):
    list_display=('job_id','created_at','status')