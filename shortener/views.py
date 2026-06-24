from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import URL

@csrf_exempt
def home(request):
    short_url = None
    if request.method == 'POST':
        original = request.POST.get('original_url')
        url_obj  = URL.objects.create(original_url=original)
        short_url = request.build_absolute_uri(
            f'/{url_obj.short_code}/'
        )
    return render(request, 'shortener/home.html',
                  {'short_url': short_url})

def redirect_url(request, short_code):
    url_obj = get_object_or_404(URL, short_code=short_code)
    url_obj.click_count += 1
    url_obj.save()
    return redirect(url_obj.original_url)