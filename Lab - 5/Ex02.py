from threading import Thread
from PIL import Image, ImageEnhance
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
    queue_w1_w2 = queue.Queue()
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
    trabalhador_1 = Thread(target=trabalhador, args=('cinzentos', queue_inicial, queue_w1_w2))
    trabalhador_1.start()
    trabalhador_2 = Thread(target=trabalhador, args=('contraste', queue_w1_w2, queue_final))
    trabalhador_2.start()
    trabalhador_2.join()
    while not queue_final.empty():
        imagem = queue_final.get()
        if imagem:
            imagem.show()
    fim = timer()
    print(f"Tempo para pipelining: {fim - inicio:.8f}")

# The program creates a queue of photographs to which we will apply 2 filters,
# each filter is applied on a different thread but the photos go to the queue of the next thread as soon as they are processed
# the output queue of one worker is the input of the next one
# The pipeline is being used to "build" the final image with the 2 filters applied
# The initial queue is where the images are initially placed
# queue_w1_w2 is the queue where the images processed after the first filter has been applied are placed
# the above queue will be the input for the second process which will then apply the contrast and put it in the final queue