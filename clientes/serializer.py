from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_name(self, value):
        if not name_valido(value):
            raise serializers.ValidationError("Não inclua números neste campo!")
        return value

    def validate_cpf(self, value):
        if not cpf_valido(value):
            raise serializers.ValidationError("O CPF é invalido!")
        return value

    def validate_rg(self, value):
        if not rg_valido(value):
            raise serializers.ValidationError("O RG deve ter 9 digitos!")
        return value

    def validate_telefone(self, value):
        if not telefone_valido(value):
            raise serializers.ValidationError("O numero de telefone deve seguir este modelo 62 91234-1234, (respeitando o espaço e traço).")
        return value

    # def validate_cliente_existe(self, email):
    #     queryset = Cliente.objects.filter(email=email)  # Corrija para usar o parâmetro passado (email), não self.kwargs['email']
    #     if queryset.exists():
    #         raise serializers.ValidationError("Este cliente já existe na base de dados!")
    #     return email

class ClienteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['name', 'telefone', 'celular']



