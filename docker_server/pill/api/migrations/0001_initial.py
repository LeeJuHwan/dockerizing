# Generated by Django 4.1.6 on 2023-02-09 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('save_files', models.FileField(blank=True, upload_to='Uploaded Files/%y/%m/%d/')),
                ('pub_date', models.DateField(auto_now=True)),
            ],
        ),
    ]