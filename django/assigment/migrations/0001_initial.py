# Generated by Django 2.0.7 on 2018-07-27 22:10

import assigment.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('options', djongo.models.fields.ArrayModelField(model_container=assigment.models.Option)),
            ],
            options={
                'db_table': 'questions',
            },
        ),
    ]
