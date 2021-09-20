from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

import datetime

from .models import Idea, Comment

def index(request):
    latest_ideas_list = Idea.objects.order_by('-votes')[:10]
    context = {'latest_ideas_list': latest_ideas_list}
    return render(request, 'polls/index.html', context)


def detail(request, post_id):
    idea = get_object_or_404(Idea, pk=post_id)
    return render(request, 'polls/detail.html', {'idea': idea})


def results(request, post_id):
    idea = get_object_or_404(Idea, pk=post_id)
    return render(request, 'polls/results.html', {'idea': idea})


def vote(request, post_id):
    idea = get_object_or_404(Idea, pk=post_id)
    idea.votes += 1
    idea.save()
    return HttpResponseRedirect(reverse('polls:results', args=(idea.id, )))


def add_idea(request):
    return render(request, 'polls/add_idea.html')


def writing_idea(request):
    idea = Idea(
        post_title=request.POST['post_title'],
        post_text=request.POST['post_text'],
        author = request.POST['user_name'],
        pub_date=datetime.datetime.now()
    )
    idea.save()
    return HttpResponseRedirect(reverse('polls:index'))


def comment(request, post_id):
    comment = Comment(
        post_id=post_id,
        user_name=request.POST['user_name'],
        comment_text=request.POST['comment_text'],
    )
    comment.save()
    return HttpResponseRedirect(reverse('polls:detail', args=(comment.post_id, )))
