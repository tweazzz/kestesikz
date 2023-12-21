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

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/kruzhok/available_teachers/', KruzhokListApi.as_view({'get': 'available_teachers'}), name='available_teachers'),
    path('api/prideofschool/available_classes/', Sport_SuccessApi.as_view({'get': 'available_classes'}), name='available_classes'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)