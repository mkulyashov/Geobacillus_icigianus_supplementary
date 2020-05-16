import cobra.test
import os
from os.path import join
from cobra import Reaction, Metabolite
data_dir = cobra.test.data_dir
pathToModel = ""
pathToOutputModel = ""
model = cobra.io.load_json_model(join(data_dir, pathToModel))

###
reaction_1 = Reaction("EX_xyl__D_e")
reaction_1.name = "D-Xylose exchange"
reaction_1.annotation["bigg.reaction"] = " EX_xyl__D_e"
reaction_1.lower_bound = 0.0
reaction_1.upper_bound = 0.0
###
reaction_2 = Reaction("XYLabc")
reaction_2.name = "D-xylose transport via ABC system"
reaction_2.annotation["bigg.reaction"] = "XYLabc"
reaction_2.annotation["seed.reaction"] = "rxn05167"
reaction_2.lower_bound = 0
reaction_2.upper_bound = 1000.0

xylose_e = Metabolite('xyl__D_e', formula='C5H10O5', name='D-Xylose', compartment='e0')
xylose_e.annotation["bigg.metabolite"] = "xyl__D"
xylose_e.annotation["seed.compound"] = "cpd00154"
xylose_c = model.metabolites.get_by_id("xyl__D_c")
h2o_c = model.metabolites.get_by_id('h2o_c')
h_c = model.metabolites.get_by_id('h_c')
pi_c = model.metabolites.get_by_id('pi_c')
atp = model.metabolites.get_by_id('atp_c')
adp = model.metabolites.get_by_id('adp_c')

reaction_1.add_metabolites({xylose_e: -1.0})
reaction_2.add_metabolites({xylose_e: -1.0, xylose_c: 1.0, atp:-1.0, h2o_c:-1.0, adp:1.0, h_c:1.0, pi_c:1.0})
model.add_reactions([reaction_1, reaction_2])

cobra.io.save_json_model(model, pathToOutputModel)
