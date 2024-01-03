from django.urls import path
from .views import index, blog, contact, detail, feature, product, service, team, testimonial, about, AboutUpdateView, AboutDeleteView, AboutCreateView, blogDetailView, teamDetailView, featuresDetailView, aboutDetailView

urlpatterns = [
    path('index/', index, name='index'),
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),
    path('about/edit/slug/', AboutUpdateView.as_view(), name="aboutUpdate"),
    path('about/delete', AboutDeleteView.as_view(), name="aboutdelete"),
    path('about/create', AboutCreateView.as_view(), name="aboutcreate"),
    path('contact/', contact, name='contact'),
    path('detail/', detail, name='detail'),
    path('feature/', feature, name='feature'),
    path('product/', product, name='product'),
    path('service/', service, name='service'),
    path('blogDetailView/', blogDetailView, name='blogDetailView'),
    path('aboutDetailView/<slug:about>/', aboutDetailView, name='aboutDetailView'),
    path('featuresDetailView/', featuresDetailView, name='featuresDetailView'),
    path('teamDetailView/', teamDetailView, name='teamDetailView'),
    path('team/', team, name='team'),
    path('testimonial/', testimonial, name='testimonial'),
]
