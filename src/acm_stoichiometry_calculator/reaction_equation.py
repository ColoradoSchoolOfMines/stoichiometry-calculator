class ReactionEquation:
    class Molecule:
        def __init__(self) -> None:
            self.elements = []
            self.number = None

        def append_element(self, name, number):
            self.elements.append((name, number))


    def __init__(self, e_string:str) -> None:
        self.reactants, self.products = interpret_equation(e_string)

    def interpret_equation(self, e_string:str):
        e_string.replace(" ", "")
        react_str, prod_str = e_string.split('=')
        return(func(react_str), func(prod_str))

    def interpret_one_side(self, side_string:str):
        molecules = side_string.split('+')
        for molecule in molecules:
            element = ""
            number = ""
            for c in molecule:
                if c.isupper() and len(element) != 0:
                    pass
                element += c