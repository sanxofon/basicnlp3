Resolver: print "" => print("")
S\*:print ([^\n]+)$
R:print(\1)

Resolver: ur'' => r''
S\*:([ =\+\(\t])ur(["'])
R:\1r\2

Resolver: raw_input() => input()
S:raw_input
R:input

Resolver: En Python3 TODAS las cadenas son unicode, no hay str.decode y no es necesario codificar la salida.

Resolver: argparse.FileType('r') => argparse.FileType('r', encoding='UTF-8')
S:argparse.FileType('r')
R:argparse.FileType('r', encoding='UTF-8')

Resolver: xrange( => range(
S:xrange(
R:range(


CREAR ENTORNO 2.7
conda create -n py2 python=2.7
activate py2
deactivate py2