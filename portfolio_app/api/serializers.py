from rest_framework import serializers
from portfolio_app.models import Courses, PapersAndPresentations, Projects, ProjectUIImages, ProjectInfo, Languages

    
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = '__all__'
    
class ProjectSerializer(serializers.ModelSerializer):
    courseCode = CourseSerializer(read_only = True)
    projLanguages = serializers.StringRelatedField(many = True)

    class Meta:
        model = Projects
        fields = '__all__'
    
class PaperAndPresSerializer(serializers.ModelSerializer):
    courseCode = CourseSerializer(read_only = True)

    class Meta:
        model = PapersAndPresentations
        fields = '__all__'

class ProjUIImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUIImages
        fields = '__all__'

class ProjectInfoSerializer(serializers.ModelSerializer):
    ui_images = ProjUIImgSerializer(many = True, read_only = True)

    class Meta:
        model = ProjectInfo
        fields = '__all__'