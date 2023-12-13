from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.views.generic.base import View
from rest_framework import viewsets
from django.views.generic import ListView, DetailView
from main.models import *
from main.serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsTeacherOfAdminSchool


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
    serializer_class = ClassroomSerializer
    permission_classes = [IsAuthenticated, IsTeacherOfAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return Classrooms.objects.filter(school=self.request.user.school)

class ClassApi(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticated, IsTeacherOfAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return Class.objects.filter(school=self.request.user.school)

class ScheduleApi(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated, IsTeacherOfAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return Schedule.objects.filter(school=self.request.user.school)

class MenuApi(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated, IsTeacherOfAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return Menu.objects.filter(school=self.request.user.school)

class SliderApi(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    permission_classes = [IsAuthenticated, IsTeacherOfAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return Slider.objects.filter(school=self.request.user.school)

class SubjectApi(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated, IsTeacherOfAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return Subject.objects.filter(school=self.request.user.school)

class schoolPasportApi(viewsets.ModelViewSet):
    queryset = schoolPasport.objects.all()
    serializer_class = schoolPasportApiSerializer
    permission_classes = [IsAuthenticated, IsTeacherOfAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return schoolPasport.objects.filter(school=self.request.user.school)

class School_AdministrationApi(viewsets.ModelViewSet):
    queryset = School_Administration.objects.all()
    serializer_class = School_AdministrationSerializer
    permission_classes = [IsAuthenticated, IsTeacherOfAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return School_Administration.objects.filter(school=self.request.user.school)

class Sport_SuccessApi(viewsets.ModelViewSet):
    queryset = Sport_Success.objects.all()
    serializer_class = Sport_SuccessSerializer
    permission_classes = [IsAuthenticated, IsTeacherOfAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return Sport_Success.objects.filter(school=self.request.user.school)

class Oner_SuccessApi(viewsets.ModelViewSet):
    queryset = Sport_Success.objects.all()
    serializer_class = Oner_SuccessSerializer
    permission_classes = [IsAuthenticated, IsTeacherOfAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return Oner_Success.objects.filter(school=self.request.user.school)

class PandikOlimpiadaApi(viewsets.ModelViewSet):
    queryset = PandikOlimpiada_Success.objects.all()
    serializer_class = PandikOlimpiada_SuccessSerializer
    permission_classes = [IsAuthenticated, IsTeacherOfAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return PandikOlimpiada_Success.objects.filter(school=self.request.user.school)

class School_RedCertificateApi(viewsets.ModelViewSet):
    queryset = RedCertificate.objects.all()
    serializer_class = RedCertificateSerializer
    permission_classes = [IsAuthenticated, IsTeacherOfAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return RedCertificate.objects.filter(school=self.request.user.school)

class School_AltynBelgiApi(viewsets.ModelViewSet):
    queryset = AltynBelgi.objects.all()
    serializer_class = AltynBelgiSerializer
    permission_classes = [IsAuthenticated, IsTeacherOfAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return AltynBelgi.objects.filter(school=self.request.user.school)

class School_SocialMediaApi(viewsets.ModelViewSet):
    queryset = School_SocialMedia.objects.all()
    serializer_class = School_SocialMediaSerializer
    permission_classes = [IsAuthenticated, IsTeacherOfAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return School_SocialMedia.objects.filter(school=self.request.user.school)

class School_DirectorApi(viewsets.ModelViewSet):
    queryset = School_Director.objects.all()
    serializer_class = School_DirectorSerializer
    permission_classes = [IsAuthenticated, IsTeacherOfAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return School_Director.objects.filter(school=self.request.user.school)

class Extra_LessonsApi(viewsets.ModelViewSet):
    queryset = Extra_Lessons.objects.all()
    serializer_class = Extra_LessonSerializer
    permission_classes = [IsAuthenticated, IsTeacherOfAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return Extra_Lessons.objects.filter(school=self.request.user.school)

class RingApi(viewsets.ModelViewSet):
    queryset = Ring.objects.all()
    serializer_class = RingSerializer
    permission_classes = [IsAuthenticated, IsTeacherOfAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return Ring.objects.filter(school=self.request.user.school)


# ========================================================================================================
class TeacherApi(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated, IsTeacherOfAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return Teacher.objects.filter(school=self.request.user.school)

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
    permission_classes = [IsAuthenticated, IsTeacherOfAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return TeacherWorkload.objects.filter(school=self.request.user.school)

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
    permission_classes = [IsAuthenticated, IsTeacherOfAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return Kruzhok.objects.filter(school=self.request.user.school)

class FacultativeListApi(viewsets.ModelViewSet):
    queryset = DopUrok.objects.all()
    serializer_class = DopUrokSerializer
    permission_classes = [IsAuthenticated, IsTeacherOfAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return DopUrok.objects.filter(school=self.request.user.school)

class DopUrokApi(viewsets.ModelViewSet):
    queryset = DopUrok.objects.all()
    serializer_class = DopUrokSerializer
    permission_classes = [IsAuthenticated, IsTeacherOfAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return DopUrok.objects.filter(school=self.request.user.school)

class DopUrokRingApi(viewsets.ModelViewSet):
    queryset = DopUrokRing.objects.all()
    serializer_class = DopUrokRingSerializer
    permission_classes = [IsAuthenticated, IsTeacherOfAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return DopUrokRing.objects.filter(school=self.request.user.school)