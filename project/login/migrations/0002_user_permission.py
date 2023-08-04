# Generated by Django 4.2.3 on 2023-07-16 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='permission',
            field=models.CharField(choices=[('admin', 'Admin'), ('viewer', 'Viewer'), ('user', 'User')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
