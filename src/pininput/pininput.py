from flet import *
from enum import Enum
from typing import Optional
from rich.pretty import pprint


class AcceptTypes(Enum):
    ONLY_NUMBER = 'only_number'
    ONLY_LETTERS = 'only_letters'
    ALL = 'all'


class InputErrorTypes(Enum):
    TYPE_ERROR = 1


class LinkedInputs(UserControl):
    __vals: list = []
    __errors: list = []

    def __init__(
        self,
        page: Page,
        inputs: Optional[TextField] = [],
        accept_type: Optional[AcceptTypes] = AcceptTypes.ALL,
        on_change: Optional[callable] = None,
        place: Optional[Row | Column] = Row(
            controls=[],
            vertical_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.CENTER
        ),
    ):
        super().__init__()
        self.page = page
        self.inputs = inputs
        self.accept_type = accept_type
        self.on_change = on_change
        self.place = place

        self.__vals = ['' for _ in range(0, len(self.inputs))]
        self.__errors = [None for _ in range(0, len(self.inputs))]
        for index, input in enumerate(self.inputs):
            input.on_change = self.__input_on_change
            input.data = {'index': index}

    def __input_on_change(self, e):
        index = e.control.data['index']
        value = e.control.value
        self.__vals[index] = value
        self.__validate(index, value)

        if self.on_change:
            self.on_change(self.__vals, self.__errors)
        else:
            self._on_change(self.__vals, self.__errors)

    def __validate(self, index: int, value: str):
        if value:
            match self.accept_type:
                case AcceptTypes.ONLY_NUMBER:
                    if not value.isdigit():
                        self.__errors[index] = InputErrorTypes.TYPE_ERROR
                        return False

                case AcceptTypes.ONLY_LETTERS:
                    if not value.isalpha():
                        self.__errors[index] = InputErrorTypes.TYPE_ERROR
                        return False

        self.__errors[index] = None
        return True

    def build(self):
        self.place.controls = self.inputs
        return self.place

    def _build(self):
        super()._build()

    def _on_change(self, values: list = [], errors: list = []):
        pprint([
            {v:errors[i]} for i,v in enumerate(values)
        ], expand_all=True)

    @property
    def errors(self):
        return self.__errors

    def clear_errors(self):
        return [None for _ in range(0, len(self.inputs))]

    @property
    def value(self):
        return self.__vals

    @value.setter
    def value(self, values: Optional[list]):
        for index, val in enumerate(values):
            if self.__validate(val):
                self.inputs[index] = val
                self.inputs[index].update()

    @property
    def string_value(self):
        return ''.join(self.__vals)
