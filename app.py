import time
from flet import *
from src.pininput.input_types import RegularLinkedInputs
from src.pininput.pininput import LinkedInputs, AcceptTypes , pprint


def main(page: Page):
    page.title = 'PIN INPUT'
    inputs = [
        TextField(
        width=50,
        text_size=20,
        text_align=TextAlign.CENTER
        ) for i in range(4)
    ]

    page.add(RegularLinkedInputs(
        page=page,
        inputs=inputs,
        accept_type=AcceptTypes.ONLY_LETTERS,
        on_error=lambda c: print('Error')
        
    ))


app(target=main)
