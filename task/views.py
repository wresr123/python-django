from django.shortcuts import render
from task.models import Client, Manufacturer


# Create your views here.
def home(request):
    return render(request, 'task/home.html')


def login(request):
    return render(request, 'task/login.html')


def select(request):
    return render(request, 'task/select.html')


def signup_cl(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        telephone = request.POST['telephone']
        company = request.POST['company']
        position = request.POST['position']

        new_client = Client(email=email, password=password, name=name, telephone=telephone, company=company,
                            position=position)
        new_client.save()
        return render(request, 'task/success.html')
    return render(request, 'task/signup_cl.html')


def signup_mn(request):
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        telephone = request.POST['telephone']
        company = request.POST['company']

        new_manufacturer = Manufacturer(email=email, password=password, name=name, telephone=telephone, company=company)
        new_manufacturer.save()
        return render(request, 'task/success.html')
    return render(request, 'task/signup_mn.html')


def success(request):
    return render(request, 'task/success.html')







