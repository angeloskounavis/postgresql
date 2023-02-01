from rest_framework import serializers

from .models import Job


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'owner', 'name', 'description',
                  'created_at')
        model = Job
