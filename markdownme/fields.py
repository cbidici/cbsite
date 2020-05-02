from django.db.models import TextField
from django.forms import fields
from .widgets import MarkdownWidget


class MarkdownField(TextField):

    def __init__(self, rows=64, **kwargs):
        super().__init__(**kwargs)
        self.rows = rows

    def formfield(self, **kwargs):
        kwargs['widget'] = MarkdownWidget(rows=self.rows)
        return super().formfield(**kwargs)
