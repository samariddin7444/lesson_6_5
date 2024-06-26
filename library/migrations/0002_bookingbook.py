# Generated by Django 5.0.3 on 2024-04-02 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('take_date', models.DateField(auto_now_add=True)),
                ('return_date', models.BooleanField(default=False)),
                ('book', models.ManyToManyField(to='library.book')),
                ('student', models.ManyToManyField(to='student.students')),
            ],
        ),
    ]
