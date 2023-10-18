from django.forms import (
    Form, CharField, BooleanField, DateTimeField
)


class TodoForm(Form):
    title = CharField(
        max_length=121,
        min_length=3,
        required=True
    )
    active = BooleanField(
        required=False,
    )
    finished = BooleanField(
        required=False,
    )
    owner = CharField(
        max_length=30,
        min_length=3,
        required=False,
    )
    create_date = DateTimeField(

    )
    is_deleted = BooleanField(
        required=False
    )
