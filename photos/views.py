from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .forms import PhotoForm


def detail(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    context = dict()
    context['photo'] = photo

    return render(request, 'photos/detail.html', context)


def create(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)

    if request.method == 'GET':
        form = PhotoForm()
    elif request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect('photos:detail', pk=photo.pk)
    context = {
        'photo_form': form
    }
    return render(request, 'photos/edit.html', context)


def index(request):
    photos = Photo.objects.all().order_by('-pk')
    context = dict()
    context['photos'] = photos

    return render(request, 'photos/list.html', context)


def delete(request):
    if request.method=='POST':
        photo_id =request.POST['pk']
        try:
            photo=Photo.objects.get(pk=photo_id, user=request.user)

        except:
            return redirect('photos:detail', pk=photo_id)
        photo.delete()
    return redirect('photos:list')

