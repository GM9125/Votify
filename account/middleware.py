from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages

class AccountCheckMiddleWare(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        if request.user.is_authenticated:
            # Avoid modifying the user object directly
            user_type = request.user.user_type
            if user_type == '1':  # Admin
                if modulename == 'voting.views':
                    if request.path != reverse('fetch_ballot'):
                        messages.error(
                            request, "You do not have access to this resource")
                        return redirect(reverse('adminDashboard'))
            elif user_type == '2':  # Voter
                if modulename == 'administrator.views':
                    messages.error(
                        request, "You do not have access to this resource")
                    return redirect(reverse('voterDashboard'))
            else:
                return redirect(reverse('account_login'))
        else:
            if request.path not in [reverse('account_login'), reverse('account_register')] and modulename not in ['django.contrib.auth.views'] and (modulename == 'administrator.views' or modulename == 'voting.views'):
                messages.error(
                    request, "You need to be logged in to perform this operation")
                return redirect(reverse('account_login'))
        return None  # Allow the view to proceed