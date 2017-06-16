rotas = []


def rota(url, *args, **kwargs):
    def decorador(func):
        rotas.append((url, func()))

    return decorador


def rotear(url, *args, **kwargs):
    url_path = [item for item in rotas if item[0] == url]
    try:
        url_path == url
        return url_path[0][1]()
    except:
        RotaInexistente('Rota inexistente')

    # return f'Imprimindo {url_path[0][0]}'


@rota('/')
def home():
    def home_rota():
        return 'home executada'
    return home_rota

@rota('/carro')
def carro(*args, **kwargs):
    def carro_rota():
        return 'Rota do carro'
    return carro_rota


@rota('/usuario')
def usuario(*args, **kwargs):
    def usuario_rota():
        return 'Rota de usuario'
    return usuario_rota


class RotaInexistente(Exception):
    def erro(self):
        raise TypeError


if __name__ == '__main__':
    # print(rotas)

    principal = rotear('/')
    print(principal)

    meucarro = rotear('/carro', 'corsa', 88)
    print(meucarro)

    pessoa = rotear('/usuario', 'Tiago')
    print(pessoa)

    # erro_url = rotear('/inexistente')
    # print(erro_url)
