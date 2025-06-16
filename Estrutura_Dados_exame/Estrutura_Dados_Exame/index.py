from collections import deque

class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao
        self.pontos = 0
        self.assistencias = 0
        self.rebotes = 0

    def __str__(self):
        return f"{self.nome} ({self.posicao}) - Pts: {self.pontos}, Ast: {self.assistencias}, Reb: {self.rebotes}"

    def atualizar_estatisticas(self, pontos, assistencias, rebotes):
        self.pontos += pontos
        self.assistencias += assistencias
        self.rebotes += rebotes


class Equipe:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []
        self.historico = deque(maxlen=10)

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)
        print(f"Jogador {jogador.nome} adicionado à equipe {self.nome}.")

    def listar_jogadores(self):
        if not self.jogadores:
            print(f"Nenhum jogador na equipe {self.nome}.")
            return
        print(f"Jogadores da equipe {self.nome}:")
        for j in self.jogadores:
            print(f" - {j}")

    def substituir_jogador(self, jogador_out, jogador_in, todas_equipes):
        for equipe in todas_equipes.values():
            if jogador_in in equipe.jogadores:
                print(f"Erro: O jogador {jogador_in.nome} já está na equipe {equipe.nome}.")
                return

        for i, jogador in enumerate(self.jogadores):
            if jogador.nome == jogador_out:
                self.jogadores[i] = jogador_in
                print(f"{jogador_out} foi substituído por {jogador_in.nome}.")
                return
        print(f"Jogador {jogador_out} não encontrado na equipe {self.nome}.")

    def adicionar_partida(self, resultado):
        self.historico.append(resultado)

    def mostrar_historico(self):
        if not self.historico:
            print(f"Sem histórico para a equipe {self.nome}.")
            return
        print(f"Últimas partidas da equipe {self.nome}:")
        for r in self.historico:
            print(f" - {r}")

    def mostrar_estatisticas(self):
        if not self.jogadores:
            print(f"Nenhum jogador na equipe {self.nome}.")
            return
        print(f"Estatísticas dos jogadores da equipe {self.nome}:")
        for jogador in self.jogadores:
            print(jogador)


class Campeonato:
    def __init__(self, nome):
        self.nome = nome
        self.equipes = {}
        self.partidas = []

    def adicionar_equipe(self, nome):
        if nome in self.equipes:
            print(f"Equipe {nome} já existe.")
            return
        self.equipes[nome] = Equipe(nome)
        print(f"Equipe {nome} adicionada.")

    def adicionar_jogador(self, nome_equipe, nome_jogador, posicao):
        equipe = self.equipes.get(nome_equipe)
        if not equipe:
            print(f"Equipe {nome_equipe} não encontrada.")
            return
        jogador = Jogador(nome_jogador, posicao)
        equipe.adicionar_jogador(jogador)

    def substituir_jogador(self, nome_equipe, jogador_out, jogador_in_nome, posicao_in):
        equipe = self.equipes.get(nome_equipe)
        if not equipe:
            print(f"Equipe {nome_equipe} não encontrada.")
            return
        novo_jogador = Jogador(jogador_in_nome, posicao_in)
        equipe.substituir_jogador(jogador_out, novo_jogador, self.equipes)

    def registrar_partida(self, eq1, eq2, pontos_eq1, pontos_eq2):
        e1 = self.equipes.get(eq1)
        e2 = self.equipes.get(eq2)
        if not e1 or not e2:
            print("Uma das equipes não existe.")
            return

        self.partidas.append((eq1, pontos_eq1, pontos_eq2, eq2))

        def resultado(pontos_a, pontos_b, adversario):
            if pontos_a > pontos_b:
                return f"Venceu {pontos_a} x {pontos_b} contra {adversario}"
            elif pontos_a < pontos_b:
                return f"Perdeu {pontos_a} x {pontos_b} contra {adversario}"
            else:
                return f"Empatou {pontos_a} x {pontos_b} contra {adversario}"

        e1.adicionar_partida(resultado(pontos_eq1, pontos_eq2, eq2))
        e2.adicionar_partida(resultado(pontos_eq2, pontos_eq1, eq1))

        print(f"Partida registrada: {eq1} {pontos_eq1} x {pontos_eq2} {eq2}")

    def mostrar_resultados(self):
        if not self.partidas:
            print("Nenhuma partida registrada.")
            return
        print("Resultados:")
        for eq1, p1, p2, eq2 in self.partidas:
            print(f"{eq1} {p1} x {p2} {eq2}")

    def mostrar_info_equipe(self, nome_equipe):
        equipe = self.equipes.get(nome_equipe)
        if not equipe:
            print("Equipe não encontrada.")
            return
        equipe.listar_jogadores()
        equipe.mostrar_historico()

    def atualizar_estatisticas_jogador(self, equipe_nome, jogador_nome, pontos, assistencias, rebotes):
        equipe = self.equipes.get(equipe_nome)
        if not equipe:
            print(f"Equipe {equipe_nome} não encontrada.")
            return
        for jogador in equipe.jogadores:
            if jogador.nome == jogador_nome:
                jogador.atualizar_estatisticas(pontos, assistencias, rebotes)
                print(f"Estatísticas de {jogador_nome} atualizadas.")
                return
        print(f"Jogador {jogador_nome} não encontrado na equipe {equipe_nome}.")

    def mostrar_estatisticas_equipe(self, nome_equipe):
        equipe = self.equipes.get(nome_equipe)
        if not equipe:
            print(f"Equipe {nome_equipe} não encontrada.")
            return
        equipe.mostrar_estatisticas()


def menu():
    campe = Campeonato("Campeonato de Basquete")

    while True:
        print("\n Menu do Campeonato ")
        print("1 - Adicionar Equipe")
        print("2 - Adicionar Jogador")
        print("3 - Registrar Partida")
        print("4 - Mostrar Resultados")
        print("5 - Mostrar Info da Equipe")
        print("6 - Atualizar Estatísticas do Jogador")
        print("7 - Substituir Jogador")
        print("8 - Ver Estatísticas dos Jogadores")
        print("9 - Sair")

        op = input("Opção: ").strip()

        if op == '1':
            nome = input("Nome da equipe: ").strip()
            if not nome:
                print("Nome inválido. Tente novamente.")
                continue
            campe.adicionar_equipe(nome)

        elif op == '2':
            equipe = input("Equipe: ").strip()
            if not equipe:
                print("Nome da equipe inválido.")
                continue

            nome_jog = input("Nome do jogador: ").strip()
            if not nome_jog:
                print("Nome do jogador inválido.")
                continue

            pos = input("Posição: ").strip()
            if not pos:
                print("Posição inválida.")
                continue

            campe.adicionar_jogador(equipe, nome_jog, pos)

        elif op == '3':
            eq1 = input("Equipe 1: ").strip()
            eq2 = input("Equipe 2: ").strip()
            try:
                g1 = int(input(f"Pontos {eq1}: "))
                g2 = int(input(f"Pontos {eq2}: "))
            except ValueError:
                print("Pontos inválidos.")
                continue
            campe.registrar_partida(eq1, eq2, g1, g2)

        elif op == '4':
            campe.mostrar_resultados()

        elif op == '5':
            nome = input("Nome da equipe: ").strip()
            campe.mostrar_info_equipe(nome)

        elif op == '6':
            equipe = input("Nome da equipe: ").strip()
            jogador = input("Nome do jogador: ").strip()
            try:
                pontos = int(input("Pontos: "))
                ast = int(input("Assistências: "))
                reb = int(input("Rebotes: "))
            except ValueError:
                print("Valores inválidos.")
                continue
            campe.atualizar_estatisticas_jogador(equipe, jogador, pontos, ast, reb)

        elif op == '7':
            equipe = input("Equipe: ").strip()
            if not equipe:
                print("Nome da equipe inválido.")
                continue

            jogador_out = input("Jogador a ser substituído: ").strip()
            if not jogador_out:
                print("Nome do jogador a ser substituído inválido.")
                continue

            jogador_in = input("Novo jogador: ").strip()
            if not jogador_in:
                print("Nome do novo jogador inválido.")
                continue

            pos = input("Posição do novo jogador: ").strip()
            if not pos:
                print("Posição inválida.")
                continue

            campe.substituir_jogador(equipe, jogador_out, jogador_in, pos)

        elif op == '8':
            equipe = input("Nome da equipe: ").strip()
            campe.mostrar_estatisticas_equipe(equipe)

        elif op == '9':
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
