"""
3. La tienda "El Gran Bazar" desea analizar sus ventas diarias y mensuales. Tienes
un diccionario que contiene las ventas de cada producto para cada día del mes.
Cada producto tiene registrado cuántas unidades se vendieron en cada día del
mes.
""" 
    print("3. La tienda \"El Gran Bazar      >>>>ZZZ)

ventas = {
    "Pan": {1: 5, 2: 3, 3: 6, 4: 8, 5: 1},
    "Agua": {1: 3, 2: 7, 3: 2, 4: 0, 5: 4},
    "Eneryeti": {1: 6, 2: 4, 3: 3, 4: 5, 5: 2},
    "Pipas": {1: 0, 2: 2, 3: 1, 4: 3, 5: 0}
}
totalVentasProducto = {}

print("1. Venta total mensual de cada producto.\n----------------------")
for producto, ventas_diarias in ventas.items():
    
    totalProducto = sum(ventas_diarias.values())
    totalVentasProducto[producto] = totalProducto
    
    print(f"Producto {producto}: {totalProducto} unidades")


print("2. Producto más vendido y menos vendido del mes.\n----------------------")
producto_mas_vendido = max(totalVentasProducto, key=totalVentasProducto.get)
total_mas_vendido = totalVentasProducto[producto_mas_vendido]

producto_menos_vendido = min(totalVentasProducto, key=totalVentasProducto.get)
total_menos_vendido = totalVentasProducto[producto_menos_vendido]

print(f"Producto más vendido: {producto_mas_vendido} ({total_mas_vendido} unidades)")
print(f"Producto menos vendido: {producto_menos_vendido} ({total_menos_vendido} unidades)")


print("3. Ventas diarias del producto con mayor venta mensual.\n----------------------")
ventas_diarias_max = ventas[producto_mas_vendido]

for dia,cantidad in ventas_diarias_max.items():
    print(f"Día {dia}: {cantidad} unidades")

print("4. Día con mayor cantidad de ventas para cada producto.\n----------------------")
for producto,ventasProducto in ventas.items():
    dia_max_ventas = max(ventas_diarias, key=ventasProducto.get)
    
    cantidad = ventasProducto[dia_max_ventas]

    print("El dia ",dia_max_ventas," del producto ",producto," ha vendido una cantidad de ",cantidad, " unidades.")