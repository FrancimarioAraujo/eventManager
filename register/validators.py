from django.core.exceptions import ValidationError
import re

class UppercaseLowercaseDigitValidator:
    def __init__(self, min_digits=1, min_lower=1, min_upper=1):
        self.min_digits = min_digits
        self.min_lower = min_lower
        self.min_upper = min_upper

    def __call__(self, password):
        # Verifique a presença de letras maiúsculas, minúsculas e números
        if (
            len(re.findall(r'[A-Z]', password)) < self.min_upper or
            len(re.findall(r'[a-z]', password)) < self.min_lower or
            len(re.findall(r'[0-9]', password)) < self.min_digits
        ):
            raise ValidationError(
                f"A senha deve conter pelo menos {self.min_upper} letra(s) maiúscula(s), "
                f"{self.min_lower} letra(s) minúscula(s) e {self.min_digits} número(s)."
            )
