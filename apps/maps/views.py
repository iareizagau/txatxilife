from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy, reverse

from .models import InterestPoint, CamperNightPoint
from .models import ImageInterestPoint, ImageCamperNightPoint


class InterestPointTemplateView(TemplateView):
    template_name = 'maps/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['interestPoints'] = InterestPoint.objects.all()
        context['interestPointsImages'] = ImageInterestPoint.objects.all()

        context['CamperNightPoints'] = CamperNightPoint.objects.all()
        context['CamperNightPointsImages'] = ImageCamperNightPoint.objects.all()
        return context


class CreateInterestPoint(CreateView):
    model = InterestPoint
    template_name = 'maps/CreateUpdateForm.html'
    success_url = reverse_lazy('maps:home')
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

        exclude_fields = ['category']
        for field_name, field in form.fields.items():
            if field_name not in exclude_fields:
                field.widget.attrs['class'] = 'form-control'
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Create Interest Point'
        return context


class UpdateInterestPoint(UpdateView):
    model = InterestPoint
    template_name = 'maps/CreateUpdateForm.html'
    success_url = reverse_lazy('maps:home')
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
        context['form_title'] = 'Update Interest Point'
        return context


class CreateCamperNightPoint(CreateView):
    model = CamperNightPoint
    template_name = 'maps/CreateUpdateForm.html'
    success_url = reverse_lazy('maps:home')
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

        exclude_fields = ['free', 'wc', 'drinking_water', 'tables',
                          'gray_sink', 'black_sink', 'electricity',
                          'wifi']
        for field_name, field in form.fields.items():
            if field_name not in exclude_fields:
                field.widget.attrs['class'] = 'form-control'
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Create Camper Night Point'
        return context


class UpdateCamperNightPoint(UpdateView):
    model = CamperNightPoint
    template_name = 'maps/CreateUpdateForm.html'
    success_url = reverse_lazy('maps:home')
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
        context['form_title'] = 'Update Camper Night Point'
        return context
