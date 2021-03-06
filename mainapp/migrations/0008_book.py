# Generated by Django 3.1.6 on 2021-03-10 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20210308_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(default='default_thumbnil.jpg', upload_to='thumbnail/')),
                ('bookpdf', models.FileField(upload_to='book/')),
                ('no_of_pages', models.IntegerField()),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.appuser')),
            ],
        ),
    ]
