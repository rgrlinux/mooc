# Generated by Django 2.0.4 on 2018-08-26 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20180813_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='courses.Lesson', verbose_name='Aula'),
        ),
    ]