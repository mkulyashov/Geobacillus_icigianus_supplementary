import cobra.test
import os
from os.path import join
from cobra import Reaction, Metabolite
pathToModel = ""
outPath = ""

data_dir = cobra.test.data_dir
model = cobra.io.load_json_model(join(data_dir, pathToModel))
rea = ["ACLS","ACLDC","BTDD-RR"]
gene_rules = ["( KFX35671.1 and KFX33302.1 )", "( KFX35671.1 and KFX33302.1 )", "EP10_RS00785"]
names = ["Acetolactate synthase", "Acetolactate decarboxylase", "R R butanediol dehydrogenase"]
for i in range(len(rea)):
    model.reactions.get_by_id(rea[i]).gene_reaction_rule = gene_rules[i]
    model.reactions.get_by_id(rea[i]).name = names[i]
cobra.io.save_json_model(model, outPath)