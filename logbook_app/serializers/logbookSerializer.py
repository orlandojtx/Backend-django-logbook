from ..models.logbook               import Logbook
from rest_framework                 import serializers

class LogbookSerializer(serializers.ModelSerializer):
    class Meta:
        model       = Logbook
        fields      = [ 'user', 'created_date']
    
    def to_representation(self,obj):
        logbook = Logbook.objects.get(id=obj.id)
        return {
            'id_bitacora'       : logbook.id,
            'fecha_creacion'    : logbook.created_date
        }
    