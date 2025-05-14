from django import forms
from .models import Candidate, Position, Voter  # Ensure Voter model exists
from account.forms import FormSettings  # Assuming FormSettings is in account/forms.py

class VoterForm(FormSettings):
    class Meta:
        model = Voter
        fields = ['phone']

class PositionForm(FormSettings):
    class Meta:
        model = Position
        fields = ['name', 'max_vote']

class CandidateForm(FormSettings):
    class Meta:
        model = Candidate
        fields = ['fullname', 'bio', 'position', 'photo']