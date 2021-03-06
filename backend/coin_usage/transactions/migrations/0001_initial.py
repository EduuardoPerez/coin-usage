# Generated by Django 3.2.9 on 2021-12-06 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coins', '0001_initial'),
        ('accounts', '0006_alter_balance_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('amount', models.FloatField(verbose_name='amount')),
                ('account_from', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions_from', to='accounts.account', verbose_name='account_from')),
                ('account_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions_to', to='accounts.account', verbose_name='account_to')),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='coins.coin', verbose_name='coin')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
