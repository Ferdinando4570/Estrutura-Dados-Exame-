📄 Documentação do Sistema de Campeonato de Basquete
👥 Integrantes:
Bento Maximo De Farias – RA: 1988175

Pedro Brene De Oliveira – RA: 2000033

Fernando Cardamoni – RA: 1960266

🏀 Introdução
Este sistema em Python gerencia um campeonato de basquete, permitindo:

Criação de equipes

Cadastro e substituição de jogadores

Registro de partidas

Exibição de resultados e histórico de jogos

Atualização de estatísticas individuais

Visualização do desempenho dos jogadores

O sistema utiliza classes, listas, dicionários e deque para organizar e armazenar os dados, oferecendo uma interface de linha de comando para interação.

🧱 Estrutura Geral
O sistema é dividido em 4 componentes principais:

Classe Jogador – Representa cada jogador.

Classe Equipe – Armazena jogadores, histórico de partidas e estatísticas.

Classe Campeonato – Controla equipes, partidas e operações principais.

Função menu() – Interface textual interativa com o usuário.

🧑‍🏀 Classe Jogador
Atributos:
nome (str): Nome do jogador

posicao (str): Posição (ex: armador, pivô)

pontos (int): Total de pontos marcados

assistencias (int): Total de assistências

rebotes (int): Total de rebotes

Métodos:
__str__(): Formata a exibição do jogador

atualizar_estatisticas(pontos, assistencias, rebotes): Atualiza os dados acumulados do jogador

🏀 Classe Equipe
Atributos:
nome (str): Nome da equipe

jogadores (list): Lista de objetos Jogador

historico (deque): Últimos 10 resultados da equipe

Métodos:
adicionar_jogador(jogador): Adiciona jogador à equipe

listar_jogadores(): Mostra todos os jogadores da equipe

substituir_jogador(jogador_out, jogador_in, todas_equipes): Substitui um jogador por outro

adicionar_partida(resultado): Adiciona resultado ao histórico (limite de 10)

mostrar_historico(): Exibe o histórico de partidas da equipe

mostrar_estatisticas(): Mostra estatísticas de todos os jogadores

🏆 Classe Campeonato
Atributos:
nome (str): Nome do campeonato

equipes (dict): Mapeia nomes para objetos Equipe

partidas (list): Lista com o histórico de partidas

Métodos:
adicionar_equipe(nome): Cria nova equipe

adicionar_jogador(nome_equipe, nome_jogador, posicao): Adiciona jogador à equipe

registrar_partida(eq1, eq2, pontos_eq1, pontos_eq2): Registra uma nova partida

mostrar_resultados(): Lista todas as partidas realizadas

mostrar_info_equipe(nome_equipe): Exibe jogadores e histórico de uma equipe

substituir_jogador(equipe, jogador_out, jogador_in, posicao_in): Troca um jogador da equipe

atualizar_estatisticas_jogador(equipe, jogador, pontos, assist, reb): Atualiza os dados do jogador

mostrar_estatisticas_equipe(nome_equipe): Exibe o desempenho estatístico de todos os jogadores

🧑‍💻 Interface: Função menu()
Opções disponíveis:
Adicionar Equipe

Adicionar Jogador

Registrar Partida

Mostrar Resultados

Mostrar Informações da Equipe

Atualizar Estatísticas do Jogador

Substituir Jogador

Ver Estatísticas dos Jogadores

Sair

Validações:
Nomes duplicados não são permitidos

Impede que um jogador esteja em mais de uma equipe

Validações de pontuação e existência de equipes/jogadores

🧠 Estruturas de Dados Utilizadas
Tipo	Uso Principal	Função
Lista	jogadores, partidas	Armazenamento sequencial de dados
Dicionário	equipes	Acesso rápido aos objetos Equipe pelo nome
Deque	historico de equipe	Armazena os últimos 10 resultados com alta performance
Tupla	Itens da lista partidas	Estrutura imutável para registro de partidas

📌 Exemplos de Uso
✅ Adicionar uma equipe:
txt
Copiar
Editar
Opção: 1
Nome da equipe: Warriors
→ Equipe Warriors adicionada com sucesso.

✅ Adicionar um jogador:
txt
Copiar
Editar
Opção: 2
Equipe: Warriors
Nome do jogador: Curry
Posição: Armador
→ Jogador Curry adicionado à equipe Warriors.

✅ Registrar uma partida:
txt
Copiar
Editar
Opção: 3
Equipe 1: Warriors
Equipe 2: Bulls
Pontos Warriors: 110
Pontos Bulls: 99
→ Partida registrada com sucesso!

✅ Atualizar estatísticas:
txt
Copiar
Editar
Opção: 6
Equipe: Warriors
Jogador: Curry
Pontos: 35
Assistências: 7
Rebotes: 4
→ Estatísticas atualizadas.

✅ Substituir jogador:
txt
Copiar
Editar
Opção: 7
Equipe: Warriors
Jogador que sairá: Curry
Novo jogador: Poole
Posição do novo jogador: Armador
→ Jogador Curry foi substituído por Poole.

✅ Ver estatísticas dos jogadores:
txt
Copiar
Editar
Opção: 8
Equipe: Warriors
→ Poole (Armador) - Pontos: 0, Assistências: 0, Rebotes: 0 **
