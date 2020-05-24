from django.shortcuts import render, redirect

def vw_index(request):
    if request.method == 'POST':
        return redirect('accounts/login', request.path)

    return render( request, "index/index.html" )