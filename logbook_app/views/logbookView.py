from logbook_app.models.logbook                                 import Logbook
from logbook_app.serializers.logbookSerializer                  import LogbookSerializer

from django.conf                                                import settings
from rest_framework                                             import generics, views, status
from rest_framework.response                                    import Response


class LogbookDetailView(generics.ListAPIView):
    serializer_class   = LogbookSerializer

    def get_queryset(self): #Que me lo trabaje con el propio user de django 
        user_id = self.kwargs['user']
        return Logbook.objects.filter(username=user_id)

class LogbookCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = LogbookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Transacción exitosa", status=status.HTTP_201_CREATED)