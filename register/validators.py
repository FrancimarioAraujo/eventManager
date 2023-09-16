from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
import re

class UppercaseLowercaseDigitValidator:
    def __init__(self, min_digits=1, min_lower=1, min_upper=1):
        self.min_digits = min_digits
        self.min_lower = min_lower
        self.min_upper = min_upper

    def __call__(self, password):
        if (
            len(re.findall(r'[A-Z]', password)) < self.min_upper or
            len(re.findall(r'[a-z]', password)) < self.min_lower or
            len(re.findall(r'[0-9]', password)) < self.min_digits
        ):
            raise ValidationError(
                f"A senha deve conter pelo menos {self.min_upper} letra(s) maiúscula(s), "
                f"{self.min_lower} letra(s) minúscula(s) e {self.min_digits} número(s)."
            )

class phoneNumberValidator:
    def validate_phone_number(value):
        phone_regex = r'^\(?([0-9]{2})\)?[ .-]?([0-9]{4,5})[ .-]?([0-9]{4})$'
        if re.match(phone_regex, value):
            return True
        else:
            raise ValidationError(
                _("O número de telefone não é válido. Certifique-se de incluir apenas números"),
                code='invalid_phone_number'
            )
