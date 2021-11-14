from in_project.logistica_rodoviaria import LogisticaRodoviaria
from in_project.logistica_maritimica import LogisticaMaritimica

logistica = LogisticaRodoviaria()
print(logistica.entregar('maças', 'caixas de madeira', 'Campinas'))
print('\n')
logistica = LogisticaMaritimica()
print(logistica.entregar('carros', 'conteiners', 'Sérvia'))