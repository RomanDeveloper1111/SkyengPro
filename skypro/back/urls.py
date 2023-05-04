from django.urls import path
from back.views import ListFileView, CreateFileView

urlpatterns = [
    path('', ListFileView.as_view(), name='list_files'),
    path('create/', CreateFileView.as_view(), name='create_file')
]
