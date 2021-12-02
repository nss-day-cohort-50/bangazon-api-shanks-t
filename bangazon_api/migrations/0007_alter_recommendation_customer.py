# Generated by Django 3.2.9 on 2021-12-02 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bangazon_api', '0006_auto_20211202_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommended_to', to=settings.AUTH_USER_MODEL),
        ),
    ]