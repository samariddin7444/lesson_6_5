# Generated by Django 5.0.3 on 2024-04-04 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_rename_name_author_first_name'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birth_date',
            field=models.DateField(auto_now_add=True, verbose_name='Birth Date'),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='book',
            name='comments',
            field=models.ManyToManyField(to='library.comments', verbose_name='UsersComments'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(verbose_name='Book Description'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.FloatField(verbose_name='Cost'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Book Title'),
        ),
        migrations.AlterField(
            model_name='bookingbook',
            name='book',
            field=models.ManyToManyField(to='library.book', verbose_name='book'),
        ),
        migrations.AlterField(
            model_name='bookingbook',
            name='student',
            field=models.ManyToManyField(to='student.students', verbose_name='Students'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=models.TextField(verbose_name='Comments'),
        ),
    ]
