from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from django.contrib import messages


# Create your views here.
def index(request, letter = None):
    if letter != None:
        contacts = Contact.objects.filter(name__istartswith=letter)
    else:
        contacts = Contact.objects.filter(name__icontains=request.GET.get('search', ''))
    context = {
        'contacts': contacts,
    }
    return render(request, 'contacts/index.html', context)


def detail(request, id):
    contact = Contact.objects.get(id=id)
    context = {
        'contact': contact
    }
    return render(request, 'contacts/detail.html', context)


def create(request):
    if request.method == 'GET':
        form = ContactForm()
        context = {
            'form': form,
        }
        return render(request, 'contacts/create.html', context)
    if request.method == 'POST':
        validation_form = ContactForm(request.POST)
        if validation_form.is_valid():
            validation_form.save()
        messages.success(request, 'Contacto creado')
        return redirect('contacts')


def edit(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == 'GET':
        form = ContactForm(instance=contact)
        context = {
            'form': form,
            'id': id,
        }
        return render(request, 'contacts/edit.html', context)
    if request.method == 'POST':
        edited_form = ContactForm(request.POST, instance=contact)
        if edited_form.is_valid():
            edited_form.save()
        context = {
            'form': edited_form,
            'id': id,
        }
        messages.success(request, 'Contacto editado')
        return render(request, 'contacts/edit.html', context)


def delete(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    messages.success(request, 'Contacto eliminado')
    return redirect('contacts')