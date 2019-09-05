# api/resources.py
from tastypie.resources import ModelResource

from gitwrap.models import dataSet
from tastypie.authorization import Authorization

class NoteResource(ModelResource):
    class Meta:
        queryset = dataSet.objects.all()
        resource_name = 'dataset'
        authorization = Authorization()
