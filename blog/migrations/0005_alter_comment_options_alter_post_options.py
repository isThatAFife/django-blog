# Generated by Django 4.2.16 on 2024-11-21 07:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["created_on"]},
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-created_on"]},
        ),
    ]
