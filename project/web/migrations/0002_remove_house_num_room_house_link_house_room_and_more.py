# Generated by Django 4.1.6 on 2023-03-10 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='num_room',
        ),
        migrations.AddField(
            model_name='house',
            name='link',
            field=models.CharField(default='test', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='room',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='floor',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]