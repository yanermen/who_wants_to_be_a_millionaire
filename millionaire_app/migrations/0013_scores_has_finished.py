# Generated by Django 3.1.4 on 2020-12-03 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('millionaire_app', '0012_questions_used_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='scores',
            name='has_finished',
            field=models.BooleanField(default=False),
        ),
    ]
