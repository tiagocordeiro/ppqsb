from functools import partial
rotas = {}


def rota(url, *args, **kwargs):
    def decorador(func):
        rotas[url] = func
        return func(), args, kwargs

    return decorador


def rotear(url, *args, **kwargs):
    if url in rotas:
        return partial(rotas[url], args, kwargs)
        # return url, rotas[url], args, kwargs
    else:
        raise RotaInexistente(f'Rota inexistente: {url}')
    # return rotas[url]()
    # return rota()
    # url_path = [item for item in rotas if item[0] == url]
    # try:
    #     url == url_path
    #     return url_path[0][1]()
    # except:
    #     raise RotaInexistente(f'Rota inexistente: {url}')

    # return f'Imprimindo {url_path[0][0]}'


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
    print(rotas)    #imprimindo rotas para conferencia

    principal = rotear('/')
    print(principal)


    meucarro = rotear('/carro', 'corsa', 88)
    print(meucarro)

    pessoa = rotear('/usuario', 'Tiago')
    print(pessoa)

    # erro_url = rotear('/inexistente')
    # print(erro_url)
