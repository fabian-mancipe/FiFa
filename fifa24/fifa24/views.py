from django.http import render


def index(request): 
    return render(request, 'index.html',{
            #context
    })

def login(request): 
    return render(request, 'login.html',{
            #context
    })

def logout(request): 
    return render(request, 'logout.html',{
            #context
    })

def rusuario(request): 
    return render(request, 'rusuario.html',{
            #context
    })