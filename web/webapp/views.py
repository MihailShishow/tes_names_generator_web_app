from flask import render_template
from generator.TES import *


seed()


NAMES_PER_REQUEST = 10


def index():
    return render_template('index.html')


# Dunmer ------------------------------------------------

def dunmer():
    title = 'Dunmer'
    generator = DunmerNG()
    male_names = [generator.generate_random_male_name()
                  for i in range(NAMES_PER_REQUEST)]
    female_names = [generator.generate_random_female_name()
                    for i in range(NAMES_PER_REQUEST)]
    names = list(zip(male_names, female_names))
    return render_template('tes.html', title=title, names=names)

# Bosmer ----------------------------------------------


def bosmer():
    title = 'Bosmer'
    generator = BosmerNG()
    male_names = [generator.generate_random_male_name()
                  for i in range(NAMES_PER_REQUEST)]
    female_names = [generator.generate_random_female_name()
                    for i in range(NAMES_PER_REQUEST)]
    names = list(zip(male_names, female_names))
    return render_template('tes.html', title=title, names=names)


# Altmer ----------------------------------------------

def altmer():
    title = 'Altmer'
    generator = AltmerNG()
    male_names = [generator.generate_random_male_name()
                  for i in range(NAMES_PER_REQUEST)]
    female_names = [generator.generate_random_female_name()
                    for i in range(NAMES_PER_REQUEST)]
    names = list(zip(male_names, female_names))
    return render_template('tes.html', title=title, names=names)


# Orsimer -------------------------------------------------

def orsimer():
    title = 'Orsimer'
    generator = OrsimerNG()
    male_names = [generator.generate_random_male_name()
                  for i in range(NAMES_PER_REQUEST)]
    female_names = [generator.generate_random_female_name()
                    for i in range(NAMES_PER_REQUEST)]
    names = list(zip(male_names, female_names))
    return render_template('tes.html', title=title, names=names)

# Argonian ----------------------------------------------


def argonian():
    title = 'Argonian'
    generator = ArgonianNG()
    male_names = [generator.generate_random_male_name()
                  for i in range(NAMES_PER_REQUEST)]
    female_names = [generator.generate_random_female_name()
                    for i in range(NAMES_PER_REQUEST)]
    names = list(zip(male_names, female_names))
    return render_template('tes.html', title=title, names=names)

# Breton ----------------------------------------------


def breton():
    title = 'Breton'
    generator = BretonNG()
    male_names = [generator.generate_random_male_name()
                  for i in range(NAMES_PER_REQUEST)]
    female_names = [generator.generate_random_female_name()
                    for i in range(NAMES_PER_REQUEST)]
    names = list(zip(male_names, female_names))
    return render_template('tes.html', title=title, names=names)

# Redguard ----------------------------------------------


def redguard():
    title = 'Redguard'
    generator = RedguardNG()
    male_names = [generator.generate_random_male_name()
                  for i in range(NAMES_PER_REQUEST)]
    female_names = [generator.generate_random_female_name()
                    for i in range(NAMES_PER_REQUEST)]
    names = list(zip(male_names, female_names))
    return render_template('tes.html', title=title, names=names)

# Imperial ----------------------------------------------


def imperial():
    title = 'Imperial'
    generator = ImperialNG()
    male_names = [generator.generate_random_male_name()
                  for i in range(NAMES_PER_REQUEST)]
    female_names = [generator.generate_random_female_name()
                    for i in range(NAMES_PER_REQUEST)]
    names = list(zip(male_names, female_names))
    return render_template('tes.html', title=title, names=names)

# Nord ----------------------------------------------


def nord():
    title = 'Nord'
    generator = NordNG()
    male_names = [generator.generate_random_male_name()
                  for i in range(NAMES_PER_REQUEST)]
    female_names = [generator.generate_random_female_name()
                    for i in range(NAMES_PER_REQUEST)]
    names = list(zip(male_names, female_names))
    return render_template('tes.html', title=title, names=names)

# Khajiit ----------------------------------------------


def khajiit():
    title = 'Khajiit'
    generator = KhajiitNG()
    male_names = [generator.generate_random_male_name()
                  for i in range(NAMES_PER_REQUEST)]
    female_names = [generator.generate_random_female_name()
                    for i in range(NAMES_PER_REQUEST)]
    names = list(zip(male_names, female_names))
    return render_template('tes.html', title=title, names=names)
