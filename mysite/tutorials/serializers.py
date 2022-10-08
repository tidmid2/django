from rest_framework import serializers
from mysite.tutorials.models import UsersTest 
from tutorials.models import Tutorial
from tutorials.models import UsersTest
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')

class UsersTestSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = UsersTest
        fields = ('id',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  'status')