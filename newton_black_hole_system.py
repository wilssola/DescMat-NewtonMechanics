# newton_black_hole_system.py

from newton import SistemaNewton, BuracoNegro, Sol, Planeta

sistema = SistemaNewton(tamanho=256)

buraco_negro = BuracoNegro(sistema, posicao=(0, 0, 0), velocidade=(0, 0, 0))

planetas = (
    Planeta(sistema, massa=10, posicao=(1000, 30, 0), velocidade=(1, 2, 0)),
    Planeta(sistema, massa=20, posicao=(1100, 40, 0), velocidade=(2, 3, 0)),
    Planeta(sistema, massa=30, posicao=(1200, 50, 0), velocidade=(3, 4, 0))
)

while True:
    sistema.calcular_interacoes_newtonianas()
    sistema.atualizar_todos()
    sistema.desenhar_todos()