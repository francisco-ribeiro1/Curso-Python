# Importando o modulo
import argparse
# Criando um parser
parser = argparse.ArgumentParser()
# Criando um argumento pos
parser.add_argument("echo1")
parser.add_argument("echo2")
# separando os argumento
args = parser.parse_args()
# Processa o argumento 
print(args.echo1, args.echo2)