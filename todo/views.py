from datetime import datetime

from django.contrib import messages
from django.http import QueryDict
from django.http.response import JsonResponse
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.views import View
from django.views.decorators.http import require_http_methods

from .models import Task, Label


def index(request):
    return redirect(reverse('tasks'))


class TaskView(View):
    def get(self, request):
        query = Task.objects.order_by('due_at', 'pk')
        is_done = request.GET.get('is_done')
        if is_done == 'yes':
            query = query.filter(is_done=True)
        elif is_done == 'no':
            pass
        else:
            query = query.filter(is_done=False)
        return render(request, 'index.html', {'tasks': query.all(), 'is_done': is_done})

    def post(self, request):
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
            messages.add_message(request, messages.SUCCESS, 'Task created')
        else:
            messages.add_message(request, messages.ERROR, 'Title is missing')
        return redirect(reverse('index'))

    def patch(self, request, pk):
        data = {}
        request_data = QueryDict(request.body)
        if 'is_done' in request_data:
            data['is_done'] = True if request_data['is_done'] == 'true' else False
        if 'due_at' in request_data:
            data['due_at'] = request_data['due_at']
        Task.objects.filter(pk=pk).update(**data)
        return JsonResponse({})

    def delete(self, request, pk):
        Task.objects.filter(pk=pk).delete()
        return JsonResponse({})


@require_http_methods(["POST"])
def task_labels(request, pk):
    task = get_object_or_404(Task, pk=pk)
    data = QueryDict(request.body)
    task.labels.clear()
    for label in data.get('labels', '').split(','):
        obj, _ = Label.objects.get_or_create(name=label)
        task.labels.add(obj)
    task.save()
    return JsonResponse({})
