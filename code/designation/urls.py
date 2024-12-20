
from django.urls import path
from .views import index_doc

urlpatterns = [
    path('', index_doc, name="documentacao"),
]
