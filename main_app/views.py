from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# Create your views here.
from django.http import HttpResponse
# import our model
from .models import Keyboard, Stablizer
from .forms import KeycapForm


class KeyboardCreate(CreateView):
    model = Keyboard
    fields = ['name', 'size', 'type', 'switches']  # referring the models field, so what fields do you
    # want to include on the form


class KeyboardUpdate(UpdateView):
    model = Keyboard
    # limit the renaming of the keyboard
    fields = ['size', 'type', 'switches']
    # redirect is happening by the get_absolute url defined


class KeyboardDelete(DeleteView):
    model = Keyboard
    success_url = '/keyboards/'

def add_stablizer(request, keyboard_id, stablizer_id):

  keyboard = Keyboard.objects.get(id=keyboard_id)
  keyboard.stablizers.add(stablizer_id)
  return redirect('detail', keyboard_id=keyboard_id)

def add_keycap(request, keyboard_id):

    # create a modelForm instance that process our request.POST data
    form = KeycapForm(request.POST)
    # validate the form
    if form.is_valid():  # <- the method comes from the FeedingForm class
        # don't save the form to the db, until we add the cat
        # to the feeding
        # pauses saving the form until later,
        new_keycap = form.save(commit=False)
        # but it creates the object we want to put in the database
        # assing the cat_id to the new_feeding (object we want to put in the db)
        # reference line 38-40 in models.py for why new_feeding.cat_id instead of new_feeding.cat
        new_keycap.keyboard_id = keyboard_id
        new_keycap.save()  # this puts the new_feeding into the feeding table

    # reference 'detail' name in the urls.py, cat_id is the <int:cat_id> in the path
    # don't forget to import redirect at the top
    return redirect('detail', keyboard_id=keyboard_id)


def home(request):
    return HttpResponse(request, 'home.html')


def about(request):
    return render(request, 'about.html')

# Add new view


def keyboards_index(request):
    # retrieving all the keyboards from the db
    keyboards = Keyboard.objects.all()
    # 'keyboards' is the name being called in the HTML, keyboards is what we are calling above
    return render(request, 'keyboards/index.html', {'keyboards': keyboards})


def keyboards_detail(request, keyboard_id):
    # find a keyboard by its id, keyboard_id is from the urls.py file for the keyboards_detail route
    keyboard = Keyboard.objects.get(id=keyboard_id)
    stablizers_keyboard_doesnt_have = Stablizer.objects.exclude(id__in = keyboard.stablizers.all().values_list('id'))
    keycap_form = KeycapForm()

    return render(request, 'keyboards/detail.html', {
        'keyboard': keyboard,
        'keycap_form': keycap_form,
        'stablizers': stablizers_keyboard_doesnt_have
    })

class StablizerList(ListView):
  model = Stablizer

class StablizerDetail(DetailView):
  model = Stablizer

class StablizerCreate(CreateView):
  model = Stablizer
  fields = '__all__'

class StablizerUpdate(UpdateView):
  model = Stablizer
  fields = ['name', 'color']

class StablizerDelete(DeleteView):
  model = Stablizer
  success_url = '/stablizers/'