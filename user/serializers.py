from rest_framework import serializers
from .models import UserAccount,UserAddress

class UserAddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserAddress
		fields = ('city', 'street_address', 'street_number', 'postal_code', 'country')

class UserSerializer(serializers.ModelSerializer):
	address = UserAddressSerializer()
	class Meta:
		model = UserAccount 
		fields = ('id', 'first_name', 'last_name', 'username', 'email', 'gender', 'phone', 'dp', 'bio','role','address','rating')
		extra_kwargs = {'address': {'read_only': True}}
class UserRegisterSerializer(serializers.ModelSerializer):
	address = UserAddressSerializer()
	class Meta:
		model = UserAccount
		fields = ('username', 'email', 'password','first_name','last_name','gender', 'phone', 'dp','bio','role', 'address')
		extra_kwargs = {'password': {'write_only': True}}
		
	def create(self, validated_data):
		address_data = validated_data.pop('address')
		user = UserAccount.objects.create_user(**validated_data)
		UserAddress.objects.create(user=user, **address_data)
		return user
	
class UserLoginSerializer(serializers.Serializer):
	email = serializers.EmailField(required = True)
	password = serializers.CharField(required = True)
