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


from django.contrib.auth.admin import UserAdmin

class UsersAdmin(UserAdmin):
    list_display = ('email', 'is_active')
    list_display_links = ('email',)
    search_fields = ('email', 'name', )
    readonly_fields = ('id', )
    ordering = ('id',)
    filter_horizontal = ()
    list_filter = ('is_active', 'is_superuser')
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


admin.site.register(Admin, UsersAdmin)

class PhotoforNewsInline(admin.TabularInline):
    model = PhotoforNews
    extra = 1

class NewsAdmin(admin.ModelAdmin):
    model = News
    inlines = [PhotoforNewsInline]

admin.site.register(News, NewsAdmin)


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

admin.site.register(DopUrok)
admin.site.register(TeacherWorkload)
admin.site.register(Sport_Success)
admin.site.register(Oner_Success)
admin.site.register(PandikOlimpiada_Success)
admin.site.register(RedCertificate)
admin.site.register(AltynBelgi)
admin.site.register(School_SocialMedia)
admin.site.register(Ring)
admin.site.register(DopUrokRing)
