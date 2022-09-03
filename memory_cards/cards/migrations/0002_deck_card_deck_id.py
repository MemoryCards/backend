# Generated by Django 4.1 on 2022-09-03 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('depiction', models.TextField(max_length=2000)),
                ('categories', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cards.category')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='deck_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cards.deck'),
        ),
    ]
