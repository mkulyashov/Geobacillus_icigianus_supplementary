import pandas as pd
import cobra.test
import os
from os.path import join
from cobra import Reaction, Metabolite

def testMetabolites(m):

    data_dir = cobra.test.data_dir
    #specify path to model
    model = cobra.io.load_json_model(join(data_dir, "D:\suplementary\model_files\FinalModel_json.json"))
    metabolite = model.metabolites.get_by_id(m)

    for boundary in model.boundary:
        boundary.bounds = (0.0, 0.0)

    exId = metabolite.id.split('_')[0] + "_e"
    ex_e = Metabolite(exId, formula=metabolite.formula, name=metabolite.name, compartment="e0")

    model.add_metabolites(ex_e)
    exchange = Reaction("EX_" + exId)
    exchange.name = "exchange"
    exchange.lower_bound = 0.0
    exchange.upper_bound = 1000.0
    exchange.add_metabolites({ex_e: -1})

    transport = Reaction("transport")
    transport.name =   metabolite.name + "_trasport"
    transport.lower_bound = -1000.0
    transport.upper_bound = 1000.0
    transport.add_metabolites({ex_e:-1,metabolite:1})

    model.add_reactions([exchange,transport])

    model.objective = transport
    sol = model.optimize()
    sol.fluxes.to_excel(metabolite.name + '_fluxes.xls')
    print(sol.objective_value)

def body():

    metabolites = ['atp_c', 'nadp_c', 'nad_c']
    for m in metabolites:
        testMetabolites(m)


a = body()