from celery import current_app
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from core_part.forms import UploadFileForm

from core_part import booksParsing as bp
from .tasks import parse_excel_file

# Create your views here.

def MainPage(req):
    session_id = req.session['user_id']
    #user = User.objects.get(id=session_id)
    #student = Student.objects.get(userPerson=user)
    return render(req, 'mainPage.html')

def uploading_excel_view(req):
    context = {}
    if req.method == 'POST':
        form = UploadFileForm(req.POST, files=req.FILES)
        context.update({'form': form})
        if form.is_valid():
            file = req.FILES['file']
            errors = bp.parse_excel_file(file)
            if errors != None:
                context.update({'parseErrors': errors})
        return render(req, 'load_excel.html', context)

    else:
        form = UploadFileForm()
        return render(req, 'load_excel.html', {'form': form})


class TaskView(View):
    def get(self, request, task_id):
        task = current_app.AsyncResult(task_id)
        response_data = {'task_status': task.status, 'task_id': task.id}
        if task.status == 'SUCCESS':
            response_data['results'] = task.get()
        return JsonResponse(response_data)
