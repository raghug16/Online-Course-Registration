from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20181019_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('roll', models.CharField(max_length=12)),
                ('year', models.CharField(max_length=4)),
                ('email', models.CharField(max_length=20)),
            ],
        ),
    ]
