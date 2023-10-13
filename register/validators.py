import re
import phonenumbers


def password_validator(password):
    # Verifica se a senha tem pelo menos 8 caracteres
    if len(password) < 8:
        return False
    
    # Verifica se a senha tem pelo menos uma letra maiúscula
    if not re.search(r'[A-Z]', password):
        return False
    
    # Verifica se a senha tem pelo menos um número
    if not re.search(r'[0-9]', password):
        return False
    
    return True

def phone_number_validator(phone):
    try:
        number = phonenumbers.parse(phone, "BR")
        return phonenumbers.is_valid_number(number)
    except phonenumbers.NumberParseException:
        return False
