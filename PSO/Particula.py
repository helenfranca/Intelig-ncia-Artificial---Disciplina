class Particula:
    def __init__(self, posicao, velocidade, fit, pBest):
        self.posicao = posicao
        self.velocidade = velocidade
        self.fit = fit
        self.pBest = pBest

    def get_fitness(self):
        return self.fit
