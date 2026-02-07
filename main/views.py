from django.shortcuts import render
from resources.models import Resource
from django.db.models import Q  # for complex queries

def home(request):
    query = request.GET.get('q')  # get the search query
    if query:
        resources = Resource.objects.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query) | 
            Q(uploaded_by__username__icontains=query)
        ).order_by('-id')
    else:
        resources = Resource.objects.all().order_by('-id')

    # Check if AJAX request
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'main/resource_feed.html', {'resources': resources})

    # Normal page load
    return render(request, 'main/index.html', {'resources': resources, 'query': query})
