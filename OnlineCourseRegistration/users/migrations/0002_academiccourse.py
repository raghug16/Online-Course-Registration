# Generated by Django 2.1.1 on 2018-10-25 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicCourse',
            fields=[
                ('academic_course_id', models.IntegerField(db_column='Academic_Course_Id', primary_key=True, serialize=False, unique=True)),
                ('academic_course_name', models.CharField(blank=True, db_column='Academic_Course_Name', max_length=45, null=True)),
                ('academic_course_rigour', models.CharField(db_column='Academic_Course_Rigour', max_length=2)),
                ('academic_course_level', models.IntegerField(db_column='Academic_Course_Level')),
                ('academic_course_pre_req', models.CharField(db_column='Academic_Course_Pre-Req', max_length=1)),
                ('academic_cours_delivery_mode', models.IntegerField(db_column='Academic_Course_Delivery_Mode')),
                ('academic_course_description', models.CharField(blank=True, db_column='Academic_Course_Description', max_length=250, null=True)),
            ],
        ),
    ]