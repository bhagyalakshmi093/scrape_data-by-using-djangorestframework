from celery import shared_task
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from .models import CryptoData

@shared_task
def scrape_crypto_data():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get('https://coinmarketcap.com/')
        rows = driver.find_elements_by_css_selector('tbody tr')
        
        for row in rows[:10]:  # scrape the top 10 cryptocurrencies
            name = row.find_element_by_css_selector('.cmc-table__cell--sort-by__name a').text
            price = row.find_element_by_css_selector('.cmc-table__cell--sort-by__price').text
            CryptoData.objects.update_or_create(name=name, defaults={'price': price})
    finally:
        driver.quit()
