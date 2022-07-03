# Generated by Django 4.0.5 on 2022-07-03 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_catalog', '0005_alter_rating_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='product_catalog.product'),
            preserve_default=False,
        ),
    ]