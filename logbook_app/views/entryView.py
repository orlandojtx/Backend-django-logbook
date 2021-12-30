from logbook_app.models.entry                                   import Entry
from logbook_app.serializers.entrySerializer                    import EntrySerializer

from django.conf                                                import settings
from rest_framework                                             import generics, views, status
from rest_framework.response                                    import Response

class EntryDetailView(generics.ListAPIView):
    serializer_class   = EntrySerializer

    def get_queryset(self): #<int:logbook>
        bitacora_id = self.kwargs['logbook']
        return Entry.objects.filter(logbook=bitacora_id)

class EntrySingleDetailView(generics.RetrieveAPIView):
    queryset           = Entry.objects.all()
    serializer_class   = EntrySerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class EntryCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = EntrySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Transacción exitosa", status=status.HTTP_201_CREATED)

class EntryUpdateView(generics.UpdateAPIView):
    serializer_class = EntrySerializer
    queryset         = Entry.objects.all()

    def update(self, request, *args, **kwargs):
        return super().update(request,*args,**kwargs)

class EntryDeleteView(generics.DestroyAPIView):
    serializer_class   = EntrySerializer
    queryset           = Entry.objects.all()

    def delete(self, request, *args, **kwargs):
        return super().destroy(request,*args,**kwargs)

