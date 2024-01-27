"""
如果是在中国大陆的话,使用下面的代码必须使用翻墙，而且还得是全局。翻墙一般用clash的tun模式比较适合。
这个脚本使用了Googletrans库，它可以读取一个文本文件中的内容，将其翻译为指定的目标语言（默认为中文'zh-CN'），
然后将翻译结果写入一个新的文本文件。

文件说明：
- `googletrans` 是一个Python库，用于使用Google Translate API 进行文本翻译。
- `read_txt(file_path)` 函数读取文本文件的内容。
- `translate_text(text, dest='zh-CN')` 函数使用Googletrans进行文本翻译。
- `main()` 函数是整个脚本的主要执行逻辑，定义了输入和输出文件路径，执行文件读取、翻译和写入的步骤。

请确保你的系统中已安装 `googletrans` 库，可以使用以下命令安装：
    pip install googletrans==4.0.0-rc1

使用方法：
1. 替换 `input_file_path` 变量为你的输入文件路径。
2. 替换 `output_file_path` 变量为你的输出文件路径。
3. 运行脚本，它将读取文本文件，翻译内容，并将翻译结果写入新的文本文件。
"""
from googletrans import Translator

def read_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def translate_text(text, dest='zh-CN'):
    translator = Translator()
    translated_text = translator.translate(text, dest=dest)
    return translated_text.text

def main():
    input_file_path = '新建文本文档.txt'
    output_file_path = 'translated_output.txt'
    
    # 读取txt文件内容
    text_to_translate = read_txt(input_file_path)

    # 使用Googletrans进行翻译
    translated_text = translate_text(text_to_translate)

    # 将翻译结果写入新的txt文件
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(translated_text)

if __name__ == "__main__":
    main()
