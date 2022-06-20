from threading import Thread
from PIL import Image, ImageEnhance, ImageFilter
import os
import queue
from timeit import default_timer as timer


def aplicar_efeito(imagem, efeito):
    if efeito == 'cinzentos':
        enh = ImageEnhance.Color(imagem)
        imagem = enh.enhance(0.0)
    elif efeito == 'contraste':
        enh = ImageEnhance.Contrast(imagem)
        imagem = enh.enhance(1.8)
    elif efeito == 'arestas':
        imagem = imagem.filter(ImageFilter.FIND_EDGES)
    elif efeito == 'blur':
        imagem = imagem.filter(ImageFilter.BLUR)
    # imagem.show()
    return imagem


def trabalhador(tarefa, input_queue, output_queue):
    while True:
        imagem = input_queue.get()
        if imagem is None:
            output_queue.put(None)
            return
        imagem = aplicar_efeito(imagem, tarefa)
        output_queue.put(imagem)


if __name__ == '__main__':
    diretoria = "./imagens"
    inicio = timer()
    queue_inicial = queue.Queue()
    queue2 = queue.Queue()
    queue3 = queue.Queue()
    queue4 = queue.Queue()
    queue_final = queue.Queue()
    # put images in the initial queue
    for file in os.listdir(diretoria):
        # Read image
        imagem = Image.open(diretoria + "/" + str(file))
        # Display image
        imagem.show()
        queue_inicial.put(imagem)
    # put the terminator in the work queue
    queue_inicial.put(None)
    trabalhador_1 = Thread(target=trabalhador, args=('cinzentos', queue_inicial, queue2))
    trabalhador_1.start()

    trabalhador_2 = Thread(target=trabalhador, args=('contraste', queue2, queue3))
    trabalhador_2.start()

    trabalhador_3 = Thread(target=trabalhador, args=('arestas', queue3, queue4))
    trabalhador_3.start()

    trabalhador_4 = Thread(target=trabalhador, args=('blur', queue4, queue_final))
    trabalhador_4.start()

    trabalhador_4.join()
    while not queue_final.empty():
        imagem = queue_final.get()
        if imagem:
            imagem.show()
    fim = timer()
    print(f"Time of pipelining: {fim - inicio:.8f}")


