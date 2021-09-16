# Generated by Django 3.2.7 on 2021-09-16 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210915_1921'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bill',
            unique_together={('credit_card', 'name', 'date')},
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Está ativo?')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Data de finalização do serviço')),
                ('has_promotion', models.BooleanField(default=False, verbose_name='Tem promoção?')),
                ('promotion_count', models.SmallIntegerField(default=0, verbose_name='Número de meses com a promoção')),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bill', verbose_name='Conta')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
            },
        ),
        migrations.CreateModel(
            name='Installment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.SmallIntegerField(verbose_name='Número de parcelas')),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bill', verbose_name='Conta')),
            ],
            options={
                'verbose_name': 'Parcelamento',
                'verbose_name_plural': 'Parcelamentos',
            },
        ),
        migrations.RemoveField(
            model_name='bill',
            name='end_service_date',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='has_promotion',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='installment_count',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='promotion_count',
        ),
    ]
