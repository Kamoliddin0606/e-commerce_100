# Generated by Django 4.0.6 on 2022-08-01 04:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0011_rename_wishlist_wishitem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WishItem',
            new_name='Wishlist',
        ),
    ]
