# Generated by Django 2.2.4 on 2019-08-20 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('bylaw', 'bylaw'), ('minutes', 'minutes')], max_length=50),
        ),
    ]
