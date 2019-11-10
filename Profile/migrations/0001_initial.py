# Generated by Django 2.2.6 on 2019-10-20 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('landloard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TenantProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_full_name', models.CharField(blank=True, max_length=191, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=191, null=True)),
                ('user_picture', models.ImageField(upload_to='tenant_profile')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoomateSelection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_roomate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Profile.TenantProfile')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentRequestHeaders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_request_id', models.CharField(max_length=100)),
                ('checkout_request_id', models.CharField(max_length=100)),
                ('response_description', models.CharField(max_length=100)),
                ('phone_number_used_for_payment', models.CharField(blank=True, max_length=100)),
                ('hostel_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landloard.LandlordProfile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]