from django.contrib import admin
from django.urls import path
from login.views import CustomTokenObtainPairView
from clientes.views import ClientesView, ClienteCreateView, ClienteUpaDateView, ClienteDeleteView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/login/', CustomTokenObtainPairView.as_view()),
    path('api/clientes/', ClientesView.as_view()),
    path('api/clientes/criar/', ClienteCreateView.as_view(), name='cliente-create'),
    path('api/clientes/update/<int:pk>/', ClienteUpaDateView.as_view(), name='cliente-update'),
    path('api/clientes/delete/<int:pk>/', ClienteDeleteView.as_view(), name='cliente-delete'),
]
