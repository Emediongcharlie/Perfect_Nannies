from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from Perfect_Nannies_App.models import User, Guardian, Nanny


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role']


class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = ['id', 'user', 'address']


class NannySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nanny
        fields = ['id', 'user', 'address']


class NannyRegistrationSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=11)
    address = serializers.CharField(max_length=100)
    date_of_birth = serializers.DateField()
    name_of_next_of_kin = serializers.CharField(max_length=100)
    phone_number_of_next_of_kin = serializers.CharField(max_length=11)
    # guardian_id = serializers.PrimaryKeyRelatedField(queryset=Guardian.objects.all(), write_only=True)

    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'role', 'phone_number', 'address',
                  'date_of_birth', 'name_of_next_of_kin', 'phone_number_of_next_of_kin']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user_data = {
            "username": validated_data.pop("username"),
            "email": validated_data.pop("email"),
            "first_name": validated_data.pop("first_name"),
            "last_name": validated_data.pop("last_name"),
            "password": make_password(password),
            "role": validated_data.pop("role"),
        }

        # guardian_id = validated_data.pop("guardian_id")
        # try:
        #     guardian = Guardian.objects.get(id=guardian_id.id)
        # except Guardian.DoesNotExist:
        #     raise serializers.ValidationError({"guardian_id": "Guardian does not exist."})

        nanny_data = {
            "phone_number": validated_data.pop("phone_number"),
            "address": validated_data.pop("address"),
            "date_of_birth": validated_data.pop("date_of_birth"),
            "name_of_next_of_kin": validated_data.pop("name_of_next_of_kin"),
            "phone_number_of_next_of_kin": validated_data.pop("phone_number_of_next_of_kin"),
            # "guardian": guardian

        }

        validated_data["password"] = make_password(password)
        user = User.objects.create(**user_data)

        # if user.role == "nanny":
        Nanny.objects.create(user=user, **nanny_data)

        return user


class GuardianRegistrationSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=11)
    address = serializers.CharField(max_length=100)
    name_of_next_of_kin = serializers.CharField(max_length=100)
    phone_number_of_next_of_kin = serializers.CharField(max_length=11)

    password = serializers.CharField(write_only=True, min_length=8, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'role', 'phone_number', 'address',
                  'name_of_next_of_kin', 'phone_number_of_next_of_kin']

    def create(self, validated_data):
        password = validated_data.pop("password")
        # if not password:
        #     raise serializers.ValidationError({"password": "This field is required."})

        user_data = {
            "username": validated_data.pop("username"),
            "email": validated_data.pop("email"),
            "first_name": validated_data.pop("first_name"),
            "last_name": validated_data.pop("last_name"),
            "password": make_password(password),
            "role": validated_data.pop("role"),
        }

        guardian_data = {
            "phone_number": validated_data.pop("phone_number"),
            "address": validated_data.pop("address"),
            "name_of_next_of_kin": validated_data.pop("name_of_next_of_kin"),
            "phone_number_of_next_of_kin": validated_data.pop("phone_number_of_next_of_kin"),
        }

        validated_data["password"] = make_password(password)
        user = User.objects.create(**user_data)

        # if user.role == "guardian":
        Guardian.objects.create(user=user, **guardian_data)

        return user


class NannyLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True, min_length=8, required=True)


class GuardianLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True, min_length=8, required=True)


class GuardianNannyAssignmentSerializer(serializers.ModelSerializer):
    nanny_id = serializers.IntegerField()
    guardian_id = serializers.IntegerField()

    def validate(self, data):
        try:
            nanny = Nanny.objects.get(user_id=data["nanny_id"])
            guardian = Guardian.objects.get(user_id=data["guardian_id"])
        except Nanny.DoesNotExist:
            raise ValidationError("Nanny not found")
        except Guardian.DoesNotExist:
            raise ValidationError("Guardian not found")
        return data

    def save(self):
        nanny = Nanny.objects.get(user_id=self.validated_data["nanny_id"])
        guardian = Nanny.objects.get(user_id=self.validated_data["guardian_id"])
        nanny.guardian = guardian
        nanny.save()
        return nanny
