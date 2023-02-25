from flet import *
from src.linkedinputs.linkedinputs import RegularLinkedInputs, AcceptTypes


def main(page: Page):
    page.title = 'Banl Card'
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.bgcolor = '#0d1117'

    # a couple of iranian banks ...
    banks = [
        {'name': 'بانک ملی ایران', 'code': '603799'},
        {'name': 'بانک سپه', 'code': '589210'},
        {'name': 'بانک توسعه صادرات', 'code': '627648'},
        {'name': 'بانک صنعت و معدن', 'code': '627961'},
        {'name': 'بانک کشاورزی', 'code': '603770'},
        {'name': 'بانک مسکن', 'code': '628023'},
        {'name': 'پست بانک ایران', 'code': '627760'},
        {'name': 'بانک توسعه تعاون', 'code': '502908'},
        {'name': 'بانک اقتصاد نوین', 'code': '627412'},
        {'name': 'بانک پارسیان', 'code': '622106'},
        {'name': 'بانک پاسارگاد', 'code': '502229'},
        {'name': 'بانک کارآفرین', 'code': '627488'},
        {'name': 'بانک سامان', 'code': '621986'},
        {'name': 'بانک سینا', 'code': '639346'},
        {'name': 'بانک سرمایه', 'code': '639607'},
        {'name': 'بانک تات', 'code': '636214'},
        {'name': 'بانک شهر', 'code': '502806'},
        {'name': 'بانک دی', 'code': '502938'},
        {'name': 'بانک صادرات', 'code': '603769'},
        {'name': 'بانک ملت', 'code': '610433'},
        {'name': 'بانک تجارت', 'code': '627353'},
        {'name': 'بانک رفاه', 'code': '589463'},
        {'name': 'بانک انصار', 'code': '627381'},
        {'name': 'بانک مهر اقتصاد', 'code': '639370'}
    ]
    bank_name = Text(
        value='نامشخص',
        size=24,
        color=colors.WHITE38,
        weight=FontWeight.W_600,
        text_align=TextAlign.RIGHT,
        expand=True

    )

    def on_change_input(i, v, e):
        val = ''.join(v)
        codes = [
            b['code'] for b in banks
        ]
        if len(val) >= 6 and val[0:6] in codes:
            bank = banks[int(codes.index(val[0:6]))]['name']
            bank_name.value = bank
            bank_name.update()
        else:
            bank_name.value = 'نامشخص'
            bank_name.update()

    page.add(
        Container(
            content=Column(
                [
                    Row(
                        [
                            Row(
                                [
                                    bank_name,
                                    Image(
                                        src_base64='PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciICB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgd2lkdGg9IjEyOHB4IiBoZWlnaHQ9IjEyOHB4Ij48cmVjdCB3aWR0aD0iNDgwIiBoZWlnaHQ9IjE2MCIgeD0iMTYiIHk9IjE3NiIgZmlsbD0iI2Y4ZmFmYyIvPjxwYXRoIGZpbGw9IiM2ZGE1NDQiIGQ9Ik00NDYsNzZINjZjLTI3LjYxNCwwLTUwLDIyLjM4Ni01MCw1MHY1MGgzMHYyMGgyMHYtMjBoMzB2MjBoMjB2LTIwaDMwdjIwaDIwdi0yMCBoMzB2MjBoMjB2LTIwaDMwdjIwaDIwdi0yMGgzMHYyMGgyMHYtMjBoMzB2MjBoMjB2LTIwaDMwdjIwaDIwdi0yMGgzMHYyMGgyMHYtMjBoMzB2LTUwQzQ5Niw5OC4zODYsNDczLjYxNCw3Niw0NDYsNzZ6Ii8+PHBhdGggZmlsbD0iI2Q3MDAyOSIgZD0iTTI4OS4zMzMsMjIzLjVjMCwyNi42MDYtMTAuODA4LDQ5LjczMy0yNSw1Ni40MDFWMjIzLjVoLTE2LjY2N3Y1Ni40IGMtMTQuMTkxLTYuNjY3LTI1LTI5Ljc5NS0yNS01Ni40SDIwNmMwLDQyLjA1NiwyMS45NjIsNzUsNTAsNzVjMjguMDM3LDAsNTAtMzIuOTQ0LDUwLTc1SDI4OS4zMzN6Ii8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTQ2NiwzMzZ2LTIwaC0yMHYyMGgtMzB2LTIwaC0yMHYyMGgtMzB2LTIwaC0yMHYyMGgtMzB2LTIwaC0yMHYyMGgtMzB2LTIwaC0yMHYyMCBoLTMwdi0yMGgtMjB2MjBoLTMwdi0yMGgtMjB2MjBoLTMwdi0yMEg5NnYyMEg2NnYtMjBINDZ2MjBIMTZ2MzB2LTEwdjMwYzAsMjcuNjE0LDIyLjM4Niw1MCw1MCw1MGgzODBjMjcuNjE0LDAsNTAtMjIuMzg2LDUwLTUwIHYtMzB2MTB2LTMwSDQ2NnoiLz48L3N2Zz4=',
                                        width=50,
                                        height=50,
                                        fit=ImageFit.COVER,
                                    ),
                                ],
                                expand=True
                            )
                        ],
                        alignment=MainAxisAlignment.START,
                        vertical_alignment=CrossAxisAlignment.END
                    ),
                    Container(
                        content=Column(
                            [
                                RegularLinkedInputs(
                                    page=page,
                                    inputs=[
                                        TextField(
                                            text_size=20,
                                            text_align=TextAlign.CENTER,
                                            bgcolor='#1a1e24',
                                            border_radius=13,
                                            width=80,
                                            height=50,
                                            content_padding=0,
                                            text_style=TextStyle(
                                                weight=FontWeight.W_600
                                            ),
                                            border_color=colors.TRANSPARENT,
                                            focused_border_color='#58a6ff',
                                            hint_text='****',
                                        ) for _ in range(4)
                                    ],
                                    place=Row(alignment=MainAxisAlignment.SPACE_BETWEEN,
                                              vertical_alignment=CrossAxisAlignment.CENTER, spacing=10),
                                    accept_length=4,
                                    accept_type=AcceptTypes.ONLY_NUMBER,
                                    on_change=on_change_input
                                ),
                                Row(
                                    [
                                        Row(
                                            [
                                                Text(
                                                    value='CVV2: ',
                                                    size=18,
                                                    color=colors.WHITE38,
                                                    weight=FontWeight.W_600,
                                                    text_align=TextAlign.RIGHT,
                                                ),
                                                RegularLinkedInputs(
                                                    page=page,
                                                    inputs=[
                                                        TextField(
                                                            text_size=20,
                                                            text_align=TextAlign.CENTER,
                                                            bgcolor='#1a1e24',
                                                            border_radius=13,
                                                            width=70,
                                                            height=50,
                                                            content_padding=0,
                                                            text_style=TextStyle(
                                                                weight=FontWeight.W_600
                                                            ),
                                                            border_color=colors.TRANSPARENT,
                                                            focused_border_color='#58a6ff',
                                                            hint_text='****',
                                                            password=True
                                                        )
                                                    ],
                                                    accept_length=4,
                                                    accept_type=AcceptTypes.ONLY_NUMBER,
                                                ),
                                            ]
                                        ),
                                        Row(
                                            [
                                                Text(
                                                    value='Expire date: ',
                                                    size=18,
                                                    color=colors.WHITE38,
                                                    weight=FontWeight.W_600,
                                                    text_align=TextAlign.RIGHT,
                                                ),
                                                RegularLinkedInputs(
                                                    page=page,
                                                    inputs=[
                                                        TextField(
                                                            text_size=20,
                                                            text_align=TextAlign.CENTER,
                                                            bgcolor='#1a1e24',
                                                            border_radius=13,
                                                            width=60,
                                                            height=50,
                                                            content_padding=0,
                                                            text_style=TextStyle(
                                                                weight=FontWeight.W_600
                                                            ),
                                                            border_color=colors.TRANSPARENT,
                                                            focused_border_color='#58a6ff',
                                                            hint_text='**',
                                                        )
                                                    ],
                                                    accept_length=2,
                                                    accept_type=AcceptTypes.ONLY_NUMBER,
                                                ),
                                                Text('/',size=20, color=colors.WHITE38,weight=FontWeight.W_600),
                                                RegularLinkedInputs(
                                                    page=page,
                                                    inputs=[
                                                        TextField(
                                                            text_size=20,
                                                            text_align=TextAlign.CENTER,
                                                            bgcolor='#1a1e24',
                                                            border_radius=13,
                                                            width=60,
                                                            height=50,
                                                            content_padding=0,
                                                            text_style=TextStyle(
                                                                weight=FontWeight.W_600
                                                            ),
                                                            border_color=colors.TRANSPARENT,
                                                            focused_border_color='#58a6ff',
                                                            hint_text='**',
                                                        )
                                                    ],
                                                    accept_length=2,
                                                    accept_type=AcceptTypes.ONLY_NUMBER,
                                                )
                                            ]
                                        )
                                    ],
                                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                                )
                            ],
                            spacing=20
                        ),
                        padding=Padding(left=30, right=30, top=10, bottom=10),
                    )

                ],
                spacing=20
            ),
            width=500,
            height=250,
            bgcolor='#21262d',
            border_radius=15,
            padding=15
        )
    )


app(target=main)
