from data_analysis.models import DataSequence, DataSet
from rest_framework import serializers


class DataSequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSequence
        fields = '__all__'

class DataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSet
        fields = '__all__'

