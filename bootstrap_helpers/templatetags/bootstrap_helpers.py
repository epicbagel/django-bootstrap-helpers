#coding: utf8
from random import randint

from django import template
register = template.Library()

def get_field_id(field):
	widget = field.field.widget
	return widget.id_for_label(widget.attrs.get('id') or field.auto_id)

def get_field_name(field):
	widget = field.field.widget
	return widget.attrs.get('name')

@register.filter
def placeholder(field, text = None):
   field.field.widget.attrs.update({
	   'placeholder' : text or field.label,
   })
   return field
   
@register.filter
def required(field, required):
	if required:
		field.field.widget.attrs.update({'required' : True})
	return field

@register.filter
def css(field, text):
	field.field.widget.attrs.update({
		'class' : text,
	})
	return field

# Displays a form field and label
@register.inclusion_tag('bootstrap/field.html')
def render_field(field, prepend = None, label_text = None, url = None, url_text = None, toggle_text = None):
	widget = field.field.widget
	context = locals()
	context.update({
		'name' : field.field.widget.attrs.get('name'),
		'field_type' : field.field.widget.__class__.__name__.lower(),
		'for_id' : widget.id_for_label(widget.attrs.get('id') or field.auto_id),
	})
	return context

# Displays a form field and label
@register.inclusion_tag('bootstrap/messages.html')
def render_messages(messages):
	return locals()



