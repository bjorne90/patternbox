from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    # Add any additional fields you want for the user profile
    profile_image = models.ImageField(upload_to='profile_images', blank=True)
    is_creator = models.BooleanField(default=False)

    # Add unique related_name arguments for groups and user_permissions
    groups = models.ManyToManyField(Group, blank=True, related_name='profiles_user_set')
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='profiles_user_set',
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
        related_query_name='profiles_user',
    )


class Pattern(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    # Add any additional fields for the pattern, such as description, image, etc.

    def __str__(self):
        return self.title
