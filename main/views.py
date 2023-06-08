from django.shortcuts import render


def about(request):
    return render(request, 'about.html', {})


def contacts(request):
    return render(request, 'contacts.html', {})


def hobbies(request):
    return render(request, 'hobbies.html', {})
