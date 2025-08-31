# properties/signals.py
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Property
from .utils import CACHE_KEY_ALL_PROPERTIES


def invalidate_all_properties_cache():
    cache.delete(CACHE_KEY_ALL_PROPERTIES)


@receiver(post_save, sender=Property)
def property_saved(sender, instance, **kwargs):
    # Invalidate on create and update
    invalidate_all_properties_cache()


@receiver(post_delete, sender=Property)
def property_deleted(sender, instance, **kwargs):
    # Invalidate on delete
    invalidate_all_properties_cache()
