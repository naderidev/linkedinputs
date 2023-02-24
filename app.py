from flet import *
from src.pininput.pininput import LinkedInputs, AcceptTypes


def main(page: Page):
    page.title = 'PIN INPUT'
    inputs = [
        TextField(
        width=50,
        text_size=20,
        text_align=TextAlign.CENTER
        ) for i in range(4)
    ]

    page.add(LinkedInputs(
        page=page,
        inputs=inputs,
        accept_type=AcceptTypes.ONLY_NUMBER
        
    ))


app(target=main)
