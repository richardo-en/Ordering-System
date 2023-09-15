from functools import wraps
from django.http import HttpResponseForbidden

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Check if the user has the "employee" role
        if request.user.role == 'Admin':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Access Denied: You do not have permission to access this page.")
    return _wrapped_view