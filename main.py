import sys
sys.path.insert(1, './scripts/')
import generate
import filename
import config
import argparse
import json

templateFile = config.templateFile
saveFile = config.saveFile
contextFile = config.contextFile


with open(contextFile) as json_file:
    context = json.load(json_file)

# Initiate the parser with a description
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--savefile", help="Path to save new file(do not add extension)")
parser.add_argument("-t", "--templatefile", help="Path to template document")
parser.add_argument("-c", "--context", help="Context string")
args = parser.parse_args()

if args.savefile:
    saveFile = args.savefile

if args.templatefile:
    templateFile = args.templatefile

if args.context:
    with open(args.context) as json_file:
        context = json.load(json_file)
  


def replace():    
    try:
        gen = filename.generateDocName(saveFile)
        generate.createWordDoc(templateFile, gen, context)
    except Exception as e:
        print(e)
    else:
      print("Document generated at: "+gen+ " Using template: "+templateFile)




print("Generating file from template: "+templateFile)
print("Saving file as: "+saveFile)
print("context file: "+contextFile)

replace()