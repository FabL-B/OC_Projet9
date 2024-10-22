from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import UserFollows
from accounts.models import CustomUser


@login_required
def manage_subscriptions(request):
    """View to manage users search, following users and followed users."""
    # Get followed users and followers
    followed_users = UserFollows.objects.filter(user=request.user)
    followers = UserFollows.objects.filter(followed_user=request.user)

    # Get user search
    search_results = None
    # If user search is submitted
    if "username" in request.GET:
        username = request.GET.get("username")
        if username:
            user_to_follow = CustomUser.objects.filter(
                username=username).first()
            # Check if searched user exist
            # and is not current user or already followed
            if (
                user_to_follow and
                user_to_follow != request.user and
                user_to_follow.id not in followed_users.values_list(
                    'followed_user', flat=True)
            ):
                search_results = user_to_follow

    context = {
        "followed_users": followed_users,
        "followers": followers,
        "search_results": search_results,
    }
    return render(request, "subscriptions/subscriptions.html", context)


@login_required
def follow_user(request, user_id):
    """Allow user to confirm following."""
    # Get the user to follow from the ID in the URL
    user_to_follow = CustomUser.objects.get(id=user_id)
    UserFollows.objects.get_or_create(
        user=request.user, followed_user=user_to_follow)

    return redirect("subscriptions:subscriptions")


@login_required
def unfollow(request, followed_user_id):
    """Allow user to unfollow another user."""
    # Get the user to unfollow from the ID in the URL
    followed_user = CustomUser.objects.get(id=followed_user_id)
    UserFollows.objects.filter(
        user=request.user, followed_user=followed_user).delete()

    return redirect("subscriptions:subscriptions")
