# Generated by Django 4.0.2 on 2022-02-27 13:59

from django.db import migrations, models
import django.db.models.deletion
import frontend.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=frontend.models.Image.generate_name)),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=200)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.image')),
            ],
        ),
    ]
