from functools import partial
import functools

rotas = {}


def rota(url, *args, **kwargs):
    @functools.wraps(rota)
    def decorador(func):
        rotas[url] = func
        return func

    return decorador


def rotear(url, *args, **kwargs):
    print(kwargs)
    if url in rotas:
        if not args:
            return rotas[url]()
        else:
            nome = args[0]
            if len(args) == 1:
                return rotas[url] (nome)
            elif len(args) == 2:
                ano = args[1]
                return rotas[url] (nome, ano)
            else:
                pass
    else:
        raise RotaInexistente(f'Rota inexistente: {url}')


@rota('/')
def home():
    def home_rota():
        return 'home executada'

    return home_rota


@rota('/carro')
def carro():
    def carro_rota(nome, ano):
        return f'{nome} ano {ano}'

    return carro_rota


@rota('/usuario')
def usuario():
    def usuario_rota(nome):
        return f'salvando {nome}'

    return usuario_rota


class RotaInexistente(Exception):
    def erro(self):
        raise TypeError


if __name__ == '__main__':
    # print(rotas)    #imprimindo rotas para conferencia

    principal = rotear('/')
    print(principal)
    print(principal.__name__)


    meucarro = rotear('/carro', 'corsa', 88)
    print(meucarro)

    pessoa = rotear('/usuario', 'Tiago')
    print(pessoa)

    # erro_url = rotear('/inexistente')
    # print(erro_url)
