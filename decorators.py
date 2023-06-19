from rest_framework.response import Response
from rest_framework import status
from .models import User

def role_required (allowed_roles = ['HR', 'Manager', 'admin']):

    def decorator(view_func):

        def wrap(request, *args, **kwargs):
            usr = args[0].usr
            if usr['unique_name'] == 'Anonymous User':
                return Response('You are restricted', status = status.HTTP_401_UNAUTHORIZED)
            else:
                User_role = User.objects.get(email = usr['unique_name'])
                if User_role.role in allowed_roles:
                    print('Authorized')
                    return view_func(request, *args, **kwargs)
                else:
                    print('Unauthorized')
                    return Response('You are not an authorized user', status = status.HTTP_401_UNAUTHORIZED)
        return wrap

    return decorator