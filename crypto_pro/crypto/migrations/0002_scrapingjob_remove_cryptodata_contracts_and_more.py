# Generated by Django 5.0.6 on 2024-06-10 07:45

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapingJob',
            fields=[
                ('job_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='PENDING', max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='cryptodata',
            name='contracts',
        ),
        migrations.DeleteModel(
            name='Contract',
        ),
    ]
