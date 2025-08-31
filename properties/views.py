# properties/views.py
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .utils import get_all_properties

# 15-minute view cache (Task 1) + 1-hour queryset cache (Task 2)
@cache_page(60 * 15)
def property_list(request):
    data = get_all_properties()
    return JsonResponse({"count": len(data), "results": data})
