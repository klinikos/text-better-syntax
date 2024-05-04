#!/usr/bin/python

import argparse
import re
import os


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

    # Se o nome do arquivo de saída não foi fornecido, gerar automaticamente
    if not output_file:
        # Obter o nome do arquivo de entrada sem a extensão
        output_file = os.path.splitext(input_file)[0] + ".html"

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

if __name__ == "__main__":
    # Configurar a análise de argumentos da linha de comando
    parser = argparse.ArgumentParser(description='Converte arquivo TXT para HTML')
    parser.add_argument('input_file', type=str, help='Nome do arquivo de entrada TXT')
    parser.add_argument('output_file', nargs='?', type=str, help='Nome do arquivo de saída HTML')

    # Obter os argumentos da linha de comando
    args = parser.parse_args()

    # Chamar a função para converter o arquivo TXT para HTML
    txt_to_html(args.input_file, args.output_file)