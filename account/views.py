from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import JsonResponse
from .email_backend import EmailBackend
from django.contrib import messages
from .forms import CustomUserForm  # Only CustomUserForm is in account/forms.py
from voting.forms import CandidateForm, PositionForm, VoterForm  # Import from voting/forms.py
from django.contrib.auth import login, logout
from voting.models import Candidate, Position  # Import from voting/models.py instead of account.models

# Existing authentication views
def account_login(request):
    if request.user.is_authenticated:
        if request.user.user_type == '1':
            return redirect(reverse("adminDashboard"))
        else:
            return redirect(reverse("voterDashboard"))

    context = {}
    if request.method == 'POST':
        user = EmailBackend.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            if user.user_type == '1':
                return redirect(reverse("adminDashboard"))
            else:
                return redirect(reverse("voterDashboard"))
        else:
            messages.error(request, "Invalid details")
            return redirect("/")

    return render(request, "voting/login.html", context)

def account_register(request):
    userForm = CustomUserForm(request.POST or None)
    voterForm = VoterForm(request.POST or None)
    context = {
        'form1': userForm,
        'form2': voterForm
    }
    if request.method == 'POST':
        if userForm.is_valid() and voterForm.is_valid():
            user = userForm.save(commit=False)
            voter = voterForm.save(commit=False)
            voter.admin = user
            user.save()
            voter.save()
            messages.success(request, "Account created. You can login now!")
            return redirect(reverse('account_login'))
        else:
            messages.error(request, "Provided data failed validation")
    return render(request, "voting/reg.html", context)

def account_logout(request):
    user = request.user
    if user.is_authenticated:
        logout(request)
        messages.success(request, "Thank you for visiting us!")
    else:
        messages.error(request, "You need to be logged in to perform this action")
    return redirect(reverse("account_login"))

# Add views for candidates
def view_candidates(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Candidate added successfully!")
            return redirect('viewCandidates')
        else:
            messages.error(request, "Failed to add candidate. Please check the form.")
    else:
        form = CandidateForm()

    candidates = Candidate.objects.all()
    return render(request, 'candidates.html', {'form1': form, 'candidates': candidates})

def view_candidate(request):
    if request.method == 'GET':
        candidate_id = request.GET.get('id')
        candidate = get_object_or_404(Candidate, id=candidate_id)
        form = CandidateForm(instance=candidate)
        return JsonResponse({'form': str(form), 'fullname': candidate.fullname})

def update_candidate(request):
    if request.method == 'POST':
        candidate_id = request.POST.get('id')
        candidate = get_object_or_404(Candidate, id=candidate_id)
        form = CandidateForm(request.POST, request.FILES, instance=candidate)
        if form.is_valid():
            form.save()
            messages.success(request, "Candidate updated successfully!")
        else:
            messages.error(request, "Failed to update candidate.")
        return redirect('viewCandidates')

def delete_candidate(request):
    if request.method == 'POST':
        candidate_id = request.POST.get('id')
        candidate = get_object_or_404(Candidate, id=candidate_id)
        candidate.delete()
        messages.success(request, "Candidate deleted successfully!")
        return redirect('viewCandidates')

# Add views for positions
def view_positions(request):
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Position added successfully!")
            return redirect('viewPositions')
        else:
            messages.error(request, "Failed to add position. Please check the form.")
    else:
        form = PositionForm()

    positions = Position.objects.all()
    return render(request, 'positions.html', {'form1': form, 'positions': positions})

def view_position(request):
    if request.method == 'GET':
        position_id = request.GET.get('id')
        position = get_object_or_404(Position, id=position_id)
        return JsonResponse({
            'id': position.id,
            'name': position.name,
            'max_vote': position.max_vote,
        })

def update_position(request):
    if request.method == 'POST':
        position_id = request.POST.get('id')
        position = get_object_or_404(Position, id=position_id)
        form = PositionForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
            messages.success(request, "Position updated successfully!")
        else:
            messages.error(request, "Failed to update position.")
        return redirect('viewPositions')

def delete_position(request):
    if request.method == 'POST':
        position_id = request.POST.get('id')
        position = get_object_or_404(Position, id=position_id)
        position.delete()
        messages.success(request, "Position deleted successfully!")
        return redirect('viewPositions')