from django.shortcuts import render

def vw_index(request): # primera vista
    return render( request, "index/index.html" )