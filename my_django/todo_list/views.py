from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from .models import TodoTask
from .forms import TodoForm


def index(request):
    return render(
            request=request,
            template_name='index.html'
    )


def create_todo(request):
    context = {}

    if request.method == 'GET':
        form = TodoForm()
        context['form'] = form
        return render(
            request=request,
            template_name='create.html',
            context=context
        )
    # else POST method
    form = TodoForm(request.POST)
    if form.is_valid():
        title = form.data['title']
        finished = form.data.get('finished')
        create_date = form.data.get('create_data')

        context['title'] = title
        context['finished'] = finished

        todo_task = TodoTask.objects.create(
            title="title",
            owner='Denero',
        )

        return render(
            request,
            template_name='result_of_create.html',
            context=context
        )

    else:

        context['form'] = form
        return render(
            request=request,
            template_name='create.html',
            context=context
        )
