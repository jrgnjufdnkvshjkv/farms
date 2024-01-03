from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import About, Team, Blog, Newsletter, Features
from .forms import NewsletterForm
from django.views.generic import UpdateView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
class AboutUpdateView(UpdateView):
    model = About
    fields = ('name', 'bio', 'img')
    template_name = 'aboutEdit.html'

class AboutDeleteView(DeleteView):
    model = About
    template_name = 'AboutDelete.html'
    success_url = reverse_lazy('index')

class AboutCreateView(CreateView):
    model = About
    template_name = 'aboutCreate.html'
    fields = ('name', 'bio', 'img')

def index(request):
    about = About.objects.all()
    team = Team.objects.all()
    blog = Blog.objects.all()
    features = Features.objects.all()
    letter = NewsletterForm(request.POST or None)
    if request.method == "POST" and letter.is_valid():
        letter.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!!!<h2>")
    context = {
        "about": about,
        "team": team,
        "blog": blog,
        "features": features,
        "newsletter": newsletter,
        "letter": letter,
    }
    return render(request, "index.html", context=context)

def about(request):
    about = About.objects.all()
    context = {
        "about": about
    }
    return render(request, "about.html", context=context)

def blog(request):
    letter = NewsletterForm(request.POST or None)
    if request.method == "POST" and letter.is_valid():
        letter.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!!!<h2>")
    context = {
        "form": letter
    }
    return render(request, "blog.html", context=context)

def contact(request):
    return render(request, "contact.html", context={})

def detail(request):
    return render(request, "detial.html", context={})

def feature(request):
     features = Features.objects.all()
     context = {
         "features": features
     }
     return render(request, "feature.html", context=context)

def product(request):
    return render(request, "product.html", context={})

def service(request):
    return render(request, "service.html", context={})

def team(request):
    team = Team.objects.all()
    context = {
        "team": team
    }
    return render(request, "team.html", context=context)

def testimonial(request):
    return render(request, "testimonial.html", context={})


def aboutDetailView(request, about):
    about = get_object_or_404(About, slug=about)
    context = {
        'about': about
    }
    return render(request, "aboutDetailView.html", context=context)

def blogDetailView(request):
    return render(request, "blogDetailView.html", context={})

def teamDetailView(request):
    return render(request, "teamDetailView.html", context={})

def featuresDetailView(request):
    return render(request, "featuresDetailView.html", context={})

def newsletter(request):
    letter = NewsletterForm(request.POST or None)
    if request.method == "POST" and letter.is_valid():
        letter.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!!!<h2>")
    context = {
        "letter": letter
    }
    return render(request, "base.html", context=context)
