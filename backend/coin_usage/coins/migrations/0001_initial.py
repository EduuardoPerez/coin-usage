# Generated by Django 3.2.9 on 2021-12-05 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('ticker_symbol', models.CharField(error_messages={'unique': 'A coin with that ticker symbol already exists.'}, max_length=5, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'coin',
                'ordering': ['ticker_symbol'],
            },
        ),
    ]