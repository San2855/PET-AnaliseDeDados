import math
def distancia(x1,y1,x2,y2):
  dist= math.sqrt(math.pow((x2-x1),2)+math.pow(y2-y1,2))
  print('A distância é :', dist)
  return dist
def distanciaEntrePontosCalculados(dist1, dist2):
  distP= math.sqrt(math.pow((dist2),2)+math.pow(dist1, 2))
  print('A distância entre os pontos é :', distP )
  return distP

dist1 = distancia(2,3,5,6)
dist2 = distancia(2,5,5,9)
dist3 = distancia(6,3,5,8)
dist4 = distancia(9,6,4,1)
dist5 = distancia(5,4,7,2)
dist6 = distancia(1,3,3,4)



distanciaEntrePontosCalculados(dist1, dist2)
distanciaEntrePontosCalculados(dist1, dist3)
distanciaEntrePontosCalculados(dist1, dist4)
distanciaEntrePontosCalculados(dist1, dist5)
distanciaEntrePontosCalculados(dist1, dist6)