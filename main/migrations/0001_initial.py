# Generated by Django 4.2.3 on 2023-07-16 23:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('duration', models.CharField(blank=True, default='', max_length=200)),
                ('cost', models.CharField(choices=[('one-thousand', 'R1000.00'), ('two-thousand', 'R2000.00'), ('three-thousand', 'R3000.00'), ('four-thousand', 'R4000.00'), ('five-thousand', 'R5000.00')], default='SELECT-COURSE-COST', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(blank=True, default='', max_length=200)),
                ('course', models.CharField(choices=[('SELECT-COURSE', 'SELECT COURSE'), ('ICDL-WORK-FORCE', 'ICDL WORK FORCE'), ('ICDL-PROFESSIONAL', 'ICDL PROFESSIONAL'), ('ICDL-STUDENT', 'ICDL STUDENT'), ('ICDL-DIGITAL-CITIZEN', 'ICDL DIGITAL CITIZEN')], default='SELECT-COURSE', max_length=30)),
                ('email_address', models.TextField()),
                ('phone_number', models.CharField(max_length=12)),
                ('date_enrolled', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date modified')),
                ('courses', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.courses', verbose_name='Series')),
            ],
        ),
    ]
