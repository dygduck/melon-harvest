############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller,
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.name = name
        self.is_bestseller = is_bestseller

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    cas = MelonType("cas", 2003, "orange", False, False, "Casaba")
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")
    all_melon_types.append(cas)

    cren = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    cren.add_pairing("proscuitto")
    all_melon_types.append(cren)

    yw = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print "%s pairs well with:" % (melon.name)
        for pairing in melon.pairings:
            print "-", pairing
    return None


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_codes = {}
    for melon in melon_types:
        melon_codes[melon.code] = melon.name
    return None

############
# Part 2   #
############


class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, code, shape, color, harvested_from_field, harvested_by):
        self.code = code
        self.shape = shape
        self.color = color
        self.harvested_from_field = harvested_from_field
        self.harvested_by = harvested_by

    def is_sellable(self):
        if self.shape > 5 and self.color > 5 and self.harvested_from_field != 3:
            self.is_sellable = True
        else:
            self.is_sellable = False
        return self.is_sellable


def make_melons():
    """Returns a list of Melon objects."""
    melons = []

    melon1 = Melon(MelonType["yw"], 8, 7, 2, 'Sheila')
    melons.append(melon1.name)

    melon2 = Melon(melon_types["yw"], 3, 4, 2, 'Sheila')
    melons.append(melon2)

    melon3 = Melon(melon_types["yw"], 9, 8, 3, 'Sheila')
    melons.append(melon3)

    melon4 = Melon(melon_types["cas"], 10, 6, 35, 'Sheila')
    melons.append(melon4)

    melon5 = Melon(melon_types["cren"], 8, 9, 35, 'Michael')
    melons.append(melon5)

    melon6 = Melon(melon_types["cren"], 8, 2, 35, "Michael")
    melons.append(melon6)

    melon7 = Melon(melon_types["cren"], 2, 3, 4, "Michael")
    melons.append(melon7)

    melon8 = Melon(melon_types["musk"], 6, 7, 4, "Michael")
    melons.append(melon8)

    melon9 = Melon(melon_types["yw"], 7, 10, 3, 'Sheila')
    melons.append(melon9)

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melons:
        if melon.is_sellable is True:
            sellability = "CAN BE SOLD"
        else:
            sellability = "NOT SELLABLE"
        print "Harvested by %s from Field %d %s" % (melon.harvested_by,
                                                    melon.harvested_from_field,
                                                    sellability)


melon_types = make_melon_types()
print_pairing_info(melon_types)
make_melon_type_lookup(melon_types)
melons = make_melons()
get_sellability_report(melons)
