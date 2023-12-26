from django.urls import path, include,re_path
from . import views
from main.views import *
from rest_framework import routers
from djoser.views import UserViewSet
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'api/admin', AdminsApi)
router.register(r'api/school', SchoolsApi)
router.register(r'api/classroom', ClassroomApi)
router.register(r'api/teacher', TeacherApi)
router.register(r'api/class', ClassApi)
router.register(r'api/schedule', ScheduleApi)
router.register(r'api/menu', MenuApi)
router.register(r'api/slider', SliderApi)
router.register(r'api/subject', SubjectApi)
router.register(r'api/schoolpasport', schoolPasportApi)
router.register(r'api/school_administration', School_AdministrationApi)
router.register(r'api/school_director', School_DirectorApi)
router.register(r'api/extra_lesson', Extra_LessonsApi)
router.register(r'api/kruzhok', KruzhokListApi)
router.register(r'api/Sport_SuccessApi', Sport_SuccessApi)
router.register(r'api/Oner_SuccessApi', Oner_SuccessApi)
router.register(r'api/PandikOlimpiadaApi', PandikOlimpiadaApi)
router.register(r'api/School_RedCertificateApi', School_RedCertificateApi)
router.register(r'api/School_AltynBelgiApi', School_AltynBelgiApi)
router.register(r'api/School_SocialMediaApi', School_SocialMediaApi)
router.register(r'api/ringApi', RingApi)
router.register(r'api/DopUrokApi', DopUrokApi)
router.register(r'api/DopUrokRingApi', DopUrokRingApi)
router.register(r'api/newsApi', NewsApi)
router.register(r'api/teacher-read', TeacherReadApi, basename='teacher-read')
router.register(r'api/kruzhok/read-only', ReadOnlyKruzhokApi,basename='kruzhok-read')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/available_school/', SchoolsApi.as_view({'get': 'available_school'}), name='available-school'),
    path('api/available_teachers/', KruzhokListApi.as_view({'get': 'available_teachers'}), name='available_teachers'),
    path('api/available_classes/', Sport_SuccessApi.as_view({'get': 'available_classes'}), name='available_classes'),
    path('api/available_classrooms/', ClassroomApi.as_view({'get': 'available_classrooms'}), name='available_classrooms'),
    path('api/available_ring/', ScheduleApi.as_view({'get': 'available_ring'}), name='available-ring'),
    path('api/available_subject/', ScheduleApi.as_view({'get': 'available_subject'}), name='available-subject'),
    path('api/available_typez/', Extra_LessonsApi.as_view({'get': 'available_typez'}), name='available-typez'),
    path('api/kruzhok/upload_photo/', KruzhokListApi.as_view({'post': 'upload_photo'}), name='upload_photo'),
    path('api/teacher/upload_photo/', TeacherApi.as_view({'post': 'upload_photo'}), name='upload_photo'),
    path('api/schoolpasport/upload_photo/', schoolPasportApi.as_view({'post': 'upload_photo'}), name='upload_photo'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)