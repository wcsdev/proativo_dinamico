from django.shortcuts import render,redirect

# Create your views here.

def index_doc(request):
    return redirect('/api/docs')