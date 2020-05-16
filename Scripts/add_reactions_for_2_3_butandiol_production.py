import cobra.test
import os
from os.path import join
from cobra import Reaction, Metabolite
pathToModel = ""
outPath = ""
#
data_dir = cobra.test.data_dir
model = cobra.io.read_sbml_model(join(data_dir, "pathToModel"))
###
reaction_1 = Reaction("BTDD-RR")
reaction_1.name = "(R,R)-Butane-2,3-diol:NAD+ oxidoreductase"
reaction_1.subsystem = "Butanoate metabolism"
reaction_1.annotation["bigg.reaction"] = "BTDD-RR"
reaction_1.annotation["seed.reaction"] = "rxn39373"
reaction_1.lower_bound = -1000.0
reaction_1.upper_bound = 1000.0
###
reaction_2 = Reaction("ACLDC")
reaction_2.name = "(S)-2-Hydroxy-2-methyl-3-oxobutanoate carboxy-lyase"
reaction_2.subsystem = "Butanoate metabolism"
reaction_2.annotation["bigg.reaction"] = "ACLDC"
reaction_2.annotation["seed.reaction"] = "rxn15383"
reaction_2.lower_bound = 0.0
reaction_2.upper_bound = 1000.0
###
reaction_3 = Reaction("EX_btd_RR_e")
reaction_3.name = "Exchange for (R,R)-2,3-Butanediol"
reaction_3.annotation["bigg.reaction"] = "EX_btd_RR_e"
reaction_3.annotation["seed.reaction"] = "EX_cpd01947"
reaction_3.lower_bound = 0.0
reaction_3.upper_bound = 1000.0
###
reaction_4 = Reaction("BTDt-RR")
reaction_4.name = "(R,R)-butanediol transport"
reaction_4.annotation["bigg.reaction"] = "BTDt-RR"
reaction_4.annotation["seed.reaction"] = "rxn11322"
reaction_4.lower_bound = -1000.0
reaction_4.upper_bound = 1000.0
###
cpd00003 = model.metabolites.get_by_id("nad_c")
cpd00004 = model.metabolites.get_by_id("nadh_c")
cpd00067 = model.metabolites.get_by_id("h_c")
cpd19047 = model.metabolites.get_by_id("alac__S_c")
cpd00020 = model.metabolites.get_by_id("pyr_c")
cpd01947 = Metabolite("btd_RR_c", formula = "C4H10O2", name = "(R,R)-2,3-Butanediol", compartment = "c0")
cpd01947_e = Metabolite("btd_RR_c_e", formula = "C4H10O2", name = "(R,R)-2,3-Butanediol", compartment = "e0")
cpd00011 = model.metabolites.get_by_id("co2_c")
cpd19008 = Metabolite("actn__R_c", formula = "C4H8O2", name = "(R)-2-acetoin", compartment = "c0")


reaction_1.add_metabolites({cpd00003:-1.0,cpd01947:-1.0, cpd00004:1.0, cpd00067:1.0, cpd19008:1.0})
reaction_2.add_metabolites({cpd00067:-1,cpd19047:-1,cpd00011:1, cpd19008:1})
reaction_4.add_metabolites({cpd01947_e:-1})
reaction_5.add_metabolites({cpd01947_e:-1,cpd01947:1})
model.add_reactions([reaction_1, reaction_2, reaction_3, reaction_4])


cobra.io.write_sbml_model(model, outPath)
cobra.io.save_json_model(model, outPath)