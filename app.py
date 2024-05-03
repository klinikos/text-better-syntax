#!/usr/bin/python

import re

template = """<!DOCTYPE html>
<html>
    <head>
    <style>
        pre{margin: 0 auto;}
        h1{margin: 0 auto;}
    </style>
    <title>Arquivo TXT convertido para HTML</title>
    </head>
<body>"""

def txt_to_html(input_file, output_file):
    # Abrir o arquivo de entrada para leitura
    with open(input_file, 'r') as f:
        # Ler o conteúdo do arquivo de texto
        text_content = f.readlines()

    # Abrir o arquivo de saída para escrita
    with open(output_file, 'w') as f:
        # Escrever o cabeçalho do arquivo HTML
        f.write(template)

        # Variável para acompanhar se estamos dentro ou fora de uma tag <b>
        inside_bold = False

        # Iterar sobre as linhas do arquivo de texto
        for line in text_content:
            # Verificar se a linha começa com #
            if line.startswith("##"):
                # Se começar com #, escrever dentro de uma tag <h1>
                f.write("\n\n<h2>")
                f.write(line.lstrip("#").strip())  # Remover o # e espaços em branco
                f.write("</h2>\n")
            elif line.startswith("#"):
                f.write("\n\n<h1>")
                f.write(line.lstrip("#").strip())
                f.write("</h1>\n")
            else:
                # Caso contrário, substituir ** por <b> e </b>
                line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)

                # Escrever a linha normalmente dentro de uma tag <pre>
                f.write("<pre>")
                f.write(line.rstrip())
                f.write("</pre>\n")

        # Escrever o final do arquivo HTML
        f.write("\n</body>\n</html>")

# Exemplo de uso
input_file = 'exemplo.txt'  # Nome do arquivo de texto de entrada
output_file = 'saida.html'  # Nome do arquivo HTML de saída

txt_to_html(input_file, output_file)
