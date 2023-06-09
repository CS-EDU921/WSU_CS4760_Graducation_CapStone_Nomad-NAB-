# Generated by Django 4.1.3 on 2023-03-18 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NeedABedAPI', '0003_location_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demographics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_key', models.BinaryField(default=b'none', max_length=50)),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Nonbinary')])),
                ('veteran', models.BooleanField(default=False)),
                ('pregnant', models.BooleanField(default=False)),
                ('victim_dv', models.BooleanField(default=False)),
                ('lgbtq', models.BooleanField(default=False)),
                ('custodian', models.BooleanField(default=False)),
                ('dog', models.BooleanField(default=False)),
                ('poc', models.BooleanField(default=False)),
                ('disabled', models.BooleanField(default=False)),
                ('esl', models.BooleanField(default=False)),
                ('deaf', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='location',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='location',
            name='shelter_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_type',
            field=models.CharField(max_length=50),
        ),
    ]
