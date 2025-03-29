# Generated by Django 4.2 on 2025-03-28 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Special_services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_zero', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='service')),
                ('content_one', models.TextField()),
                ('content_zero', models.TextField()),
                ('content_two', models.TextField()),
                ('content_three', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(to='portfolio.category')),
                ('specials', models.ManyToManyField(to='service.special_services')),
            ],
        ),
    ]
