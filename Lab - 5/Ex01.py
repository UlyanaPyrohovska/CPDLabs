from PIL import Image, ImageEnhance
import os
from timeit import default_timer as timer


def cinzentos(imagem):
    enh = ImageEnhance.Color(imagem)
    imagem = enh.enhance(0.0)
    return imagem


def contraste(imagem):
    enh = ImageEnhance.Contrast(imagem)
    imagem = enh.enhance(1.8)
    return imagem


if __name__ == '__main__':
    inicio = timer()
    diretoria = "./imagens"  # Images must be in the images folder
    for file in os.listdir(diretoria):
        im = Image.open(diretoria + "/" + str(file))
        im.show()
        im = cinzentos(im)
        im = contraste(im)
        im.show("B&W e mais contraste")
    fim = timer()
    print(f"Tempo para tratamento sequencial: {fim - inicio:.8f}")

# The program applies the black and white filter and increases the contrast to each photo in the images folder sequentially
# The gray function applies the B&W filter and the contrast function increases the contrast
