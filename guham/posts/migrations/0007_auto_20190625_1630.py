# Generated by Django 2.1.8 on 2019-06-25 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20190625_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='study_place',
            field=models.CharField(choices=[('강남', '강남역'), ('교대', '교대역'), ('역삼', '역삼역')], max_length=10),
        ),
    ]