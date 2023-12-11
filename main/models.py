from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth.models import User
import datetime

class Admin(models.Model):
    email = models.CharField('email', max_length=100)
    password = models.CharField('password', max_length=100)
    school = models.OneToOneField('School', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Admins'
        unique_together = ['school']

    def __str__(self):
        return f'{self.email}'


class School(models.Model):
    school_full_name = models.CharField('school_full_name', max_length=255)
    url = models.CharField('url', max_length=255)
    city = models.CharField('city', max_length=255)
    logo = models.ImageField(blank=True, null=True)
    user = models.ForeignKey('Admin', on_delete=models.CASCADE, null=True, related_name='Admins')

    class Meta:
        verbose_name_plural = 'Schools'

    def __str__(self):
        return f'{self.school_full_name}'

class Classrooms(models.Model):
    classroom_name = models.CharField(max_length=250)
    classroom_number = models.IntegerField(default=1)
    flat = models.IntegerField()
    korpus = models.IntegerField()
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Classrooms'

    def __str__(self):
        return f'{self.classroom_name}'
    
class Teacher(models.Model):
    full_name = models.CharField(max_length=250)
    photo3x4 = models.ImageField(null=True, blank=True)
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    classl = models.OneToOneField('Class', on_delete=models.SET_NULL, null=True, blank=True, related_name="teacher")
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True)
    short_info = models.TextField()

    class Meta:
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return f'{self.full_name}'

class Class(models.Model):
    class_name = models.CharField(max_length=150)
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    classroom = models.ForeignKey('Classrooms', on_delete=models.CASCADE, null=True)
    class_teacher = models.OneToOneField(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='class_teacher')

    class Meta:
        verbose_name_plural = 'Classes'

    def __str__(self):
        return f'{self.class_name}'
    
class TeacherWorkload(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True)
    classl = models.ForeignKey('Class', on_delete=models.CASCADE, null=True)
    count = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 51)])
    classroom = models.ForeignKey('Classrooms', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.teacher} Workload"
    

class Schedule(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    Monday = "Пн"
    Tuesday = "Вт"
    Wednesday = "Ср"
    Thursday = "Чт"
    Friday = "Пт"
    Saturday = "Сб"
    WEEK_DAY_CHOICES = [
        (Monday, "Пн"),
        (Tuesday, "Вт"),
        (Wednesday, "Ср"),
        (Thursday, "Чт"),
        (Friday, "Пт"),
        (Saturday, "Сб")
    ]
    week_day = models.CharField(
        max_length=20,
        choices=WEEK_DAY_CHOICES,
        default=Monday,
    )
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True)
    classl = models.ForeignKey('Class', on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True)
    classroom = models.ForeignKey('Classrooms', on_delete=models.CASCADE, null=True)
    start_time = models.TimeField(default=datetime.time(0, 0))
    end_time = models.TimeField(default=datetime.time(0, 0))
    teacher2 = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True,blank=True, related_name='teacher_g2')
    classroom2 = models.ForeignKey('Classrooms', on_delete=models.CASCADE, null=True,blank=True, related_name='classroom_g2')
    subject2 = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True, blank=True, related_name='subject_g2')
    plan = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 10)])
    smena = models.IntegerField(choices=[(1, '1 смена'), (2, '2 смена'),(3, '3 смена'),(4, '4 смена')], default=1)

    def __str__(self):
        return f'{self.school} {self.classl} - {self.week_day} - {self.start_time.strftime("%H:%M")} - {self.end_time.strftime("%H:%M")}'

class Facultative(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    Monday = "Пн"
    Tuesday = "Вт"
    Wednesday = "Ср"
    Thursday = "Чт"
    Friday = "Пт"
    Saturday = "Сб"
    WEEK_DAY_CHOICES = [
        (Monday, "Пн"),
        (Tuesday, "Вт"),
        (Wednesday, "Ср"),
        (Thursday, "Чт"),
        (Friday, "Пт"),
        (Saturday, "Сб")
    ]
    week_day = models.CharField(
        max_length=20,
        choices=WEEK_DAY_CHOICES,
        default=Monday,
    )
    faculative_name = models.CharField(max_length=200)
    classl = models.ForeignKey('Class', on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True)
    classroom = models.ForeignKey('Classrooms', on_delete=models.CASCADE, null=True)
    start_time = models.TimeField(default=datetime.time(0, 0))
    end_time = models.TimeField(default=datetime.time(0, 0))

    def __str__(self):
        return f'{self.school} - {self.classl} - {self.week_day} - {self.faculative_name}'



class Menu(models.Model):
    food_name = models.CharField(max_length=250)
    food_reti = models.CharField(max_length=150)
    food_sostav = models.TextField()
    vihod_1 = models.CharField(max_length=100, null=True)
    vihod_2 = models.CharField(max_length=100, null=True)
    vihod_3 = models.CharField(max_length=100, null=True)
    Monday = "Пн"
    Tuesday = "Вт"
    Wednesday = "Ср"
    Thursday = "Чт"
    Friday = "Пт"
    Saturday = "Сб"
    WEEK_DAY_CHOICES = [
        (Monday, "Пн"),
        (Tuesday, "Вт"),
        (Wednesday, "Ср"),
        (Thursday, "Чт"),
        (Friday, "Пт"),
        (Saturday, "Сб")
    ]
    week_day = models.CharField(
        max_length=20,
        choices=WEEK_DAY_CHOICES,
        default=Monday,
    )
    school = models.ForeignKey('School', on_delete=models.CASCADE, null = True)

    class Meta:
        verbose_name_plural = 'Menu'

    def __str__(self):
        return f'{self.food_name}'

class Slider(models.Model):
    slider_name = models.CharField(max_length=355)
    slider_photo = models.ImageField()
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Slider'

    def __str__(self):
        return f'{self.slider_name}'

class News(models.Model):
    INSTAGRAM = 'instagram'
    FACEBOOK = 'facebook'
    MANUAL = 'manual'
    SOCIAL_MEDIA_CHOICES = [
        (INSTAGRAM, 'Instagram'),
        (FACEBOOK, 'Facebook'),
        (MANUAL, 'Manual'),
    ]
    date = models.DateField()
    text = models.TextField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='news')
    type = models.CharField(
        max_length=10,
        choices=SOCIAL_MEDIA_CHOICES,
        default=MANUAL, 
    )
    photos = models.ManyToManyField('PhotoforNews', related_name='news_photos', blank=True)
    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return f'{self.date}  {self.school} news'

class PhotoforNews(models.Model):
    image = models.ImageField(upload_to='main/static/img/school_news')
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news_photos',null=True)

    
class Subject(models.Model):
    full_name = models.CharField(max_length=250)
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Subjects'

    def __str__(self):
        return f'{self.full_name}'



# =============== School Pasport ============================================================

class schoolPasport(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    school_address = models.CharField(max_length=250)
    amount_of_children = models.IntegerField()
    ul_sany = models.IntegerField()
    kiz_sany = models.IntegerField()
    school_lang = models.CharField(max_length=255)
    status = models.CharField(max_length=250)
    vmestimost = models.IntegerField()
    dayarlyk_class_number = models.IntegerField(null=True)
    dayarlyk_student_number = models.IntegerField(null=True)
    number_of_students = models.IntegerField()
    number_of_classes = models.IntegerField()
    number_of_1_4_students = models.IntegerField()
    number_of_1_4_classes = models.IntegerField()
    number_of_5_9_students = models.IntegerField()
    number_of_5_9_classes = models.IntegerField()
    number_of_10_11_students = models.IntegerField()
    number_of_10_11_classes = models.CharField(max_length=20)
    amount_of_family = models.CharField(max_length=20)
    amount_of_parents = models.CharField(max_length=20)
    all_pedagog_number = models.IntegerField(null=True)
    pedagog_sheber = models.IntegerField(null=True)
    pedagog_zertteushy = models.IntegerField(null=True)
    pedagog_sarapshy = models.IntegerField(null=True)
    pedagog_moderator = models.IntegerField(null=True)
    pedagog = models.IntegerField(null=True)
    pedagog_stazher = models.IntegerField(null=True)
    pedagog_zhogary = models.IntegerField(null=True)
    pedagog_1sanat = models.IntegerField(null=True)
    pedagog_2sanat = models.IntegerField(null=True)
    pedagog_sanat_zhok = models.IntegerField(null=True)
    school_history = models.TextField(null=True)

    class Meta:
        verbose_name_plural = 'School Pasport'

    def __str__(self):
        return f'{self.school} + School Passport'
    
class School_SocialMedia(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    INSTAGRAM = 'instagram'
    FACEBOOK = 'facebook'
    website = 'website'
    SOCIAL_MEDIA_CHOICES = [
        (INSTAGRAM, 'Instagram'),
        (FACEBOOK, 'Facebook'),
        (website, 'Manual'),
    ]
    type = models.CharField(
        max_length=10,
        choices=SOCIAL_MEDIA_CHOICES,
        default=website, 
    )
    instagram_account = models.CharField(max_length=250)
    class Meta:
        verbose_name_plural = "School Social Media"

    def __str__(self):
        return f'{self.school} Social Media {self.type}'


class School_Administration(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    administrator_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    administator_photo = models.ImageField()
    position = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "School Administration"

    def __str__(self):
        return f'{self.school} - {self.administrator_name}'


# =================== Pride_of_the_School =====================================================

class Sport_Success(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=100)
    photo = models.ImageField()
    student_success = models.TextField()
    classl = models.ForeignKey('Class', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = f"Pride of the School Sport"
    
    def __str__(self):
        return f'{self.fullname}'
    
class Oner_Success(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=100)
    photo = models.ImageField()
    student_success = models.TextField()
    classl = models.ForeignKey('Class', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = f"Pride of the School Oner"
    
    def __str__(self):
        return f'{self.fullname}'
    
class PandikOlimpiada_Success(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=100)
    photo = models.ImageField()
    student_success = models.TextField()
    classl = models.ForeignKey('Class', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = f"Pride of the School Olimpiada"
    
    def __str__(self):
        return f'{self.fullname}'

class RedCertificate(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=100)
    photo = models.ImageField()
    student_success = models.CharField(max_length=250)
    endyear = models.CharField(max_length=10, default="2011-2022")

    class Meta:
        verbose_name_plural = "Red Certificate"
    
    def __str__(self):
        return f'{self.fullname}, {self.school}, {self.endyear}'

class AltynBelgi(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=100)
    photo = models.ImageField()
    student_success = models.CharField(max_length=250)
    endyear = models.CharField(max_length=10, default="2011-2022")

    class Meta:
        verbose_name_plural = "AltynBelgi"
    
    def __str__(self):
        return f'{self.fullname}, {self.school}, {self.endyear}'

# class School_History(models.Model):
#     school_photo = models.ImageField(upload_to='main/static/img')
#     school_full_name = models.CharField(max_length=100)
#     established =  models.DateField(verbose_name='Established')
#     school_directors = models.TextField()
#     school = models.ForeignKey('School', on_delete=models.CASCADE, null = True)

#     class Meta:
#         verbose_name_plural = "School History"

#     def __str__(self):
#         return f'{self.school_full_name} + History'
    
class School_Director(models.Model):
    director_name = models.CharField(max_length=100)
    director_photo = models.ImageField()
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "School Director"
    
    def __str__(self):
        return f'{self.director_name}'

class Extra_Lessons(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    type_short_name = models.CharField(max_length=100)
    type_full_name = models.CharField(max_length=200)
    type_color = ColorField(verbose_name='Выберите цвет')

    class Meta:
        verbose_name_plural = "Extra Lessons"
    
    def __str__(self):
        return f'{self.type_full_name}'



# ====================================================
#             History 

class JobHistory(models.Model):
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True)
    start_date = models.DateField()
    end_date = models.DateField(max_length=200)
    job_characteristic = models.TextField(default='')

    class Meta:
        verbose_name_plural = "Job History"
    
    def __str__(self):
        return f'{self.teacher} History'


class SpecialityHistory(models.Model):
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True)
    end_date = models.DateField()
    speciality_university = models.TextField()
    srednee = "Среднее"
    Viswee = "Высшее"
    degree_choices= [
        (srednee, "Среднее"),
        (Viswee, "Высшее"),
    ]
    degree = models.CharField(
        max_length=20,
        choices=degree_choices,
        default=Viswee,
    )


    class Meta:
        verbose_name_plural = "Speciality History"
    
    def __str__(self):
        return f'{self.teacher} Speciality History'
    

    # ======================================================================================

class Kruzhok(models.Model):
    kruzhok_name = models.CharField(max_length=250)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to='main/static/img',null=True)
    purpose = models.CharField(max_length=500)
    Monday = "Пн"
    Tuesday = "Вт"
    Wednesday = "Ср"
    Thursday = "Чт"
    Friday = "Пт"
    Saturday = "Сб"
    WEEK_DAY_CHOICES = [
        (Monday, "Пн"),
        (Tuesday, "Вт"),
        (Wednesday, "Ср"),
        (Thursday, "Чт"),
        (Friday, "Пт"),
        (Saturday, "Сб")
    ]

    def __str__(self):
        return f'{self.kruzhok_name} - {self.school}'

class Lesson(models.Model):
    kruzhok = models.ForeignKey(Kruzhok, on_delete=models.CASCADE, related_name='lessons')
    week_day = models.CharField(
        max_length=20,
        choices=Kruzhok.WEEK_DAY_CHOICES,
        default=Kruzhok.Monday,
    )
    start_end_time = models.CharField(max_length=150, default="8:00-8:45")
    lesson_order = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ['kruzhok', 'week_day', 'start_end_time', 'lesson_order']

    def __str__(self):
        return f'{self.kruzhok.kruzhok_name} - {self.get_week_day_display()} {self.start_time} - {self.end_time}'