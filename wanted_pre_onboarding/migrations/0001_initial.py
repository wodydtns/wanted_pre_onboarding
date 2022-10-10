# Generated by Django 4.1.2 on 2022-10-07 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=20)),
                ('company_nation', models.CharField(max_length=20)),
                ('company_region', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('user_password', models.CharField(max_length=200)),
                ('user_create_date', models.DateTimeField()),
                ('user_update_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('employment_id', models.AutoField(primary_key=True, serialize=False)),
                ('employment_position', models.CharField(max_length=50)),
                ('employment_reward', models.IntegerField(default=0)),
                ('employment_use_tech', models.CharField(max_length=50)),
                ('employment_content', models.TextField()),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wanted_pre_onboarding.company')),
            ],
        ),
        migrations.CreateModel(
            name='Applyment',
            fields=[
                ('applyment_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wanted_pre_onboarding.company')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wanted_pre_onboarding.employment')),
            ],
        ),
    ]
