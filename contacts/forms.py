from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):

    class Meta:

        model = Contact
        exclude = ('creation_date',)
        labels = {
            'name': 'Nombre',
            'last_name': 'Apellido',
            'mobile': 'Móvil', 
            'phone': 'Teléfono',
            'email': 'Email',
            'company': 'Compañía',
            'notes': 'Notas',
        }