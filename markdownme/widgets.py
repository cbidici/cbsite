from django.conf import settings
from django.forms import Media
from django.forms.widgets import Widget


class MarkdownWidget(Widget):
    template_name = 'markdownme/markdown.html'

    def __init__(self, rows=None, attrs=None):
        super().__init__(attrs)
        self.attrs['rows']=rows

    @property
    def media(self):
        return Media(
            css = {
                'all': (settings.STATIC_URL+'markdownme/css/github.min.css',
                        settings.STATIC_URL+'markdownme/css/markdownme.css',)
            },
            js = (settings.STATIC_URL+'markdownme/js/marked.min.js',
                  settings.STATIC_URL+'markdownme/js/highlight.min.js',
                  settings.STATIC_URL+'markdownme/js/purify.min.js',
                  settings.STATIC_URL+'markdownme/js/markdownme.js',)
        )
