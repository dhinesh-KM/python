from django.core.serializers.json import DjangoJSONEncoder
from .models import product

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, product):
            return str(obj)
        return super().default(obj)
