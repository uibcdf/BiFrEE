# Configuration file for MolSysMT

# Set this variable true while testing
_testing = False

# Set this variable true while debugging
_debugging = False

# Selection shortcuts

selection_shortcuts={
        'MolSysMT': {
            'backbone':'(atom_name==["CA", "N", "C", "O"])',
            'hydrogens':'(atom_type=="H")',
            'hydrogen':'(atom_type=="H")',
            }
        }

# Units

def set_default_quantities_form(form='pint'):

    from molsysmt import pyunitwizard as puw
    puw.configure.set_default_form(form)

def set_default_quantities_parser(form='pint'):

    from molsysmt import pyunitwizard as puw
    puw.configure.set_default_parser(form)

def set_default_standard_units(standards=['nm', 'ps', 'K', 'mole', 'amu', 'e',
    'kJ/mol', 'kJ/(mol*nm**2)', 'N', 'degrees']):

    from molsysmt import pyunitwizard as puw
    puw.configure.set_standard_units(standards)

# Sphinx

# Is sphinx working?
from os import environ
_sphinx_is_working = ('SPHINXWORKING' in environ)
del(environ)

# NGLview
_view_from_htmlfiles=False
if _sphinx_is_working:
    _view_from_htmlfiles=True

