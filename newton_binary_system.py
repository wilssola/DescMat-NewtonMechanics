# newton_binary_system.py

from newton import SistemaNewton, Sol, Planeta

sistema = SistemaNewton(256)

sois = (
    Sol(sistema, massa=7_500, posicao=(50, 50, 50), velocidade=(5, 0, 5)),
    Sol(sistema, massa=12_500, posicao=(-50, -50, 50), velocidade=(-4, 0, -4)),
)

planetas = (
    Planeta(
        sistema,
        10,
        posicao=(100, 100, 0),
        velocidade=(0, 5, 5),
    ),
    Planeta(
        sistema,
        20,
        posicao=(0, 0, 0),
        velocidade=(-10, 10, 0),
    ),
)

while True:
    sistema.calcular_interacoes_newtonianas()
    sistema.atualizar_todos()
    sistema.desenhar_todos()