from validate_docbr import CPF # pacote python para validação de doc brasileiros.

import re # esta biblioteca trabalha com expressões regulares

def cpf_valido(numero_do_cpf):
    cpf = CPF()
    return cpf.validate(numero_do_cpf)

def name_valido(name):
    return all(c.isalpha() or c.isspace() for c in name)


def rg_valido(rg):
    return len(rg) == 9


def telefone_valido(telefone):
    """Verifica se o celular é valido (11 91234-1234)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, telefone)
    return resposta
