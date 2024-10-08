from django.db import models

from LITReview import settings


class UserFollows(models.Model):
    """A model to represent the 'following' relationship between users."""

    # Users this user is following
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='following'
    )

    # Users who are following this user
    followed_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='followed_by'
    )

    class Meta:
        # Ensure that each user can only follow another user once
        unique_together = ('user', 'followed_user')

    def __str__(self):
        return f"{self.user} follows {self.followed_user}"
