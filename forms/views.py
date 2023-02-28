from django.shortcuts import render
from .models import *
from .forms import *
import json
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict


# Create your views here.

def forms(request):
    details = Details.objects.all()
    context = {'details': details}
    if request.method == 'POST':
        data = json.loads(request.body)
        form = DetailsForm(data)

        if form.is_valid():
            details_data, _ = Details.objects.get_or_create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email']
            )
            return JsonResponse(model_to_dict(details_data))
        return JsonResponse({'errors': form.errors})

    return render(request, 'forms.html', context)
