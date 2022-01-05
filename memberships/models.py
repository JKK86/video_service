from django.db import models

FREE = 1
BASIC = 2
PREMIUM = 3


class Membership(models.Model):

    MEMBERSHIP_CHOICES = (
        (FREE, "free"),
        (BASIC, "basic"),
        (PREMIUM, "premium"),
    )

    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    type = models.IntegerField(choices=MEMBERSHIP_CHOICES, default=FREE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stripe_plan_id = models.CharField(max_length=64)

    def __str__(self):
        return self.get_type_display()


class Subscription(models.Model):
    stripe_subscription_id = models.CharField(max_length=64)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE, related_name="subscriptions")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.profile.user.username
