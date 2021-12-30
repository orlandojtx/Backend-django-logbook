from ..models.entry                 import Entry
from rest_framework                 import serializers

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model       = Entry
        fields      = [ 'logbook', 'date', 'physichologist', 'attendance', 'description','satisfaction']
    
    def to_representation(self,obj):
        entry = Entry.objects.get(id=obj.id)
        return {
            'id'            : entry.id,
            'bitacora'      : entry.logbook.username,
            'fecha'         : entry.date,
            'psicologo'     : entry.physichologist,
            'asistencia'    : entry.attendance,
            'descripcion'   : entry.description,
            'satisfaccion'  : entry.satisfaction
        }
    