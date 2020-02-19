from django.shortcuts import render
from core_part.forms import UploadFileForm

from core_part import booksParsing as bp


# Create your views here.


def upload_excel_file(req):
    context = {}
    if req.method == 'POST':
        form = UploadFileForm(req.POST, files=req.FILES)
        context.update({'form': form})
        if form.is_valid():
            file = req.FILES['file']
            errors = bp.parse_excel_file(file)
            if errors != None:
                context.update({'parseErrors': errors})
        return render(req, 'mainPage.html', context)

    else:
        form = UploadFileForm()
        return render(req, 'mainPage.html', context)


