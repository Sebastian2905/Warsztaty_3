# Generated by Django 2.1.5 on 2019-02-07 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_res', models.DateField()),
                ('description', models.TextField(max_length=500)),
                ('witch_room', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reservation_app.Room')),
            ],
        ),
    ]