__author__ = 'RAJ'
from rest_framework import serializers
from yaas_app.models import Auction

class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ('title', 'category', 'description', 'price', 'startdate', 'enddate', 'status', 'seller')