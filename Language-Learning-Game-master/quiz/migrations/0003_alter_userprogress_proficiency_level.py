# Generated by Django 4.2.2 on 2023-12-23 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_alter_exercise_choice_a_alter_exercise_choice_b_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprogress',
            name='proficiency_level',
            field=models.CharField(choices=[('Novice', 'Novice'), ('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='Novice', max_length=20),
        ),
    ]