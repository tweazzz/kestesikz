from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import Admin
from .models import *
from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['email','school']


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classrooms
        fields = ['id','classroom_name', 'classroom_number', 'flat', 'korpus','school']
        read_only_fields = ['school']

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id','class_name','language','classroom','class_teacher','osnova_plan','osnova_smena','dopurok_plan','dopurok_smena', 'school']
        read_only_fields = ['school']


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id','week_day','ring','classl','teacher','subject','classroom','teacher2','classroom2','typez','school']
        read_only_fields = ['school']

class RingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ring
        fields = ['id','plan','smena','number','start_time','end_time','school']
        read_only_fields = ['school']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','food_name','food_reti','food_sostav','vihod_1','vihod_2','vihod_3','week_day','school']
        read_only_fields = ['school']

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['id','slider_name','slider_photo','school']
        read_only_fields = ['school']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id','full_name','type','school']
        read_only_fields = ['school']

class schoolPasportApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = schoolPasport
        fields = ['id','school_address','established', 'amount_of_children','ul_sany','kiz_sany','school_lang','status','vmestimost','dayarlyk_class_number','dayarlyk_student_number','number_of_students','number_of_classes','number_of_1_4_students','number_of_1_4_classes','number_of_5_9_students','number_of_5_9_classes','number_of_10_11_students','number_of_10_11_classes','amount_of_family','amount_of_parents','all_pedagog_number','pedagog_sheber','pedagog_zertteushy','pedagog_sarapshy','pedagog_moderator','pedagog','pedagog_stazher','pedagog_zhogary','pedagog_1sanat','pedagog_2sanat','pedagog_sanat_zhok','school_history','school']
        read_only_fields = ['school']

class School_AdministrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = School_Administration
        fields = ['id','administrator_name','phone_number','administator_photo','position','school']
        read_only_fields = ['school']

# ======================================================================
class ClassForProudSSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'class_name']

class Sport_SuccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport_Success
        fields = ['id','fullname','photo','student_success','classl','school']
        read_only_fields = ['school']

class Oner_SuccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oner_Success
        fields = ['id','fullname','photo','student_success','classl','school']
        read_only_fields = ['school']

class PandikOlimpiada_SuccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = PandikOlimpiada_Success
        fields = ['id','fullname','photo','student_success','classl','school']
        read_only_fields = ['school']

class RedCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedCertificate
        fields = ['id','fullname','photo','student_success','endyear','school']
        read_only_fields = ['school']

class AltynBelgiSerializer(serializers.ModelSerializer):
    class Meta:
        model = AltynBelgi
        fields = ['id','fullname','photo','student_success','endyear','school']
        read_only_fields = ['school']

class School_SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = School_SocialMedia
        fields = ['id','type','account_name','school']
        read_only_fields = ['school']

class School_DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = School_Director
        fields = ['id','director_name','director_photo','phone_number','email','school']
        read_only_fields = ['school']

class Extra_LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra_Lessons
        fields = ['id','type_full_name','type_color','school']
        read_only_fields = ['school']


class DopUrokSerializer(serializers.ModelSerializer):
    class Meta:
        model = DopUrok
        fields = ['id','week_day','ring','classl','teacher','classroom','typez','school']
        read_only_fields = ['school']

class DopUrokRingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DopUrokRing
        fields = ['id','plan','smena','number','start_time','end_time','school']
        read_only_fields = ['school']
# ==================================================================================================


class YearField(serializers.Field):
    def to_representation(self, obj):
        return obj.year if obj else None

    def to_internal_value(self, data):
        try:
            return serializers.DateTimeField().to_internal_value(f"{data}-01-01T00:00:00Z")
        except serializers.ValidationError:
            raise serializers.ValidationError("Invalid year format")

class JobHistorySerializer(serializers.ModelSerializer):
    start_date = YearField()
    end_date = YearField()

    class Meta:
        model = JobHistory
        fields = ['start_date', 'end_date', 'job_characteristic']

class SpecialityHistorySerializer(serializers.ModelSerializer):
    end_date = YearField()

    class Meta:
        model = SpecialityHistory
        fields = ['end_date', 'speciality_university', 'mamandygy', 'degree']

class TeacherSerializer(serializers.ModelSerializer):
    job_history = JobHistorySerializer(many=True, read_only=True)
    speciality_history = SpecialityHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ['id','full_name','photo3x4','subject','pedagog','job_history','speciality_history','school']
        read_only_fields = ['school']


    def to_representation(self, instance):
        representation = super(TeacherSerializer, self).to_representation(instance)
        job_history_data = JobHistorySerializer(instance.jobhistory_set.all().order_by('id'), many=True).data
        speciality_history_data = SpecialityHistorySerializer(instance.specialityhistory_set.all().order_by('id'), many=True).data
        representation['job_history'] = job_history_data
        representation['speciality_history'] = speciality_history_data
        return representation

class TeacherCreateSerializer(serializers.ModelSerializer):
    school = serializers.PrimaryKeyRelatedField(
        queryset=School.objects.all(),
        write_only=True,
        required=False
    )
    classl = serializers.PrimaryKeyRelatedField(
        queryset=Class.objects.all(),
        write_only=True,
        required=False
    )
    job_history = JobHistorySerializer(many=True, required=False)
    speciality_history = SpecialityHistorySerializer(many=True, required=False)

    class Meta:
        model = Teacher
        fields = '__all__'

    def create(self, validated_data):
        job_history_data = validated_data.pop('job_history', [])
        speciality_history_data = validated_data.pop('speciality_history', [])

        school = validated_data.pop('school', None)
        if school:
            validated_data['school'] = school
        elif 'school' in validated_data and validated_data['school'] is None:
            validated_data.pop('school')

        classl = validated_data.pop('classl', None)
        if classl:
            validated_data['classl'] = classl
        elif 'classl' in validated_data and validated_data['classl'] is None:
            validated_data.pop('classl')

        subject = validated_data.pop('subject', None)
        if subject:
            validated_data['subject'] = subject
        elif 'subject' in validated_data and validated_data['subject'] is None:
            validated_data.pop('subject')

        teacher = Teacher.objects.create(**validated_data)

        for job_data in job_history_data:
            JobHistory.objects.create(teacher=teacher, **job_data)

        for speciality_data in speciality_history_data:
            SpecialityHistory.objects.create(teacher=teacher, **speciality_data)

        return teacher

class TeacherWorkloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherWorkload
        fields = '__all__'

# Kruzhok
# --------------------------------------------------------------------------------------------

class SimpleTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'full_name']

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['week_day', 'start_end_time']

class KruzhokSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)
    teacher = SimpleTeacherSerializer()

    class Meta:
        model = Kruzhok
        fields = ['id', 'kruzhok_name', 'school', 'teacher', 'photo', 'purpose', 'lessons']
        read_only_fields = ['school']

    def create(self, validated_data):
        lessons_data = validated_data.pop('lessons')
        kruzhok = Kruzhok.objects.create(**validated_data)
        
        lesson_order_counter = 1
        for lesson_data in lessons_data:
            Lesson.objects.create(kruzhok=kruzhok, lesson_order=lesson_order_counter, **lesson_data)
            lesson_order_counter += 1

        return kruzhok
    
    def update(self, instance, validated_data):
        lessons_data = validated_data.pop('lessons')
        instance.kruzhok_name = validated_data.get('kruzhok_name', instance.kruzhok_name)
        instance.purpose = validated_data.get('purpose', instance.purpose)
        instance.save()

        teacher_data = validated_data.get('teacher', {})
        teacher_id = teacher_data.get('id')
        if teacher_id:
            teacher = Teacher.objects.get(id=teacher_id)
            instance.teacher = teacher
            instance.save()

        instance.lessons.all().delete()
        lesson_order_counter = 1
        for lesson_data in lessons_data:
            Lesson.objects.create(kruzhok=instance, lesson_order=lesson_order_counter, **lesson_data)
            lesson_order_counter += 1

        return instance

    def to_representation(self, instance):
        representation = super(KruzhokSerializer, self).to_representation(instance)
        teacher_data = SimpleTeacherSerializer(instance.teacher).data
        representation['teacher'] = teacher_data
        lessons_data = LessonSerializer(instance.lessons.all(), many=True).data
        representation['lessons'] = lessons_data
        return representation
    
    def delete(self):
        instance = self.instance
        instance.delete()
        return instance

class PhotoforNews(serializers.ModelSerializer):
    class Meta:
        model = PhotoforNews
        fields = ['image']

class NewsSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'date', 'text', 'type', 'photos', 'school']
        read_only_fields = ['school']

    def get_photos(self, obj):
        photos_queryset = obj.photos.all()
        return [self.context['request'].build_absolute_uri(photo.image.url) if photo.image else None for photo in photos_queryset]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['photos'] = [self.context['request'].build_absolute_uri(photo.image.url) if photo.image else None for photo in instance.photos.all()]
        return representation
