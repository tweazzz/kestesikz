from django.contrib import admin

# Register your models here.

from main.models import *



class JobHistoryInline(admin.TabularInline):
    model = JobHistory
    extra = 1

class SpecialityHistoryInline(admin.TabularInline):
    model = SpecialityHistory
    extra = 1

class TeacherAdmin(admin.ModelAdmin):
    inlines = [JobHistoryInline, SpecialityHistoryInline]

admin.site.register(Teacher, TeacherAdmin)


class ClassAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'school', 'classroom', 'class_teacher')
    list_editable = ('class_teacher',)
    search_fields = ('class_name', 'school__name', 'classroom__name', 'class_teacher__full_name')

class PhotoforNewsInline(admin.TabularInline):
    model = PhotoforNews
    extra = 1

class NewsAdmin(admin.ModelAdmin):
    model = News
    inlines = [PhotoforNewsInline]

admin.site.register(News, NewsAdmin)

admin.site.register(Class, ClassAdmin)
admin.site.register(Admin)
admin.site.register(School)
admin.site.register(Classrooms)
admin.site.register(Schedule)
class RingAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TimeField: {'widget': admin.widgets.AdminTimeWidget},
    }
admin.site.register(Menu)
admin.site.register(Slider)
admin.site.register(Subject)
admin.site.register(schoolPasport)
admin.site.register(School_Administration)
admin.site.register(School_Director)
admin.site.register(Extra_Lessons)
class LessonInline(admin.TabularInline): 
    model = Lesson
    extra = 1  

class KruzhokAdmin(admin.ModelAdmin):
    inlines = [LessonInline]

admin.site.register(Kruzhok, KruzhokAdmin)

admin.site.register(Facultative)
admin.site.register(TeacherWorkload)
admin.site.register(Sport_Success)
admin.site.register(Oner_Success)
admin.site.register(PandikOlimpiada_Success)
admin.site.register(RedCertificate)
admin.site.register(AltynBelgi)
admin.site.register(School_SocialMedia)