__author__ = 'Jonathan'
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.serializers import Serializer
from tastypie.paginator import Paginator
from .models import dependence


class dependenceResource(ModelResource):
    class Meta:
        resource_name = 'dependence'
        queryset = dependence.objects.all().order_by('id')
        paginator_class = Paginator
        limit = 10
        serializer = Serializer()

    def dehydrate(self, bundle):
        bundle.data['check'] = 'false'
        return bundle


        # fields = ('id', 'name', 'age', 'sex', 'get_sex_display', 'dob', 'alive', 'get_alive_display')
        #serializer = Serializer()
        #offset = 10

    # create a fields as do you wish
    #def dehydrate(self, bundle):
    #    bundle.data['custom_field'] = "Whatever you want"
    #    return bundle

