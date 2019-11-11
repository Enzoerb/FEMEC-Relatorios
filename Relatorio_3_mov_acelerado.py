import matplotlib.pyplot as plt
import math
        

#Gerando dados iniciais
L = [[21, 17.3, 19.3], [22.3, 18.7, 20.5], [22.6, 19.0, 20.4], [25.8, 22.1, 24.0]]
media_L = [(i[0] + i[1] + i[2])/3 for i in L]
incerteza_L = [math.sqrt( ((L[i][0] - media_L[i])**2 + 
                           (L[i][1] - media_L[i])**2 + 
                           (L[i][2] - media_L[i])**2)/6)for i in range(4)]

dt = [[0.487, 0.485, 0.484], [0.296, 0.297, 0.296], [0.231, 0.232, 0.232], [0.222, 0.223, 0.222]]
media_dt = [(i[0] + i[1] + i[2])/3 for i in dt]
incerteza_dt = [math.sqrt(((dt[i][0] - media_dt[i])**2 + 
                           (dt[i][1] - media_dt[i])**2 + 
                           (dt[i][2] - media_dt[i])**2)/6) for i in range(4)]
media_dt_soma = [round(media_dt[0], 4), round(media_dt[0] + media_dt[1], 4), round(media_dt[0] + media_dt[1] + media_dt[2], 3), round(media_dt[0] + media_dt[1] + media_dt[2] + media_dt[3], 3)]
incerteza_dt_soma = [round(incerteza_dt[0], 4), round(math.sqrt(incerteza_dt[0]**2 + incerteza_dt[1]**2), 4), round(math.sqrt(incerteza_dt[0]**2 + incerteza_dt[1]**2 + incerteza_dt[2]**2), 3), round(math.sqrt(incerteza_dt[0]**2 + incerteza_dt[1]**2 + incerteza_dt[2]**2 + incerteza_dt[3] ** 2), 3)]

dt2 = [i*i for i in media_dt_soma]
incerteza_dt2 = [media_dt_soma[i] * incerteza_dt_soma[i] * 2 for i in range(len(media_dt))]

v = [media_L[i]/media_dt[i] for i in range(4)]
incerteza_v = [v[i] * math.sqrt((incerteza_L[i]/media_L[i])**2 + (incerteza_dt[i]/ media_dt[i])**2) for i in range(4)]

#Aplicando Incerteza e Criando Tabela
incerteza_L = [round(incerteza_L[i], 0) for i in range(4)]
incerteza_Y = [0.0, incerteza_L[0], round(math.sqrt(incerteza_L[0]**2 + incerteza_L[1]**2), 0), round(math.sqrt(incerteza_L[0]**2 + incerteza_L[1]**2 + incerteza_L[2]**2), 0), round(math.sqrt(incerteza_L[0]**2 + incerteza_L[1]**2 + incerteza_L[2]**2 + incerteza_L[3] ** 2), 0)]

media_L = [round(media_L[i], 0) for i in range(4)]
Y = [0.0, round(media_L[0], 0), round(media_L[0] + media_L[1], 0), round(media_L[0] + media_L[1] + media_L[2], 0), round(media_L[0] + media_L[1] + media_L[2] + media_L[3], 0)] 

incerteza_dt = [round(incerteza_dt[i], 4) for i in range(4)]
incerteza_dt_soma = [0.0] + incerteza_dt_soma
incerteza_dt2 = [round(incerteza_dt2[i], 4) for i in range(0, 1)] + [round(incerteza_dt2[i], 3) for i in range(1, 4)]
incerteza_X = [0.0] + incerteza_dt2

media_dt = [round(media_dt[i], 4) for i in range(4)]
media_dt_soma = [0.0] + [round(media_dt_soma[i], 4) for i in range(0, 2)] + [round(media_dt_soma[i], 3) for i in range(2, 4)]
dt2 = [round(dt2[i], 1) for i in range(0, 2)] + [round(dt2[i], 1) for i in range(2, 4)]
X = [0.0] + dt2

incerteza_v = [round(incerteza_v[i], 0) for i in range(4)]
v = [round(v[i], 0) for i in range(4)]

tabela2 = [Y, incerteza_Y, X, incerteza_X]

#Criando Somatórias
somatoria_y = 0
somatoria_x = 0
somatoria_1 = 0
somatoria_xy = 0
somatoria_x2 = 0

#Executando Somatórias
for i in range(1, len(X)):
    somatoria_y += Y[i]/(incerteza_Y[i]**2)
    somatoria_x += X[i]/(incerteza_Y[i]**2)
    somatoria_1 += 1/(incerteza_Y[i]**2)
    somatoria_xy += (Y[i] * X[i])/(incerteza_Y[i]**2)
    somatoria_x2 += (X[i]**2)/(incerteza_Y[i]**2)

#Arrumando eros de conversões das somatórias
somatoria_y = round(somatoria_y , 10)
somatoria_x = round(somatoria_x , 10)
somatoria_1 = round(somatoria_1 , 10)
somatoria_xy = round(somatoria_xy , 10)
somatoria_x2 = round(somatoria_x2 , 10)
    
#Calculando A e B
a = round(((somatoria_y * somatoria_x) - (somatoria_1 * somatoria_xy))/((somatoria_x**2) - (somatoria_x2 * somatoria_1)) , 14)
b = (somatoria_y - (a * somatoria_x))/(somatoria_1)

#Calculando <X>, <X²>, <incerteza²>
chaves_x = somatoria_x / somatoria_1
chaves_x2 = somatoria_x2 / somatoria_1
chaves_incerteza = len(X) / somatoria_1

#Calculando Delta_A e Delta_B
delta_a = (1 / math.sqrt(len(X))) * math.sqrt((chaves_incerteza / (chaves_x2 - (chaves_x**2))))
delta_b = (1 / math.sqrt(len(X))) * math.sqrt(((chaves_incerteza * chaves_x2) / (chaves_x2 - (chaves_x**2))))

#Estimando valores
valores_estimados = [(j, round(a*j + b, 2)) for j in range(5)]

#Print Tabela 2
print(f"""
 ________________________________________________
|Sensor |X(cm) |incerteza X |t2(s) |incerteza t2 | 
|------ |------|------------|------|-------------|
|1      |{Y[0]}   |{incerteza_Y[0]}         |{X[0]}   |{incerteza_X[0]}          |  
|------ |------|------------|------|-------------|  
|2      |{Y[1]}  |{incerteza_Y[1]}         |{X[1]}   |{incerteza_X[1]}       |
|------ |------|------------|------|-------------|
|3      |{Y[2]}  |{incerteza_Y[2]}         |{X[2]}   |{incerteza_X[2]}        |
|------ |------|------------|------|-------------|
|4      |{Y[3]}  |{incerteza_Y[3]}         |{X[3]}   |{incerteza_X[3]}        |
|------ |------|------------|------|-------------|
|5      |{Y[4]}  |{incerteza_Y[4]}         |{X[4]}   |{incerteza_X[4]}        |
|_______|______|____________|______|_____________|
""")

#Exibindo dados
print(f"""
X: {X}
Y: {Y}
Valores Estimados: {valores_estimados}
a = {a}
b = {b}
delta_a = {delta_a}
delta_b = {delta_b}
""")

#Plotando Gráfico
plt.scatter(X, Y, s = 20, color = 'blue', label = 'pontos experimentais')
plt.scatter(X, [Y[i] + incerteza_Y[i] for i in range(5)], s = 2, color = 'green', label = 'incertezas experimentais')
plt.scatter(X, [Y[i] - incerteza_Y[i] for i in range(5)], s = 2,  color = 'green')
for i in range(len(X)):
    plt.plot([X[i], X[i]], [Y[i] - incerteza_Y[i], Y[i] + incerteza_Y[i]], color = 'green')
plt.plot(X, [a*j + b for j in X], 'red', label = 'best fitting line')
plt.legend()
plt.ylabel("x(cm)")
plt.xlabel("Delta t(s)")
plt.title("X vs Delta t (MUV)")
plt.show()
