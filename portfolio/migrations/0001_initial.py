# Generated by Django 4.2 on 2025-03-28 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image1', models.ImageField(default='default.jpg', upload_to='portfolio')),
                ('image2', models.ImageField(default='default.jpg', upload_to='portfolio')),
                ('image3', models.ImageField(default='default.jpg', upload_to='portfolio')),
                ('image4', models.ImageField(default='default.jpg', upload_to='portfolio')),
                ('content_one', models.TextField()),
                ('quoto', models.TextField()),
                ('content_two', models.TextField()),
                ('project_data', models.DateField(auto_now_add=True)),
                ('price', models.PositiveIntegerField()),
                ('status', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.category')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='root.client')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='root.team')),
            ],
        ),
    ]
