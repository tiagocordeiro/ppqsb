rotas = []
# rotas = {}


def rota(url, *args, **kwargs):
    def decorador(func):
        rotas.append((url, func(), args, kwargs))
        

    return decorador
#
# def rota(url, *args, **kwargs):
#     def decorador(func):
#         rotas = url, args, kwargs
#         func(rota)
#
#     return decorador

def rotear(url, *args, **kwargs):
    # for url in rotas:
    #     print(rotas)
    #
    # print(url, args, kwargs)
    # return url, args, kwargs
    return url, args


@rota('/')
def home(*args):
    def home_rota():
        return 'home executada'
    return home_rota()


@rota('/carro')
def carro(*args):
    def carro_rota():
        return 'rota do carro'
    return carro_rota()


@rota('/usuario')
def usuario(*args, **kwargs):
    return f'salvando {args} {kwargs}'


class RotaInexistente(Exception):
    def erro(self):
        raise TypeError


if __name__ == '__main__':
    print(rotas)
    principal = rotear('/')
    print(principal)

    meucarro = rotear('/carro', 'corsa', 88)
    print(meucarro)

    pessoa = rotear('/usuario', 'Tiago')
    print(pessoa)

    erro_url = rotear('/inexistente')
    print(erro_url)
