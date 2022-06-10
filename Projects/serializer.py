from rest_framework import serializers
from .models import Profile,Projects
 
class ProfileSerializer(serializers.ModelSerializer):
   class Meta:
       model = Profile
       fields = ('bio', 'image', 'user')

class ProjectsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Projects
       fields = ('title', 'image', 'user','description','link','technologies_used','location')