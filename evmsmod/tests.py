from django.test import TestCase
from djanngo.Http import HttpResponse

# Create your tests here.
def fview(request):
    return HttpResponse("<h1>E-Vaccination Management System</h1>")
