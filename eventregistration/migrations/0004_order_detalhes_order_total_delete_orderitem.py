# Generated by Django 4.2.4 on 2023-11-11 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventregistration', '0003_orderitem_ticket_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='detalhes',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]