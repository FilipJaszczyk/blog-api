from rest_framework.serializers import ModelSerializer


class ReadOnlyModelSerializer(ModelSerializer):
    """Works like regural ModelSerializer but passes all fields to read_only_fields property in Meta class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        setattr(self.Meta, "read_only_fields", [*self.fields])
