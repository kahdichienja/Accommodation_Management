# Generated by Django 2.2.6 on 2019-10-26 19:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0007_hostelpaymentplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostelpaymentplan',
            name='amountpaid',
            field=models.CharField(default=django.utils.timezone.now, max_length=191),
            preserve_default=False,
        ),
    ]
