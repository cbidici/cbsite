from django.db.models import TextField
from .widgets import MarkdownWidget


class MarkdownField(TextField):

    def formfield(self, **kwargs):
        kwargs['widget']=MarkdownWidget
        return super().formfield(**kwargs)
