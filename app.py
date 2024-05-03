#!/usr/bin/python

import re

def txt_to_html(input_file, output_file):
    # Abrir o arquivo de entrada para leitura
    with open(input_file, 'r') as f:
        # Ler o conteúdo do arquivo de texto
        text_content = f.readlines()

    # Abrir o arquivo de saída para escrita
    with open(output_file, 'w') as f:
        # Escrever o cabeçalho do arquivo HTML
        f.write("<!DOCTYPE html>\n<html>\n<head><style>pre{margin: 0 auto;}h1{margin: 0 auto;}</style>\n<title>Arquivo TXT convertido para HTML</title>\n</head>\n<body>\n")

        # Variável para acompanhar se estamos dentro ou fora de uma tag <b>
        inside_bold = False

        # Iterar sobre as linhas do arquivo de texto
        for line in text_content:
            # Verificar se a linha começa com #
            if line.startswith("#"):
                # Se começar com #, escrever dentro de uma tag <h1>
                f.write("<h1>")
                f.write(line.lstrip("#").strip())  # Remover o # e espaços em branco
                f.write("</h1>")
            else:
                # Caso contrário, substituir ** por <b> e </b>
                line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)

                # Escrever a linha normalmente dentro de uma tag <pre>
                f.write("<pre>")
                f.write(line)
                f.write("</pre>")

        # Escrever o final do arquivo HTML
        f.write("</body>\n</html>")

# Exemplo de uso
input_file = 'exemplo.txt'  # Nome do arquivo de texto de entrada
output_file = 'saida.html'  # Nome do arquivo HTML de saída

txt_to_html(input_file, output_file)
