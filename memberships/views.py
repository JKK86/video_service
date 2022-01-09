from django.shortcuts import render
from django.views.generic import ListView

from memberships.models import Membership


class MembershipListView(ListView):
    model = Membership
    template_name = 'membership_select.html'
    context_object_name = 'plans'

