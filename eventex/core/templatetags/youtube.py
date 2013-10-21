from django.template import (Context, Template, Node, TemplateSyntaxError,
                             Variable, VariableDoesNotExist, Library)

TEMPLATE = '''
<object width="480" height="385">
    <param name="movie" value="http://www.youtube.com/v/{{ id }}" />
    <param name="allowFullScreen" value="true" />
    <param name="allowScriptAccess" value="always" />
    <embed scr="http://www.youtube.com/v/{{ id }}"
           type="application/x-shockwave-flash" allowscriptaccess="always"
           allowfullscreen="true" width="480" height="385">
    </embed>
</object>
'''

def do_youtube(parse, token):
    try:
        # split_contents() knows not to split quoted strings
        tag_name, id_ = token.split_contents()
    except ValueError:
        raise TemplateSyntaxError, "%r tag requer 1 argumento" % token.contents.split[0]
    return YoutubeNode(id_)


class YoutubeNode(Node):
    def __init__(self, id_):
        self.id = Variable(id_)

    def render(self, context):
        try:
            actual_id = self.id.resolve(context)
        except VariableDoesNotExist:
            actual_id = self.id

        t = Template(TEMPLATE)
        c = Context({'id': actual_id}, autoescape=context.autoescape)
        return t.render(c)

register = Library()
register.tag('youtube', do_youtube)
