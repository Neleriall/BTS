from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login as login_view, authenticate, logout 
from app.forms import ContactForm, LogisticForm, ProfileForm
from app.models import About, Contact, Parcel, ParcelInfo, Slider, Why
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    services = ParcelInfo.objects.all()
    images = Slider.objects.all()
    why = Why.objects.all()
    return render(request, 'home.html', {"services": services, "images": images, "why": why})

def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password == confirm_password:
            try:
                if User.objects.filter(username=username).exists():
                    return render(request, "register.html", {"created": False, "error": "Имя пользователя уже существует"})
                if User.objects.filter(email=email).exists():
                    return render(request, "register.html", {"created": False, "error": "Email уже существует"})

                user = User.objects.create(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=make_password(password),
                )

                login(request)
                return redirect("app:home")
            except Exception as e:
                return render(request, "register.html", {"created": False, "error": str(e)})

        return render(request, "register.html", {"created": False, "error": "Пароли не совпадают"})
    
    return render(request, "register.html", {"created": True})


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            return redirect("app:login")

        user = get_object_or_404(User, username=username)
        cheked = user.check_password(raw_password=password)

        if not cheked:
            return redirect("app:login")

        user = authenticate(request, username=username, password=password)

        login_view(request, user)

        return redirect("app:home")

    return render(request, "login.html")


def signout(request):
    logout(request)
    return redirect("app:register")


def profile(request, username):
    user = get_object_or_404(User, username=username)
    
    if request.user == user:
        requests = Parcel.objects.filter(user=request.user)
    else:
        requests = Parcel.objects.none()  
    
    return render(request, 'profile.html', {"user": user, "requests": requests})

def profileform(request):
    initial_data = {}
    if request.user.is_authenticated:
        initial_data['sender_name'] = request.user.username

    if request.method == 'POST':
        form = ProfileForm(request.POST, initial=initial_data)
        if form.is_valid():
            data_form = form.save(commit=False)
            data_form.user = request.user
            data_form.save()
            return redirect('app:profile', username=request.user.username)
    else:
        form = ProfileForm(initial=initial_data)
    return render(request, 'profileform.html', {'form': form})


def serviceDetail(request, id):
    service = get_object_or_404(ParcelInfo, id=id)
    services = ParcelInfo.objects.all()

    if request.method == "POST":
        form = LogisticForm(request.POST)
        if form.is_valid():
            data_form = form.save(commit=False)
            data_form.user = request.user
            form.save()
            return redirect('app:serviceDetail', id=id)
    else:
        form = LogisticForm()

    return render(request, "serviceDetail.html", {"service": service, "services": services, "form": form})


def about(request):
    about = About.objects.get(id=1) 
    return render(request, 'about.html', {"about": about})


def services(request):
    services = ParcelInfo.objects.all()
    return render(request, 'services.html', {"services": services})


def contact(request):
    contact = Contact.objects.get(id=1)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {"contact": contact, "form": form})


def applicationDetail(request, id):
    application = get_object_or_404(Parcel, id=id)

    return render(request, 'applicationDetail.html', {'application': application})


def base_view(request):
    links = Contact.objects.get(id=1)

    return render(request, 'base.html', {'info': links})