# Generated by Django 4.2.5 on 2023-10-13 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloghome', '0012_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
