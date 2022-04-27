# Generated by Django 3.2 on 2022-04-27 19:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles1', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_name', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('review', models.TextField(blank=True, max_length=300, null=True)),
                ('buy_again', models.BooleanField(default=True)),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles1.userprofile')),
                ('wine_name', models.ManyToManyField(to='products.Wine')),
            ],
        ),
    ]
