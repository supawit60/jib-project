from django.views import View
from django.http import HttpResponse
from django.shortcuts import render

from .models import Worker


# class base view
class WorkerListView(View):
    def get(self, request):
        workers = Worker.objects.all()
        print(workers)
        # html = ''
        # for worker in workers:
        #     html += f'<li>{worker.first_name}</li>'

        worker_list = []
        for worker in workers:
            worker_list.append(worker.first_name)

        return render(request, 'worker_list.html', {
            'workers': worker_list
        })
