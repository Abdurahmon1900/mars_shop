# Generated by Django 5.1 on 2024-09-12 04:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='student_group', to='users.group'),
            preserve_default=False,
        ),
    ]
