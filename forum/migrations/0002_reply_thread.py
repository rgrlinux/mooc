# Generated by Django 2.0.4 on 2018-08-27 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='thread',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='threads', to='forum.Thread', verbose_name='Tópico'),
            preserve_default=False,
        ),
    ]
