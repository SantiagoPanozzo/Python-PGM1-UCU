departamentos = {'Artigas','Canelones','Cerro Largo','Colonia','Durazno','Flores','Florida','Lavalleja','Maldonado','Montevideo','Paysandú','Río Negro','Rivera','Rocha','Salto','San José','Soriano','Tacuarembó','Treinta y Tres'}
fronteras = {'Artigas','Rivera','Salto','Soriano','Tacuarembó','Paysandú','Cerro Largo','Mercedes','Montevideo','Maldonado','Colonia','Río Negro','Treinta y Tres','Rocha'}
departamentos_serranos={"Maldonado", "Lavalleja", "Rocha", "Treinta y Tres", "Cerro Largo"}
departamentos_playas={"Maldonado", "Rocha"}

no_frontera = departamentos-fronteras
no_front_sierra = no_frontera-departamentos_serranos
sierrasyplayas = departamentos_serranos&departamentos_playas
atracciones = departamentos_serranos|departamentos_playas
ninguna = departamentos-atracciones

print(f'''
- ¿Qué departamentos de Uruguay no tienen fronteras con otro país?:
        R: {', '.join(no_frontera)}
- ¿Cuáles de los departamentos que no tienen fronteras otros países tampoco tienen sierras?
        R: {', '.join(no_front_sierra)}
- Si un turista te pregunta qué departamentos visitar que incluya ambas atracciones (sierras y playas oceánicas), ¿cuál sería la respuesta? 
        R: {', '.join(sierrasyplayas)}
- Si un turista te pregunta qué departamentos tienen alguna atracción turística, ¿cuál sería la respuesta?
        R: {', '.join(atracciones)}
- ¿Qué departamentos no ofrecen ninguna atracción turística de las aquí mencionadas? (ninguna de las dos)
        R: {', '.join(ninguna)}
''')