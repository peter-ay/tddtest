from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item


# Create your views here.
def home_page(request):
    # return HttpResponse('<html><title>To-Do lists</title></html>')
    # return render(request,'home.html')
    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()
    # return render(request, 'home.html', {
    # 'new_item_text': request.POST.get('item_text', ''),
    # })
    # if request.method == 'POST':
    #     new_item_text = request.POST['item_text']  #➊
    #     Item.objects.create(text=new_item_text)  #➋
    # else:
    #     new_item_text = ''  #➌
    # return render(
    #     request,
    #     'home.html',{
    #         'new_item_text': new_item_text,  #➍
    #     })
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    return render(request, 'home.html')
