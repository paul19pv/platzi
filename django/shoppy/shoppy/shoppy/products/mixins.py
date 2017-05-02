from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
class AuthRedirectMixin(object):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return super(AuthRedirectMixin,self).get(self,request,*args,**kwargs)
class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url='/login'))
    def dispatch(self,request,*args,**kwargs):
        return super(LoginRequiredMixin,self).dispatch(self,request,*args,**kwargs)
