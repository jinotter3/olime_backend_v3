# Generated by Django 4.1.4 on 2023-01-03 21:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contents', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='books',
            field=models.ManyToManyField(blank=True, related_name='contents', to='contents.book'),
        ),
        migrations.AlterField(
            model_name='content',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='contents', to='categories.category'),
        ),
        migrations.AlterField(
            model_name='content',
            name='leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='content',
            name='lectures',
            field=models.ManyToManyField(blank=True, related_name='contents', to='contents.lecture'),
        ),
        migrations.AlterField(
            model_name='content',
            name='tracks',
            field=models.ManyToManyField(blank=True, related_name='contents', to='contents.track'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='books',
            field=models.ManyToManyField(blank=True, related_name='books', to='contents.book'),
        ),
        migrations.AlterField(
            model_name='track',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='tracks', to='categories.category'),
        ),
        migrations.AlterField(
            model_name='track',
            name='leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to=settings.AUTH_USER_MODEL),
        ),
    ]