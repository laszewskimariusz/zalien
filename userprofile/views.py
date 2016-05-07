from django.shortcuts import render


def profile(request):
    title = "Home"
    context = {
        "title": title,

    }
    return render(request, "profile.html", context)


from django.shortcuts import render
