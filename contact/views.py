
from django.shortcuts import render
from .models import contact


# Create your views here.
def contactnew(request):
      if request.method == 'POST':
                name = request.POST.get('name')
                email = request.POST.get('email')
                subject = request.POST.get('subject')
                message = request.POST.get('message')
                contact.objects.create(name = name, email=email, subject=subject,message=message)
            
                return render(request, "indexnew.html")  
      return render(request,"indexnew.html")