from django.db import models


# Create your models here.
class DataSetFile(models.Model):
    file = models.FileField(upload_to="dataset_files")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file}"

class DataSequenceFile(models.Model):
    file = models.FileField(upload_to="datasequence_files")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file}"

class DataSequence(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    protein_id = models.CharField(max_length=15, blank=False, null=False)
    protein_sequence = models.CharField(max_length=40000, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.protein_id}"


class DataSet(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    protein_id = models.CharField(max_length=15, blank=False, null=False)
    organism_taxa_id = models.CharField(max_length=20, blank=False, null=False)
    organism_clade_idenitifer = models.CharField(max_length=5, blank=False, null=False)
    organism_scientific_name = models.CharField(max_length=50, blank=False, null=False)
    domain_description = models.TextField(blank=False, null=False)
    domain_id = models.CharField(max_length=70, blank=False, null=False)
    domain_start_coordinate = models.CharField(max_length=10, blank=False, null=False)
    domain_end_coordinate = models.CharField(max_length=10, blank=False, null=False)
    length_of_protein = models.CharField(max_length=10, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.protein_id}"


