from django.http import HttpResponseForbidden

def role_required(required_role):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.role != required_role:
                return HttpResponseForbidden("You do not have permission to access this page.")
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
