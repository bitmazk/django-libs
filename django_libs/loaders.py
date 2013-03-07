"""Utility functions for loading classes from strings."""
from django.conf import settings


def load_member(fqn):
    """Loads and returns a class for a given fully qualified name."""
    modulename, member_name = split_fqn(fqn)
    module = __import__(modulename, globals(), locals(), member_name)
    return getattr(module, member_name)


def load_member_from_setting(setting_name, settings_module=None):
    settings_to_use = settings_module or settings
    setting_value = getattr(settings_to_use, setting_name)
    return load_member(setting_value)


def split_fqn(fqn):
    """Returns the left and right part of the import."""
    return fqn.rsplit('.', 1)
