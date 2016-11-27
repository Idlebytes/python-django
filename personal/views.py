from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("<h2>personal site</h2>")
    return render(request, 'personal/home.html') 

def contact(request):
    return render(request, 'personal/contact.html', {'content' : ['For any queries, please contact me at ', 'hostmaster@django.com']})