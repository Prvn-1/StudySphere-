from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ResourceForm
from .forms import  RatingForm
from .models import Resource
from .models import Rating
from django.contrib.admin.views.decorators import staff_member_required
from django.http import FileResponse, Http404
import os

@login_required
def upload_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.uploaded_by = request.user
            resource.save()
            messages.success(request, 'Resource uploaded successfully and pending approval!')
            return redirect('resource_list')
    else:
        form = ResourceForm()
    return render(request, 'resources/upload_resource.html', {'form': form})

@login_required
def resource_list(request):
    resources = Resource.objects.filter(status='approved').order_by('-uploaded_at')
    return render(request, 'resources/resource_list.html', {'resources': resources})


@staff_member_required
def manage_resources(request):
    pending_resources = Resource.objects.filter(status='pending')
    return render(request, 'resources/manage_resources.html', {'resources': pending_resources})


@staff_member_required
def approve_resource(request, resource_id):
    resource = Resource.objects.get(id=resource_id)
    resource.status = 'approved'
    resource.save()
    messages.success(request, f"{resource.title} has been approved!")
    return redirect('manage_resources')


@staff_member_required
def reject_resource(request, resource_id):
    resource = Resource.objects.get(id=resource_id)
    resource.status = 'rejected'
    resource.save()
    messages.error(request, f"{resource.title} has been rejected!")
    return redirect('manage_resources')

@login_required
def download_resource(request, pk):
    try:
        resource = Resource.objects.get(pk=pk, status='approved')
        resource.download_count += 1
        resource.save()
        file_path = resource.file.path
        return FileResponse(open(file_path, 'rb'), as_attachment=True)
    except (Resource.DoesNotExist, FileNotFoundError):
        raise Http404("File not found")

@login_required
def rate_resource(request, pk):
    resource = Resource.objects.get(pk=pk)
    existing_rating = Rating.objects.filter(resource=resource, user=request.user).first()

    if request.method == 'POST':
        form = RatingForm(request.POST, instance=existing_rating)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.resource = resource
            rating.user = request.user
            rating.save()
            messages.success(request, '⭐ Your rating has been submitted!')
            return redirect('resource_detail', pk=pk)
    else:
        form = RatingForm(instance=existing_rating)

    return render(request, 'resources/rate_resource.html', {'form': form, 'resource': resource})

def resource_detail(request, pk):
    resource = Resource.objects.get(pk=pk)
    ratings = resource.ratings.all()
    avg = resource.average_rating()
    return render(request, 'resources/resource_detail.html', {'resource': resource, 'ratings': ratings, 'avg': avg})

@login_required
def resource_edit(request, pk):
    resource = get_object_or_404(Resource, pk=pk, uploaded_by=request.user)
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES, instance=resource)
        if form.is_valid():
            form.save()
            messages.success(request, "Resource updated.")
            return redirect('profile')
    else:
        form = ResourceForm(instance=resource)
    return render(request, 'resources/resource_edit.html', {'form': form, 'resource': resource})

@login_required
def resource_delete(request, pk):
    resource = get_object_or_404(Resource, pk=pk, uploaded_by=request.user)
    if request.method == 'POST':
        resource.delete()
        messages.success(request, "Resource deleted.")
        return redirect('profile')
    return render(request, 'resources/resource_delete_confirm.html', {'resource': resource})