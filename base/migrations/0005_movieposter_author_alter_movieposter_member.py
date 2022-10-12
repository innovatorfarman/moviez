# Generated by Django 4.1.2 on 2022-10-12 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0004_rename_poster_movieposter_poster_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieposter',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='movieposter',
            name='member',
            field=models.ManyToManyField(related_name='member', to=settings.AUTH_USER_MODEL),
        ),
    ]