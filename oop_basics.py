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

from tkinter.ttk import Label, Frame, Entry, Button, Style, Combobox, Radiobutton
from tkinter import Tk, X, LEFT, TOP, RIGHT, END, IntVar


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
    croquettes_limit = 100
    energy_limit = 25
    factor = 0

    # Constructor
    def __init__(self, name, race, color, size):
        self.name = name
        self.race = race
        self.color = color
        self.size = size

    def bark(self):
        print('woof, woof')
        lbl_msg.configure(text='woof, woof')

    def run(self, distance, unit, speed, cat=''):
        if type(cat) == Cat:
            print(f'{self.name} va a correr tras {cat.name}')
            # print(f'{self.name} va a correr tras {cat.get_name()}')
        if self.energy > 0:
            if unit == 'm':
                self.factor = 10
            elif unit == 'km':
                self.factor = 10 / 1000

            if self.isSit:
                self.up()
            print(
                f'{self.name} está corriendo una distancia de {distance}{unit} a una velocidad de {speed}')
            self.energy -= 0.75 * (distance / self.factor)
            self.show_energy()
        else:
            print(f'{self.name} ya no puede correr, necesita comer primero')

    def walk(self, steps, direction):
        if self.energy > 0:
            if self.isSit:
                self.up()
            if direction == 'atrás' or direction == 'adelante':
                print(f'{self.name} camina {steps} pasos hacia {direction}')
            else:
                print(f'{self.name} camina {steps} pasos hacia la {direction}')
            self.energy -= 0.25 * steps
            self.show_energy()
        else:
            print(
                f'{self.name} no puede caminar, necesita comer para obtener energía...')

    def sniff(self, whatever):
        print(f'{self.name} está olfateando {whatever}')

    def scratch(self, whatever):
        print(f'{self.name} está rascando {whatever}')

    def eat(self, croquettes, number_of_croquettes):
        if self.croquettes_limit > 0 and self.energy_limit <= 25:
            if self.energy + number_of_croquettes * croquettes.get_proteins(self) <= 25 and self.croquettes_limit - number_of_croquettes > 0:
                print(
                    f'{self.name} se está comiendo {number_of_croquettes} croquetas')
                croquettes.disolve()
                croquettes.liberation()
                self.energy += number_of_croquettes * \
                    croquettes.get_proteins(self)
                self.croquettes_limit -= number_of_croquettes
            else:
                print(
                    f'{self.name} no puede comer tantas croquetas, porque excede su energía máxima')
            self.show_energy()
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


class Cat():
    race = ''
    color = ''
    size = ''
    name = ''
    nose = True
    legs = 4
    energy = 0
    isSit = False
    isUp = True
    croquettes_limit = 100
    energy_limit = 25
    factor = 0
    has_eaten = False

    # Constructor
    def __init__(self, name, race, color, size):
        self.name = name
        self.race = race
        self.color = color
        self.size = size

    def bark(self):
        print('woof, woof')

    def run(self, distance, unit, speed, cat=''):
        if type(cat) == Cat:
            print(f'{self.name} va a correr tras {cat.name}')
            # print(f'{self.name} va a correr tras {cat.get_name()}')
        if self.energy > 0:
            if unit == 'm':
                self.factor = 10
            elif unit == 'km':
                self.factor = 10 / 1000

            if self.isSit:
                self.up()
            print(
                f'{self.name} está corriendo una distancia de {distance}{unit} a una velocidad de {speed}')
            self.energy -= 0.75 * (distance / self.factor)
            self.show_energy()
        else:
            print(f'{self.name} ya no puede correr, necesita comer primero')

    def walk(self, steps, direction):
        if self.energy > 0:
            if self.isSit:
                self.up()
            if direction == 'atrás' or direction == 'adelante':
                print(f'{self.name} camina {steps} pasos hacia {direction}')
            else:
                print(f'{self.name} camina {steps} pasos hacia la {direction}')
            self.energy -= 0.25 * steps
            self.show_energy()
        else:
            print(
                f'{self.name} no puede caminar, necesita comer para obtener energía...')

    def sniff(self, whatever):
        print(f'{self.name} está olfateando {whatever}')

    def scratch(self, whatever):
        print(f'{self.name} está rascando {whatever}')

    def eat(self, croquettes, number_of_croquettes):
        if self.croquettes_limit > 0 and self.energy_limit <= 25:
            if self.energy + number_of_croquettes * croquettes.get_proteins(self) <= 25 and self.croquettes_limit - number_of_croquettes > 0:
                print(
                    f'{self.name} se está comiendo {number_of_croquettes} croquetas')
                croquettes.disolve()
                croquettes.liberation()
                self.energy += number_of_croquettes * \
                    croquettes.get_proteins(self)
                self.croquettes_limit -= number_of_croquettes
                self.has_eaten = True
            else:
                print(
                    f'{self.name} no puede comer tantas croquetas, porque excede su energía máxima')
            self.show_energy()
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
    animal = ''

    # Constructor
    def __init__(self, vitamins, ingredients, protein_pct, flavor, animal, race_for, name='Delmon'):
        self.name = name
        self.vitamins = vitamins
        self.protein_pct = protein_pct
        self.ingredients = ingredients
        self.flavor = flavor
        self.race_for = race_for
        self.animal = animal

    def disolve(self):
        self.algo = 0
        print(
            f'Croquetas {self.name} para {self.animal} en proceso de disolución...')

    def liberation(self):
        print(f'Croquetas {self.name} liberando nutrientes...')

    def get_proteins(self, animal):
        if type(animal) == Dog or type(animal) == Cat:
            print(
                f'Liberando nutrientes para {animal.name}')
            return self.protein_pct
        else:
            print(f'Sólo un perro puede aprovechar las proteínas /=')


figo = Cat('Figo', 'Angora', 'Blanco', 'Regular')


# Perros
pastorcillo = Dog('Pastorcillo', 'Pastor Alemán', 'Miel/Negro', 'Grande')
solovino = Dog('Solovino', 'eléctrico', 'gris percudido', 'mediano')
firulais = Dog('Firulais', 'Pastor Alemán', 'Miel/negro', 'grande')

# Croquetas
dog_chow = Croquettes(['Complejo B', 'D', 'A', 'Zinc'], [
                      'Huesos de pollo molidos', 'Carne de cerdo', 'Carne de res', 'vegetales'], 0.21, 'Carnes a las finas hierbas', 'Perro', 'Grandes', 'Dog Chow')
pedigree = Croquettes(['Hierro', 'A', 'Riboflavina', 'Zinc', 'Selenio'], [
                      'Carne de res', 'huesos molidos de cerdo'], 0.17, 'Trocitos de carne y huesos', 'Perro', 'Medianas', 'Pedigree')
del_monton = Croquettes(['Vitaminas'], [
                        'Ingredientes'], 0.1, 'Salmón ahumado', 'Gato', 'todas las razas')

# Lista de instancias de tipo Cat o Dog
pet_list = []


def main_function():
    solovino.sit()
    solovino.sniff('un gato')
    solovino.walk(3, 'izquierda')
    solovino.eat(dog_chow, 160)
    solovino.walk(3, 'izquierda')
    solovino.run(5, 'm', '500m/s')
    solovino.run(1, 'm', '500m/s', figo)
    solovino.eat(dog_chow, 1)
    figo.eat(dog_chow, 1)
    if not figo.has_eaten:
        figo.eat(dog_chow, 6)
    else:
        print(f'{figo.name} ya comió, no lo estés engordando...')


# main_function()

def add_new_pet():
    cmb_pet_name.state(['!readonly'])
    entry_pet_race.state(['!readonly'])
    entry_pet_color.state(['!readonly'])
    entry_pet_size.state(['!readonly'])
    cmb_pet_name.delete(0, END)
    entry_pet_race.delete(0, END)
    entry_pet_color.delete(0, END)
    entry_pet_size.delete(0, END)
    btn_create_pet.configure(text='Crear nueva mascota', command=create_pet)


def create_pet():
    pet = find_pet()
    print(f'>>>>PET {pet}')
    if pet == None:
        # if cmb_pet_type.get() == 'Perro':
        if opt.get() == 0:
            print('Creando perro')
            pet = Dog(str(cmb_pet_name.get()), str(entry_pet_race.get()),
                      str(entry_pet_color.get()), str(entry_pet_size.get()))
        else:
            print('Creando gato')
            pet = Cat(cmb_pet_name.get(), entry_pet_race.get(),
                      entry_pet_color.get(), entry_pet_size.get())
        pet_list.append(pet)
        add_pet_to_list()
        cmb_pet_name.delete(0, END)
        entry_pet_color.delete(0, END)
        entry_pet_race.delete(0, END)
        entry_pet_size.delete(0, END)
    else:
        print(f'Actualizando mascota raza>>>> {entry_pet_race.get() }')
        pet_list[pet].race = entry_pet_race.get()
        pet_list[pet].color = entry_pet_color.get()
        pet_list[pet].size = entry_pet_size.get()
        entry_pet_race.state(['readonly'])
        entry_pet_color.state(['readonly'])
        entry_pet_size.state(['readonly'])
        btn_create_pet.configure(
            text='Agregar nueva mascota', command=add_new_pet)

    if not (cmb_pet_name.get() in cmb_pet_name['values']):
        add_pet_to_list()


def show_pet_type(event):
    print(f'>>> Has seleccionado {cmb_pet_type.get()} ')


def add_pet_to_list():
    values = list(cmb_pet_name['values'])
    values.append(cmb_pet_name.get())
    cmb_pet_name['values'] = values


def add_pet(event):
    add_pet_to_list()


def enable_entrys():
    entry_pet_race.state(['!readonly'])
    entry_pet_color.state(['!readonly'])
    entry_pet_size.state(['!readonly'])
    btn_create_pet.configure(text='Actualizar información')
    btn_modify.pack_forget()


def find_pet():
    for pet in pet_list:
        if cmb_pet_name.get() == pet.name:
            return pet_list.index(pet)
    return None


def show_pet(event):
    pet = find_pet()
    cmb_pet_name.state(['readonly'])
    if type(pet_list[pet]) == Dog:
        # cmb_pet_type.current(0)  # Perro en Combobox
        opt.set(0)
    else:
        # cmb_pet_type.current(1)  # Gato en Combobox
        opt.set(1)
    # entry_pet_race.setvar(name, pet.race)
    entry_pet_race.insert(0, pet_list[pet].race)
    # entry_pet_color.setvar(color, pet.color)
    entry_pet_color.insert(0, pet_list[pet].color)
    # entry_pet_size.setvar(size, pet.size)
    entry_pet_size.insert(0, pet_list[pet].size)
    entry_pet_race.state(['readonly'])
    entry_pet_color.state(['readonly'])
    entry_pet_size.state(['readonly'])
    btn_modify.pack(side=LEFT)


def x_pet_type(event):
    if len(cmb_pet_type.get())-1 == 0:
        print('>>> Combo vacío')
    else:
        print('>>> Todavía hay caracteres')


def show_selected():
    print(f'Opción seleccionada: {opt.get()}')


def main_window(dimension, title):
    global root
    global lbl_msg
    global entry_pet_race
    global entry_pet_color
    global entry_pet_size
    # global cmb_pet_type
    global cmb_pet_name
    global btn_create_pet
    global btn_modify
    global opt

    root = Tk()
    root.geometry(dimension)
    root.title(title)

    frm_pet_name = Frame(root)
    Label(frm_pet_name, text='Nombre de la mascota:').pack(side=LEFT)
    cmb_pet_name = Combobox(frm_pet_name, width=33)
    cmb_pet_name.bind('<Return>', add_pet)
    cmb_pet_name.bind('<<ComboboxSelected>>', show_pet)
    cmb_pet_name.pack(side=RIGHT)
    frm_pet_name.pack(fill=X, padx=10, pady=10)

    frm_pet_type = Frame(root)
    Label(frm_pet_type, text='Tipo de mascota:').pack(side=LEFT)

    # Widget Combobox #
    # cmb_pet_type = Combobox(frm_pet_type, state='readonly', width=33)
    # cmb_pet_type['values'] = ('Perro', 'Gato')
    # cmb_pet_type.current(0)
    # cmb_pet_type.pack(side=RIGHT)
    ###################

    # Widget Radiobutton #
    opt = IntVar()
    rb_dog = Radiobutton(frm_pet_type, text='Perro', value=0,
                         command=show_selected, variable=opt)
    rb_dog.pack()
    rb_cat = Radiobutton(frm_pet_type, text='Gato', value=1,
                         command=show_selected, variable=opt)
    rb_cat.pack()
    ###################

    frm_pet_type.pack(fill=X, padx=10, pady=10)

    frm_pet_race = Frame(root)
    Label(frm_pet_race, text='Raza:').pack(side=LEFT)
    entry_pet_race = Entry(frm_pet_race, width=35)
    entry_pet_race.pack(side=RIGHT, fill=X)
    frm_pet_race.pack(fill=X, padx=10, pady=10)

    frm_pet_color = Frame(root)
    Label(frm_pet_color, text='Color:').pack(side=LEFT)
    entry_pet_color = Entry(frm_pet_color, width=35)
    entry_pet_color.pack(side=RIGHT, fill=X)
    frm_pet_color.pack(fill=X, padx=10, pady=10)

    frm_pet_size = Frame(root)
    Label(frm_pet_size, text='Tamaño:').pack(side=LEFT)
    entry_pet_size = Entry(frm_pet_size, width=35)
    entry_pet_size.pack(side=RIGHT, fill=X)
    frm_pet_size.pack(fill=X, padx=10, pady=10)

    btn_create_pet = Button(root, text='Crear nueva mascota',
                            command=create_pet)
    btn_create_pet.pack(side=LEFT)

    btn_modify = Button(
        root, text='Modificar información', command=enable_entrys)

    frm_msg = Frame(root)
    lbl_msg = Label(frm_msg)
    lbl_msg.pack()
    frm_msg.pack(fill=X)


main_window('400x300', 'Perros & Gatos')
# firulais.bark()

root.mainloop()

# Misión:
# Modificar el código para que el usuario agregue mascotas por nombre mediante un Combobox
# y pueda seleccionar solamente entre 2 tipos de mascotas(Perro o Gato) de un segundo Combobox.
# Si el usuario ya ha agregado una mascota y selecciona su nombre, la aplicación deberá mostrar
# sus características correspondientes y mostrar el botón "Modificar".
# Si el usuario borra el contenido del Combobox correspondiente al nombre de la mascota, entonces
# la aplicación deberá borrar toda la información del formulario y ocultar el botón "Modificar"
# y habilitar todos los entrys para permitir al usuario agregar una nueva mascota.
# El botón modificar, habilitará todos los entrys para permitir al usuario actualizar los datos
# de su mascota.
