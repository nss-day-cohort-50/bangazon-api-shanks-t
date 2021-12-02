# Generated by Django 3.2.9 on 2021-12-02 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bangazon_api', '0005_auto_20211130_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='favorites',
            field=models.ManyToManyField(related_name='favorites', through='bangazon_api.Favorite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='like',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked', to='bangazon_api.product'),
        ),
    ]