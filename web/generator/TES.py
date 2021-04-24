from datasets.the_elder_scrolls import *
from random import seed, choice, random
from .markov import MName


seed()


class AltmerNG:
    def __init__(self):
        self._generator_male = MName(
            ALTMER_MALE_NAMES, ALTMER_MALE_NAMES_CHAIN_LENGTH)
        self._generator_female = MName(
            ALTMER_FEMALE_NAMES, ALTMER_FEMALE_NAMES_CHAIN_LENGTH)

    def generate_random_male_name(self):
        return f"{self._generator_male.generate()}"

    def generate_random_female_name(self):
        return f"{self._generator_female.generate()}"


class ArgonianNG:
    def __init__(self):
        self._generator_male = MName(
            ARGONIAN_MALE_SINGLE_WORD_NAMES, ARGONIAN_MALE_NAMES_CHAIN_LENGTH)
        self._generator_female = MName(
            ARGONIAN_FEMALE_SINGLE_WORD_NAMES, ARGONIAN_FEMALE_NAMES_CHAIN_LENGTH)

    def generate_random_male_single_word_name(self):
        return f"{self._generator_male.generate()}"

    def generate_random_female_single_word_name(self):
        return f"{self._generator_female.generate()}"

    def generate_random_male_hyphenated_name(self):
        prefix = choice(ARGONIAN_MALE_PREFIXES).title()
        suffix = choice(ARGONIAN_MALE_SUFFICES).title()
        return f"{prefix}-{suffix}"

    def generate_random_female_hyphenated_name(self):
        prefix = choice(ARGONIAN_FEMALE_PREFIXES).title()
        suffix = choice(ARGONIAN_FEMALE_SUFFICES).title()
        return f"{prefix}-{suffix}"

    def generate_random_male_name(self):
        if random() < 0.5:
            name = self.generate_random_male_single_word_name()
        else:
            name = self.generate_random_male_hyphenated_name()
        return name

    def generate_random_female_name(self):
        if random() < 0.5:
            name = self.generate_random_female_single_word_name()
        else:
            name = self.generate_random_female_hyphenated_name()
        return name


class BosmerNG:
    def __init__(self):
        self._generator_male = MName(
            BOSMER_MALE_NAMES, BOSMER_MALE_NAMES_CHAIN_LENGTH)
        self._generator_female = MName(
            BOSMER_FEMALE_NAMES, BOSMER_FEMALE_NAMES_CHAIN_LENGTH)

    def generate_random_male_name(self):
        return f"{self._generator_male.generate()}"

    def generate_random_female_name(self):
        return f"{self._generator_female.generate()}"


class BretonNG:
    def __init__(self):
        self._generator_male = MName(
            BRETON_MALE_NAMES, BRETON_MALE_NAMES_CHAIN_LENGTH)
        self._generator_female = MName(
            BRETON_FEMALE_NAMES, BRETON_FEMALE_NAMES_CHAIN_LENGTH)
        self._generator_family = MName(
            BRETON_FAMILY_NAMES, BRETON_FAMILY_NAMES_CHAIN_LENGTH)

    def generate_random_male_name(self):
        return f"{self._generator_male.generate()} {self._generator_family.generate()}"

    def generate_random_female_name(self):
        return f"{self._generator_female.generate()} {self._generator_family.generate()}"


class DunmerNG:
    def __init__(self):
        self._generator_male = MName(
            DUNMER_MALE_NAMES, DUNMER_MALE_NAMES_CHAIN_LENGTH)
        self._generator_female = MName(
            DUNMER_FEMALE_NAMES, DUNMER_FEMALE_NAMES_CHAIN_LENGTH)
        self._generator_family = MName(
            DUNMER_FAMILY_NAMES, DUNMER_FAMILY_NAMES_CHAIN_LENGTH)

    def generate_random_male_name(self):
        return f"{self._generator_male.generate()} {self._generator_family.generate()}"

    def generate_random_female_name(self):
        return f"{self._generator_female.generate()} {self._generator_family.generate()}"


class ImperialNG:
    def __init__(self):
        self._generator_male = MName(
            IMPERIAL_MALE_NAMES, IMPERIAL_MALE_NAMES_CHAIN_LENGTH)
        self._generator_female = MName(
            IMPERIAL_FEMALE_NAMES, IMPERIAL_FEMALE_NAMES_CHAIN_LENGTH)
        self._generator_family = MName(
            IMPERIAL_FAMILY_NAMES, IMPERIAL_FAMILY_NAMES_CHAIN_LENGTH)

    def generate_random_male_name(self):
        return f"{self._generator_male.generate()} {self._generator_family.generate()}"

    def generate_random_female_name(self):
        return f"{self._generator_female.generate()} {self._generator_family.generate()}"


class KhajiitNG:
    def __init__(self):
        self._generator_male = MName(
            KHAJIIT_MALE_NAMES, KHAJIIT_MALE_NAMES_CHAIN_LENGTH)
        self._generator_female = MName(
            KHAJIIT_FEMALE_NAMES, KHAJIIT_FEMALE_NAMES_CHAIN_LENGTH)

    def generate_random_male_name(self):
        prefix = choice(KHAJIIT_MALE_AFFIXES)
        suffix = choice(KHAJIIT_MALE_AFFIXES)
        given_name = self._generator_male.generate()

        while suffix == prefix or len(suffix) < 2:
            suffix = choice(KHAJIIT_MALE_AFFIXES)

        chance = random()

        if chance < 0.25:  # use only given name
            name = given_name
        elif chance < 0.5:  # use only prefix
            name = f"{prefix.title()}'{given_name}"
        elif chance < 0.75:  # use only suffix
            name = f"{given_name}-{suffix}"
        else:  # use both affixes
            name = f"{prefix.title()}'{given_name}-{suffix}"

        return name

    def generate_random_female_name(self):
        prefix = choice(KHAJIIT_FEMALE_AFFIXES)
        suffix = choice(KHAJIIT_FEMALE_AFFIXES)
        given_name = self._generator_male.generate()

        while suffix == prefix or len(suffix) < 2:
            suffix = choice(KHAJIIT_FEMALE_AFFIXES)

        chance = random()

        if chance < 0.25:  # use only given name
            name = given_name
        elif chance < 0.5:  # use only prefix
            name = f"{prefix.title()}'{given_name}"
        elif chance < 0.75:  # use only suffix
            name = f"{given_name}-{suffix}"
        else:  # use both affixes
            name = f"{prefix.title()}'{given_name}-{suffix}"

        return name


class NordNG:
    def __init__(self):
        self._generator_male = MName(
            NORD_MALE_NAMES, NORD_MALE_NAMES_CHAIN_LENGTH)
        self._generator_female = MName(
            NORD_FEMALE_NAMES, NORD_FEMALE_NAMES_CHAIN_LENGTH)

    def generate_random_male_name(self):
        return f"{self._generator_male.generate()} {choice(NORD_FAMILY_NAMES)}"

    def generate_random_female_name(self):
        return f"{self._generator_female.generate()} {choice(NORD_FAMILY_NAMES)}"


class OrsimerNG:
    def __init__(self):
        self._generator_male = MName(
            ORSIMER_MALE_NAMES, ORSIMER_MALE_NAMES_CHAIN_LENGTH)
        self._generator_female = MName(
            ORSIMER_FEMALE_NAMES, ORSIMER_FEMALE_NAMES_CHAIN_LENGTH)

    def generate_random_male_name(self):
        first_name = self._generator_male.generate()
        if random() < 0.1:
            last_name = self._generator_male.generate()
        else:
            last_name = self._generator_female.generate()

        return f"{first_name} gro-{last_name}"

    def generate_random_female_name(self):
        first_name = self._generator_female.generate()
        if random() < 0.5:
            last_name = self._generator_male.generate()
        else:
            last_name = self._generator_female.generate()

        return f"{first_name} gra-{last_name}"


class RedguardNG:
    def __init__(self):
        self._generator_male = MName(
            REDGUARD_MALE_NAMES, REDGUARD_MALE_NAMES_CHAIN_LENGTH)
        self._generator_female = MName(
            REDGUARD_FEMALE_NAMES, REDGUARD_FEMALE_NAMES_CHAIN_LENGTH)

    def generate_random_male_name(self):
        return f"{self._generator_male.generate()}"

    def generate_random_female_name(self):
        return f"{self._generator_female.generate()}"
