class ReactionEquation:
    class Molecule:
        def __init__(self) -> None:
            self.elements = []
            self.number = None

        def append_element(name, number):
            self.elements.append((name, number))


    def __init__(self) -> None:
        self.reactants = []
        self.products = []