from django.shortcuts import render

def landing_page_view(request):
    context = {}  # Add any context data you want to pass to the template
    return render(request, 'main.html', context)
