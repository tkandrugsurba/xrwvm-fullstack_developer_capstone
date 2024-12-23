# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView  # Added for serving React pages
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # Path for registration - updated to serve the React page
    path('register/', TemplateView.as_view(template_name="index.html"), name='register'),

    # Path for login - updated to serve the React page
    path('login/', TemplateView.as_view(template_name="index.html"), name='login'),

    # Path for dealer reviews view

    # Path for add a review view

    path('logout/', view=views.logout_request, name='logout'),
    path('get_cars/', view=views.get_cars, name='getcars'),  # Added the get_cars path
    path('get_dealers/', view=views.get_dealerships, name='get_dealers'),
    path('get_dealers/<str:state>/',
         view=views.get_dealerships, name='get_dealers_by_state'),
    path('dealer/<int:dealer_id>/',
         view=views.get_dealer_details, name='dealer_details'),
    path('reviews/dealer/<int:dealer_id>/',
         view=views.get_dealer_reviews, name='dealer_details'),
    path('add_review/', view=views.add_review, name='add_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
