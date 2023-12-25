# Generated by Django 4.2.7 on 2023-12-25 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dopurok',
            name='faculative_name',
        ),
        migrations.AddField(
            model_name='dopurok',
            name='classroom2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classroom2', to='main.classrooms'),
        ),
        migrations.AddField(
            model_name='dopurok',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.subject'),
        ),
        migrations.AddField(
            model_name='dopurok',
            name='subject2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject2', to='main.subject'),
        ),
        migrations.AddField(
            model_name='dopurok',
            name='teacher2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher2', to='main.teacher'),
        ),
    ]
