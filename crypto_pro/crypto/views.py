# from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import pandas as pd
from rest_framework import viewsets
from .models import CryptoData
from .serializers import CryptoDataSerializer

class CryptoDataViewSet(viewsets.ModelViewSet):
    queryset = CryptoData.objects.all()
    serializer_class = CryptoDataSerializer


# url = 'https://coinmarketcap.com/currencies/bitcoin/'
# tables=[]
# for i in range(1,3):
#     print('processing page{0}'.format(i))
#     params  = {
#             'page' :1
#     }
#     response = requests.get(url,headers=headers,params=params)
#     soup = BeautifulSoup(response.content,'html.parser')
#     # tables.append(pd.read_html(str(soup))[0])
# pd.read_html(str(soup))[0]




    
#     @action(detail=False, methods=['post'])
#     def start_scraping(self, request):
#         coins = request.data.get('coins', [])
#         job = ScrapingJob.objects.create()

#         for coin in coins:
#             scrape_crypto_data.delay(job.job_id, coin)

#         return Response({'job_id': str(job.job_id)}, status=status.HTTP_202_ACCEPTED)
    
#     @action(detail=True, methods=['get'])
#     def scraping_status(self, request, pk=None):
#         job = ScrapingJob.objects.get(job_id=pk)
#         serializer = ScrapingJobSerializer(job)
#         return Response(serializer.data, status=status.HTTP_200_OK)
