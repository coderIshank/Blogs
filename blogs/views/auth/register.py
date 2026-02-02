from django.shortcuts import render
from django.views import View


class RegisterView(View):
    template_name = 'auth/register.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return render(request, self.template_name)
