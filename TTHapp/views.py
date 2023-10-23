from django.shortcuts import render
from .forms import EditorForm
from .models import Editor

def home(request):
    form = EditorForm()
    return render(request, 'home.html', {'form': form})
