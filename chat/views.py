# chat/views.py
from django.shortcuts import render

def test_view(request):
    return render(request, 'chat/test.html')