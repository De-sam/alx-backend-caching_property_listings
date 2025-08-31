from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property

# Cache this view for 15 minutes (900 seconds)
@cache_page(60 * 15)
def property_list(request):
    """
    Returns a JSON list of all properties.
    View-level caching ensures the entire response is cached in Redis.
    (We'll refactor to low-level queryset caching in Task 2.)
    """
    qs = Property.objects.all().values(
        "id", "title", "description", "price", "location", "created_at"
    )
    data = list(qs)
    return JsonResponse({"count": len(data), "results": data})
