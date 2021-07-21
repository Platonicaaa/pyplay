from django import template

import accounts.utils as utils

register = template.Library()


@register.filter
def is_buyer(user):
    return utils.is_buyer(user)


@register.filter
def is_provider(user):
    return utils.is_provider(user)


@register.filter
def is_admin(user):
    return utils.is_admin(user)
