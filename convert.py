import docx

doc = docx.Document('Untrust attribution Debug.docx')

with open('Untrust attribution Debug.md', 'w', encoding='utf-8') as f:
    for para in doc.paragraphs:
        text = ''
        for run in para.runs:
            t = run.text
            if run.bold:
                t = '**' + t + '**'
            if run.italic:
                t = '*' + t + '*'
            text += t
        style_name = para.style.name if para.style else ''
        if 'Heading 1' in style_name:
            f.write('# ' + text + '\n\n')
        elif 'Heading 2' in style_name:
            f.write('## ' + text + '\n\n')
        elif 'Heading 3' in style_name:
            f.write('### ' + text + '\n\n')
        elif 'List' in style_name:
            f.write('- ' + text + '\n')
        else:
            f.write(text + '\n\n')