# Generated by Django 5.0.2 on 2024-02-29 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questioners', '0007_category_time_frame'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
