from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy, reverse

from .models import InterestPoint, CamperNightPoint


# Create your views here.
class CreateInterestPoint(CreateView):
    model = InterestPoint
    template_name = 'maps/CreateUpdateForm.html'
    success_url = reverse_lazy('home:index')
    fields = '__all__'

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(**kwargs)
        initial['name'] = 'Enter name'
        return initial

    def get_form(self, *args, **kwargs):
        form = super().get_form(**kwargs)
        exclude_fields = ['created']
        for field_name in exclude_fields:
            form.fields.pop(field_name, None)

        for field_name, field in form.fields.items():
            field.widget.attrs['class'] = 'form-control'
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Create Community'
        return context


class UpdateInterestPoint(UpdateView):
    model = InterestPoint
    template_name = 'maps/CreateUpdateForm.html'
    success_url = reverse_lazy('home:index')
    fields = '__all__'

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(**kwargs)
        initial['name'] = 'Enter name'
        return initial

    def get_form(self, *args, **kwargs):
        form = super().get_form(**kwargs)
        exclude_fields = ['created']
        for field_name in exclude_fields:
            form.fields.pop(field_name, None)

        for field_name, field in form.fields.items():
            field.widget.attrs['class'] = 'form-control'
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Create Community'
        return context