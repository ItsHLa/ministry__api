from rest_framework.response import Response
from rest_framework import status
def allow_user(allow_role=()):
    def decorator(view_func):
        def wrapper_func(request , *args , **kwargs):
            if request.user.groups.filter(name__in=allow_role).exists():
                return view_func(request , *args , **kwargs)
            else:
                return Response({"msg":'user dose not have access to this'},status = status.HTTP_400_BAD_REQUEST )
        return wrapper_func
    return decorator

            