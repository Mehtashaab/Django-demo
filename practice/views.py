from django.http import response
from django.shortcuts import render

def home(request):

    data = [
        {'name':'Abhishek','lastname':'Mehta','age':'24'},
        {'name':'Arman','lastname':'Sharma','age':'25'},
        {'name':'Aman','lastname':'Katoch','age':'26'},
        {'name':'Akhil','lastname':'Rana','age':'22'}
    ]
    return render(request, 'index.html',context={'data':data})