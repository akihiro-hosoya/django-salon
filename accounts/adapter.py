from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user = super(AccountAdapter, self).save_user(request, user, form, commit=False)
        if request.user.is_staff:
            user.account_type = 2
        else:
            user.account_type = 1
        user.save()