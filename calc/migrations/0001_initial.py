# Generated by Django 4.2.9 on 2024-01-30 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona', models.CharField(choices=[('manager', 'Manager'), ('sales', 'Sales')], max_length=10)),
                ('sales_group', models.CharField(choices=[('checkout', 'Checkout'), ('payouts', 'Payouts'), ('banking', 'Banking')], max_length=10)),
                ('gross_profit', models.FloatField()),
                ('target_profit', models.FloatField()),
            ],
        ),
    ]
