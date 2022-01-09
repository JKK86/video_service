from django.db import models

FREE = 'Free'
BASIC = 'Basic'
PREMIUM = 'Premium'


class Membership(models.Model):

    MEMBERSHIP_CHOICES = (
        (FREE, "Free"),
        (BASIC, "Basic"),
        (PREMIUM, "Premium"),
    )

    slug = models.SlugField(max_length=64)
    type = models.CharField(max_length=10, choices=MEMBERSHIP_CHOICES, default=FREE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stripe_plan_id = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.get_type_display()

    class Meta:
        ordering = ['price', ]


class Subscription(models.Model):
    stripe_subscription_id = models.CharField(max_length=64)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE, related_name="subscriptions")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.profile.user.username
