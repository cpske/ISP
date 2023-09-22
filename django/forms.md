---
title: Forms in Django
---

Django has two kinds of Forms:

* django.forms.Form - generic form. You create a subclass and define fields for the values you want in the form.
* django.forms.models.ModelForm - form that wraps a Model.

## What can forms do?

* Render as an HTML form containining input fields.
* Validate input values, both on client-side and server-side.
  - avoids the need to write the code yourself
  - you should still be careful that the server-side validations are thorough
* On server, a form can return the data from form fields.
* A ModelForm can directly save form data to a Model object in the database, using `form.save()`.

### Don't Rely on Client-side Form Validation

A malicious user can send form data directly to the server,
without going through your form.  Or, he can save the HTML source of form page and remove the validation checks.

A general rule in web apps is never trust any data received
from a client.  The server-side app should validate everything.  Client-side validation is for the benefit of the user, so he doesn't waste time submitting invalid data.

## Example of a ModelForm

For the Todo example (`Todo` is a model with a date, text, and boolean done field),
```python
from django import forms

class TodoForm(forms.models.ModelForm):

    class Meta:
        model = Todo
        fields = ['date', 'text', 'done']
        # custom labels for input fields
        labels = {
            'date': 'Date (dd/mm/yyyy)',
            'text': 'Description',
            'done': 'Done?',
        }

    def clean_date(self):
        "Verify the date.
         See: https://docs.djangoproject.com/en/2.1/ref/forms/validation/
        """
        date = self.cleaned_data['date']
        today = datetime.date.today()
        if date > today:
           raise forms.ValidationError("Date cannot be in the future",code='invalid')
        

    def clean(self):
       """Perform any validation not specific to a particular field.
           Be sure to call the superclass method first.
           See: https://docs.djangoproject.com/en/2.1/ref/forms/validation/
           Local: file:///usr/local/doc/django/uguide/ref/forms/validation.html
        """
        cleaned = super().clean()
        text = cleaned.get('text')
        # verify the text description
        return cleaned
```

A ModelForm will use any validation rules that are defined in the Model class,
so you don't need to duplicate them.

## Validating a ModelForm

Call `form.is_valid()`.  Returns True or False and also sets the `errors` dict.


```python
form = TodoForm(data={'text': ''})
if form.isValid():
    print("data is ok")
else:
    # look for error in 'text' field
    print( form.errors['text'] )
```

Error messages are in the `form.errors` dictionary, as shown above.

If you want to access the errors in a *template* then use:
{% raw %}
```
{% if form.errors %}
   {{ form.text.errors }}
{% endif %}
```
{% endraw %}
