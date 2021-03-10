from rest_framework import serializers
from .models import  Usuario, UsuarioDisciplina

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from .views import login

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Senha"
    )

    password_confirm = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Confirme a senha"
    )

    is_staff = serializers.BooleanField(
        label="Membro da Equipe",
        help_text="Indica que usuário consegue acessar o site de administração."
    )

    is_superuser = serializers.BooleanField(
        label="SuperUsuário",
        help_text="Indica que este usuário tem todas as permissões sem atribuí-las explicitamente."
    )

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password', 'password_confirm', 'is_staff', 'is_superuser','status')
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        conta = Usuario(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            is_staff=self.validated_data['is_staff'],
            is_superuser=self.validated_data['is_superuser'],
            status=self.validated_data['status']
        )
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']

        if password != password_confirm:
            raise serializers.ValidationError({'password': 'As senhas não são iguais.'})
        conta.set_password(password)
        conta.save()
        return conta
    """class Meta:
        model = Usuario
        fields = ('__all__')"""


class ListarUsuario(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('__all__')

class  UsuarioDisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioDisciplina
        fields = ('__all__')


