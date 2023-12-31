# Generated by Django 4.2.2 on 2023-12-22 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('proficiency_level', models.IntegerField(default=0)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.language')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('difficulty', models.IntegerField()),
                ('choice_a', models.CharField(max_length=255)),
                ('choice_b', models.CharField(max_length=255)),
                ('choice_c', models.CharField(max_length=255)),
                ('choice_d', models.CharField(max_length=255)),
                ('correct_choice', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.language')),
            ],
        ),
    ]
