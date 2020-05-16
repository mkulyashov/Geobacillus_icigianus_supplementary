import cobra.test
import os
from os.path import join
pathToModel = ""
outPath = ""
dic = {}
met_dic = {}
data_dir = cobra.test.data_dir
model = cobra.io.load_json_model(join(data_dir, pathToModel))
reaction_desc = "D:\model_CG_reactions_id_rev_tsv.txt"
with open(reaction_desc, 'r') as r_d:
    for _ in range(1):
        next(r_d)
    for line in r_d:
        row = line.split("\t")
        if "NULL" not in row[1]:
            if "[" in row[1]:
                a = row[1].replace("[","")
                b = a.replace("]", "")
                c = b.replace("'", "")
                massive = c.split(",")
                if row[0] in model.reactions:
                    rea = model.reactions.get_by_id(row[0])
                    rea.id = massive[0].replace(" ", "_")
            else:
                if row[0] in model.reactions:
                    rea = model.reactions.get_by_id(row[0])
                    if rea.id != row[1]:
                        rea.id = row[1].replace(" ", "_")
        elif "NULL" not in row[2]:
            if "[" in row[2]:
                row[2].replace("[","")
                row[2].replace("]", "")
                row[2].replace("'", "")
                massive = row[2].split(",")
                if row[0] in model.reactions:
                    rea = model.reactions.get_by_id(row[0])
                    rea.id = massive[0].replace(" ", "_")
            else:
                if row[0] in model.reactions:
                    rea = model.reactions.get_by_id(row[0])
                    if rea.id != row[2]:
                        rea.id = row[2].replace(" ", "_")
cobra.io.save_json_model(model, outPath)
