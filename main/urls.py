from django.urls import path, include
from . import views
from main.views import *
from rest_framework import routers

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
router.register(r'api/facultative', FacultativeListApi)
router.register(r'api/Sport_SuccessApi', Sport_SuccessApi)
router.register(r'api/Oner_SuccessApi', Oner_SuccessApi)
router.register(r'api/PandikOlimpiadaApi', PandikOlimpiadaApi)
router.register(r'api/School_RedCertificateApi', School_RedCertificateApi)
router.register(r'api/School_AltynBelgiApi', School_AltynBelgiApi)
router.register(r'api/School_SocialMediaApi', School_SocialMediaApi)
router.register(r'api/ringApi', RingApi)

urlpatterns = [
    path('', include(router.urls)),
]