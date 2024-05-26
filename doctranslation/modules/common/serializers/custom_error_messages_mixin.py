

class CustomErrorMessagesMixin:
    FIELD_ERROR_MESSAGES = {
        'required': 'required',
        'blank': 'blank',
        'invalid_choice': 'invalidChoice',
        'incorrect_type': 'incorrectType',
        'invalid': 'invalid',
    }

    VALIDATOR_ERROR_MESSAGES = {
        'UniqueValidator': 'duplicate',
        'EmailValidator': 'wrongFormat',
        'MaxLengthValidator': 'maxLengthExceeded',
        'MinLengthValidator': 'lessThanMinLength',
        'MinValueValidator': 'lessThanMinValue',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.replace_validators_messages()

    def replace_validators_messages(self):
        fields = self.fields

        for field_name in fields:
            field = fields[field_name]
            for field_error in field.error_messages:
                override_error_message = self.FIELD_ERROR_MESSAGES.get(field_error)
                if override_error_message:
                    field.error_messages[field_error] = override_error_message

            for validator in field.validators:
                validator_type = type(validator).__name__
                validator_message = self.VALIDATOR_ERROR_MESSAGES.get(validator_type)
                if validator_message:
                    validator.message = validator_message
