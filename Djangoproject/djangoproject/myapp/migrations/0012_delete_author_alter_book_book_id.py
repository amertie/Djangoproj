# Generated by Django 5.0.1 on 2024-02-18 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_author_remove_book_author_alter_book_book_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.CharField(default='e7a31a64', max_length=20, unique=True),
        ),
    ]