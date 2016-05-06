from django.shortcuts import render


def login(request):

    title = "Home"
    context = {
        "title": title,

    }
    return render(request, "login.html", context)