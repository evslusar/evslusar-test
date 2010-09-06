from django import template
from django.core import urlresolvers


class EditLinkNode(template.Node):
    def __init__(self, object_name):
        self.object_var = template.Variable(object_name)

    def reverse_edit_link(self, obj):
        obj_id = obj.id
        app_label = obj._meta.app_label
        module_name = obj._meta.module_name
        return urlresolvers.reverse('admin:%s_%s_change' % (app_label, module_name), args=(obj_id,))

    def render(self, context):
        obj = self.object_var.resolve(context)
        link = self.reverse_edit_link(obj)
        return '<a href="%s">Edit %s</a>' % (link, obj._meta.module_name)


def compile_edit_link_tag(parser, token):
    try:
        tag_name, object_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "edit_link tag requires a single argument"
    return EditLinkNode(object_name)

register = template.Library()
register.tag('edit_link', compile_edit_link_tag)
