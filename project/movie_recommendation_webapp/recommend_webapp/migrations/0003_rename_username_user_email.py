# Generated by Django 4.1 on 2022-09-20 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_webapp', '0002_rename_email_user_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='email',
        ),
    ]