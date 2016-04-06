from django.http import HttpResponse
from django.shortcuts import redirect, render

from lists.models import Item


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

    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()

    return render(request, 'home.html', {'items':items,})
