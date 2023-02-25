import time
from flet import *
from src.linkedinputs.linkedinputs import LinkedInputs, AcceptTypes, pprint, RegularLinkedInputs


def main(page: Page):
    page.title = 'PIN INPUT'
    inputs = [
        TextField(
            width=100,
            text_size=20,
            text_align=TextAlign.CENTER
        ) for i in range(4)
    ]

    page.add(RegularLinkedInputs(
        page=page,
        inputs=inputs,
        accept_type=AcceptTypes.ONLY_NUMBER,
        accept_length=4,
        on_error=lambda c: print('Error')

    ))


app(target=main)
