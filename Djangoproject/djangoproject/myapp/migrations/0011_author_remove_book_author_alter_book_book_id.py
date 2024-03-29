# Generated by Django 5.0.1 on 2024-02-18 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_delete_author_alter_book_book_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.CharField(default='3f826c06', max_length=20, unique=True),
        ),
    ]
