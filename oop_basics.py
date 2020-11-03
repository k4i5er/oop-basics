class Mandarina():
    size = 0
    color_types = ('verde', 'naranja', 'oscuro')
    color = ''
    state_types = ('inmadura', 'madura', 'podrida')
    state = ''
    vitamin_types = ('C', 'D')
    vitamins = ''
    mineral_types = ('zinc', 'potasio')
    minerals = ''
    object_type = 'fruta'
    birth_time = 0
    odor_types = ('leve', 'moderado', 'intenso', 'nauseabundo')
    odor = ''
    shape = 'toroide'
    types_of = ('injerto', 'normal')
    type_of = ''
    seeds = 0
    weight = 0
    volume = 0
    mass = 0
    peel_types = ('gruesa', 'delgada')
    peel_thickness = ''
    number_of_segments = 0
    size_of_segments = 0

    def rot():
        state = state_types[2]
        odor = odor_types[3]

    def show_props():
        print(f'''
        tamaño = {size}
        color = {color}
        estado = {state}
        vitaminas = {vitamins}
        minerales = {minerals}
        tipo = {object_type}
        tiempo de nacimiento = {birth_time}
        olor = {odor}
        forma = {shape}
        tipo de planta = {type_of}
        número de semillas = {seeds}
        peso = {weight}
        volumen = {volume}
        masa = {mass}
        grosor de cáscara = {peel_thickness}
        número de gajos = {number_of_segments}
        tamaño de gajos = {size_of_segments}
        ''')


# Creo una instancia de la clase Mandarina
mandi = Mandarina()

mandi.show_props()
mandi.rot()
mandi.show_props()
