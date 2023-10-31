from PIL import Image

from PIL import Image
from io import BytesIO

def validar_imagem(imagem):
    try:
        img = Image.open(imagem)

        formato_valido = img.format in ['JPEG', 'PNG']
        largura, altura = img.size
        dimensoes_validas = largura == altura == 300

        if formato_valido and dimensoes_validas:
            return True
        else:
            return False

    except:
        return False
