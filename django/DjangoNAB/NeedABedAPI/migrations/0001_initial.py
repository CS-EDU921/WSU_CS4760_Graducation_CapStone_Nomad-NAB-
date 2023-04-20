# Generated by Django 4.1.3 on 2023-02-20 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField(max_length=100)),
                ('image', models.ImageField(default='images/none/noimg.jpg', upload_to='images')),
            ],
        ),
    ]