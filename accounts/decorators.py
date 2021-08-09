from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *arg, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *arg, **kwargs)
    return wrapper_func

def authenticated_user(view_func):
    def wrapper_func(request, *arg, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *arg, **kwargs)
        else:
            return redirect('login', **kwargs)
    return wrapper_func