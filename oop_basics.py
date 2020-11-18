class Mandarina():

    energy_amount = 7
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

    # Método 'sucio'
    @classmethod
    def rot(cls):
        cls.state = cls.state_types[2]
        cls.odor = cls.odor_types[3]
        cls.weight = 7.7
        cls.size_of_segments = cls.weight * cls.volume

    # Método 'fancy' (elegante)
    @classmethod
    def show_props(cls):
        print(f'''
        tamaño = {cls.size}
        color = {cls.color}
        estado = {cls.state}
        vitaminas = {cls.vitamins}
        minerales = {cls.minerals}
        tipo = {cls.object_type}
        tiempo de nacimiento = {cls.birth_time}
        olor = {cls.odor}
        forma = {cls.shape}
        tipo de planta = {cls.type_of}
        número de semillas = {cls.seeds}
        peso = {cls.weight}
        volumen = {cls.volume}
        masa = {cls.mass}
        grosor de cáscara = {cls.peel_thickness}
        número de gajos = {cls.number_of_segments}
        tamaño de gajos = {cls.size_of_segments}
        ''')

    @classmethod
    def get_energy(cls):
        return cls.energy_amount


class Person():
    energy = 0
    name = ''
    isUp = True
    # Método constructor

    def __init__(self, name='Sin nombre'):
        self.name = name
        self.energy = 1

    def set_energy(self, from_who):
        self.energy = self.energy + from_who
        # cls.energy = from_who

    def show_props(self):
        print(f'''
        Nombre: {self.name}
        Energía: {self.energy}
        ''')

    def set_name(self, name):
        self.name = name

    def walk(self, steps, direction):
        if not(self.isUp):  # self.isUp == True
            self.up()
        print(f'{self.name} caminando {steps} pasos hacia {direction}')

    def run(self, speed, distance):
        if not (self.isUp):
            self.up()
        print(
            f'{self.name} corriendo a una velocidad de {speed} una distancia de {distance}')

    def sit(self):
        if self.isUp:
            print(f'{self.name} ahora está sentado')
            self.isUp = False
        else:
            print(f'{self.name} ya está sentado /=')

    def up(self):
        if not (self.isUp):
            print(f'{self.name} ahora está de pié')
        else:
            print(f'{self.name} ya está de pié /=')


            # Creo una instancia de la clase Mandarina
mandi = Mandarina()  # Instancia/Objeto
# eduardo.set_name('Eduardo')
# gilberto.set_name('Gilberto')
bibiana = Person('Bibiana')
# bibiana.set_name('Bibiana')
otro = Person()

a = 0  # Variable

# mandi.show_props()
# # eduardo.show_props()
# # mandi.rot()
# # mandi.show_props()
# eduardo.set_energy(mandi.get_energy())
# gilberto.set_energy(mandi.get_energy())
# eduardo.show_props()
# gilberto.show_props()
# eduardo.set_energy(mandi.get_energy())
# gilberto.set_energy(mandi.get_energy())
# eduardo.show_props()
# gilberto.show_props()
# eduardo.set_energy(mandi.get_energy())
# gilberto.set_energy(mandi.get_energy())
# eduardo.show_props()
# gilberto.show_props()
# gilberto.set_energy(mandi.get_energy())
# eduardo.show_props()
# gilberto.show_props()
# bibiana.show_props()
# otro.show_props()
# otro.set_name('Ya tengo nombre')
# otro.show_props()

# Funcionalidades para implementar a la clase Person:
# - Caminar un número de pasos (hacia adelante o atrás)
# - Correr
# - Sentarse
# - Pararse
# - Detenerse

eduardo = Person('Eduardo')
eduardo.walk(3, 'adelante')
eduardo.sit()
gilberto = Person('Gilberto')
gilberto.walk(5, 'atrás')
gilberto.run('1Km/h', '5Km')
eduardo.up()
eduardo.sit()
eduardo.up()
