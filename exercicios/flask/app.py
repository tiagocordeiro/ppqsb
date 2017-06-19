rotas = {}


def rota(url):
    def decorador(func):
        rotas[url] = func
        return func

    return decorador


def rotear(url, *args, **kwargs):
    if url in rotas:
        return rotas[url](*args, **kwargs)
    else:
        raise RotaInexistente(f'Rota inexistente: {url}')


@rota('/')
def home():
    def home_rota():
        return 'home executada'

    return home_rota


@rota('/carro')
def carro():
    def carro_rota(*args, **kwargs):
        if 'nome' and 'ano' in kwargs:
            return f'{kwargs["nome"]} ano {kwargs["ano"]}'
        if args is not None:
            nome = args[0]
            ano = args[1]
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
    # print(principal.__name__)
    #
    outrocarro = rotear('/carro', 'Fusca', 79)
    print(outrocarro)

    carronomeado = rotear('/carro', nome='Monza', ano=84)
    print(carronomeado)

    pessoa = rotear('/usuario', 'Tiago')
    print(pessoa)

    # erro_url = rotear('/inexistente')
    # print(erro_url)
