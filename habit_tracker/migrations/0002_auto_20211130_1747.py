# Generated by Django 3.2.9 on 2021-11-30 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='habit',
            name='frequency',
        ),
    ]
