from django.core.validators import RegexValidator


class UserNameValidator(RegexValidator):
    regex = '^[a-zA-Z0-9]+(_[a-zA-Z0-9]+)*$'