import unittest # import TestCase
from  models import Usuario
from models import AvaliacaoFisica


class test_usario(unittest.TestCase):
    def test_usuario(self): # criando alunos para teste
        self.usuario1 = Usuario('marcos','marcos@gmail.com')
        self.usuario2 = Usuario('victor','victor@gmail.com')



class TestAvalicaoFisica(unittest.TestCase):
    def test_avaliacaofisica(self): # As entradas não podem ser negativas
        self.assertFalse(AvaliacaoFisica.peso(40))
        self.assertFalse(AvaliacaoFisica.altura(160))
        self.assertFalse(AvaliacaoFisica.imc(30))
        self.assertFalse(AvaliacaoFisica.braco_d(30))
        self.assertFalse(AvaliacaoFisica.perna_e(45))
        self.assertFalse(AvaliacaoFisica.cintura(50),)

# chamar todos os tests 
if __name__ == '__main__':
    unittest.main()