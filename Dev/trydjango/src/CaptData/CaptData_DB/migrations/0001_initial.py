# Generated by Django 2.1.7 on 2021-07-27 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaptData_Tbl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Capt_ID', models.CharField(max_length=50)),
                ('Capt_Data', models.CharField(max_length=1000)),
            ],
        ),
    ]
