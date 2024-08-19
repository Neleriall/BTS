from app.models import Contact


def get_info(request):
    contact = Contact.objects.first()  
    return {'contact': contact}