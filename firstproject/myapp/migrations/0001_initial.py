# Generated by Django 2.1.5 on 2019-06-12 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credited_salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.DateField()),
                ('hours', models.IntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.Employee')),
            ],
        ),
        migrations.AddField(
            model_name='salary',
            name='days',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.WorkHours'),
        ),
    ]
