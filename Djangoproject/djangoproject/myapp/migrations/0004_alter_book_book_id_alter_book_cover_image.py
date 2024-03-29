# Generated by Django 5.0.1 on 2024-02-18 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_book_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.CharField(default='e48854ed', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(null=True, upload_to='book_covers/'),
        ),
    ]
