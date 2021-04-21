from django.shortcuts import render,redirect
from .models import Category, Kind, MensCostume, MensBlouse
from .forms import FormMessage


# Create your views here.
def main_page_view(request):

    categories = Category.objects.filter(is_visible=True).order_by('category_order')
    for item in categories:
        kinds = Kind.objects.filter(category=item.pk).filter(is_visible=True).order_by('kind_order')
        item.kinds=kinds

    promo = Kind.objects.filter(category__title='Акция')


    return render(request, 'index.html',context={
        'categories': categories,
        'promo': promo,
    })



# для перехода в категорию Женщины

def product_woman_view(request):
    man = Kind.objects.filter(category__title='Женщины')
    return render(request, 'productsman.html', context={'man': man })


# для перехода в категорию Мужчины

def product_man_view(request):
    man = Kind.objects.filter(category__title='Мужчины')
    return render(request, 'productsman.html', context={'man': man})


# для перехода в категорию Спорт

def product_sport_view(request):
    man = Kind.objects.filter(category__title='Спорт')
    return render(request, 'productsman.html', context={'man': man})

# для перехода в  продуктам разновидности

def product_detail_view(request, pk):
    kind = MensCostume.objects.filter(category=pk)
    return render(request, 'product_detail_view.html', context={
        'kind': kind
    })


# для перехода в разновидность продукции

def categoryt_detail_view(request, pk):
    man = Kind.objects.filter(category=pk)
    return render(request, 'productsman.html', context={
        'man': man
    })


# для перехода в  продукту
def kind_detail_view(request,pk):
    man =MensCostume.objects.get(pk=pk)
    return render(request,'kind_detail_view.html', context={'man': man})



def contact_page_view(request):
    if request.method=='POST':

        form = FormMessage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form =FormMessage()
    return render (request, 'contact.html', context={
        'form': form
    })