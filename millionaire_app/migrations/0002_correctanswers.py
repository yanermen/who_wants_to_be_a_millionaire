# Generated by Django 3.1.3 on 2020-11-30 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('millionaire_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorrectAnswers',
            fields=[
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='millionaire_app.questions')),
                ('correct_answers', models.CharField(max_length=50)),
            ],
        ),
    ]
