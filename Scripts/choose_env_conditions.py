import cobra.test
import os
from os.path import join
from cobra import Reaction, Metabolite

pathToModel = ""
outPath = ""
conditionsFile = ""
data_dir = cobra.test.data_dir

model = cobra.io.load_json_model(join(data_dir, pathToModel))
ex = model.exchanges

with open(conditionsFile, 'r') as inp:
    for line in inp:
        row = line.split(',')
        id = row[0]
        l_b = row[1]
        u_b = row[2]
        print(u_b)
        if id in ex:
            r = model.reactions.get_by_id(id)
            r.upper_bound = float(u_b)
            r.lower_bound = float(l_b)
cobra.io.save_json_model(model, outPath)
