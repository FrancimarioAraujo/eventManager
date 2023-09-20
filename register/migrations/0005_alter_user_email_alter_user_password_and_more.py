# Generated by Django 4.2.4 on 2023-09-15 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_alter_user_email_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]