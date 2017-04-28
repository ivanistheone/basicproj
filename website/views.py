from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

from .models import Restaurant




def index(request):
    # print(request.__dict__['META'])
    all_restaurants = Restaurant.objects.all()

    template = loader.get_template('website/index.html')
    context = { 'key': 'value', 
                'restaurants': all_restaurants}
    html_str = template.render(context, request)
    return HttpResponse(html_str)