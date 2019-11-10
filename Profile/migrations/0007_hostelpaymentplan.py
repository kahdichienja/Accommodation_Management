# Generated by Django 2.2.6 on 2019-10-26 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('landloard', '0001_initial'),
        ('Profile', '0006_auto_20191023_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostelPaymentplan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landloard.HostelPlan')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]