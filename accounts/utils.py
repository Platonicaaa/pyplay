def is_buyer(user):
    return user.is_authenticated and user.groups.filter(name='Buyer').exists()


def is_provider(user):
    return user.is_authenticated and user.groups.filter(name='Provider').exists()


def is_admin(user):
    return user.is_authenticated and user.is_superuser
