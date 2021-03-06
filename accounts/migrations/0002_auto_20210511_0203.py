# Generated by Django 3.0.14 on 2021-05-10 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='auth_token',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='created_id',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='is_verified',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
