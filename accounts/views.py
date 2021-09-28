from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def home(request):
    # if request.user.is_authenticated:
    #     return render(request, 'pages/home.html')
    # else:
    #     return redirect('login')
    return render(request, 'pages/home.html')
