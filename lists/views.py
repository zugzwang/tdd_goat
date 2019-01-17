from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.

def home_page(request):
    return render(request, 'home.html')

def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/only_one/')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
