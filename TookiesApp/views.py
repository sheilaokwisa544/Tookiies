from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def contact(request):
    return render(request, 'contact.html')
def order(request):
    return render(request, 'order.html')
def payment(request):
    return render(request, 'payment.html')