from PIL import Image, ImageFilter, ImageEnhance
import os
from timeit import default_timer as timer


def arestas(imagem):
    imagem = imagem.filter(ImageFilter.FIND_EDGES)
    return imagem


def desfocagem(imagem):
    imagem = imagem.filter(ImageFilter.BLUR)
    return imagem


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
    diretoria = "./imagens"
    for file in os.listdir(diretoria):
        im = Image.open(diretoria + "/" + str(file))
        im.show()
        im = cinzentos(im)
        im = contraste(im)
        im = arestas(im)
        im = desfocagem(im)
        im.show("B&W, more contrast, edges and blur")
    fim = timer()
    print(f"Time for sequential treatment: {fim - inicio:.8f}")

