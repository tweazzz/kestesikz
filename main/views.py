from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.views.generic.base import View
from rest_framework import viewsets
from django.views.generic import ListView, DetailView
from main.models import *
from main.serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsAdminSchool,IsSuperAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *
from rest_framework.decorators import action

class AdminsApi(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAdminSchool]

class SchoolsApi(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsSuperAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SchoolFilter


class ClassroomApi(viewsets.ModelViewSet):
    queryset = Classrooms.objects.all()
    serializer_class = ClassroomSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClassroomFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return Classrooms.objects.all()
            else:
                return Classrooms.objects.filter(school=self.request.user.school)
        return Classrooms.objects.all()

class ClassApi(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClassFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return Class.objects.all()
            else:
                return Class.objects.filter(school=self.request.user.school)
        return Class.objects.all()

class ScheduleApi(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ScheduleFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return Schedule.objects.all()
            else:
                return Schedule.objects.filter(school=self.request.user.school)
        return Schedule.objects.all()


class MenuApi(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MenuFilter


    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return Menu.objects.all()
            else:
                return Menu.objects.filter(school=self.request.user.school)
        return Menu.objects.all()


class SliderApi(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SliderFilter


    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return Slider.objects.all()
            else:
                return Slider.objects.filter(school=self.request.user.school)
        return Slider.objects.all()


class SubjectApi(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SubjectFilter


    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return Subject.objects.all()
            else:
                return Subject.objects.filter(school=self.request.user.school)
        return Subject.objects.all()


class schoolPasportApi(viewsets.ModelViewSet):
    queryset = schoolPasport.objects.all()
    serializer_class = schoolPasportApiSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = School_PasportFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return schoolPasport.objects.all()
            else:
                return schoolPasport.objects.filter(school=self.request.user.school)
        return schoolPasport.objects.all()


class School_AdministrationApi(viewsets.ModelViewSet):
    queryset = School_Administration.objects.all()
    serializer_class = School_AdministrationSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = School_AdministrationFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return School_Administration.objects.all()
            else:
                return School_Administration.objects.filter(school=self.request.user.school)
        return School_Administration.objects.all()


class Sport_SuccessApi(viewsets.ModelViewSet):
    queryset = Sport_Success.objects.all()
    serializer_class = Sport_SuccessSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = Sport_SuccessFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return Sport_Success.objects.all()
            else:
                return Sport_Success.objects.filter(school=self.request.user.school)
        return Sport_Success.objects.all()
    
    @action(detail=False, methods=['get'])
    def available_classes(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                classes = Class.objects.all()
            else:
                classes = Class.objects.filter(school=self.request.user.school)

            serializer = ClassForProudSSerializer(classes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)


class Oner_SuccessApi(viewsets.ModelViewSet):
    queryset = Oner_Success.objects.all()
    serializer_class = Oner_SuccessSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = Oner_SuccessFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return Oner_Success.objects.all()
            else:
                return Oner_Success.objects.filter(school=self.request.user.school)
        return Oner_Success.objects.all()
    @action(detail=False, methods=['get'])
    def available_classes(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                classes = Class.objects.all()
            else:
                classes = Class.objects.filter(school=self.request.user.school)

            serializer = ClassForProudSSerializer(classes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)


class PandikOlimpiadaApi(viewsets.ModelViewSet):
    queryset = PandikOlimpiada_Success.objects.all()
    serializer_class = PandikOlimpiada_SuccessSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PandikOlimpiada_SuccessFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return PandikOlimpiada_Success.objects.all()
            else:
                return PandikOlimpiada_Success.objects.filter(school=self.request.user.school)
        return PandikOlimpiada_Success.objects.all()
    @action(detail=False, methods=['get'])
    def available_classes(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                classes = Class.objects.all()
            else:
                classes = Class.objects.filter(school=self.request.user.school)

            serializer = ClassForProudSSerializer(classes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)


class School_RedCertificateApi(viewsets.ModelViewSet):
    queryset = RedCertificate.objects.all()
    serializer_class = RedCertificateSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = RedCertificateFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return RedCertificate.objects.all()
            else:
                return RedCertificate.objects.filter(school=self.request.user.school)
        return RedCertificate.objects.all()


class School_AltynBelgiApi(viewsets.ModelViewSet):
    queryset = AltynBelgi.objects.all()
    serializer_class = AltynBelgiSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AltynBelgiFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return AltynBelgi.objects.all()
            else:
                return AltynBelgi.objects.filter(school=self.request.user.school)
        return AltynBelgi.objects.all()

class School_SocialMediaApi(viewsets.ModelViewSet):
    queryset = School_SocialMedia.objects.all()
    serializer_class = School_SocialMediaSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = School_SocialMediaFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return School_SocialMedia.objects.all()
            else:
                return School_SocialMedia.objects.filter(school=self.request.user.school)
        return School_SocialMedia.objects.all()


class School_DirectorApi(viewsets.ModelViewSet):
    queryset = School_Director.objects.all()
    serializer_class = School_DirectorSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = School_DirectorFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return School_Director.objects.all()
            else:
                return School_Director.objects.filter(school=self.request.user.school)
        return School_Director.objects.all()


class Extra_LessonsApi(viewsets.ModelViewSet):
    queryset = Extra_Lessons.objects.all()
    serializer_class = Extra_LessonSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = Extra_LessonsFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return Extra_Lessons.objects.all()
            else:
                return Extra_Lessons.objects.filter(school=self.request.user.school)
        return Extra_Lessons.objects.all()


class RingApi(viewsets.ModelViewSet):
    queryset = Ring.objects.all()
    serializer_class = RingSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = RingFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return Ring.objects.all()
            else:
                return Ring.objects.filter(school=self.request.user.school)
        return Ring.objects.all()


class TeacherApi(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TeacherFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return Teacher.objects.all()
            else:
                return Teacher.objects.filter(school=self.request.user.school)
        return Teacher.objects.all()

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
    permission_classes = [IsAdminSchool]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)
    def get_queryset(self):
        return TeacherWorkload.objects.filter(school=self.request.user.school)

class JobHistoryViewSet(viewsets.ModelViewSet):
    queryset = JobHistory.objects.all()
    serializer_class = JobHistorySerializer
    permission_classes = [IsAdminSchool]

class SpecialityHistoryViewSet(viewsets.ModelViewSet):
    queryset = JobHistory.objects.all()
    serializer_class = SpecialityHistorySerializer
    permission_classes = [IsAdminSchool]

class KruzhokListApi(viewsets.ModelViewSet):
    queryset = Kruzhok.objects.all()
    serializer_class = KruzhokSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = KruzhokFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return Kruzhok.objects.all()
            else:
                return Kruzhok.objects.filter(school=self.request.user.school)
        return Kruzhok.objects.all()
    
    @action(detail=False, methods=['get'])
    def available_teachers(self, request, *args, **kwargs):
        teachers = Teacher.objects.all()
        serializer = SimpleTeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        lessons = instance.lessons.all()
        for lesson in lessons:
            lesson.delete()
        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)

class DopUrokApi(viewsets.ModelViewSet):
    queryset = DopUrok.objects.all()
    serializer_class = DopUrokSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = DopUrokFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return DopUrok.objects.all()
            else:
                return DopUrok.objects.filter(school=self.request.user.school)
        return DopUrok.objects.all()


class DopUrokRingApi(viewsets.ModelViewSet):
    queryset = DopUrokRing.objects.all()
    serializer_class = DopUrokRingSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = DopUrokRingFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return DopUrokRing.objects.all()
            else:
                return DopUrokRing.objects.filter(school=self.request.user.school)
        return DopUrokRing.objects.all()


class NewsApi(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminSchool]
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(school=self.request.user.school)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return News.objects.all()
            else:
                return News.objects.filter(school=self.request.user.school)
        return News.objects.all()