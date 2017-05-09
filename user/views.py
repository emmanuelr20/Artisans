from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from .forms import UserForm, UserAccountForm, LoginForm
from .models import UserAccount, Rating
from Artisans.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
DEFAULT_IMG = 'icon-user-default.png'
# Create your views here.
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'confirmation_message.txt')
def index_view(request):
    context = {
        'login_form': LoginForm(),
        'sign_up_form': UserForm(),
    }
    return render(request, 'base.html', context)

def register_view(request, slug = None):
    login_form = LoginForm()
    context = {'login_form': login_form }
    if slug: 
        context['link_slug'] = slug
    form = UserForm(request.POST or None)
    print(slug)
    if form.is_valid():
        form_data = form.save(commit = False)
        if User.objects.filter(email = form_data.email).exists():
            user = authenticate(username = form_data.email, password =form_data.password)
            if user:
                login(request, user)
                if slug:
                    return redirect(reverse('user:details', kwargs={ 'slug': slug }))
                return redirect(reverse('user:profile'))
            messages.info(request, 'Sorry this email has already being used')
            context['sign_up_form']: UserForm(data=form_data)
            return redirect(reverse('user:register'))
        else:
            new_user = User.objects.create(
                username = form_data.email,
                email = form_data.email,
                first_name = form_data.first_name,
                )
            new_user.set_password(form_data.password)
            new_user.save()
            new_useraccount = UserAccount.objects.create(user = new_user)
            new_useraccount.activation_code = get_random_string()
            new_useraccount.profile_picture = DEFAULT_IMG
            new_useraccount.slug = new_useraccount.create_slug()
            new_useraccount.tel = form_data.last_name
            new_useraccount.save()
            new_user_rating = Rating.objects.create(useraccount = new_useraccount)
            new_user_rating.save()
            link = r'http://127.0.0.1/user/activate/' + str(new_user.id) + '/' + new_user.useraccount.activation_code
            confirm_message = open(file_path)
            comfirm_message = confirm_message.read()
            comfirm_message = comfirm_message.replace('{{{}}}', link)
            send_mail('Artisans', comfirm_message, EMAIL_HOST_USER, [new_user.email, EMAIL_HOST_USER], True)
            login_new_user = authenticate(username = form_data.email, password = form_data.password)
            login(request, login_new_user)
            if slug:
                    return redirect(reverse('user:details', kwargs={ 'slug': slug }))
            return redirect(reverse('user:profile'))
    context['sign_up_form'] = form
    return render(request, 'base.html', context)

def login_view(request, slug=None):
    form = LoginForm(request.POST or None)
    context = { 'login_form': form, 'link_slug':slug }
    if form.is_valid():
        username = form.cleaned_data.get('email')
        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Email has not been registered!')
            return render(request, 'user/login.html', context)
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            if slug:
                    return redirect(reverse('user:details', kwargs={ 'slug': slug }))
            return redirect(reverse('user:profile'))
        else:
            messages.warning(request, 'User email or password is incorrect!')
            return render(request, 'user/login.html', context)
    return render(request, 'base.html', context)

def home_view(request):
    context= {}
    return render(request, 'user/home.html', context)

def logout_view(request):
    logout(request)
    return redirect(reverse('index'))

def profile_view(request):
    if request.user.is_authenticated():
        return render(request, 'user/profile.html')
    else: 
        return redirect(reverse('index'))

def details_view(request, slug):
    if request.user.is_authenticated():
        if UserAccount.objects.filter(slug = slug).exists():
            user_account = UserAccount.objects.filter(slug = slug)[0]
            user_profile = user_account.user
            context = {
                'user_profile': user_profile,
            }
        else:
            return HttpResponse('artisan does not exists')
    else:
        return redirect(reverse('user:register_branch', kwargs={ 'slug': slug }))
    return render(request, 'user/profile.html', context)

def artisans_view(request, query_type=None):
    if query_type == None or query_type.lower() == 'all':
        artisans_list = UserAccount.objects.filter(acc_type = 'artisan').order_by('rating__overall_rating')
    else:
        artisans_list = UserAccount.objects.filter(occupation = query_type).order_by('rating__overall_rating')
    paginator = Paginator(artisans_list, 4)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        artisans = paginator.page(page)
    except PageNotAnInteger:
        artisans = paginator.page(1)
    except EmptyPage:
        artisans = paginator.page(paginator.num_pages)
    context = {'artisans' : artisans, 'page_request_var': page_request_var, 'sign_up_form' : UserForm() , 'login_form': LoginForm()}
    return render(request, 'user/artisans.html', context)
