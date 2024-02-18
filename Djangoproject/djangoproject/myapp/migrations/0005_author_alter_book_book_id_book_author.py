# Generated by Django 5.0.1 on 2024-02-18 08:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_book_book_id_alter_book_cover_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.CharField(default='79ec3bc3', max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.author'),
            preserve_default=False,
        ),
    ]
