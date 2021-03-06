# Generated by Django 3.1.6 on 2021-03-07 13:51

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('mainapp', '0003_auto_20210304_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='doubts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='appuser',
            old_name='interest',
            new_name='tags',
        ),
        migrations.CreateModel(
            name='solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.doubts')),
            ],
        ),
        migrations.AddField(
            model_name='doubts',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.appuser'),
        ),
        migrations.AddField(
            model_name='doubts',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
