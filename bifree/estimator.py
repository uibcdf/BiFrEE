from .complex import Complex

class Estimator():

    def __init__(self, molecular_system, receptor_selection=None, ligand_selection=None):

        self.complex = Complex(molecular_system, receptor_selection=receptor_selection,
                ligand_selection=ligand_selection)

