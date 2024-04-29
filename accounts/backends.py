from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend ,UserModel
from django.db.models import Q

UserModel = User


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(
                Q(username__iexact=username)|
                 Q(email__iexact=username))
        except UserModel.DoesNotExist:
            pass
        except UserModel.MultipleObjectsReturned:
            user = UserModel.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).order_by('id').first()

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
    