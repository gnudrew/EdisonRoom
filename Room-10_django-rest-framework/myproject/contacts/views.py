from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer
 
@api_view(['GET', 'POST'])
def contact_list(request):
    """
    List all snippets, or create a new snippet. 
    """
    if request.method == 'GET':
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        print('serializer.data :')
        print(serializer.data)
        return Response(serializer.data)
 
    elif request.method == 'POST':
        print(request.data)

        serializer = ContactSerializer(data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)