# Generated by Django 4.1.1 on 2022-10-03 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pattern', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Pattern',
                'verbose_name_plural': 'Patterns',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Type',
                'verbose_name_plural': 'Types',
            },
        ),
        migrations.RemoveField(
            model_name='photo',
            name='filters',
        ),
        migrations.DeleteModel(
            name='filters',
        ),
        migrations.AddField(
            model_name='photo',
            name='pattern',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='helder.pattern'),
        ),
        migrations.AddField(
            model_name='photo',
            name='types',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='helder.type'),
        ),
    ]
