class Commit:
    def __init__(self,id, mensagem, autor, pai):
        self.id = id
        self.mensagem = mensagem
        self.autor = autor
        self.pai = pai 
    def historico(self):
        atual = self
        
        while atual:
            print(atual.mensagem)
            atual = atual.pai

class Repositorio:
    def __init__(self, autor):
        self.autor = autor
        self.ultimo_commit = None
        self.contador = 0
    def commitar(self, mensagem):
        self.contador = self.contador + 1
        novo_commit = Commit(self.contador, mensagem, self.autor, self.ultimo_commit)
        self.ultimo_commit = novo_commit
    def log(self):
        if self.ultimo_commit:
           self.ultimo_commit.historico()
    def total_de_commits(self):
        return self.contador


repo = Repositorio("Vinicius amaro - 6326015")

repo.commitar("Criei o repositorio")
repo.commitar("Criei a classe Commit")
repo.commitar("Criei o historico")

print("Historico:")
repo.log()

print("Total de commits:", repo.total_de_commits())