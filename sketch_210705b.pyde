w, h = 1000, 1000
from random import normalvariate
from random import randint
import json
#CUIDADO CON ESTO
min_diff =90

# Espacio entre quads


#Repeticiones
iter=1

#(30,144,255)=AZUL
#(220,20,60)=ROJO
#(255,255,102)=AMARILLO
#(0,250,154)=VERDE
#(138,43,226)=MORADO

colors = [(138,43,226),(255,255,102),(30,144,255),(255,255,255), (220,20,60),(0,250,154),(0, 0, 0)]

#Ajuste de subdivision
splits = [0.5,1,1.5]

# Borde del canvas
edge = 10

# Desviaciones estandar y otras constantes
meanit=20
stdevit=6
meancol=3
stdevcol=0.9

#Funcion random normal lista
def normal_choice(lst, mean=None, stddev=None):
    if mean is None:
        # if mean is not specified, use center of list
        mean = (len(lst) - 1) / 2

    if stddev is None:
        # if stddev is not specified, let list be -3 .. +3 standard deviations
        stddev = len(lst) / 6

    while True:
        index = int(normalvariate(mean, stddev) + 0.5)
        if 0 <= index < len(lst):
            return index

def setup():
    size(w, h)
    pixelDensity(2)
    for k in range(iter):
        sep = randint(0,10)
        subdivisions=int(normalvariate(meanit,stdevit))
        background(255)

        quads = []
    # Rectángulo inicial
        quads.append([(edge, edge), (w - edge, edge), (w - edge, h - edge), (edge, h - edge)])
    
    # Separar celdas
        for i in range(subdivisions):
            q_index = int(random(len(quads)))
            q = quads[q_index]
            q_lx = q[0][0]
            q_rx = q[1][0]
            q_ty = q[0][1]
            q_by = q[2][1]
        
            s = splits[int(random(len(splits)))]
            if (random(1) < .5):
                if ((q_rx - q_lx) > min_diff):
                # Redefiniendo el valor de  x  (y es el mismo)
                    x_split = (q_rx - q_lx)/2 * s + q_lx
                
                    quads.pop(q_index)
                    quads.append([(q_lx, q_ty), (x_split - sep, q_ty), (x_split - sep, q_by), (q_lx, q_by)])
                    quads.append([(x_split + sep, q_ty), (q_rx, q_ty), (q_rx, q_by), (x_split + sep, q_by)])
            
            
            else:
                if ((q_by - q_ty) > min_diff):
                    y_split = (q_by - q_ty)/2 * s + q_ty
                
                    quads.pop(q_index)
                    quads.append([(q_lx, q_ty), (q_rx, q_ty), (q_rx, y_split - sep), (q_lx, y_split - sep)])
                    quads.append([(q_lx, y_split + sep), (q_rx, y_split + sep), (q_rx, q_by), (q_lx, q_by)])
        

        stroke(0)
        strokeWeight(2)
    #Atributos
        purple=0
        yellow=0
        bluee=0
        white=0
        redd=0
        greeen=0
        black=0
        
        for q in quads:
            aux=colors[int(normal_choice(colors,meancol,stdevcol))]
            if aux==0:
                purple+=1
            elif aux==1:
                yellow+=1
            elif aux==2:
                bluee+=1
            elif aux==2:
                white+=1
            elif aux==3:
                redd+=1
            elif aux==4:
                greeen+=1
            else:
                black+=1    
            fill(*aux)
            beginShape()
            for p in q:
                vertex(p)
            endShape(CLOSE)
            save("Examples/Classic/" + str(k) + ".png")
            atributos= "Purple:" +str(purple),
                  "Yellow:" + str(yellow),
                  "Blue= " +str(bluee),
                  "White ":white,
                  "Red":redd,
                  "Green":greeen,
                  "Black":black
                }"""
            
            saveJSON(json.dumps(json_k),"Examples/Classic/"  + str(k) + ".json")
          
