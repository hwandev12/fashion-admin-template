from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin

class OrganiserAndLoginRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organised:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)