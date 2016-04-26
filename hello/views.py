from django.shortcuts import render




def home(request):

    title = "Hi world"
    context = {
        "title": title,

    }
    return render(request, "home.html", context)