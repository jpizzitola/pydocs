# pydocs
autodocs to work with jenkins job

used python 3.9.5
---------------------------------
{%....%}  block for statements

{{....}}  expressions used to print to template output

{#....#} block expressions comments that are not included in the template output

#....## block used as line statements

------------------------------------
py -m pip install jinja2
py -m pip install jinja_markdown
------------------------------------
>>> from jinja2 import Template
>>> from jinja_markdown import MarkdownExtension


https://blog.formpl.us/how-to-generate-word-documents-from-templates-using-python-cb039ea2c890
----------------------------------------------
EXAMPLE
----------------------------------------------
>>> t = Template("Hello {{ something }}!")
>>> t.render(something="World")
u'Hello World!'

>>> t = Template("My favorite numbers: {% for n in range(1,10) %}{{n}} " "{% endfor %}")
>>> t.render()
u'My favorite numbers: 1 2 3 4 5 6 7 8 9 '