# Generated by Django 4.2.4 on 2023-10-16 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0029_conversacion_alter_comment_user_alter_profile_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversacion',
            old_name='user_dos',
            new_name='destinatario',
        ),
        migrations.RenameField(
            model_name='conversacion',
            old_name='user_uno',
            new_name='emisor',
        ),
    ]