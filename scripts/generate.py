from docxtpl import DocxTemplate


def createWordDoc(temp, save, context):
    doc = DocxTemplate(temp)
    doc.render(context)
    doc.save(save)
