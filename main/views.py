from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.views.generic.base import View
from rest_framework import viewsets
from django.views.generic import ListView, DetailView
from main.models import *
from main.serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.


class AdminsApi(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated]

class SchoolsApi(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAuthenticated]

class ClassroomApi(viewsets.ModelViewSet):
    queryset = Classrooms.objects.all()
    serializer_class = ClassroomApiSerializer
    permission_classes = [IsAuthenticated]

class TeacherApi(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

class ClassApi(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticated]

class ScheduleApi(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]

class MenuApi(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class SliderApi(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    permission_classes = [IsAuthenticated]

class SubjectApi(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]

class schoolPasportApi(viewsets.ModelViewSet):
    queryset = schoolPasport.objects.all()
    serializer_class = schoolPasportApiSerializer
    permission_classes = [IsAuthenticated]

class School_AdministrationApi(viewsets.ModelViewSet):
    queryset = School_Administration.objects.all()
    serializer_class = School_AdministrationSerializer
    permission_classes = [IsAuthenticated]

class Pride_of_the_SchoolApi(viewsets.ModelViewSet):
    queryset = Pride_of_the_School.objects.all()
    serializer_class = Pride_of_the_SchoolSerializer
    permission_classes = [IsAuthenticated]

class School_HistoryApi(viewsets.ModelViewSet):
    queryset = School_History.objects.all()
    serializer_class = School_HistorySerializer
    permission_classes = [IsAuthenticated]

class School_DirectorApi(viewsets.ModelViewSet):
    queryset = School_Director.objects.all()
    serializer_class = School_DirectorSerializer
    permission_classes = [IsAuthenticated]

class Extra_LessonsApi(viewsets.ModelViewSet):
    queryset = Extra_Lessons.objects.all()
    serializer_class = Extra_LessonSerializer
    permission_classes = [IsAuthenticated]


# ========================================================================================================
class TeacherApi(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return TeacherCreateSerializer
        return TeacherSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = TeacherCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TeacherCreateSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherWorkloadApi(viewsets.ModelViewSet):
    queryset = TeacherWorkload.objects.all()
    serializer_class = TeacherWorkloadSerializer
    permission_classes = [IsAuthenticated]

class JobHistoryViewSet(viewsets.ModelViewSet):
    queryset = JobHistory.objects.all()
    serializer_class = JobHistorySerializer
    permission_classes = [IsAuthenticated]

class SpecialityHistoryViewSet(viewsets.ModelViewSet):
    queryset = JobHistory.objects.all()
    serializer_class = SpecialityHistorySerializer
    permission_classes = [IsAuthenticated]

class KruzhokListApi(viewsets.ModelViewSet):
    queryset = Kruzhok.objects.all()
    serializer_class = KruzhokSerializer

class FacultativeListApi(viewsets.ModelViewSet):
    queryset = Facultative.objects.all()
    serializer_class = FacultativeSerializer