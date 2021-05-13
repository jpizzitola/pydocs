# Python-Jinja .docx templater

Generates a new docx file based off a template using Python and Jinja
## Tech

Python libraries:

- [jinja2] - HTML enhanced for web apps!
- [docx] - Library used for creating word documents.
- [docxtpl] - Generate documents using word documents as jinja templates.


## Installation

Requires [python](https://www.python.org/downloads/release/python-390/)  to run.

Install the dependencies:

```sh
py -m pip install jinja2
py -m pip install docx
py -m pip install docxtpl
```

## Configuration

There are a few variables in config.py that tell the script where your template is and where to place the generated file. These can be overwritten from command line.

| Variable | About | Example | Override Flag|
| ------ | ------ | ------ | ------ |
| templateFile | Location of the template file Jinja will use to generate new document from | "./template/test_template.docx" | -t
| saveFile | Location and name the script will save the generated document(will append .docx to the filename) | "./generated-doc/generated_doc" | -s
| context | Location of json file with values the script will replace your template variables with. ('variable':"replacementvalue") | "./context.json" | -c


## Usage

Generate document from template(variables defined in config.py):

```sh
py main.py
```

Generate document from other template file:
```sh
py main.py -t "./template/other_test_template.docx"
```
Generate document to other save file:
```sh
py main.py -s "./generated-doc/other-save-file"
```
Generate document using other json file with defined value replacements:
```sh
py main.py -c "./othercontext.json"
```

## Template Expressions
```sh
{%....%}  block for statements
----------------------------------------------------
{{....}}  expressions used to print to template output
----------------------------------------------------
{#....#} block expressions comments that are not included in the template output
----------------------------------------------------
#....## block used as line statements
```

   [docxtpl]: <https://pypi.org/project/docxtpl/>
   [docx]: <https://pypi.org/project/docx/>
   [jinja2]: <https://pypi.org/project/Jinja2/>
   
