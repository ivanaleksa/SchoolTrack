# Generated by Django 3.0.8 on 2020-10-25 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('rang', models.CharField(max_length=30, verbose_name='Должность')),
                ('photo', models.ImageField(upload_to='photoTeacher/', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
            },
        ),
    ]
