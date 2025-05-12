from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializers

@api_view(['POST'])
def students_create(request):
    serializer = StudentSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Data created'})
    return Response(serializer.errors, status=400)

