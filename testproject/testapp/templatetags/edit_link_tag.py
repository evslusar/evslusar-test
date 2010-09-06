from django import template
from django.core import urlresolvers

class VariableIsNotModelInstance(Exception):
    pass

def object_name(obj):
    try:
        return obj._meta.module_name
    except AttributeError:
        raise VariableIsNotModelInstance

def reverse_edit_link(obj):
    obj_name = object_name(obj)
    try:
        obj_id = obj.id
        app_label = obj._meta.app_label
    except AttributeError:
        raise VariableIsNotModelInstance
    return urlresolvers.reverse('admin:%s_%s_change' % (app_label, obj_name), args=(obj_id,))

class EditLinkNode(template.Node):
    def __init__(self, object_name):
        self.object_var = template.Variable(object_name)

    def render(self, context):
        obj = self.object_var.resolve(context)
        link = reverse_edit_link(obj)
        return '<a href="%s">Edit %s "%s"</a>' % (link, object_name(obj), unicode(obj))


def compile_edit_link_tag(parser, token):
    try:
        tag_name, object_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "edit_link tag requires a single argument"
    return EditLinkNode(object_name)

register = template.Library()
register.tag('edit_link', compile_edit_link_tag)
