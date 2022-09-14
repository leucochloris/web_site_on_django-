# Generated by Django 4.1 on 2022-09-13 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('user_id', models.IntegerField(auto_created=True, max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='ID юзера')),
                ('name', models.TextField(verbose_name='Имя юзера')),
                ('surname', models.TextField(verbose_name='Фамилия юзера')),
                ('city', models.TextField(verbose_name='Город юзера')),
                ('age', models.TextField(verbose_name='Возраст юзера')),
                ('level', models.TextField(verbose_name='Уровень владения юзера')),
                ('phone', models.IntegerField(max_length=15, verbose_name='Телефон юзера')),
                ('join_date', models.DateTimeField(verbose_name='Дата регистрации')),
                ('is_active', models.BooleanField(default=0, verbose_name='Cтатус юзера АКТИВ/НЕ АКТИВНЫЙ')),
            ],
        ),
    ]
