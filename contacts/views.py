from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView, DeleteView
from django.views.generic.base import TemplateView

from contacts.forms import ContactCardForm
from contacts.models import Contact


def index(request):
    return render(request, "index.html")


class ContactsListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    context_object_name = "contacts"
    template_name = "contacts/contact_list.html"
    paginate_by = 5

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)


class ContactDetailsView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = "contacts/contact_details.html"
    context_object_name = "details"

    def get_context_data(self, **kwargs):
        contact = get_object_or_404(Contact, pk=kwargs['pk'], user=self.request.user)
        context = {"contact": contact}
        return context


class ContactCreateView(LoginRequiredMixin, CreateView):
    form_class = ContactCardForm
    success_url = reverse_lazy('contacts')
    template_name = 'contacts/contact_edit.html'

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user
        return initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        messages.success(self.request, 'Created')
        return redirect(self.get_success_url())


class ContactEditView(LoginRequiredMixin, FormView):
    login_url = reverse_lazy('login')
    template_name = "contacts/contact_edit.html"
    form_class = ContactCardForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        pk = self.kwargs.get('pk', None)
        kwargs['instance'] = get_object_or_404(Contact, pk=pk, user=self.request.user)
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        messages.success(self.request, 'Updated')
        return HttpResponseRedirect(reverse_lazy('details', kwargs={'pk': self.object.pk}))


class ContactDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Contact
    success_url = reverse_lazy('contacts')
    template_name_suffix = "_delete"

    def get_object(self, queryset=None):
        obj = super().get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(request, "Deleted")
        return response
