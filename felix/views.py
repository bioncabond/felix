from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Felix


class FelixListView(ListView):
    template_name = "felixtemps/felix-list.html"
    model = Felix


class FelixDetailView(DetailView):
    template_name = "felixtemps/felix-detail.html"
    model = Felix


class FelixCreateView(CreateView):
    template_name = "felixtemps/felix-create.html"
    model = Felix
    fields = ['name', 'description', 'purchaser']


class FelixUpdateView(UpdateView):
    template_name = "felixtemps/felix-update.html"
    model = Felix
    fields = ['name', 'description', 'purchaser']


class FelixDeleteView(DeleteView):
    template_name = "felixtemps/felix-delete.html"
    model = Felix
    success_url = reverse_lazy("felix_list")