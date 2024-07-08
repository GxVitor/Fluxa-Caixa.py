import pandas as pd

arquivo = 'data/Entrada.xlsx'

def lerArquivoEntrada():
    # Caminho do Arquivo 
    planilha = pd.read_excel(arquivo, sheet_name="Entrada", parse_dates=['Data']) 
    return planilha

planilha = lerArquivoEntrada()




#Função para Salvar osplanilha na Planilha do Excel
def inputPlanilhaEntrada(Tipo,Valor,Data, Nota, Divisao , Vencimento, Vencimento2="",Vencimento3="",Vencimento4=""):

    planilha = pd.read_excel(arquivo, sheet_name="Entrada", parse_dates=['Data']) 

    #Criando um DataFrame com osplanilha Novos
    novaLinha = pd.DataFrame({"Tipo": [Tipo],
                            "Valor": [pd.to_numeric(float(Valor))],
                            "Data": [Data],
                            "Nota": [Nota],
                            "Divisao": [Divisao],
                            "Vencimento": [Vencimento],
                            "Vencimento2": [Vencimento2],
                            "Vencimento3": [Vencimento3],
                            "Vencimento4": [Vencimento4]})

    planilha = pd.concat([ planilha , novaLinha], ignore_index=True)
    # Use o método to_excel() para salvar o DataFrame no arquivo Excel
    planilha.to_excel(arquivo, index=False, sheet_name="Entrada")
    lerArquivoEntrada()
    


#Vai Retiorno a Coluna Tipo em um Array
def RetonoInfEntrada(nomeColuna = "" , planilha = planilha):
    planilha = pd.read_excel(arquivo, sheet_name="Entrada", parse_dates=['Data'])
    if nomeColuna == "":
        print("Error")
    else:
        return planilha[nomeColuna].tolist()
    
    return "Coluna Inexistente"

def filtroEntrada(data):
    planilha = pd.read_excel(arquivo, sheet_name="Entrada", parse_dates=['Data']) 

    Datas = pd.to_datetime(planilha["Vencimento"], format="%d/%m/%Y")
    DatasVencimento2 = pd.to_datetime(planilha["Vencimento2"], format="%d/%m/%Y")
    DatasVencimento3 = pd.to_datetime(planilha["Vencimento3"], format="%d/%m/%Y")
    DatasVencimento4 = pd.to_datetime(planilha["Vencimento4"], format="%d/%m/%Y")

    resultado = planilha[(Datas >= pd.to_datetime(data, format="%d/%m/%Y")) | (DatasVencimento2 >= pd.to_datetime(data, format="%d/%m/%Y")) | (DatasVencimento3 >= pd.to_datetime(data, format="%d/%m/%Y")) | (DatasVencimento4 >= pd.to_datetime(data, format="%d/%m/%Y"))]
    return resultado

def filtroEntradaPesquija(data):
    planilha = pd.read_excel(arquivo, sheet_name="Entrada", parse_dates=['Data']) 
    Datas = pd.to_datetime(planilha["Vencimento"], format="%d/%m/%Y")

    resultado = planilha[Datas >= pd.to_datetime(data, format="%d/%m/%Y")]
    return resultado.to_dict(orient='records')


def filtroEntradaEspecifico(data):
    planilha = pd.read_excel(arquivo, sheet_name="Entrada", parse_dates=['Data']) 
    Datas = pd.to_datetime(planilha["Vencimento"], format="%d/%m/%Y")
    DatasVencimento2 = pd.to_datetime(planilha["Vencimento2"], format="%d/%m/%Y")
    DatasVencimento3 = pd.to_datetime(planilha["Vencimento3"], format="%d/%m/%Y")
    DatasVencimento4 = pd.to_datetime(planilha["Vencimento4"], format="%d/%m/%Y")

    resultado = planilha[(Datas == pd.to_datetime(data, format="%d/%m/%Y")) | (DatasVencimento2 ==  pd.to_datetime(data, format="%d/%m/%Y")) | (DatasVencimento3 ==  pd.to_datetime(data, format="%d/%m/%Y")) | (DatasVencimento4 ==  pd.to_datetime(data, format="%d/%m/%Y"))]
    print(resultado)
    return resultado.to_dict(orient='records')


def filtroEntradaPerido(datainicial, datafinal):
    planilha = pd.read_excel(arquivo, sheet_name="Entrada", parse_dates=['Data']) 
    Datas = pd.to_datetime(planilha["Vencimento"], format="%d/%m/%Y")
    DatasVencimento2 = pd.to_datetime(planilha["Vencimento2"], format="%d/%m/%Y")
    DatasVencimento3 = pd.to_datetime(planilha["Vencimento3"], format="%d/%m/%Y")
    DatasVencimento4 = pd.to_datetime(planilha["Vencimento4"], format="%d/%m/%Y")



    # Crie uma máscara booleana para as datas dentro do intervalo
    mascara = ((Datas >= pd.to_datetime(datainicial, format="%d/%m/%Y")) & (Datas <= pd.to_datetime(datafinal, format="%d/%m/%Y"))) | ((DatasVencimento2 >= pd.to_datetime(datainicial, format="%d/%m/%Y")) & (DatasVencimento2 <= pd.to_datetime(datafinal, format="%d/%m/%Y"))) | ((DatasVencimento3 >= pd.to_datetime(datainicial, format="%d/%m/%Y")) & (DatasVencimento3 <= pd.to_datetime(datafinal, format="%d/%m/%Y"))) | ((DatasVencimento4 >= pd.to_datetime(datainicial, format="%d/%m/%Y")) & (DatasVencimento4 <= pd.to_datetime(datafinal, format="%d/%m/%Y")))


    # Aplique a máscara para obter o resultado
    resultado = planilha[mascara]
    
    return resultado.to_dict(orient='records')

#print("Sem Resltado" if teste["Vencimento1"] == "nan" else teste["Vencimento1"])