from django.shortcuts import render
from django.views import View

class LoginView(View):
    template_name = 'auth/login.html'
    def get(self, request):
        return render(request, self.template_name)
