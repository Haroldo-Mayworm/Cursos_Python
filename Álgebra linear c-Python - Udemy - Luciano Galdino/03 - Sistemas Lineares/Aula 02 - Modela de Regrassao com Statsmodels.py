import pandas as pd

import statsmodels.formula.api as smf
import statsmodels.stats.api as sms

nota = pd.read_excel("Aula 02 - concurso - Dados.xlsx")

modelo = smf.ols("nota ~ inicio_estudo + tempo_estudo_dia", data=nota).fit()

print(modelo.summary())
