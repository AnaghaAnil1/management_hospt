from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    input_type='date'

class Bookingform(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date': DateInput(),
        }

        labels = {
            'pa_name' : "Patient Name ",
            'pa_phone' : "Patient Phone ", 
            'pa_email' : "Patient Email ",
            'doc_name' : "Doctor Name ", 
            'booking_date' : "Booking Date ",
        }

