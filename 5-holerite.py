def holerite(salario, taxa_inss=0.09, vale_transporte=0.03, plano_saude=347):
    inss = salario * taxa_inss
    taxa_vt = salario * vale_transporte
    taxa_ps = plano_saude * 0.15
    salario_liquido = salario - inss - taxa_ps - taxa_vt
    print(f'''Salário integral: {salario}
INSS: {inss}
Vale transporte: {taxa_vt}
Plano de Saúde: {taxa_ps}
Salário Líquido: {salario_liquido}''')

holeriteN = holerite(2000)
