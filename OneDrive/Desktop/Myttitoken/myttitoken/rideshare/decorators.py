
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

def csrf_exempt_view(view_func):
    return method_decorator(csrf_exempt)(view_func)
