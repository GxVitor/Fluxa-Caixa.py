from entrada import RetonoInfEntrada, filtroEntrada, filtroEntradaEspecifico, filtroEntradaPerido, filtroEntradaPesquija, inputPlanilhaEntrada
from saida import RetonoInfSaida, filtroSaida, filtroSaidaEspecifico, filtroSaidaPerido, filtroSaidaPesquija, inputPlanilhaSaida


class EntradaDados:
    
    resultaTipoEntrada = RetonoInfEntrada("Tipo")
    resultaValorEntrada = RetonoInfEntrada("Valor")
    resultaDataEntrada = RetonoInfEntrada("Data")
    resultaNotaEntrada = RetonoInfEntrada("Nota")
    resultaDivisaoEntrada = RetonoInfEntrada("Divisao")
    resultaVencimentoEntrada = RetonoInfEntrada("Vencimento")
    resultaVencimento2Entrada = RetonoInfEntrada("Vencimento2")
    resultaVencimento3Entrada = RetonoInfEntrada("Vencimento3")
    resultaVencimento4Entrada = RetonoInfEntrada("Vencimento4")
    resultadoSoma = 0
    
    tamanho = len(resultaTipoEntrada)

    def GetAtualizar(self):
        self.resultaTipoEntrada = RetonoInfEntrada("Tipo")
        self.resultaValorEntrada = RetonoInfEntrada("Valor")
        self.resultaDataEntrada = RetonoInfEntrada("Data")
        self.resultaNotaEntrada = RetonoInfEntrada("Nota")
        self.resultaDivisaoEntrada = RetonoInfEntrada("Divisao")
        self.resultaVencimentoEntrada = RetonoInfEntrada("Vencimento")
        self.resultaVencimento2Entrada = RetonoInfEntrada("Vencimento2")
        self.resultaVencimento3Entrada = RetonoInfEntrada("Vencimento3")
        self.resultaVencimento4Entrada = RetonoInfEntrada("Vencimento4")

    def GetTipo(self):
        self.GetAtualizar()
        return self.resultaTipoEntrada

    def GetValor(self):
        self.GetAtualizar()
        return self.resultaValorEntrada
    
    def GetData(self):
        self.GetAtualizar()
        return self.resultaDataEntrada
        
    def GetNota(self):
        self.GetAtualizar()
        return self.resultaNotaEntrada
    
    def GetDivisao(self):
        self.GetAtualizar()
        return self.resultaDivisaoEntrada
    
    def GetVencimento(self):
        self.GetAtualizar()
        return self.resultaVencimentoEntrada 
    
    def GetVencimento2(self):
        self.GetAtualizar()
        return self.resultaVencimento2Entrada
    
    def GetVencimento3(self):
        self.GetAtualizar()
        return self.resultaVencimento3Entrada

    def GetVencimento4(self):
        self.GetAtualizar()
        return self.resultaVencimento4Entrada
    
    def GetTamanho(self):
        self.GetAtualizar()
        return len(self.resultaTipoEntrada)
    
    def SetValores(self, tipo, valor, data, nota, divisao, vencimento,vencimento2="",vencimento3="",vencimento4=""):
        self.resultaTipoEntrada.append(tipo)
        self.resultaValorEntrada.append(valor)
        self.resultaDataEntrada.append(data)
        self.resultaNotaEntrada.append(nota)
        self.resultaDivisaoEntrada.append(divisao)
        self.resultaVencimentoEntrada.append(vencimento)
        self.resultaVencimento2Entrada.append(vencimento2)
        self.resultaVencimento3Entrada.append(vencimento3)
        self.resultaVencimento4Entrada.append(vencimento4)

    def SomaEntradas(self):
        self.resultadoSoma = 0
        for i in range(len(self.resultaValorEntrada)):
            self.resultadoSoma += self.resultaValorEntrada[i]
        return round(self.resultadoSoma,2)
    
    def AddPlanilha(self, tipo,valor,data,nota, divisao, vencimento, vencimento2="",vencimento3="", vencimento4=""):
        inputPlanilhaEntrada(tipo,valor,data,str(nota), divisao, vencimento, vencimento2,vencimento3, vencimento4)
    
    def RetornoVencimentoEntrada(Date):
        return filtroEntrada(Date)

    def RetornoPesquijaVencimentoEntrada(Metodo,DateInicial, DateFinal = 0):
        if Metodo == "1":
            return filtroEntradaPesquija(DateInicial)
        elif Metodo == "2":
            return filtroEntradaPerido(DateInicial, DateFinal)
        elif Metodo == "3":
            return filtroEntradaEspecifico(DateInicial)

class SaidaDados:
    
    resultaTipoSaida = RetonoInfSaida("Tipo")
    resultaValorSaida = RetonoInfSaida("Valor")
    resultaDataSaida = RetonoInfSaida("Data")
    resultaNotaSaida = RetonoInfSaida("Nota")
    resultaDivisaoSaida = RetonoInfSaida("Divisao")
    resultaVencimentoSaida = RetonoInfSaida("Vencimento")
    resultaVencimento2Saida = RetonoInfSaida("Vencimento2")
    resultaVencimento3Saida = RetonoInfSaida("Vencimento3")
    resultaVencimento4Saida = RetonoInfSaida("Vencimento4")
    resultadoSoma = 0
    
    tamanho = len(resultaTipoSaida)

    def GetAtualizar(self):
        self.resultaTipoSaida = RetonoInfSaida("Tipo")
        self.resultaValorSaida = RetonoInfSaida("Valor")
        self.resultaDataSaida = RetonoInfSaida("Data")
        self.resultaNotaSaida = RetonoInfSaida("Nota")
        self.resultaDivisaoSaida = RetonoInfSaida("Divisao")
        self.resultaVencimentoSaida = RetonoInfSaida("Vencimento")
        self.resultaVencimento2Saida = RetonoInfSaida("Vencimento2")
        self.resultaVencimento3Saida = RetonoInfSaida("Vencimento3")
        self.resultaVencimento4Saida = RetonoInfSaida("Vencimento4")

    def GetTipo(self):
        self.GetAtualizar()
        return self.resultaTipoSaida

    def GetValor(self):
        self.GetAtualizar()
        return self.resultaValorSaida
    
    def GetData(self):
        self.GetAtualizar()
        return self.resultaDataSaida 
    
    def GetNota(self):
        self.GetAtualizar()
        return self.resultaNotaSaida
        
    def GetDivisao(self):
        self.GetAtualizar()
        return self.resultaDivisaoSaida

    def GetVencimento(self):
        self.GetAtualizar()
        return self.resultaVencimentoSaida
    
    def GetVencimento2(self):
        self.GetAtualizar()
        return self.resultaVencimento2Saida
        
    def GetVencimento3(self):
        self.GetAtualizar()
        return self.resultaVencimento3Saida 
    
    def GetVencimento4(self):
        self.GetAtualizar()
        return self.resultaVencimento4Saida
    

    def GetTamanho(self):
        self.GetAtualizar()
        return len(self.resultaTipoSaida)
    
    def SetValores(self, tipo, valor, data, nota, divisao, vencimento,vencimento2="",vencimento3="",vencimento4=""):
        self.resultaTipoSaida.append(tipo)
        self.resultaValorSaida.append(valor)
        self.resultaDataSaida.append(data)
        self.resultaNotaSaida.append(nota)
        self.resultaDivisaoSaida.append(divisao)
        self.resultaVencimentoSaida.append(vencimento)
        self.resultaVencimento2Saida.append(vencimento2)
        self.resultaVencimento3Saida.append(vencimento3)
        self.resultaVencimento4Saida.append(vencimento4)

    def SomaSaida(self):
        self.resultadoSoma = 0
        for i in range(len(self.resultaValorSaida)):
            self.resultadoSoma += self.resultaValorSaida[i]
        return round(self.resultadoSoma,2)
    
    def AddPlanilha(self, tipo,valor,data,nota, divisao, vencimento, vencimento2="",vencimento3="", vencimento4=""):
        inputPlanilhaSaida(tipo,valor,data,str(nota), divisao, vencimento, vencimento2,vencimento3, vencimento4)

    def RetornoVencimentoSaida(Date):
        return filtroSaida(Date)
    
    def RetornoPesquijaVencimento(self,Metodo,DateInicial, DateFinal = 0):
        if Metodo == "1":
            return filtroSaidaPesquija(DateInicial)
        elif Metodo == "2":
            return filtroSaidaPerido(DateInicial, DateFinal)
        elif Metodo == "3":
            return filtroSaidaEspecifico(DateInicial)