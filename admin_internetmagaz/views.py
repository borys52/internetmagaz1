from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DeleteView, UpdateView, CreateView
from django.shortcuts import render,redirect
from main_internetmagaz.forms import Message
from main_internetmagaz.models import Category
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .forms import CategoryForm
from django.contrib import messages
# Create your views here.


def list_of_messages(request):
    messages = Message.objects.filter(is_processed=False).order_by('pub_date')
    paginator = Paginator(messages,2)
    page = request.GET.get('page')
    messages = paginator.get_page(page)
    return render(request, 'messages.html', context={'messages': messages})

def update_message(request, pk):
    Message.objects.filter(pk=pk).update(is_processed=True)
    return redirect('/admin-panel/messages/')

def updated_messages(request):
    messages= Message.objects.filter(is_processed=True)
    return render(request, 'updated_messages.html', context={'messages': messages})

def cancel_update_message(request,pk):
    Message.objects.filter(pk=pk).update(is_processed=False)
    return redirect('list_of_messages')

def list_of_categories(request):
    items = Category.objects.all().order_by('category_order')
    return render(request, 'categories.html', context={'items': items})


class CategoryAddView(SuccessMessageMixin, CreateView):
    #login_url = reverse_lazy('login')
    #group_required = ["manager", 'admin']
    model = Category
    form_class = CategoryForm
    template_name = 'category_add.html'
    success_url = reverse_lazy('list_of_categories')
    success_message = 'Категория успешно создана!'

class CategoryDeleteView(DeleteView):
    #login_url = reverse_lazy('login')
    #group_required = ["manager", 'admin']
    model = Category
    success_url = reverse_lazy('list_of_categories')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Категория успешно удалена!')
        return self.post(request, *args, **kwargs)

class CategoryUpdateView(SuccessMessageMixin, UpdateView):
    #login_url = reverse_lazy('login')
    #group_required = ['manager', 'admin']
    model = Category
    form_class = CategoryForm
    template_name = 'category_update.html'
    success_url = reverse_lazy('list_of_categories')
    success_message = 'Категория успешно изменена!'