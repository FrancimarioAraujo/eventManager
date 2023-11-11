# Generated by Django 4.2.4 on 2023-11-11 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='ticketPrice',
        ),
        migrations.AlterField(
            model_name='events',
            name='capacity',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('qtd_ticket', models.PositiveIntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.events')),
            ],
        ),
    ]