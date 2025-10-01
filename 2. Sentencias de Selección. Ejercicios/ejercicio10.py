# Ejercicio 10 | Miguel Angel Gambero

"""
10.Escribe un programa que a partir de información de un donante determine si
puede donar sangre. Las condiciones para donar son:
a. No se debe donar en ayunas.
b. Edad: Comprendida entre los 18 y 65 años.
c. Peso: Superior a 50kg.
d. Tensión arterial: dentro de límites adecuados para la extracción.
i. Tensión diastólica (baja): entre 50mm Hg y 100 mm Hg
ii. Tensión sistólica (alta): entre 90mm y 180mm Hg
e. Pulso (frecuencia cardiaca): entre 50 y 110 pulsaciones
f. Valores de hemoglobina:
i. En hombres: superior a 13,5 gramos por litro
ii. En mujeres: superior a 12,5 gramos por litro.
g. Plaquetas: más de 150.000 cc
h. Proteínas totales: más de 6 gr/dl.
"""
ayunas = input("¿Viene en ayunas? (s/n): ").lower()
edad = int(input("Dime tu edad: "))
peso = float(input("Dime tu peso (kg): "))
tension_diastolica = int(input("Dime tu tensión diastólica (mm Hg): "))
tension_sistolica = int(input("Dime tu tensión sistólica (mm Hg): "))
pulso = int(input("Dime tu pulso (pulsaciones por minuto): "))
sexo = input("Dime tu sexo (h/m): ").lower()
hemoglobina = float(input("Dime tu nivel de hemoglobina (g/l): "))
plaquetas = int(input("Dime tu nivel de plaquetas (cc): "))
proteinas = float(input("Dime tu nivel de proteínas totales (gr/dl): "))
puede_donar = True

if ayunas == 's':
    puede_donar = False
if not (18 <= edad <= 65):
    puede_donar = False
if peso <= 50:
    puede_donar = False
if not (50 <= tension_diastolica <= 100):
    puede_donar = False
if not (90 <= tension_sistolica <= 180):
    puede_donar = False
if not (50 <= pulso <= 110):
    puede_donar = False
if sexo == 'h' and hemoglobina <= 13.5:
    puede_donar = False
if sexo == 'm' and hemoglobina <= 12.5:
    puede_donar = False
if plaquetas <= 150000:
    puede_donar = False
if proteinas <= 6:
    puede_donar = False
if puede_donar:
    print("Puedes donar sangre")
else:
    print("No puedes donar sangre")