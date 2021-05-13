# pydocs
autodocs to work with jenkins job

used python 3.9.5
---------------------------------
{%....%}  block for statements

{{....}}  expressions used to print to template output

{#....#} block expressions comments that are not included in the template output

#....## block used as line statements

------------------------------------

https://blog.formpl.us/how-to-generate-word-documents-from-templates-using-python-cb039ea2c890
Generation example code used:
https://github.com/Vnessah/docx-gen

----------------------------------------------
                    EXAMPLE
----------------------------------------------
Needed for word document output

----------------------------------------------
py -m pip install jinja2
py -m pip install docx
py -m pip install docxtpl
----------------------------------------------
python-docx. This is a very powerful library used for creating word documents with basically all the elements you need — images, header, footer, page breaks, etc. While this library is great for creating docx files, it’s not very good at modifying them. We need this library in order to set the dimensions of any image we might add to the document, as you will see later on.

python-docx-template. This library is designed to generate documents using word documents as jinja templates. It makes slotting in custom values into a word document a lot easier. You can find more information in this article on library documentation here.