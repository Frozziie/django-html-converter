from django.shortcuts import render
from .models import Editor
from .form import FormEditor

def index(request):
    form = FormEditor()
    return render(request, 'converter/index.html', {'form': form})
