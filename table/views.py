from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from table.forms import ItemForm
from table.models import Item
from table.filters import ItemFilter


def index(request):
    items = Item.objects.all()
    filter = ItemFilter(request.GET, queryset=items)
    items = filter.qs
    paginator = Paginator(items, 1)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        items = paginator.page(paginator.num_pages)

    return render(request, 'index.html',
           {'items': items,
            'page': page,
            'filter': filter})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'form is incorrect'

    form = ItemForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'create.html', context)
