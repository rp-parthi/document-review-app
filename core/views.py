from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User, Document, Comment
from django.utils import timezone

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('register')
        
        user = User.objects.create_user(username=username, password=password)
        messages.success(request, 'Account created. Please log in.')
        return redirect('login')

    return render(request, 'core/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.role == 'submitter':
                return redirect('submitter_dashboard')
            if user.role == 'reviewer':
                return redirect('reviewer_dashboard')
            else:
                messages.error(request, 'Your account is pending role assignment. Contact admin.')
                return redirect('login')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    
    return render(request, 'core/login.html')

@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    
@login_required
def submitter_dashboard(request):
    if request.user.role != 'submitter':
        if request.user.role == 'reviewer':
            return redirect('reviewer_dashboard')
        return redirect('login')
    
    documents = Document.objects.filter(uploaded_by=request.user)
    return render(request, 'core/submitter_dashboard.html', {'documents': documents})
    
@login_required
def reviewer_dashboard(request):
    if request.user.role != 'reviewer':
        if request.user.role == 'submitter':
            return redirect('submitter_dashboard')
        return redirect('login')
    
    documents = Document.objects.filter(assigned_to=request.user)
    return render(request, 'core/reviewer_dashboard.html', {'documents': documents})

@login_required
def upload_document(request):
    if request.user.role != 'submitter':
        if request.user.role == 'reviewer':
            return redirect('reviewer_dashboard')
        return redirect('login')
    
    if request.method == 'POST':
        title = request.POST['title']
        file = request.FILES['file']
        assigned_to_id = request.POST['assigned_to']
        action = request.POST['action']

        assigned_to = User.objects.get(id=assigned_to_id)

        document = Document.objects.create(title=title, file=file, uploaded_by=request.user, assigned_to=assigned_to,) 

        if action == 'draft':
            document.status = 'draft'
        elif action == 'submit':
            document.status = 'under_review'

        document.save()
        return redirect('submitter_dashboard')

    reviewers = User.objects.filter(role='reviewer')
    return render(request, 'core/upload_document.html', {'reviewers': reviewers})

@login_required
def document_detail(request, id):
    document = get_object_or_404(Document, id=id)
    comments = Comment.objects.filter(document=document)
    return render(request, 'core/document_detail.html', {'document': document, 'comment': comments})


@login_required
def edit_document(request, id):
    document = get_object_or_404(Document, id=id)

    if request.user != document.uploaded_by:
        return redirect('submitter_dashboard')
    
    if document.status != 'draft':
        return redirect('document_detail', id=id)
    
    if request.method == 'POST':
        document.title = request.POST['title']
        document.assigned_to = User.objects.get(id=request.POST['assigned_to'])
        action = request.POST['action']

        if 'file' in request.FILES:
            document.file = request.FILES['file']

        if action == 'draft':
            document.status = 'draft'
        elif action == 'submit':
            document.status = 'under_review'

        document.save()
        return redirect('document_detail', id=id)

    reviewers = User.objects.filter(role='reviewer')
    return render(request, 'core/edit_document.html', {'document': document, 'reviewers': reviewers})

@login_required
def add_comment(request, id):
    document = get_object_or_404(Document, id=id)

    if request.method == 'POST':
        text = request.POST['text']
        Comment.objects.create(text=text, author=request.user, document=document)

        return redirect('document_detail', id=id)
    return redirect('document_detail', id=id)

@login_required
def approve_document(request, id):
    document = get_object_or_404(Document, id=id)

    if request.user.role != 'reviewer':
        return redirect('login')
    
    if request.user != document.assigned_to:
        return redirect('reviewer_dashboard')
    
    if request.method == 'POST':
        if document.status == 'under_review':
            document.status = 'approved'
            document.date_reviewed = timezone.now()
            document.save()
        return redirect('reviewer_dashboard')
    
    return redirect('reviewer_dashboard')

@login_required
def reject_document(request, id):
    document = get_object_or_404(Document, id=id)

    if request.user.role != 'reviewer':
        return redirect('login')

    if request.user != document.assigned_to:
        return redirect('reviewer_dashboard')

    if request.method == 'POST':
        if document.status == 'under_review':
            document.status = 'rejected'
            document.date_reviewed = timezone.now()
            document.save()
        return redirect('reviewer_dashboard')

    return redirect('reviewer_dashboard')