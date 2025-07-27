from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # fields = (
        #     "id",
        #     "email",
        #     "phone",
        #     "birth_date",
        #     "created_at",
        #     "updated_at",
        # )
