from django.shortcuts import render, get_object_or_404
from .models import Story

# Create your views here.
def story(request):
    story = Story.objects.order_by('date')
    return render(request, 'story/story.html', {'story': story})


def detail(request, story_id):
    story = get_object_or_404(Story, pk=story_id)
    return render(request, 'story/detail.html', {'story': story})
