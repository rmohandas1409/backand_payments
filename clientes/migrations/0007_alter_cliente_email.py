# Generated by Django 4.2.7 on 2023-11-19 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clientes", "0006_cliente_ativo_cliente_rg"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cliente",
            name="email",
            field=models.EmailField(default="", max_length=150),
        ),
    ]