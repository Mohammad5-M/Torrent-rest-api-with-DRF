from rest_framework import serializers
from torran_api.models import files


class SR_TORRENT(serializers.ModelSerializer):
    class Meta:
        image_url = serializers.ImageField(required=False)

        model = files
        fields = ['id', 'name', 'info', 'magnet_url', 'DandT',
                  'category', 'Downloads', 'size', 'uploader', 'image_url']


# class MyModelSerializer(serializers.ModelSerializer):

#     creator = serializers.ReadOnlyField(source='creator.username')
#     creator_id = serializers.ReadOnlyField(source='creator.id')
#     image_url = serializers.ImageField(required=False)

#     class Meta:
#         model = files
#         fields = ['id', 'creator', 'creator_id',
#                   'title', 'description', 'image_url']
