# Generated by Django 3.2 on 2021-05-17 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0006_remove_user_about'),
        ('store', '0014_auto_20210517_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('games', models.ManyToManyField(to='store.Game')),
            ],
            options={
                'ordering': ['cart_id', '-created_at'],
            },
        ),
    ]
