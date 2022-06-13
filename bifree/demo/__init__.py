from pathlib import PurePath

parent = PurePath(__file__).parent

demo = {}

# Barnase-Barstart

# Alanine dipeptide

demo['barnase_barstar']={}
demo['barnase_barstar']['pdb']=parent.joinpath('barnase_barstar.pdb').__str__()


