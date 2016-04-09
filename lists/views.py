from django.http import HttpResponse
from django.shortcuts import redirect, render

from lists.models import Item, List


def home_page(request):
    # The code before redirect to home page
    #  if request.method == 'POST':
    #     new_item_text = request.POST['item_text']
    #     Item.objects.create(text=new_item_text)
    # else:
    #     new_item_text = ''
    #
    # return render(request, 'home.html',{
    #     'new_item_text': new_item_text,
    # })

    # The code with redirect

    # if request.method == 'POST':
    #     Item.objects.create(text=request.POST['item_text'])
    #     return redirect('/lists/the-only-list-in-the-world/')
    #
    # items = Item.objects.all()
    # return render(request, 'home.html')

    #code after new list views have taken over the redirect
    return render(request, 'home.html')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    return render(request, 'list.html', {'list':list_,})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))








