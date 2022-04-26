#import pytest # import TestCase
import pytest
from models import AvaliacaoFisica
from models import Usuario
#from softfit.Administrador.models import AvaliacaoFisica


def test_nome_usuario():
    assert Usuario.nome('cariani') == 'cariani'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        Usuario.nome(9)




def test_avaliacao_fisica():
    peso_t = AvaliacaoFisica.peso(80)
    altura_t = AvaliacaoFisica.altura(178)
    imc_t = AvaliacaoFisica.imc(12)
    braco_d_t = AvaliacaoFisica.braco_d(39)
    perna_e_t = AvaliacaoFisica.perna_e(50)
    cintura_t = AvaliacaoFisica.cintura(70)
    comentario_af_t = AvaliacaoFisica.comentario_af("possui assimetria")

    