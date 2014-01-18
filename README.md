===
Django template tag library for Bootstrap 3
===

Simple, small library for handling the display of Bootstrap 3 field and messages. 

Installation
------------
1. Install using pip:

        pip install -e git://github.com/epicbagel/django-bootstrap-helpers.git#egg=django-bootstrap-helpers-dev

2. Add to INSTALLED_APPS:

        'bootstrap_helpers',

Use in templates
----------------

    {% load bootstrap_helpers %}
    
    {# Rending a form field #}
    <form action="/url/to/submit/" method="post">
        {% csrf_token %}
        {% for field in form %}
          {% render_field form.field %}
        {% endfor %}
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>

    {# Rending the message stack from django.contrib.messages #}
    <div class="row">
      <div class="md-col-12">
        {% render_messages %}
      </div>
    </div>
    
