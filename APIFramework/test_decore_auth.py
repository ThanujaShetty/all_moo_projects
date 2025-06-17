import requests


def with_auth(token):
    def decorators(func):
        def wrapper(*args, **kwargs):
            headers = kwargs.get("headers", {})
            headers['Authorization'] = f'Bearer {token}'
            kwargs['headers'] = headers
            return func(*args,**kwargs)
        return wrapper
    return decorators

