from .pininput import LinkedInputs, AcceptTypes, InputErrorTypes
from flet import *
from typing import Optional


class RegularLinkedInputs(LinkedInputs):
    def __init__(
        self, page: Page,
            inputs: Optional[TextField] = [],
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
            on_change=on_change,
            on_error=on_error,
            on_complete=on_complete,
            place=place
        )
        self.accept_length = accept_length
        self.one_by_one = one_by_one

    def _on_change(self, current_index: int, values: list = [], errors: list = []):
        self.__validate_length(current_index, values[current_index])
        if self.one_by_one and (current_index + 1) < len(values):
            self.inputs[current_index + 1].focus()

    def __validate_length(self, current_index: int, value: str):
        if not self.errors[current_index]:
            if len(value) > self.accept_length:
                self.errors[current_index] = InputErrorTypes.LENGTH_ERROR
                self.inputs[current_index].value = value[0: self.accept_length]
                self.inputs[current_index].update()
                return False

            self.errors[current_index] = None
            return True
