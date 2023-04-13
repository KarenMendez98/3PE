from django import forms

class PasajeroForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=50)
    destino=forms.CharField(max_length=50)


class PaqueteForm(forms.Form):
    lugar= forms.CharField(max_length=50)
    cant_pasajeros= forms.CharField(max_length=50)
    cant_dias= forms.CharField()


class VisitaGForm(forms.Form):
    tipo= forms.CharField(max_length=50)
    ciudad= forms.CharField(max_length=50)   