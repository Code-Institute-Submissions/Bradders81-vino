from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm



def profile(request):
    """
    Renders User Profile information
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
   
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    context = {'profile': profile, 'form': form, 'orders': orders, }
    return render(request, 'profiles1/profile.html', context)
