# Generated by Django 5.0.1 on 2024-02-18 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_book_author_alter_book_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.CharField(default='ea22e163', max_length=20, unique=True),
        ),
    ]
