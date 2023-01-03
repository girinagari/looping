from django.shortcuts import render

# Create your views here.
def looping(request):
    d={'name':'Ashu','L':[11,22,33,44,55,66,77,88,99,110,121,132,143,154,165,176,187,]}
    return render(request,'looping.html',d)
