# Generated by Django 2.2 on 2021-06-10 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg_app', '0003_auto_20210528_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friended_users',
            field=models.ManyToManyField(related_name='_user_friended_users_+', to='login_reg_app.User'),
        ),
    ]
