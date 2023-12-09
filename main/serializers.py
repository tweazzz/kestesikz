from rest_framework import serializers

from .models import *


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class ClassroomApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classrooms
        fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class schoolPasportApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = schoolPasport
        fields = '__all__'

class School_AdministrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = School_Administration
        fields = '__all__'

class Pride_of_the_SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pride_of_the_School
        fields = '__all__'

class School_HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = School_History
        fields = '__all__'

class School_DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = School_Director
        fields = '__all__'

class Extra_LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra_Lessons
        fields = '__all__'


class FacultativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultative
        fields = '__all__'
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
        fields = ['end_date', 'speciality_university', 'degree']

class TeacherSerializer(serializers.ModelSerializer):
    job_history = JobHistorySerializer(many=True, read_only=True)
    speciality_history = SpecialityHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = [
            'id', 'full_name', 'photo3x4', 'school', 'classl', 'subject', 'short_info',
            'job_history', 'speciality_history'
        ]

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
    subject = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(),
        write_only=True,
        required=False
    )
    job_history = JobHistorySerializer(many=True, required=False)
    speciality_history = SpecialityHistorySerializer(many=True, required=False)

    class Meta:
        model = Teacher
        fields = ['full_name', 'photo3x4', 'short_info', 'job_history', 'speciality_history', 'school', 'classl', 'subject']

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

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['week_day', 'start_time', 'end_time']

class KruzhokSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Kruzhok
        fields = ['id', 'kruzhok_name', 'school', 'teacher', 'photo', 'purpose', 'lessons']

    def create(self, validated_data):
        lessons_data = validated_data.pop('lessons')
        kruzhok = Kruzhok.objects.create(**validated_data)
        
        lesson_order_counter = 1
        for lesson_data in lessons_data:
            Lesson.objects.create(kruzhok=kruzhok, lesson_order=lesson_order_counter, **lesson_data)
            lesson_order_counter += 1

        return kruzhok