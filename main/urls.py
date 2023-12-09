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
router.register(r'api/pride_of_the_school', Pride_of_the_SchoolApi)
router.register(r'api/school_director', School_DirectorApi)
router.register(r'api/extra_lesson', Extra_LessonsApi)
router.register(r'api/kruzhok', KruzhokListApi)
router.register(r'api/facultative', FacultativeListApi)
router.register(r'api/teacherworkload', TeacherWorkloadApi)


urlpatterns = [
    path('', include(router.urls)),
]