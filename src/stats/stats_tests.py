from statsmodels.tsa.stattools import kpss
from statsmodels.tsa.stattools import adfuller
import pandas as pd
import numpy

def adf_test(timeseries):
	print ('Teste de Dickey-Fuller aumentado:')
	print ()
	dftest = adfuller(timeseries, autolag='AIC')
	dfoutput = pd.Series(
		dftest[0:4],
		index=[
			'Valor Medido',
			'p-Valor',
			'#Lags usados',
			'Numero de Oberservacoes'
		]
	)
	for key,value in dftest[4].items():
        	dfoutput['Valor Critico (%s)'%key] = value
	print (dfoutput)
	print()
	if dfoutput[0] < dfoutput['Valor Critico (10%)'] and dfoutput[1] < 0.05:
		print("H0 rejeitada (não possui raíz unitária)")
	else:
		print("H0 não rejeitada (série possui raíz unitária)")

def kpss_test(timeseries):
	print ("Teste de Kwiatkowski-Phillips-Schmidt-Shin:")
	print ()
	kpsstest = kpss(timeseries, regression='c', nlags="auto");
	kpss_output = pd.Series(
		kpsstest[0:3],
		index=[
			'Valor Medido',
			'p-Valor',
			'#Lags usados'
		]
	)
	for key, value in kpsstest[3].items():
		kpss_output['Valor Critico (%s)'%key] = value
	print (kpss_output)
	print ()
	if ((kpss_output["p-Valor"] < 0.05)):
		print("H0 rejeitada (série possui raíz unitária e não é estacionária)")
	else:
		print("H0 não rejeitada (série é estacionária com tendência)")
