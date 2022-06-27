from rest_framework import serializers
from torran_api.models import files

class SR_TORRENT(serializers.ModelSerializer):
    class Meta:
        model = files
        fields = ['id', 'name', 'info', 'magnet_url', 'DandT', 'category', 'Downloads','size','uploader']
