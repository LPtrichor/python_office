from pylatex import Document, Section, Subsection, Command

# 创建LaTeX文档对象
doc = Document('output', documentclass='article')

# 添加标题和作者
doc.preamble.append(Command('title', 'My First LaTeX Document'))
doc.preamble.append(Command('author', 'Your Name'))
doc.preamble.append(Command('date', 'September 2023'))

# 创建文档内容
with doc.create(Section('Introduction')):
    doc.append('This is the introduction section.')

with doc.create(Section('Methods')):
    with doc.create(Subsection('Method 1')):
        doc.append('Description of method 1.')

    with doc.create(Subsection('Method 2')):
        doc.append('Description of method 2.')

# 保存为PDF文件
doc.generate_pdf()
print("PDF文件已成功生成。")