from django.shortcuts import render
from .forms import CommentForm
from .models import UserComments
from django.http import JsonResponse

def form_view(request):
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data      # function that helps with data normalization
            uc = UserComments(
                first_name = cd['first_name'],
                last_name = cd['last_name'],
                comment = cd['comment'],
            )
            uc.save()
            return JsonResponse({
                'message': 'success'
            })

    return render(request, 'blog.html', {'form': form})