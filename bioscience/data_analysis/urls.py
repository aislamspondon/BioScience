from data_analysis import views
from django.urls import path

urlpatterns = [
    path('upload_dataset/', views.upload_dataset_csv, name="data_analysis_csv"),
    path('upload_datasequence/', views.upload_datasequence_csv, name="data_sequence_csv"),
    path('datasequence/convert_csv', views.convert_datasequence, name="datasequence_convert_csv"),
    path('dataset/convert_csv', views.convert_dataset, name="dataset_convert_csv"),

    # List DataSequence 
    path('datasequence/', views.list_datasequence, name="list_datasequence"),
    path('datasequence/protein/', views.add_datasequence, name="datasequence_protein"),
    path('datasequence/<str:protein_id>', views.datasequence, name="datasequence"),
    path('datasequence/<str:protein_id>/update/', views.datasequence_update, name="datasequence_update"),
    path('datasequence/<str:protein_id>/delete/', views.datasequence_delete, name="datasequence_delete"),

    # List DataSet 
    path('dataset/', views.list_dataset, name="list_dataset"),
    path('dataset/protein/', views.add_dataset, name="dataset_protein"),
    path('dataset/<str:protein_id>', views.dataset, name="dataset"),
    path('dataset/<str:protein_id>/update/', views.dataset_update, name="dataset_update"),
    path('dataset/<str:protein_id>/delete/', views.dataset_delete, name="dataset_delete"),

]