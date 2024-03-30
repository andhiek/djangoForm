from django.shortcuts import render

# Create your views here.
from .forms import ContactForm


def index(request):

    form_contact = ContactForm()

    context = {
        'page_title': 'Contact',
        'title': 'Contact',
        'subtitle': 'Form Contact',
        'heading': '',
        'contact_forms': form_contact

    }

    if request.method == "POST":
        context['nama_lengkap'] = request.POST['nama_lengkap']
        
    print(request.POST)


    return render(request, 'contact/index.html', context)
