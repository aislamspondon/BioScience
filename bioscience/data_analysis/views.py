# from django.shortcuts import render
import csv

import pandas as pd
from data_analysis.models import (DataSequence, DataSequenceFile, DataSet,
                                  DataSetFile)
from data_analysis.serializers import DataSequenceSerializer, DataSetSerializer
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.

# Create Table From Dataset Upload 
 
def create_db_dataset(file_path):
    data = pd.read_csv(file_path, delimiter=',')
    list_of_csv = [list(row) for row in data.values]
    for l in list_of_csv:
        DataSet.objects.create(
            protein_id = l[0],
            organism_taxa_id = l[1],
            organism_clade_idenitifer = l[2],
            organism_scientific_name = l[3],
            domain_description = l[4],
            domain_id = l[5],
            domain_start_coordinate = l[6],
            domain_end_coordinate = l[7],
            length_of_protein = l[8]
        )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_dataset_csv(request):
    file = request.FILES.get('file')
    obj = DataSetFile.objects.create(file=file)
    create_db_dataset(obj.file)
    return Response({"message": "Upload CSV Data Analysis Done"}, status=status.HTTP_200_OK)


# Create Table From Data Sequence Upload 
 
def create_db_datasequence(file_path):
    data = pd.read_csv(file_path, delimiter=',')
    list_of_csv = [list(row) for row in data.values]
    for l in list_of_csv:
        DataSequence.objects.create(
            protein_id = l[0],
            protein_sequence = l[1],
        )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_datasequence_csv(request):
    file = request.FILES.get('file')
    obj = DataSequenceFile.objects.create(file=file)
    create_db_datasequence(obj.file)
    return Response({"message": "Upload CSV Data Sequence Done"}, status=status.HTTP_200_OK)



# Show all data set 

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_datasequence(request):
    data = request.data
    serializer = DataSequenceSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response({"message": "Not Valid"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_datasequence(request):
    data = DataSequence.objects.all()
    serializer = DataSequenceSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def datasequence(request, protein_id):
    data = DataSequence.objects.filter(protein_id=protein_id)
    if not data.exists():
        return Response({"message": "Data Sequence Not Exits"}, status=status.HTTP_404_NOT_FOUND)
    serializer = DataSequenceSerializer(data.first(), many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def datasequence_update(request, protein_id):
    data = request.data
    data_sequence = DataSequence.objects.filter(protein_id=protein_id)
    obj = data_sequence.first()
    serializer = DataSequenceSerializer(obj, many=False)
    obj.protein_sequence = data['protein_sequence']
    obj.save()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def datasequence_delete(request, protein_id):
    qs = DataSequence.objects.filter(protein_id=protein_id)
    if not qs.exists():
        return Response({"message": "Data Sequence not exits"}, status=status.HTTP_404_NOT_FOUND)
    obj = qs.first()
    obj.delete()
    return Response({"message": "Data Sequence Removed"}, status=200)

@api_view(['GET'])
def convert_datasequence(request):
    data_sequence = DataSequence.objects.all()
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=data_sequence_export.csv'
    writer = csv.writer(response)
    writer.writerow(['Protein ID', 'Protein Sequence'])
    data_sequence_fields = data_sequence.values_list('protein_id', 'protein_sequence')
    for data in data_sequence_fields:
        writer.writerow(data)
    return response


# Show all data sequence

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_dataset(request):
    data = request.data
    serializer = DataSetSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response({"message": "Not Valid"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_dataset(request):
    data = DataSet.objects.all()
    serializer = DataSetSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dataset(request, protein_id):
    data = DataSet.objects.filter(protein_id=protein_id)
    if not data.exists():
        return Response({"message": "Data Set Not Exits"}, status=status.HTTP_404_NOT_FOUND)
    serializer = DataSetSerializer(data.first(), many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def dataset_update(request, protein_id):
    data = request.data
    data_set = DataSet.objects.filter(protein_id=protein_id)
    obj = data_set.first()
    serializer = DataSetSerializer(obj, many=False)
    obj.protein_id = data['protein_id']
    obj.organism_taxa_id = data['organism_taxa_id']
    obj.organism_clade_idenitifer = data['organism_clade_idenitifer']
    obj.organism_scientific_name = data['organism_scientific_name']
    obj.domain_description = data['domain_description']
    obj.domain_id = data['domain_id']
    obj.domain_start_coordinate = data['domain_start_coordinate']
    obj.domain_end_coordinate = data['domain_end_coordinate']
    obj.length_of_protein = data['length_of_protein']
    obj.save()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def dataset_delete(request, protein_id):
    qs = DataSet.objects.filter(protein_id=protein_id)
    if not qs.exists():
        return Response({"message": "Data Set not exits"}, status=status.HTTP_404_NOT_FOUND)
    obj = qs.first()
    obj.delete()
    return Response({"message": "Data Set Removed"}, status=200)


@api_view(['GET'])
def convert_dataset(request):
    data_set = DataSet.objects.all()
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=data_set_export.csv'
    writer = csv.writer(response)
    writer.writerow(['Protein ID', 'Organism TAXA ID', 'Organism Clade Idenitifer', 'Organism Scientific name ("Genus Species")', 'Domain description', 'Domain ID', 'Domain Start Coordinate', 'Domain End Coordinate', 'Length of Protein'])
    data_set_fields = data_set.values_list('protein_id', 'organism_taxa_id', 'organism_clade_idenitifer', 'organism_scientific_name', 'domain_description', 'domain_id', 'domain_start_coordinate', 'domain_end_coordinate', 'length_of_protein')
    for data in data_set_fields:
        writer.writerow(data)
    return response




