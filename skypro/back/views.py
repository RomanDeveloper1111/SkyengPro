from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from back.models import UserFile
from back.forms import FileForm


class ListFileView(ListView):
    model = UserFile
    template_name = 'back/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['userfiles'] = UserFile.objects.filter(author=self.request.user.pk)
        return context


class CreateFileView(CreateView):
    template_name = 'back/create.html'
    model = UserFile
    form_class = FileForm
    success_url = reverse_lazy('list_files')

    def form_valid(self, form):
        form.instance.author = 1
        form.save()
        return super().form_valid(form)

