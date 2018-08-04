from django.forms import ModelForm
from ..models import Estado

class EstadoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        # Adiciona uma class CSS aos campos do formulário.
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


    class Meta:
        model = Estado
        fields = '__all__'