from django.shortcuts import render
from .models import Budget, Item


def home(request):
    context = {
        'Item': Item.objects.all(),
        'Budget': Budget.objects.all()
    }
    return render(request, 'expenses/home.html', context)
