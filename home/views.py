from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments, Doctors
from .forms import Bookingform
# Create your views here.
def index(request):

    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    form = Bookingform()
    dict_form={
        'form' : form
    }
    return render(request,'booking.html', dict_form)

def doctor(request):
    dict_docs = {
        'doctors': Doctors.objects.all
    }
    return render(request,'doctor.html', dict_docs)

def dept(request):
    dict_deptt={
        'deptt': Departments.objects.all()
    }
    return render(request,'department.html', dict_deptt)

def contact(request):
    return render(request,'contact.html')