from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
#import our model
from .models import Keyboard

def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def about(request):
    return render(request, 'about.html')

# Add new view
def keyboards_index(request):
    # retrieving all the cats from the db
    keyboards = Keyboard.objects.all()
    return render(request, 'keyboards/index.html', { 'keyboards': keyboards }) #'cats' is the name being called in the HTML, cats is what we are calling above

def keyboards_detail(request, keyboard_id):
    # find a cat by its id, cat_id is from the urls.py file for the cats_detail route
  keyboard = Keyboard.objects.get(id=keyboard_id)
  return render(request, 'keyboards/detail.html', { 'keyboard': keyboard })