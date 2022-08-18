############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, name, code, first_harvest, color, is_seedless, is_bestseller
    ):
        """Initialize a melon."""

        self.pairings = []

        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

    def __repr__(self):
        return f'<MelonType object name={self.name}, code={self.code}, first harvet = {self.first_harvest}, color = {self.color}, is seedless = {self.is_seedless}, is bestseller = {self.is_bestseller}>'


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType(
        "Muskmelon",
        "musk",
        1998,
        "green",
        True,
        True
    )
    musk.add_pairing("mint")

    casaba = MelonType(
        "Casaba",
        "cas",
        2003,
        "orange",
        True,
        False
    )
    casaba.add_pairing("strawberries")
    casaba.add_pairing('mint')

    crenshaw = MelonType(
        "Crenshaw",
        "cren",
        1996,
        "green",
        True,
        False
    )
    crenshaw.add_pairing("proscuitto")

    yellow_watermelon = MelonType(
        "Yellow Watermelon",
        "yw",
        2013,
        "yellow",
        True,
        True
    )
    yellow_watermelon.add_pairing("ice cream")

    all_melon_types.extend([musk, casaba, crenshaw, yellow_watermelon])

    return all_melon_types

#print(make_melon_types())


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        #                                   list ==> str
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f'- {pairing}')
        #return None

print_pairing_info(make_melon_types())


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dictionary = {}

    for melon in melon_types:
        melon_dictionary[melon.code] = melon
    print(melon_dictionary)
    return melon_dictionary

#make_melon_type_lookup(make_melon_types())


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""
    # Needs __init__ and is_sellable methods
    def __init__(
        self, melon_type, shape_rating, color_rating, harvested_field, harvested_by
    ):
        """Initialize a melon."""

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_field = harvested_field
        self.harvested_by = harvested_by


    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.harvested_field != 3:
            return True
        else:
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    harvest_melon_list = []

    Melon_1 = Melon(
        "yw",
        8,
        7,
        2,
        "Sheila",
    )
    Melon_1.is_sellable()

    Melon_2 = Melon(
        "yw",
        3,
        4,
        2,
        "Sheila",
    )
    Melon_2.is_sellable()

    Melon_3 = Melon(
        "yw",
        9,
        8,
        3,
        "Sheila",
    )
    Melon_3.is_sellable()

    Melon_4 = Melon(
        "cas",
        10,
        6,
        35,
        "Sheila",
    )
    Melon_4.is_sellable()

    Melon_5 = Melon(
        "cren",
        8,
        2,
        35,
        "Michael",
    )
    Melon_5.is_sellable()

    Melon_6 = Melon(
        "cren",
        8,
        2,
        35,
        "Michael",
    )
    Melon_6.is_sellable()

    Melon_7 = Melon(
        "cren",
        2,
        3,
        4,
        "Michael",
    )
    Melon_7.is_sellable()

    Melon_8 = Melon(
        "musk",
        6,
        7,
        4,
        "Michael",
    )
    Melon_8.is_sellable()

    Melon_9 = Melon(
        "yw",
        7,
        10,
        3,
        "Sheila",
    )
    Melon_9.is_sellable()

    harvest_melon_list.extend([Melon_1, Melon_2, Melon_3, Melon_4, Melon_4, Melon_5, Melon_6, Melon_7, Melon_8, Melon_9])

    return harvest_melon_list



def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    # Harvested by Sheila from Field 2 (CAN BE SOLD)
    for melon in melons:
        if melon.is_sellable == True:
            print(f"Harvested by {melon.harvested_by} from Field {melon.harvested_field} (CAN BE SOLD)")

        else:
            print(f"Harvested by {melon.harvested_by} from Field {melon.harvested_field} (NOT SELLABLE)")

#if line 243 is called within a print statement, None will print below the output
#at the end of the harvested by lines
get_sellability_report(make_melons(MelonType))