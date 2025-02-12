from django.contrib.auth.mixins import UserPassesTestMixin

class RoleRequiredMixin(UserPassesTestMixin):
    required_role = None

    def test_func(self):
        return self.request.user.role == self.required_role
