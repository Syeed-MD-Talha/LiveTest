from django.shortcuts import render,redirect
from .models import contact_model
from .forms import ContactForm
from django.shortcuts import get_object_or_404

# Create your views here.
def homepage(request):
    contact=contact_model.objects.all()
    return render(request, 'pages/home.html', {'contacts': contact})
    

def detail_page(request, id):
    contact = get_object_or_404(contact_model, id=id)
    return render(request, 'pages/detail.html', {'contact': contact})


def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ContactForm()
    return render(request, 'pages/create.html', {'form': form})


def edit_delete(request):
    contact=contact_model.objects.all()
    return render(request, 'pages/edit_delete.html', {'contacts': contact})


def edit_contact(request, id):
    contact = get_object_or_404(contact_model, id=id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'pages/edit.html', {'form': form})

def delete_contact(request,id):
    contact = get_object_or_404(contact_model, id=id)
    contact.delete()
    return redirect('edit_delete')

def search_contact(request):
    first_name = request.GET.get('first_name', '')
    email = request.GET.get('email', '')

    # Check if either first_name or email is provided
    contacts = contact_model.objects.all()
    
    if first_name:
        contacts = contacts.filter(first_name__icontains=first_name)
    if email:
        contacts = contacts.filter(email__icontains=email)

    return render(request, 'pages/edit_delete.html', {'contacts': contacts})
