import molsysmt as msm
import numpy as np

class Complex():

    def __init__(self, molecular_system, receptor_selection=None, ligand_selection=None, check=True):

        self.molecular_system = molecular_system
        self._molsys = msm.convert(molecular_system, to_form='molsysmt.MolSys')

        self.receptor_atoms = None
        self.ligand_atoms = None
        self.complex_atoms = None

        if receptor_selection is None:

            atoms_per_molecule, molecule_index = msm.get(self._molsys, element='molecule',
                    selection='molecule_type not in ["water", "ion", "cosolvent"]', atom_index=True, molecule_index=True)

            n_molecules = len(molecule_index)

            max_n_atoms = 0
            biggest_molecule_index = None

            for ii in range(n_molecules):
                if max_n_atoms < len(atoms_per_molecule[ii]):
                    biggest_molecule_index = ii

            receptor_atoms = atoms_per_molecule[biggest_molecule_index]

        else:

            receptor_atoms = msm.select(self._molsys, selection=receptor_selection)

        if ligand_selection is None:

            n_molecules = msm.get(self._molsys, element='atom', selection='molecule_type not in ["water", "ion", "cosolvent"]', n_molecules=True)

            if n_molecules==2:

                ligand_atoms = msm.select(self._molsys, element='atom',
                        selection='(molecule_type not in ["water", "ion", "cosolvent"]) and (atom_index not in @receptor_atoms)')

            else:

                raise ValueError("The molecule system needs to have two molecules.")

        self.receptor_atoms = receptor_atoms
        self.ligand_atoms = ligand_atoms
        self.complex_atoms = np.sort(np.concatenate([self.receptor_atoms, self.ligand_atoms]))

        if check:
            if not self.is_a_complex():
                raise ValueError("It is not a complex.")

    def get_receptor(self, to_form='molsysmt.MolSys'):

        receptor = msm.extract(self._molsys, selection=self.receptor_atoms, to_form=to_form)

        return receptor

    def get_ligand(self, to_form='molsysmt.MolSys'):

        ligand = msm.extract(self._molsys, selection=self.ligand_atoms, to_form=to_form)

        return ligand

    def get_complex(self, to_form='molsysmt.MolSys'):

        complex = msm.extract(self._molsys, selection=self.complex_atoms, to_form=to_form)

        return complex

    def is_a_complex(self):

        return True

