Django has two kinds of Forms:

* django.forms.Form - generic form. You define field in a Form subclass.
* django.forms.models.ModelForm - form that wraps a Model.

## What can forms do?

* Render as HTML containining input fields.
* Validate input values, both on client-side and server-side.
* On server, can extract data from form fields.
* A ModelForm can directly save Model object to database (form.save())



### Example of a ModelForm

For the Todo example,
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

### Validating a ModelForm

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
