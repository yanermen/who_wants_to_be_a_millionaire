# Generated by Django 3.1.4 on 2020-12-02 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('millionaire_app', '0011_auto_20201202_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='used_questions',
            field=models.BooleanField(default=False),
        ),
    ]
