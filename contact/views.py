
from django.shortcuts import render
from .models import contact


# Create your views here.
def contactnew(request):
      if request.method == 'POST':
                name = request.POST.get('name')
                email = request.POST.get('email')
                subject = request.POST.get('subject')
                message = request.POST.get('message')
                contact_data = contact(name = name, email=email, subject=subject,message=message)
                contact_data.save()
                return render(request, "indexnew.html")  
      return render(request,"indexnew.html")