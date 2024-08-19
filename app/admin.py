from django.contrib import admin
from app.forms import ContactForm

from app.models import About, Contact, Form, Parcel, ParcelInfo, Slider, Why 

admin.site.register(ParcelInfo)
admin.site.register(Parcel)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Form)
admin.site.register(Slider)
admin.site.register(Why)


