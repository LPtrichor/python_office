import PyPDF2

# 定义变量来存储PDF文件的路径
pdf_file_path = './'
pdf_name = '罗-ER-Trends_and_gaps_in_photovoltaic_power_forecasting_with_machine_learning.pdf'
pdf_path = pdf_file_path + pdf_name
# 打开PDF文件
with open(pdf_path, 'rb') as file:
    # 创建PDF阅读器对象
    pdf_reader = PyPDF2.PdfReader(file)

    # 创建一个空字符串来存储所有文本内容
    all_text = ""

    # 获取PDF文件的页数
    num_pages = len(pdf_reader.pages)

    # 获取当前页
    # 逐页读取文本内容
    for page_number in range(num_pages):
        page = pdf_reader.pages[page_number]

        # 提取文本内容
        text = page.extract_text()

        # 将当前页的文本内容添加到总文本中
        all_text += text

pdf_name_txt = pdf_name.split('.')[0] + '.txt'
# 将所有文本内容写入文本文件
with open(pdf_name_txt, 'w', encoding='utf-8') as output_file:
    output_file.write(all_text)

print("PDF内容已成功写入output.txt文件。")


'''
import PyPDF2

# 打开PDF文件
with open('./FiLM.pdf', 'rb') as file:
    # 创建PDF阅读器对象
    pdf_reader = PyPDF2.PdfReader(file)

    # 获取PDF文件的页数
    num_pages = len(pdf_reader.pages)

    # 逐页读取文本内容
    for page_number in range(num_pages):
        # 获取当前页
        page = pdf_reader.pages[page_number]

        # 提取文本内容
        text = page.extract_text()
        
        # 打印文本内容
        print(f"Page {page_number+1}:")
        print(text)
'''


'''
# import PyPDF3/
from PyPDF2 import PdfMerger

# Open the PDF file and extract text from it
# with open("D:\Study\Y1下\光伏项目\大组汇报\第八次汇报\论文", "rb") as file:
with open("./FiLM.pdf", "rb") as file:
    # reader = PyPDF2.PdfMerger(file)
    reader = PdfMerger(file)

    # Extract text from each page and store it in a list
    text = []
    print(reader.pages)
    for page_num in range(reader.pages):
        text.append(reader.getPage(page_num).extractText())

text_content = "\n".join(text)
text_snippet = text_content[:2000]  # Displaying first 2000 characters as a snippet

text_snippet
'''

'''
# Search for sections that might discuss the experimental methods, like "experiment", "methodology", "evaluation", etc.
possible_sections = ["experiment", "methodology", "evaluation", "results", "dataset", "implementation details", "experimental setup"]

# Find the starting indices of these sections in the text
section_indices = {section: text_content.lower().find(section) for section in possible_sections}
valid_section_indices = {section: idx for section, idx in section_indices.items() if idx != -1}

valid_section_indices

# Continuing to extract more content from the "experiment" section
experiment_snippet_continued = experiment_section[2000:4000]  # Extracting the next 2000 characters

experiment_snippet_continued

'''
