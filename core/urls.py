from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/submitter/', views.submitter_dashboard, name='submitter_dashboard'),
    path('dashboard/reviewer/', views.reviewer_dashboard, name='reviewer_dashboard'),
    path('documents/upload/', views.upload_document, name='upload_document'),
    path('documents/<int:id>/', views.document_detail, name='document_detail'),
    path('documents/<int:id>/edit/', views.edit_document, name='edit_document'),
    path('documents/<int:id>/comment/', views.add_comment, name='add_comment'),
    path('documents/<int:id>/approve/', views.approve_document, name='approve_document'),
    path('documents/<int:id>/reject/', views.reject_document, name='reject_document'),
]