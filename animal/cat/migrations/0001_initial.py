# Generated by Django 3.2.6 on 2021-09-25 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='short',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
                ('alfanumeric', models.CharField(max_length=100)),
            ],
        ),
    ]