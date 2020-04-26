from django.forms.widgets import Widget


class MarkdownWidget(Widget):
    template_name = 'markdownme/markdown.html'

