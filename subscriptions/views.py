from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import UserFollows
from accounts.models import CustomUser



@login_required
def manage_subscriptions(request):
    """Main view to manage users search, following users and followed users."""
    search_results = None

    if 'username' in request.GET:
        username = request.GET.get('username')
        if username:
            user_to_follow = CustomUser.objects.filter(username=username).first()
            if user_to_follow and (user_to_follow != request.user):
                search_results = user_to_follow

    followed_users = UserFollows.objects.filter(user=request.user)
    followers = UserFollows.objects.filter(followed_user=request.user)

    context = {
        'followed_users': followed_users,
        'followers': followers,
        'search_results': search_results,
    }
    return render(request, 'subscriptions/subscriptions.html', context)

@login_required
def follow_user(request, user_id):
    """Allow user to confirm following."""
    user_to_follow = CustomUser.objects.get(id=user_id)
    UserFollows.objects.get_or_create(
        user=request.user,
        followed_user=user_to_follow
        )
    
    return redirect('subscriptions:subscriptions')

@login_required
def unfollow(request, followed_user_id):
    """Allow user to unfollow another user."""
    followed_user = CustomUser.objects.get(id=followed_user_id)
    UserFollows.objects.filter(
        user=request.user,
        followed_user=followed_user).delete()
    
    return redirect('subscriptions:subscriptions')
