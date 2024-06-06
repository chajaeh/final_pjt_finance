from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()
from dj_rest_auth.serializers import UserDetailsSerializer

class CustomUserDetailsSerializer(UserDetailsSerializer):
  class Meta:
    extra_fields = []
    if hasattr(UserModel, 'USERNAME_FIELD'):
      extra_fields.append(UserModel.USERNAME_FIELD)
    if hasattr(UserModel, 'EMAIL_FIELD'):
      extra_fields.append(UserModel.EMAIL_FIELD)
    if hasattr(UserModel, 'first_name'):
      extra_fields.append('first_name')
    if hasattr(UserModel, 'last_name'):
      extra_fields.append('last_name')
    if hasattr(UserModel, 'age'):
      extra_fields.append('age')
    if hasattr(UserModel, 'asset'):
      extra_fields.append('asset')
    if hasattr(UserModel, 'financial_products'):
      extra_fields.append('financial_products')
    if hasattr(UserModel, 'salary'):
      extra_fields.append('salary')
    if hasattr(UserModel, 'warned'):
      extra_fields.append('warned')
    model = UserModel
    fields = ('pk', *extra_fields)
    read_only_fields = ('email',)
    
class UserUpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = get_user_model()
    fields = ('age', 'asset', 'salary', 'financial_products', 'warned',)