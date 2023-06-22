# Generated by Django 4.2.1 on 2023-06-21 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deliver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient_name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('delivery_date', models.DateField()),
                ('is_delivered', models.BooleanField(default=False)),
            ],
        ),
    ]
