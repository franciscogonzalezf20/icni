from .Invalid_Number_State import InvalidNumberState
from .Valid_Number_State import ValidNumberState


class NumberFactory:
    def create_number_state(self, number:str):
        if len(number) == 24:
            return ValidNumberState()
        elif len(number) == 23:
            return ValidNumberState()
        else:
            return InvalidNumberState()