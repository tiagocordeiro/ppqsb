_roteador = {}


def rota(url):
    def decorador(func):
        _roteador[url] = func
        return func

    return decorador


def rotear(url, nome=None, ano: int = 0, *args, **kwargs):
    if url == '/':
        return 'home executada'
    elif url == '/carro':
        if nome is None:
            raise TypeError('Nome não pode ser vazio')
        else:
            return f'{nome} ano {ano}'
    elif url == '/usuario':
        if nome is None:
            raise TypeError('Usuário não pode ser vazio')
        else:
            return f'salvando {nome}'
    else:
        # print(f'Rota inexistente: {url}')
        raise RotaInexistente(f'Rota inexistente: {url}')


class RotaInexistente(Exception):
    def erro(self):
        raise TypeError


if __name__ == '__main__':
    carro = rotear('/carro', 'Fusca', 88)
    print(carro)
    pessoa = rotear('/usuario', 'Tiago')
    print(pessoa)
    carronomeado = rotear('/carro', ano=2000, nome='Gol')
    print(carronomeado)
    # erro = rotear('/asdafsdfds')
    # print(erro)
    # carroerro = rotear('/carro')
    usuario_sem_nome = rotear('/usuario', 'foo')
    print(usuario_sem_nome)