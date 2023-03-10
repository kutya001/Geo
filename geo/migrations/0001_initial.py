# Generated by Django 4.1.7 on 2023-02-22 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('deleted_date', models.DateTimeField(null=True, verbose_name='Дата удаления')),
                ('name_culture', models.CharField(max_length=200, verbose_name='Культура')),
            ],
            options={
                'db_table': 'appGeaDjango_culture',
            },
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('deleted_date', models.DateTimeField(null=True, verbose_name='Дата удаления')),
                ('name_farmer', models.CharField(max_length=200, verbose_name='Фермер')),
            ],
            options={
                'db_table': 'appGeaDjango_farmer',
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('deleted_date', models.DateTimeField(null=True, verbose_name='Дата удаления')),
                ('name_season', models.CharField(max_length=200, verbose_name='Сезон')),
            ],
            options={
                'db_table': 'appGeaDjango_season',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('deleted_date', models.DateTimeField(null=True, verbose_name='Дата удаления')),
                ('name_place', models.CharField(max_length=200, verbose_name='Земля')),
                ('culture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo.culture', verbose_name='Култура')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo.farmer', verbose_name='Фермер')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo.season', verbose_name='Сезон')),
            ],
            options={
                'db_table': 'appGeaDjango_place',
            },
        ),
    ]
