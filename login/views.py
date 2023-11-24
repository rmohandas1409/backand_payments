from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        refresh = response.data.get('refresh')
        access = response.data.get('access')
        # Você pode retornar apenas o token de acesso se quiser
        return Response({'token': access}, status=response.status_code)
