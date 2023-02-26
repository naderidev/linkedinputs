from typing import Optional
from flet import (
    Page,
    CrossAxisAlignment,
    MainAxisAlignment,
    Row,
    TextField,
    TextAlign,
    TextStyle,
    FontWeight,
    colors
)
from .linkedinputs import AcceptTypes, RegularLinkedInputs


class PinInputT1(RegularLinkedInputs):

    def __init__(
        self,
            page: Page,
            accept_type: Optional[AcceptTypes] = AcceptTypes.ALL,
            on_change: Optional[callable] = None,
            correct_answer: str = None,
            on_complete: Optional[callable] = None,
            accept_length: int = 1
    ):
        super().__init__(
            page=page,
            inputs=self.pin_inputs(),
            accept_type=accept_type,
            on_change=on_change,
            on_error=None,
            on_complete=self._on_complete,
            place=Row(
                vertical_alignment=CrossAxisAlignment.CENTER,
                alignment=MainAxisAlignment.CENTER,
                spacing=15
            ),
            accept_length=accept_length,
        )
        self.__on_complete = on_complete
        self.correct_answer = correct_answer

    def pin_inputs(self):
        return [
            TextField(
                text_size=20,
                text_align=TextAlign.CENTER,
                bgcolor='#1a1e24',
                border_radius=13,
                width=50,
                height=50,
                content_padding=0,
                text_style=TextStyle(
                    weight=FontWeight.W_600
                ),
                border_color=colors.TRANSPARENT,
                focused_border_color='#58a6ff',
            ) for _ in range(4)
        ]

    def _on_error(self, c):
        pass

    def _on_complete(self, c):
        if self.correct_answer:
            self._input_action_style(not self.is_correct)

        if self.__on_complete:
            self.__on_complete(self.is_correct, self)

    def _on_change(self, current_index: int, values: list = [], errors: list = []):
        super()._on_change(current_index, values, errors)
        
        if self.correct_answer:
            self._input_action_style(True, True)

    def _input_action_style(self, error: bool, clear=False):
        for input in self.inputs:
            input.border_color = (
                colors.GREEN if not error else colors.RED) if not clear else self.pin_inputs()[0].border_color
            input.update()
    
    @property
    def is_correct(self):
        return self.correct_answer == self.string_value
