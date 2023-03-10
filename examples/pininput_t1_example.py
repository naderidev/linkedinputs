import random
from flet import *
from linkedinputs import PinInputT1
from linkedinputs import AcceptTypes


def main(page: Page):
    page.title = 'PIN INPUT'
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.bgcolor = '#0d1117'
    passowrd = str(random.randrange(1000, 9999))
    pininput = PinInputT1(
        page=page,
        accept_type=AcceptTypes.ONLY_NUMBER,
        accept_length=1,
        correct_answer=passowrd,
    )

    def on_verify_btn_clicked(e):
        e.page.snack_bar = SnackBar(
            content=Text("Your password is correct", color=colors.GREEN) if pininput.is_correct else Text(
                "Your password is not correct", color=colors.RED),
            action="Alright!",
            open=True,
            bgcolor='#1a1e24'
        )
        e.page.update()

    page.add(
        Column(
            [
                Column(
                    [
                        Text(
                            value='Step 2',
                            size=28,
                            text_align=TextAlign.LEFT
                        ),
                        Text(
                            value='Enter the code that was sent to you',
                            text_align=TextAlign.LEFT,
                            size=15,
                            color=colors.WHITE70
                        ),
                    ]
                ),
                pininput,
                Container(
                    bgcolor=colors.BLUE,
                    content=Text(
                        value='Verify & Login',
                        size=15,
                        weight=FontWeight.W_600
                    ),
                    border_radius=10,
                    padding=Padding(left=75, right=75, top=8, bottom=8),
                    on_click=on_verify_btn_clicked
                ),
                Text(
                    value='Correct password is: ' + passowrd,
                    color=colors.WHITE38
                )
            ],
            spacing=20,
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,

        )
    )


app(target=main)
