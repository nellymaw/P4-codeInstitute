# Generated by Django 4.0.5 on 2022-07-13 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_comment_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
