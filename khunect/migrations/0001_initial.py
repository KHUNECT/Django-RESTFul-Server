# Generated by Django 2.1 on 2018-10-02 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('realname', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('phoneNum', models.CharField(max_length=20)),
                ('image', models.ImageField(default='media/default_image.jpeg', upload_to='')),
            ],
        ),
    ]