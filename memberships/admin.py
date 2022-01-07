from django.contrib import admin

from memberships.models import Membership, Subscription


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'type', 'price']
    fields = ['name', 'slug', 'type', 'price']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['stripe_subscription_id', 'profile', 'is_active']
    list_editable = ['is_active', ]
