# newton_solar_system.py

from newton import SistemaNewton, Sol, Planeta

sistema = SistemaNewton(tamanho=256)

sol = Sol(sistema, posicao=(0, 0, 0), velocidade=(0, 0, 0))

planetas = (
    Planeta(sistema, massa=10, posicao=(110, 60, 0), velocidade=(2, 6, 0)),
    Planeta(sistema, massa=20, posicao=(130, 50, 0), velocidade=(1, 6, 0)),
    Planeta(sistema, massa=30, posicao=(150, 70, 0), velocidade=(2, 6, 0)),
    Planeta(sistema, massa=30, posicao=(150, 30, 0), velocidade=(2, 6, 0))
)

while True:
    sistema.calcular_interacoes_newtonianas()
    sistema.atualizar_todos()
    sistema.desenhar_todos()