# Generated by Django 4.0.6 on 2022-07-21 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(choices=[('FO', 'Football'), ('IH', 'Ice Hcckey'), ('GO', 'Golf'), ('TE', 'Tennis'), ('PA', 'Padel'), ('OT', 'Other')], default='FO', max_length=2),
        ),
    ]
