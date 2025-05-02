from django.shortcuts import render
from portfolio_app.models import Courses, ProjectUIImages, PapersAndPresentations, Projects, ProjectInfo, Languages
from portfolio_app.api.serializers import CourseSerializer, ProjUIImgSerializer, PaperAndPresSerializer, ProjectSerializer, ProjectInfoSerializer, LanguageSerializer
from rest_framework import generics, permissions


# Course Views
class CourseList(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CourseDetails(generics.RetrieveAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Project Info View
class ProjectInfoDetails(generics.RetrieveAPIView):
    queryset = ProjectInfo.objects.all()
    serializer_class = ProjectInfoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'projectID'


# Projet UI Image Connector Views
class ProjectUIImgList(generics.ListAPIView):
    queryset = ProjectUIImages.objects.all()
    serializer_class = ProjUIImgSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProjectUIImgDetails(generics.RetrieveAPIView):
    queryset = ProjectUIImages.objects.all()
    serializer_class = ProjUIImgSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'projectInfoID'


# Papers and Presentations Views
class PaperAndPresentationList(generics.ListAPIView):
    queryset = PapersAndPresentations.objects.all()
    serializer_class = PaperAndPresSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PaperAndPresentationDetails(generics.RetrieveAPIView):
    queryset = PapersAndPresentations.objects.all()
    serializer_class = PaperAndPresSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LanguageList(generics.ListAPIView):
    queryset = Languages.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]      

# Projects Views
class ProjectList(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProjectDetails(generics.RetrieveAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
