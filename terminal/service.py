from django.db import transaction

from .models import Сurrency
from .exception import BankError

class Bank:

    def _get_remainder(self):
        return {
            currency.denomination: currency.number for currency in Сurrency.objects.all().order_by('-denomination')
        }

    def withdraw(self, amount):
        withdraw = {}

        for denomination, number_own in self._get_remainder().items():
            number_need, amount_residual = divmod(amount, denomination)

            if number_need == 0:
                continue
            
            if number_need > number_own:
                number_need = number_own
                amount_residual = amount - number_need * denomination

            withdraw[denomination] = number_need
            amount = amount_residual

        if amount > 0:
            raise self.MatchingError()

        return withdraw

    def status(self):
        return self._get_remainder()

    @transaction.atomic
    def set(self, currencies):
        for denomination, number in currencies.items():
            currency, _created = Сurrency.objects.get_or_create(denomination=denomination)

            currency.denomination = denomination
            currency.number = number
            
            currency.save()

    def reset(self):
        Сurrency.objects.all().delete()

    class MatchingError(BankError):
        def __init__(self):
            super().__init__('Not found matching banknotes')
