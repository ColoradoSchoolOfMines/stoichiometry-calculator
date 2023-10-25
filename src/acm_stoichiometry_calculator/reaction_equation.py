class ReactionEquation:
    class Molecule:
        def __init__(self, name) -> None:
            self.name = name
            self.elements = []
            self.number = None

        def append_element(self, name, number):
            if number == '':
                number = '1'
            if number is str:
                number = int(number)
            self.elements.append((name, number))

    def __init__(self, e_string: str) -> None:
        self.reactants, self.products = self.interpret_equation(e_string)

    def interpret_equation(self, e_string: str):
        e_string.replace(" ", "")
        react_str, prod_str = e_string.split('=')
        return (self.interpret_one_side(react_str), self.interpret_one_side(prod_str))

    def interpret_one_side(self, side_string: str):
        side = []
        molecules = side_string.split('+')
        for molecule in molecules:
            element = ''
            number = ''
            side.append(self.Molecule(molecule))
            for c in molecule:
                if c.isupper() and len(element) != 0:
                    side[-1].append_element(element, number)
                    element = ''
                    number = ''
                if c.isalpha():
                    element += c
                elif c.isdigit():
                    number += c
            side[-1].append_element(element, number)
        return side


if __name__ == "__main__":
    # TODO: Interpret "Al(NO3)3 + NaOH = Al(OH)3 + NaNO3 -> AlN3O9 + NaOH = AlO3H3 + NaNO3"
    eq = ReactionEquation('PCl5 + H2O = H3PO4 + HCl')
    for mol in eq.reactants:
        print(mol.name)
        print(mol.elements)
    print('=')
    for mol in eq.products:
        print(mol.name)
        print(mol.elements)
