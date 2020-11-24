# class Mandarina():

#     energy_amount = 7
#     size = 0
#     color_types = ('verde', 'naranja', 'oscuro')
#     color = ''
#     state_types = ('inmadura', 'madura', 'podrida')
#     state = ''
#     vitamin_types = ('C', 'D')
#     vitamins = ''
#     mineral_types = ('zinc', 'potasio')
#     minerals = ''
#     object_type = 'fruta'
#     birth_time = 0
#     odor_types = ('leve', 'moderado', 'intenso', 'nauseabundo')
#     odor = ''
#     shape = 'toroide'
#     types_of = ('injerto', 'normal')
#     type_of = ''
#     seeds = 0
#     weight = 0
#     volume = 0
#     mass = 0
#     peel_types = ('gruesa', 'delgada')
#     peel_thickness = ''
#     number_of_segments = 0
#     size_of_segments = 0

#     # Método 'sucio'
#     @classmethod
#     def rot(cls):
#         cls.state = cls.state_types[2]
#         cls.odor = cls.odor_types[3]
#         cls.weight = 7.7
#         cls.size_of_segments = cls.weight * cls.volume

#     # Método 'fancy' (elegante)
#     @classmethod
#     def show_props(cls):
#         print(f'''
#         tamaño = {cls.size}
#         color = {cls.color}
#         estado = {cls.state}
#         vitaminas = {cls.vitamins}
#         minerales = {cls.minerals}
#         tipo = {cls.object_type}
#         tiempo de nacimiento = {cls.birth_time}
#         olor = {cls.odor}
#         forma = {cls.shape}
#         tipo de planta = {cls.type_of}
#         número de semillas = {cls.seeds}
#         peso = {cls.weight}
#         volumen = {cls.volume}
#         masa = {cls.mass}
#         grosor de cáscara = {cls.peel_thickness}
#         número de gajos = {cls.number_of_segments}
#         tamaño de gajos = {cls.size_of_segments}
#         ''')

#     @classmethod
#     def get_energy(cls):
#         return cls.energy_amount


# class Person():
#     energy = 0
#     name = ''
#     isUp = True
#     isStill = True
#     # Método constructor

#     def __init__(self, name='Sin nombre'):
#         self.name = name
#         self.energy = 1

#     def set_energy(self, from_who):
#         self.energy = self.energy + from_who
#         # cls.energy = from_who

#     def show_props(self):
#         print(f'''
#         Nombre: {self.name}
#         Energía: {self.energy}
#         ''')

#     def set_name(self, name):
#         self.name = name

#     def walk(self, steps, direction):
#         if not(self.isUp):  # self.isUp == True
#             self.up()
#         self.stop(False)
#         print(f'{self.name} caminando {steps} pasos hacia {direction}')
#         self.stop()

#     def run(self, speed, distance):
#         if not (self.isUp):
#             self.up()
#         self.stop(False)
#         print(
#             f'{self.name} corriendo a una velocidad de {speed} una distancia de {distance}')
#         self.stop()

#     def sit(self):
#         if self.isUp:  # estaDePie
#             print(f'{self.name} ahora está sentado')
#             self.isUp = False
#         else:
#             print(f'{self.name} ya está sentado /=')

#     def up(self):
#         if not (self.isUp):
#             print(f'{self.name} ahora está de pié')
#         else:
#             print(f'{self.name} ya está de pié /=')

#     def stop(self, still=True):
#         self.isStill = still
#         if self.isStill:
#             print(f'{self.name} está detenido')
#         else:
#             print(f'{self.name} listo para moverse')
#             self.isStill = True


#             # Creo una instancia de la clase Mandarina
# mandi = Mandarina()  # Instancia/Objeto
# # eduardo.set_name('Eduardo')
# # gilberto.set_name('Gilberto')
# bibiana = Person('Bibiana')
# # bibiana.set_name('Bibiana')
# otro = Person()

# a = 0  # Variable

# # mandi.show_props()
# # # eduardo.show_props()
# # # mandi.rot()
# # # mandi.show_props()
# # eduardo.set_energy(mandi.get_energy())
# # gilberto.set_energy(mandi.get_energy())
# # eduardo.show_props()
# # gilberto.show_props()
# # eduardo.set_energy(mandi.get_energy())
# # gilberto.set_energy(mandi.get_energy())
# # eduardo.show_props()
# # gilberto.show_props()
# # eduardo.set_energy(mandi.get_energy())
# # gilberto.set_energy(mandi.get_energy())
# # eduardo.show_props()
# # gilberto.show_props()
# # gilberto.set_energy(mandi.get_energy())
# # eduardo.show_props()
# # gilberto.show_props()
# # bibiana.show_props()
# # otro.show_props()
# # otro.set_name('Ya tengo nombre')
# # otro.show_props()

# # Funcionalidades para implementar a la clase Person:
# # - Caminar un número de pasos (hacia adelante o atrás)
# # - Correr
# # - Sentarse
# # - Pararse
# # - Detenerse

# eduardo = Person('Eduardo')
# eduardo.walk(3, 'adelante')
# eduardo.sit()
# eduardo.run('3Km/h', '1K')
# eduardo.run('7Km/h', '4K')
# gilberto = Person('Gilberto')
# gilberto.walk(5, 'atrás')
# gilberto.run('1Km/h', '5Km')
# gilberto.stop()
# eduardo.up()
# eduardo.sit()
# eduardo.up()

# Crear una clase Perro
# Atributos obligatorios:
# - Raza
# - Color
# - Talla (pequeño, mediano, grande, gigante)
# Métodos obligatorios:
# - Ladrar
# - Correr
# - Caminar
# - Olfatear
# - Rascar
# - Comer


class Dog():
    race = ''
    color = ''
    size = ''
    name = ''
    nose = True
    legs = 4
    energy = 0
    isSit = False
    isUp = True
    limit = 100

    # Constructor
    def __init__(self, name, race, color, size):
        self.name = name
        self.race = race
        self.color = color
        self.size = size

    def bark(self):
        print('woof, woof')

    def run(self, distance, speed):
        if self.isSit:
            self.up()
        print(
            f'{self.name} está corriendo una distancia de {distance} a una velocidad de {speed}')

    def walk(self, steps, direction):
        if self.isSit:
            self.up()
        if direction == 'atrás' or direction == 'adelante':
            print(f'{self.name} camina {steps} pasos hacia {direction}')
        else:
            print(f'{self.name} camina {steps} pasos hacia la {direction}')

    def sniff(self, whatever):
        print(f'{self.name} está olfateando {whatever}')

    def scratch(self, whatever):
        print(f'{self.name} está rascando {whatever}')

    def eat(self, croquettes, number_of_croquettes):
        if self.limit > 0:
            print(f'{self.name} se está comiendo {number_of_croquettes} croquetas')
            croquettes.disolve()
            croquettes.liberation()
            self.energy += number_of_croquettes * croquettes.get_proteins(self)
            self.limit -= number_of_croquettes
        else:
            print(
                f'{self.name} ya no puede seguir comiendo, está lleno a reventar...')

    def show_energy(self):
        print(f'{self.name} ahora tiene {self.energy} puntos de energía! (=')

    def sit(self):
        print(f'{self.name} ahora está sentado')
        self.isSit = True
        self.isUp = False

    def up(self):
        print(f'{self.name} ahora está de parado')
        self.isSit = False
        self.isUp = True

# Clase Croquetas
# Atributos:
# - Vitaminas
# - Porcentaje de proteína
# - Sabor
# - Ingredientes
# - Tipo de raza (para la que son recomendadas)
# Métodos:
# - Disolverse
# - Liberación de nutrientes


class Croquettes():
    vitamins = []
    protein_pct = 0
    flavor = ''
    ingredients = []
    race_for = ''
    name = ''

    # Constructor
    def __init__(self, name, vitamins, ingredients, protein_pct, flavor, race_for):
        self.name = name
        self.vitamins = vitamins
        self.protein_pct = protein_pct
        self.ingredients = ingredients
        self.flavor = flavor
        self.race_for = race_for

    def disolve(self):
        print(f'Croquetas {self.name} en proceso de disolución...')

    def liberation(self):
        print(f'Croquetas {self.name} liberando nutrientes...')

    def get_proteins(self, dog):
        if type(dog) == Dog:
            print(f'Liberando nutrientes para {dog.name}')
            return self.protein_pct
        else:
            print(f'Sólo un perro puede aprovechar las proteínas /=')


# Perros
solovino = Dog('Solovino', 'eléctrico', 'gris percudido', 'mediano')
firulais = Dog('Firulais', 'Pastor Alemán', 'Miel/negro', 'grande')

# Croquetas
dog_chow = Croquettes('Dog Chow', ['Complejo B', 'D', 'A', 'Zinc'], [
                      'Huesos de pollo molidos', 'Carne de cerdo', 'Carne de res', 'vegetales'], 0.21, 'Carnes a las finas hierbas', 'Grandes')
pedigree = Croquettes('Pedigree', ['Hierro', 'A', 'Riboflavina', 'Zinc', 'Selenio'], [
                      'Carne de res', 'huesos molidos de cerdo'], 0.17, 'Trocitos de carne y huesos', 'Medianas')

solovino.sit()
solovino.sniff('un gato')

firulais.walk(3, 'adelante')
firulais.show_energy()
firulais.eat(dog_chow, 50)
firulais.show_energy()
firulais.eat(dog_chow, 50)
firulais.show_energy()
firulais.eat(dog_chow, 5)

# ToDo:
# - Al poner al perro al caminar, debe gastar parte de su energía, dependiendo del número de
#   pasos que dé (0.25 puntos de energía por cada paso)
# - Al poner al perro a correr, debe gastar parte de su energía, dependiendo de la velocidad
#   y la distancia recorridas (0.75 puntos por cada 10 metros recorridos)
# - Establecer límites de comida, en función del número de croquetas y energía máxima que puede
#   asimilar el perro (energía máxima: 25)
