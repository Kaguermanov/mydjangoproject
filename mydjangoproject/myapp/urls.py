from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = [
    path('admin-only/', login_required(TemplateView.as_view(template_name='flatpages/admin_only.html')), name='admin-only'),
]
