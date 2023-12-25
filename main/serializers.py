from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import Admin
from .models import *
from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id','is_superuser', 'email', 'username', 'school']


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
    classroom = serializers.PrimaryKeyRelatedField(
        queryset=Classrooms.objects.all(),
        write_only=True
    )

    class Meta:
        model = Class
        fields = ['id', 'class_name', 'class_number','language', 'classroom', 'class_teacher', 'osnova_plan', 'osnova_smena', 'dopurok_plan', 'dopurok_smena', 'school']
        read_only_fields = ['school']

    def to_representation(self, instance):
        representation = super(ClassSerializer, self).to_representation(instance)
        
        if 'classroom' in representation:
            classroom_id = representation['classroom']
            if classroom_id:
                try:
                    classroom_instance = Classrooms.objects.get(id=classroom_id)
                    representation['classroom'] = str(classroom_instance)
                except Classrooms.DoesNotExist:
                    pass
        
        return representation


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
class AvailableSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'school_kz_name']

class AvailableTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'full_name']

class AvailableRingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ring
        fields = ['id', 'start_time', 'end_time']

class AvailableSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'full_name']

class AvailableClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classrooms
        fields = ['id', 'classroom_name', 'classroom_number']

class AvailableClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'class_name']

class Sport_SuccessSerializer(serializers.ModelSerializer):
    class_id = serializers.PrimaryKeyRelatedField(
        source='classl',
        queryset=Class.objects.all(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Sport_Success
        fields = ['id', 'fullname', 'photo', 'student_success', 'classl', 'school', 'class_id']
        read_only_fields = ['school']

    classl = serializers.SerializerMethodField()

    def get_classl(self, obj):
        return str(obj.classl) if obj.classl else None
    
    def create(self, validated_data):
        class_id = validated_data.pop('class_id', None)
        sport_succes = Sport_Success.objects.create(**validated_data)
        if class_id:
            try:
                class_instance = Class.objects.get(id=class_id)
                sport_succes.classl = class_instance
                sport_succes.save() 
            except Class.DoesNotExist:
                pass
        return sport_succes

class Oner_SuccessSerializer(serializers.ModelSerializer):
    class_id = serializers.PrimaryKeyRelatedField(
        source='classl',
        queryset=Class.objects.all(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Oner_Success
        fields = ['id', 'fullname', 'photo', 'student_success', 'classl', 'school', 'class_id']
        read_only_fields = ['school']

    classl = serializers.SerializerMethodField()

    def get_classl(self, obj):
        return str(obj.classl) if obj.classl else None
    
    def create(self, validated_data):
        class_id = validated_data.pop('class_id', None)

        oner_success = Oner_Success.objects.create(**validated_data)

        if class_id:
            try:
                class_instance = Class.objects.get(id=class_id)
                oner_success.classl = class_instance
                oner_success.save()
            except Class.DoesNotExist:
                pass

        return oner_success



class PandikOlimpiada_SuccessSerializer(serializers.ModelSerializer):
    class_id = serializers.PrimaryKeyRelatedField(
        source='classl',
        queryset=Class.objects.all(),
        write_only=True,
        required=False
    )

    class Meta:
        model = PandikOlimpiada_Success
        fields = ['id', 'fullname', 'photo', 'student_success', 'classl', 'school', 'class_id']
        read_only_fields = ['school']

    classl = serializers.SerializerMethodField()

    def get_classl(self, obj):
        return str(obj.classl) if obj.classl else None
    
    def create(self, validated_data):
        class_id = validated_data.pop('class_id', None)

        PandikOlimpiada = PandikOlimpiada_Success.objects.create(**validated_data)

        if class_id:
            try:
                class_instance = Class.objects.get(id=class_id)
                PandikOlimpiada.classl = class_instance
                PandikOlimpiada.save()
            except Class.DoesNotExist:
                pass

        return PandikOlimpiada

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
        fields = ['id', 'week_day', 'ring','ring_id', 'classl','classl_id', 'teacher', 'teacher_id', 'subject','subject_id', 'classroom','classroom_id', 'teacher2','teacher2_id', 'classroom2','classroom2_id', 'subject2','subject2_id', 'typez','typez_id', 'school']
        read_only_fields = ['school']

    teacher = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(),
        write_only=True,
        required=False
    )
    ring = serializers.PrimaryKeyRelatedField(
        queryset=Ring.objects.all(),
        write_only=True,
        required=False
    )
    classl = serializers.PrimaryKeyRelatedField(
        queryset=Class.objects.all(),
        write_only=True,
        required=False
    )
    subject = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(),
        write_only=True,
        required=False
    )
    classroom = serializers.PrimaryKeyRelatedField(
        queryset=Classrooms.objects.all(),
        write_only=True,
        required=False
    )
    teacher2 = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(),
        write_only=True,
        required=False
    )
    subject2 = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(),
        write_only=True,
        required=False
    )
    classroom2 = serializers.PrimaryKeyRelatedField(
        queryset=Classrooms.objects.all(),
        write_only=True,
        required=False
    )
    typez = serializers.PrimaryKeyRelatedField(
        queryset=Extra_Lessons.objects.all(),
        write_only=True,
        required=False
    )

    def create(self, validated_data):
        teacher = validated_data.pop('teacher', None)
        ring = validated_data.pop('ring', None)
        classl = validated_data.pop('classl', None)
        subject = validated_data.pop('subject', None)
        classroom = validated_data.pop('classroom', None)
        teacher2 = validated_data.pop('teacher2', None)
        subject2 = validated_data.pop('subject2', None)
        classroom2 = validated_data.pop('classroom2', None)
        typez = validated_data.pop('typez', None)

        schedule = DopUrok.objects.create(**validated_data)

        if teacher:
            schedule.teacher = teacher
        if ring:
            schedule.ring = ring
        if classl:
            schedule.classl = classl
        if subject:
            schedule.subject = subject
        if classroom:
            schedule.classroom = classroom
        if teacher2:
            schedule.teacher2 = teacher2
        if subject2:
            schedule.subject2 = subject2
        if classroom2:
            schedule.classroom2 = classroom2
        if typez:
            schedule.typez = typez

        schedule.save()

        return schedule
    
    def update(self, instance, validated_data):
        instance.week_day = validated_data.get('week_day', instance.week_day)

        teacher_id = validated_data.get('teacher')
        if teacher_id:
            instance.teacher = Teacher.objects.get(id=teacher_id)

        ring_id = validated_data.get('ring')
        if ring_id:
            instance.ring = Ring.objects.get(id=ring_id)

        classl_id = validated_data.get('classl')
        if classl_id:
            instance.classl = Class.objects.get(id=classl_id)

        subject_id = validated_data.get('subject')
        if subject_id:
            instance.subject = Subject.objects.get(id=subject_id)

        classroom_id = validated_data.get('classroom')
        if classroom_id:
            instance.classroom = Classrooms.objects.get(id=classroom_id)

        teacher2_id = validated_data.get('teacher2')
        if teacher2_id:
            instance.teacher2 = Teacher.objects.get(id=teacher2_id)

        subject2_id = validated_data.get('subject2')
        if subject2_id:
            instance.subject2 = Subject.objects.get(id=subject2_id)

        classroom2_id = validated_data.get('classroom2')
        if classroom2_id:
            instance.classroom2 = Classrooms.objects.get(id=classroom2_id)

        typez_id = validated_data.get('typez')
        if typez_id:
            instance.typez = Extra_Lessons.objects.get(id=typez_id)

        instance.save()

        return instance

    def to_representation(self, instance):
        representation = super(DopUrokSerializer, self).to_representation(instance)

        teacher_id = representation.get('teacher_id')
        if teacher_id:
            try:
                teacher_instance = Teacher.objects.get(id=teacher_id)
                representation['teacher'] = AvailableTeacherSerializer(teacher_instance).data
            except Teacher.DoesNotExist:
                pass

        ring_id = representation.get('ring_id')
        if ring_id:
            try:
                ring_instance = Ring.objects.get(id=ring_id)
                representation['ring'] = AvailableRingSerializer(ring_instance).data
            except Ring.DoesNotExist:
                pass

        classl_id = representation.get('classl_id')
        if classl_id:
            try:
                class_instance = Class.objects.get(id=classl_id)
                representation['classl'] = AvailableClassesSerializer(class_instance).data
            except Class.DoesNotExist:
                pass

        subject_id = representation.get('subject_id')
        if subject_id:
            try:
                subject_instance = Subject.objects.get(id=subject_id)
                representation['subject'] = AvailableSubjectSerializer(subject_instance).data
            except Subject.DoesNotExist:
                pass

        classroom_id = representation.get('classroom_id')
        if classroom_id:
            try:
                classroom_instance = Classrooms.objects.get(id=classroom_id)
                representation['classroom'] = AvailableClassRoomSerializer(classroom_instance).data
            except Classrooms.DoesNotExist:
                pass

        teacher2_id = representation.get('teacher2_id')
        if teacher2_id:
            try:
                teacher2_instance = Teacher.objects.get(id=teacher2_id)
                representation['teacher2'] = AvailableTeacherSerializer(teacher2_instance).data
            except Teacher.DoesNotExist:
                pass

        subject2_id = representation.get('subject2_id')
        if subject2_id:
            try:
                subject2_instance = Subject.objects.get(id=subject2_id)
                representation['subject2'] = AvailableSubjectSerializer(subject2_instance).data
            except Subject.DoesNotExist:
                pass

        classroom2_id = representation.get('classroom2_id')
        if classroom2_id:
            try:
                classroom2_instance = Classrooms.objects.get(id=classroom2_id)
                representation['classroom2'] = AvailableClassRoomSerializer(classroom2_instance).data
            except Classrooms.DoesNotExist:
                pass

        typez_id = representation.get('typez_id')
        if typez_id:
            try:
                typez_instance = Extra_Lessons.objects.get(id=typez_id)
                representation['typez'] = Extra_LessonSerializer(typez_instance).data
            except Extra_Lessons.DoesNotExist:
                pass
        
        del representation['teacher_id']
        del representation['ring_id']
        del representation['classl_id']
        del representation['subject_id']
        del representation['classroom_id']
        del representation['teacher2_id']
        del representation['subject2_id']
        del representation['classroom2_id']
        del representation['typez_id']

        return representation

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
        fields = ['id', 'full_name', 'photo3x4', 'subject', 'pedagog', 'job_history', 'speciality_history', 'school']
        read_only_fields = ['school']

    def create(self, validated_data):
        job_history_data = validated_data.pop('job_history', [])
        speciality_history_data = validated_data.pop('speciality_history', [])

        teacher = Teacher.objects.create(**validated_data)

        for job_data in job_history_data:
            JobHistory.objects.create(teacher=teacher, **job_data)

        for speciality_data in speciality_history_data:
            SpecialityHistory.objects.create(teacher=teacher, **speciality_data)

        return teacher

    def update(self, instance, validated_data):
        job_history_data = validated_data.pop('job_history', [])
        speciality_history_data = validated_data.pop('speciality_history', [])

        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.photo3x4 = validated_data.get('photo3x4', instance.photo3x4)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.pedagog = validated_data.get('pedagog', instance.pedagog)

        instance.save()

        instance.jobhistory_set.all().delete()
        for job_data in job_history_data:
            JobHistory.objects.create(teacher=instance, **job_data)

        instance.specialityhistory_set.all().delete()
        for speciality_data in speciality_history_data:
            SpecialityHistory.objects.create(teacher=instance, **speciality_data)

        return instance

class TeacherWorkloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherWorkload
        fields = '__all__'

# Kruzhok
# --------------------------------------------------------------------------------------------

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['week_day', 'start_end_time']

class KruzhokSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)
    teacher_id = serializers.PrimaryKeyRelatedField(
        source='teacher',
        queryset=Teacher.objects.all(),
        write_only=True,
        required=False
    )
    photo = serializers.ImageField(allow_null=True, required=False)

    class Meta:
        model = Kruzhok
        fields = ['id', 'kruzhok_name', 'school', 'teacher', 'photo', 'purpose', 'lessons', 'teacher_id']
        read_only_fields = ['school']

    def create(self, validated_data):
        lessons_data = validated_data.pop('lessons', [])
        teacher_id = validated_data.pop('teacher_id', None)
        photo = validated_data.pop('photo', None)

        kruzhok = Kruzhok.objects.create(**validated_data)

        if teacher_id:
            teacher = Teacher.objects.get(id=teacher_id)
            kruzhok.teacher = teacher
            kruzhok.save()

        if photo:
            kruzhok.photo = photo
            kruzhok.save()

        for lesson_data in lessons_data:
            Lesson.objects.create(kruzhok=kruzhok, **lesson_data)

        return kruzhok

    def update(self, instance, validated_data):
        lessons_data = validated_data.pop('lessons', [])
        teacher_id = validated_data.pop('teacher_id', None)

        instance.kruzhok_name = validated_data.get('kruzhok_name', instance.kruzhok_name)
        instance.purpose = validated_data.get('purpose', instance.purpose)

        if teacher_id:
            try:
                teacher = Teacher.objects.get(id=teacher_id)
                instance.teacher = teacher
                instance.save()
            except Teacher.DoesNotExist:
                pass

        Lesson.objects.filter(kruzhok=instance).delete()

        for lesson_data in lessons_data:
            Lesson.objects.create(kruzhok=instance, **lesson_data)

        if 'photo' in validated_data:
            instance.photo = validated_data['photo']

        instance.save()

        return instance

    def to_representation(self, instance):
        representation = super(KruzhokSerializer, self).to_representation(instance)
        teacher_data = AvailableTeacherSerializer(instance.teacher).data
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

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'week_day', 'ring','ring_id', 'classl','classl_id', 'teacher', 'teacher_id', 'subject','subject_id', 'classroom','classroom_id', 'teacher2','teacher2_id', 'classroom2','classroom2_id', 'subject2','subject2_id', 'typez','typez_id', 'school']
        read_only_fields = ['school']

    teacher = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(),
        write_only=True,
        required=False
    )
    ring = serializers.PrimaryKeyRelatedField(
        queryset=Ring.objects.all(),
        write_only=True,
        required=False
    )
    classl = serializers.PrimaryKeyRelatedField(
        queryset=Class.objects.all(),
        write_only=True,
        required=False
    )
    subject = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(),
        write_only=True,
        required=False
    )
    classroom = serializers.PrimaryKeyRelatedField(
        queryset=Classrooms.objects.all(),
        write_only=True,
        required=False
    )
    teacher2 = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(),
        write_only=True,
        required=False
    )
    subject2 = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(),
        write_only=True,
        required=False
    )
    classroom2 = serializers.PrimaryKeyRelatedField(
        queryset=Classrooms.objects.all(),
        write_only=True,
        required=False
    )
    typez = serializers.PrimaryKeyRelatedField(
        queryset=Extra_Lessons.objects.all(),
        write_only=True,
        required=False
    )

    def create(self, validated_data):
        teacher = validated_data.pop('teacher', None)
        ring = validated_data.pop('ring', None)
        classl = validated_data.pop('classl', None)
        subject = validated_data.pop('subject', None)
        classroom = validated_data.pop('classroom', None)
        teacher2 = validated_data.pop('teacher2', None)
        subject2 = validated_data.pop('subject2', None)
        classroom2 = validated_data.pop('classroom2', None)
        typez = validated_data.pop('typez', None)

        schedule = Schedule.objects.create(**validated_data)

        if teacher:
            schedule.teacher = teacher
        if ring:
            schedule.ring = ring
        if classl:
            schedule.classl = classl
        if subject:
            schedule.subject = subject
        if classroom:
            schedule.classroom = classroom
        if teacher2:
            schedule.teacher2 = teacher2
        if subject2:
            schedule.subject2 = subject2
        if classroom2:
            schedule.classroom2 = classroom2
        if typez:
            schedule.typez = typez

        schedule.save()

        return schedule
    
    def update(self, instance, validated_data):
        instance.week_day = validated_data.get('week_day', instance.week_day)

        teacher_id = validated_data.get('teacher')
        if teacher_id:
            instance.teacher = Teacher.objects.get(id=teacher_id)

        ring_id = validated_data.get('ring')
        if ring_id:
            instance.ring = Ring.objects.get(id=ring_id)

        classl_id = validated_data.get('classl')
        if classl_id:
            instance.classl = Class.objects.get(id=classl_id)

        subject_id = validated_data.get('subject')
        if subject_id:
            instance.subject = Subject.objects.get(id=subject_id)

        classroom_id = validated_data.get('classroom')
        if classroom_id:
            instance.classroom = Classrooms.objects.get(id=classroom_id)

        teacher2_id = validated_data.get('teacher2')
        if teacher2_id:
            instance.teacher2 = Teacher.objects.get(id=teacher2_id)

        subject2_id = validated_data.get('subject2')
        if subject2_id:
            instance.subject2 = Subject.objects.get(id=subject2_id)

        classroom2_id = validated_data.get('classroom2')
        if classroom2_id:
            instance.classroom2 = Classrooms.objects.get(id=classroom2_id)

        typez_id = validated_data.get('typez')
        if typez_id:
            instance.typez = Extra_Lessons.objects.get(id=typez_id)

        instance.save()

        return instance

    def to_representation(self, instance):
        representation = super(ScheduleSerializer, self).to_representation(instance)

        teacher_id = representation.get('teacher_id')
        if teacher_id:
            try:
                teacher_instance = Teacher.objects.get(id=teacher_id)
                representation['teacher'] = AvailableTeacherSerializer(teacher_instance).data
            except Teacher.DoesNotExist:
                pass

        ring_id = representation.get('ring_id')
        if ring_id:
            try:
                ring_instance = Ring.objects.get(id=ring_id)
                representation['ring'] = AvailableRingSerializer(ring_instance).data
            except Ring.DoesNotExist:
                pass

        classl_id = representation.get('classl_id')
        if classl_id:
            try:
                class_instance = Class.objects.get(id=classl_id)
                representation['classl'] = AvailableClassesSerializer(class_instance).data
            except Class.DoesNotExist:
                pass

        subject_id = representation.get('subject_id')
        if subject_id:
            try:
                subject_instance = Subject.objects.get(id=subject_id)
                representation['subject'] = AvailableSubjectSerializer(subject_instance).data
            except Subject.DoesNotExist:
                pass

        classroom_id = representation.get('classroom_id')
        if classroom_id:
            try:
                classroom_instance = Classrooms.objects.get(id=classroom_id)
                representation['classroom'] = AvailableClassRoomSerializer(classroom_instance).data
            except Classrooms.DoesNotExist:
                pass

        teacher2_id = representation.get('teacher2_id')
        if teacher2_id:
            try:
                teacher2_instance = Teacher.objects.get(id=teacher2_id)
                representation['teacher2'] = AvailableTeacherSerializer(teacher2_instance).data
            except Teacher.DoesNotExist:
                pass

        subject2_id = representation.get('subject2_id')
        if subject2_id:
            try:
                subject2_instance = Subject.objects.get(id=subject2_id)
                representation['subject2'] = AvailableSubjectSerializer(subject2_instance).data
            except Subject.DoesNotExist:
                pass

        classroom2_id = representation.get('classroom2_id')
        if classroom2_id:
            try:
                classroom2_instance = Classrooms.objects.get(id=classroom2_id)
                representation['classroom2'] = AvailableClassRoomSerializer(classroom2_instance).data
            except Classrooms.DoesNotExist:
                pass

        typez_id = representation.get('typez_id')
        if typez_id:
            try:
                typez_instance = Extra_Lessons.objects.get(id=typez_id)
                representation['typez'] = Extra_LessonSerializer(typez_instance).data
            except Extra_Lessons.DoesNotExist:
                pass
        
        del representation['teacher_id']
        del representation['ring_id']
        del representation['classl_id']
        del representation['subject_id']
        del representation['classroom_id']
        del representation['teacher2_id']
        del representation['subject2_id']
        del representation['classroom2_id']
        del representation['typez_id']

        return representation