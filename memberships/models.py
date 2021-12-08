from django.db import models

from video_service import settings

FREE = 1
BASIC = 2
PREMIUM = 3

MEMBERSHIP_CHOICES = (
    (FREE, "free"),
    (BASIC, "basic"),
    (PREMIUM, "premium"),
)


class Membership(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    type = models.IntegerField(choices=MEMBERSHIP_CHOICES, default=FREE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stripe_plan_id = models.CharField(max_length=64)

    def __str__(self):
        return self.get_type_display()


class UserMembership(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="membership")
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)
    stripe_customer_id = models.CharField(max_length=64)

    def __str__(self):
        return self.user.username


class Subscription(models.Model):
    stripe_subscription_id = models.CharField(max_length=64)
    user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE, related_name="subscriptions")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_membership.user.username
