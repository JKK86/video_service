# Generated by Django 4.0 on 2022-01-07 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0004_subscription_profile_delete_usermembership'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='name',
        ),
        migrations.AlterField(
            model_name='membership',
            name='stripe_plan_id',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='membership',
            name='type',
            field=models.IntegerField(choices=[('Free', 'free'), ('Basic', 'basic'), ('Premium', 'premium')], default='Free'),
        ),
    ]
