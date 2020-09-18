import argparse
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt



def loadImage(fileName, inRGB = True):
    
    if inRGB:
        img = cv.imread(cv.samples.findFile(fileName)) # Carrega a imagem colorida
    else:
        img = cv.imread(cv.samples.findFile(fileName), cv.IMREAD_GRAYSCALE) #   Carrega em escala de cinza
    
    return img


def showHistogram(img):
    #imgShape = img.shape
    #if len(img.shape) == 3:
    if img.ndim == 3:
        color = ('b','g','r')
        for i,col in enumerate(color):
            histr = cv.calcHist([img],[i],None,[256],[0,256])
            plt.plot(histr,color = col)
            plt.xlim([0,256])
        
    else:
        histr = cv.calcHist([img],[0],None,[256],[0,256])
        plt.plot(histr)
        plt.xlim([0,256])
    plt.show()

def applyFilter(img, opt = 0):
    
    if opt == 0:
        src = cv.medianBlur(img, 11) #  Aplica filtro Median Blur
    else:
        src = cv.GaussianBlur(img, (5, 5), 0) # Aplica filtro Gaussian Blur

    return src

def main():
    parser = argparse.ArgumentParser(description = 'Processamento de Imagens')
    parser.add_argument("fileName", help="Caminho para o arquivo que armazena a imagem")
    parser.add_argument("-f", "--format", choices=['rgb', 'grey'], default='rgb', 
                        help="Mostrar imagem colorida ou em tons de cinza")
    parser.add_argument("-a", "--histogram", help="Gera o histograma da imagem",
                    action="store_true")                       
    parser.add_argument("-i", "--improve", type=int, choices=[0,1,2], default=0,
                        help="Aplica um filtro medianBlur (1) ou GaussianBlur(2)")
    args = parser.parse_args()
    #  Carregando a imagem de arquivo específico ... 
    #fileName = "Imagens/b01/07180001.jpg"
    fileName = args.fileName
    # ... colorida e ...
    # srcRGB = loadImage(fileName)
    # # ... em tons de cinza. 
    # srcGrey = loadImage(fileName, False)

    if args.format == 'rgb':
        src = loadImage(fileName)
        winTitle = "Original RGB"
    else:
        src = loadImage(fileName, False)
        winTitle = "Original Grey"


    # # Mostrando a imagem colorida na tela
    # cv.namedWindow("Original RGB", cv.WINDOW_NORMAL)
    # cv.imshow("Original RGB", srcRGB)
    # # Mostrando a imagem em tons de cinza na tela
    # cv.namedWindow("Original Grey", cv.WINDOW_NORMAL)
    # cv.imshow("Original Grey", srcGrey)

    cv.namedWindow(winTitle, cv.WINDOW_NORMAL)
    cv.imshow(winTitle, src)

    cv.waitKey()

    # #  Mostrando o histograma da imagem colorida ..;
    # showHistogram(srcRGB)
    # # ... e da imagem em tons de cinza
    # showHistogram(srcGrey)

    if args.histogram:
        showHistogram(src)

    # #  Aplicando filtro medianBlur ..
    # imgFMB = applyFilter(srcGrey)
    # # ... e GaussianBlur
    # imgFGB = applyFilter(srcGrey, 1)

    # # Mostrando a imagem filtrada com medianBlur
    # cv.namedWindow("medianBlur", cv.WINDOW_NORMAL)
    # cv.imshow("medianBlur", imgFMB)
    # # Mostrando a imagem filtrada com GaussianBlur
    # cv.namedWindow("GaussianBlur", cv.WINDOW_NORMAL)
    # cv.imshow("GaussianBlur", imgFGB)

    if args.improve == 1:
        img = applyFilter(src)
        winTitle = "medianBlur"
    elif args.improve == 2:
        img = applyFilter(src, 1)
        winTitle = "GaussianBlur"

    if args.improve:
        cv.namedWindow(winTitle, cv.WINDOW_NORMAL)
        cv.imshow(winTitle, img)
        cv.waitKey()
    
    
    cv.destroyAllWindows()
    return 0

if __name__ == "__main__":
    main()

