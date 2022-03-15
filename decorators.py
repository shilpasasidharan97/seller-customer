from django.shortcuts import redirect


def auth_customer(func):
    def wrap(request, *args, **kwargs):
        if 'customer' in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('common:customlogin')
            
    return wrap

def auth_seller(func):
    def wrap(request, *args, **kwargs):
        if 'seller' in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('common:sellerlogin')
            
    return wrap