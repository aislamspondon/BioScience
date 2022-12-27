from data_analysis.models import (DataSequence, DataSequenceFile, DataSet,
                                  DataSetFile)
from django.contrib import admin

# Register your models here.
admin.site.register(DataSequence)
admin.site.register(DataSet)
admin.site.register(DataSetFile)
admin.site.register(DataSequenceFile)
