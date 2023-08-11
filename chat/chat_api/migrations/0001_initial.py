# Generated by Django 4.1.7 on 2023-03-03 22:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('current_users', models.ManyToManyField(blank=True, related_name='current_rooms', to=settings.AUTH_USER_MODEL)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]