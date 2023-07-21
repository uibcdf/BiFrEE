import molsysmt as msm

def get_binding_potential_energy(molecular_system, selection=None, groups_of_atoms=None,
                                selection_2=None, groups_of_atoms_2=None):

    n_structures = msm.get(molecular_system, n_structures=True)

    return n_structures

