from rest_framework import serializers
from .models import CryptoData,  OfficialLink, Social,ScrapingJob

# class ContractSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Contract
#         fields = ['name', 'address']

class OfficialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficialLink
        fields = ['name', 'link']

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ['name', 'url']

class CryptoDataSerializer(serializers.ModelSerializer):
    # contracts = ContractSerializer(many=True)
    official_links = OfficialLinkSerializer(many=True)
    socials = SocialSerializer(many=True)

    class Meta:
        model = CryptoData
        fields = [
            'coin', 'price', 'price_change', 'market_cap', 'market_cap_rank', 
            'volume', 'volume_rank', 'volume_change', 'circulating_supply', 
            'total_supply', 'diluted_market_cap',  'official_links', 'socials'
        ]

    def create(self, validated_data):
        # contracts_data = validated_data.pop('contracts')
        official_links_data = validated_data.pop('official_links')
        socials_data = validated_data.pop('socials')
        
        crypto_data = CryptoData.objects.create(**validated_data)
        
        # for contract_data in contracts_data:
        #     contract, created = Contract.objects.get_or_create(**contract_data)
        #     crypto_data.contracts.add(contract)
        
        for official_link_data in official_links_data:
            official_link, created = OfficialLink.objects.get_or_create(**official_link_data)
            crypto_data.official_links.add(official_link)
        
        for social_data in socials_data:
            social, created = Social.objects.get_or_create(**social_data)
            crypto_data.socials.add(social)
        
        return crypto_data

class ScrapingJobSerializer(serializers.ModelSerializer):
    results = CryptoDataSerializer(many=True, read_only=True)

    class Meta:
        model = ScrapingJob
        fields = ['job_id', 'created_at', 'coins', 'results']
