from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


def validate_cpf(value):
    cpf = [int(char) for char in value if char.isdigit()]

    if len(cpf) != 11:
        raise ValidationError('CPF must have 11 valid digits')
        
    if cpf == cpf[::-1]:
        raise ValidationError('Invalid CPF')

    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            raise ValidationError('Invalid CPF')

validate_cpf_regex = RegexValidator(
    regex='^\d{3}\.\d{3}\.\d{3}\-\d{2}$',
    message='CPF must be properly formatted',
    code='invalid'
)
