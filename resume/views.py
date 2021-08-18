from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.

def resume(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Resume Contact"
            body = {
			'full_name' : form.cleaned_data['full_name'],
            'email'     : form.cleaned_data['email'],
			'message'   : form.cleaned_data['message'], 
			}
            message = "\n\n".join(body.values())

            try:
                send_mail(subject, message, 'iamkomolafe.o.s@gmail.com', ['iamkomolafe.o.s@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("home")
        context['form'] = form
      
    form = ContactForm()

    context['form'] = form

    return render(request, 'home.html', context)