# Generated by Django 3.1.7 on 2021-03-08 12:18

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, choices=[('dr', 'Doctor'), ('fr', 'Farmer')], max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('bio', models.TextField(blank=True, max_length=2000, null=True)),
                ('years_of_experiance', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('phone_number', models.CharField(blank=True, max_length=14, null=True)),
                ('profile_pik', models.ImageField(blank=True, null=True, upload_to='profiles')),
                ('stars', models.ManyToManyField(blank=True, related_name='stars', to=settings.AUTH_USER_MODEL, verbose_name='stars')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
