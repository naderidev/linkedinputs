from flet import (
    Page,
    TextField,
    Row,
    UserControl,
    CrossAxisAlignment,
    Column,
    MainAxisAlignment
)
from enum import Enum
from typing import Optional
from rich.pretty import pprint


class AcceptTypes(Enum):
    ONLY_NUMBER = 'only_number'
    ONLY_LETTERS = 'only_letters'
    ALL = 'all'


class InputErrorTypes(Enum):
    TYPE_ERROR = 1
    LENGTH_ERROR = 2


class LinkedInputs(UserControl):
    _vals: list = []
    _errors: list = []

    def __init__(
        self,
        page: Page,
        inputs: Optional[list[TextField]] = [],
        accept_type: Optional[AcceptTypes] = AcceptTypes.ALL,
        on_change: Optional[callable] = None,
        on_error: Optional[callable] = None,
        on_complete: Optional[callable] = None,
        place: Optional[Row | Column] = Row(
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
        self.on_error = on_error
        self.on_complete = on_complete

        self._vals = ['' for _ in range(0, len(self.inputs))]
        self._errors = [None for _ in range(0, len(self.inputs))]
        for index, input in enumerate(self.inputs):
            input.on_change = self.__input_on_change
            input.data = {'index': index}

    def __input_on_change(self, e):
        index = e.control.data['index']
        value = e.control.value
        self._vals[index] = value
        self.__validate(index)

        self._on_change(index, self._vals, self._errors)

        if self.on_change:
            self.on_change(index, self._vals, self._errors)

        if '' not in self._vals and self.on_complete:
            self.on_complete(self)

        if True in [(True if isinstance(i, InputErrorTypes) else False) for i in self._errors] and self.on_error:
            self.on_error(self)

    def flash_errors(self):
        e = self.errors
        self.clear_errors()
        return e

    def __validate(self, index: int):
        if self._vals[index]:
            match self.accept_type:
                case AcceptTypes.ONLY_NUMBER:
                    if not self._vals[index].isdigit():
                        self._vals[index] = ''.join(
                            filter(str.isdigit, self._vals[index]))
                        self._errors[index] = InputErrorTypes.TYPE_ERROR
                        self.inputs[index].value = self._vals[index]
                        self.inputs[index].update()
                        return

                case AcceptTypes.ONLY_LETTERS:
                    if not self._vals[index].isalpha():
                        self._vals[index] = ''.join(
                            filter(str.isdigit, self._vals[index]))
                        self.inputs[index].value = self._vals[index]
                        self._errors[index] = InputErrorTypes.TYPE_ERROR
                        self.inputs[index].update()
                        return

        self._errors[index] = None

    def build(self):
        l = self.inputs.copy()
        if self.page.rtl:
            l.reverse()
        self.place.controls = l
        return self.place

    def _build(self):
        super()._build()

    def _on_change(self, current_index: int, values: list = [], errors: list = []):
        pprint([
            {v: errors[i]} for i, v in enumerate(values)
        ], expand_all=True)

    @property
    def errors(self):
        return self._errors

    def clear_errors(self):
        self._errors = [None for _ in range(0, len(self.inputs))]

    @property
    def value(self):
        return self._vals

    @value.setter
    def value(self, values: Optional[list]):
        for index, val in enumerate(values):
            if self.__validate(index, val):
                self.inputs[index].value = val
                self.inputs[index].update()

    @property
    def string_value(self):
        return ''.join(self._vals)


class RegularLinkedInputs(LinkedInputs):
    def __init__(
        self, page: Page,
            inputs: Optional[list[TextField]] = [],
            accept_type: Optional[AcceptTypes] = AcceptTypes.ALL,
            on_change: Optional[callable] = None,
            on_error: Optional[callable] = None,
            on_complete: Optional[callable] = None,
            place: Optional[Row | Column] = Row(
                vertical_alignment=CrossAxisAlignment.CENTER,
                alignment=MainAxisAlignment.CENTER
            ),
            accept_length: int = 1,
            one_by_one: bool = True

    ):
        super().__init__(
            page=page,
            inputs=inputs,
            accept_type=accept_type,
            on_error=on_error,
            on_complete=on_complete,
            place=place
        )
        self.accept_length = accept_length
        self.one_by_one = one_by_one
        self.on_change = on_change

    def _on_change(self, current_index: int, values: list = [], errors: list = []):
        self.__validate_length(current_index, values[current_index])
        if self.one_by_one \
                and ((current_index + 1) < len(values)) \
                and (len(values[current_index]) >= self.accept_length):
            
            self.inputs[current_index + 1].focus()

    def __validate_length(self, current_index: int, value: str):
        if not self.errors[current_index]:
            if len(value) > self.accept_length:
                val = value[0: self.accept_length]
                self.errors[current_index] = InputErrorTypes.LENGTH_ERROR
                self.inputs[current_index].value = val
                self._vals[current_index] = val
                self.inputs[current_index].update()
                return False

            self.errors[current_index] = None
            return True
