# Generated by Django 4.2.16 on 2024-12-07 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0005_alter_payment_paid_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="paid_by",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="shop.user"
            ),
        ),
    ]
