from django.shortcuts import render, redirect
from .models import Links
from django.views.generic.list import ListView
from django.contrib import messages
from .forms import LinkForm


class LinksView(ListView):
    model = Links
    template_name = 'links/links_transform.html'
    context_object_name = 'Links'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(LinksView, self).get_context_data(**kwargs)
        newLink = Links.objects.values().order_by('-id')[:2]
        ctx['newLink'] = newLink
        ctx['form'] =LinkForm()
        return ctx

    def post(self, request, *args, **kwargs):
        post = request.POST.copy()
        post['user'] = request.user
        request.POST = post
        form = LinkForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Ссылка создана')
            form.save()
        else:
            messages.error(request, 'Введите другое значение для короткой ссылки')


        return redirect('links')



