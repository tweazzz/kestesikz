# Generated by Django 4.2.7 on 2023-12-11 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AltynBelgi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=150)),
                ('student_success', models.CharField(max_length=250)),
                ('endyear', models.CharField(default='2011-2022', max_length=10)),
                ('classl', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.class')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.school')),
            ],
            options={
                'verbose_name_plural': 'Pride of the School',
            },
        ),
        migrations.CreateModel(
            name='RedCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=150)),
                ('student_success', models.CharField(max_length=250)),
                ('endyear', models.CharField(default='2011-2022', max_length=10)),
                ('classl', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.class')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.school')),
            ],
            options={
                'verbose_name_plural': 'Red Certificate',
            },
        ),
        migrations.CreateModel(
            name='School_SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram_account', models.CharField(max_length=250)),
                ('facebook_account', models.CharField(max_length=250)),
                ('youtube_account', models.CharField(max_length=250)),
                ('school_website', models.CharField(max_length=250)),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.school')),
            ],
            options={
                'verbose_name_plural': 'School Social Media',
            },
        ),
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='menu',
            name='vihod',
        ),
        migrations.RemoveField(
            model_name='pride_of_the_school',
            name='type_of_success',
        ),
        migrations.RemoveField(
            model_name='schoolpasport',
            name='email',
        ),
        migrations.RemoveField(
            model_name='schoolpasport',
            name='facebook_account',
        ),
        migrations.RemoveField(
            model_name='schoolpasport',
            name='instagram_account',
        ),
        migrations.RemoveField(
            model_name='schoolpasport',
            name='tel_phone_school',
        ),
        migrations.RemoveField(
            model_name='schoolpasport',
            name='youtube_account',
        ),
        migrations.AddField(
            model_name='classrooms',
            name='classroom_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='lesson',
            name='start_end_time',
            field=models.CharField(default='8:00-8:45', max_length=150),
        ),
        migrations.AddField(
            model_name='menu',
            name='vihod_1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='vihod_2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='vihod_3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='schoolpasport',
            name='all_pedagog_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='schoolpasport',
            name='dayarlyk_class_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='schoolpasport',
            name='dayarlyk_student_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='schoolpasport',
            name='pedagog_1sanat',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='schoolpasport',
            name='pedagog_2sanat',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='schoolpasport',
            name='pedagog_sanat_zhok',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='schoolpasport',
            name='pedagog_stazher',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='schoolpasport',
            name='pedagog_zhogary',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='schoolpasport',
            name='school_history',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='pride_of_the_school',
            name='student_success',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='schoolpasport',
            name='pedagog',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='schoolpasport',
            name='pedagog_moderator',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='schoolpasport',
            name='pedagog_sarapshy',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='schoolpasport',
            name='pedagog_sheber',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='schoolpasport',
            name='pedagog_zertteushy',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together={('kruzhok', 'week_day', 'start_end_time', 'lesson_order')},
        ),
        migrations.DeleteModel(
            name='School_History',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='start_time',
        ),
    ]