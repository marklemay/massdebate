#TODO: rename this file!

# basicly https://docs.djangoproject.com/en/1.6/howto/custom-template-tags/
from django import template
from debate.models import Statement

register = template.Library()

@register.inclusion_tag('debate/statement_snippit.html')
def link(statement):
    return {'this_statement': statement}
