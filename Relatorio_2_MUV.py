import matplotlib.pyplot as plt
import math

#Gerando dados iniciais
L = [[20.90, 17.40, 19.50], [22.30, 18.80, 20.90], [22.70, 19.00, 20.70], [25.80, 22.30, 24.60]]
media_L = [(i[0] + i[1] + i[2])/3 for i in L]
incerteza_L = [math.sqrt( ((L[i][0] - media_L[i])**2 + 
                           (L[i][1] - media_L[i])**2 + 
                           (L[i][2] - media_L[i])**2)/6)for i in range(4)]

dt = [[0.867, 0.963, 0.867], [0.907, 1.007, 0.913], [0.897, 0.986, 0.894], [1.006, 1.090, 0.989]]
media_dt = [(i[0] + i[1] + i[2])/3 for i in dt]
incerteza_dt = [math.sqrt(((dt[i][0] - media_dt[i])**2 + 
                           (dt[i][1] - media_dt[i])**2 + 
                           (dt[i][2] - media_dt[i])**2)/6) for i in range(4)]

v = [media_L[i]/media_dt[i] for i in range(4)]
incerteza_v = [v[i] * math.sqrt((incerteza_L[i]/media_L[i])**2 + (incerteza_dt[i]/ media_dt[i])**2) for i in range(4)]

#Aplicando Incerteza e Criando Tabela
incerteza_L = [round(incerteza_L[i], 0) for i in range(4)]
media_L = [round(media_L[i], 0) for i in range(4)]
Y = [0.0, round(media_L[0], 0), round(media_L[0] + media_L[1], 0), round(media_L[0] + media_L[1] + media_L[2], 0), round(media_L[0] + media_L[1] + media_L[2] + media_L[3], 0)] 
incerteza_dt = [round(incerteza_dt[i], 2) for i in range(4)]
media_dt = [round(media_dt[i], 2) for i in range(4)]
X = [0.0, round(media_dt[0], 2), round(media_dt[0] + media_dt[1], 2), round(media_dt[0] + media_dt[1] + media_dt[2], 2), round(media_dt[0] + media_dt[1] + media_dt[2] + media_dt[3], 2)]
incerteza_v = [round(incerteza_v[i], 0) for i in range(4)]
v = [round(v[i], 0) for i in range(4)]

tabela = [Y, [0.0] + incerteza_L, X, [0.0] + incerteza_dt]

#Criando Somatórias
somatoria_y = 0
somatoria_x = 0
somatoria_1 = 0
somatoria_xy = 0
somatoria_x2 = 0

#Executando Somatórias
for i in range(0, len(media_L)):
    somatoria_y += Y[i]/(incerteza_L[i]**2)
    somatoria_x += X[i]/(incerteza_L[i]**2)
    somatoria_1 += 1/(incerteza_L[i]**2)
    somatoria_xy += (Y[i] * X[i])/(incerteza_L[i]**2)
    somatoria_x2 += (X[i]**2)/(incerteza_L[i]**2)

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
chaves_incerteza = len(media_L) / somatoria_1

#Calculando Delta_A e Delta_B
delta_a = (1 / math.sqrt(len(X))) * math.sqrt((chaves_incerteza / (chaves_x2 - (chaves_x**2))))
delta_b = (1 / math.sqrt(len(X))) * math.sqrt(((chaves_incerteza * chaves_x2) / (chaves_x2 - (chaves_x**2))))

#Exibindo dados
print(f"""
X: {X}
Y: {Y}
Valores Estimados: {[round(a*j + b, 2) for j in range(5)]}
a = {a}
b = {b}
delta_a = {delta_a}
delta_b = {delta_b}
""")

#Plotando Gráfico
plt.scatter(X, Y, color = 'red')
plt.plot(X, [a*j + b for j in X], 'blue')
plt.ylabel("x(cm)")
plt.xlabel("Delta t(s)")
plt.title("X vs Delta t (MUV)")
plt.show()
