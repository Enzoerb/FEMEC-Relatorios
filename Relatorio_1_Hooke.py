import math
import matplotlib.pyplot as plt

#Gerando dados iniciais e tabela
x = [0.0, 0.0, 0.0, 0.0, 0.0]
delta_x = [round((c - x[0]), 3) for c in x]
massa = [0.0, 0.0, 0.0, 0.0, 0.0]
incerteza_m = [0.0001, 0.0001, 0.0001, 0.0001, 0.0001]
forca = [round((c - massa[0])*9.8, 3) for c in massa]
incerteza_f = [round((9.8 * math.sqrt(2) *c), 3) for c in incerteza_m]

tabela = [x, delta_x, massa, incerteza_m, forca, incerteza_f]

#Criando Somatórias
somatoria_y = 0
somatoria_x = 0
somatoria_1 = 0
somatoria_xy = 0
somatoria_x2 = 0

#Executando Somatórias
for i in range(0, len(forca)):
    somatoria_y += forca[i]/(incerteza_f[i]**2)
    somatoria_x += delta_x[i]/(incerteza_f[i]**2)
    somatoria_1 += 1/(incerteza_f[i]**2)
    somatoria_xy += (delta_x[i] * forca[i])/(incerteza_f[i]**2)
    somatoria_x2 += (delta_x[i]**2)/(incerteza_f[i]**2)

#Calculando A e B
a = round(((somatoria_y * somatoria_x) - (somatoria_1 * somatoria_xy))/((somatoria_x**2) - (somatoria_x2 * somatoria_1)) , 14)
b = (somatoria_y - (a * somatoria_x))/(somatoria_1)

#Calculando <X>, <X²>, <incerteza²>
chaves_x = somatoria_x / somatoria_1
chaves_x2 = somatoria_x2 / somatoria_1
chaves_incerteza = len(forca) / somatoria_1

#Calculando Delta_A e Delta_B
delta_a = (1 / math.sqrt(len(forca))) * math.sqrt((chaves_incerteza / (chaves_x2 - (chaves_x**2))))
delta_b = (1 / math.sqrt(len(forca))) * math.sqrt(((chaves_incerteza * chaves_x2) / (chaves_x2 - (chaves_x**2))))

print(f"""
delta_x = {delta_x}
forcas = {forca}
a = {a}
b = {b}
delta_a = {delta_a}
delta_b = {delta_b}
""")

plt.scatter(delta_x, forca, color = 'red')
plt.plot(delta_x, [a*j + b for j in delta_x])
plt.ylabel("Força(N)")
plt.xlabel("Delta X(m)")
plt.title("Força x Delta X (Lei de Hooke)")
plt.show
