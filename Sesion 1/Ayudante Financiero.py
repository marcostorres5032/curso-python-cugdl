# 1  -  Definicion de variables
presupuesto = 501
transporte = 200
comida = 200
material_escolar = 100
# 2 - Calculo del gasto total y dinero restante
gasto_total = transporte + comida + material_escolar
dinero_restante = presupuesto - gasto_total
# 3.1 - Mostrar resultados
print("Tu presupuesto es de $", presupuesto, "pesos.")
print("Tu gasto total es de $", gasto_total, "pesos.")
# 3.2 Parametros if para mostrar resultados y recomendaciones
if dinero_restante > 0:
    print("Te queda(n) $", dinero_restante, "peso(s) después de cubrir tus gastos.")
    if dinero_restante >= 100:
        print("¡Buen trabajo! Tienes un buen margen de ahorro!") 
    if dinero_restante < 100:
        print("Cuidado. Estás cerca de gastar todo tu dinero. Considera reducir algunos gastos.")
if dinero_restante < 0:
    print("No puedes cubrir estos gastos")
if dinero_restante == 0:
    print("No te queda dinero después de cubrir tus gastos.")
    print("Gastaste todo tu dinero. Intenta ahorrar un poco a la próxima.")