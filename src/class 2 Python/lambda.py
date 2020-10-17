gente =[
    {"nombre": "Pepe", "casa": "la suya"},
    {"nombre": "Sech", "casa": "la del sech"},
    {"nombre": "Ricardo", "casa": "La Milo's house"}
]

gente.sort(key=lambda persona: persona["nombre"])

print(gente)
