from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function(get,post,patch,put,delete)',
            'Is similar to django views',
            'Gives you the most controll over your app logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'hello', 'an_apiview': an_apiview})
