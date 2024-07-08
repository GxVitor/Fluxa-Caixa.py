


from datetime import datetime
import json
from flask import Flask, flash , redirect , render_template, request, session
import pandas as pd
from ControleClass import EntradaDados, SaidaDados


app = Flask(__name__)
app.config['SECRET_KEY'] = "Admin"


#Instaciando a Class com os Dados
dadosEntrada = EntradaDados()
dadosSaida = SaidaDados()


#Pagina para o Usuario Logar
@app.route('/')
def login():
    return render_template('Login.html', name="Login")

#Verificar se o Usuario Existe no Sistima e Redireciona Ele para o index
@app.route('/verificar-login', methods = ["POST"])
def verificarLogin():

    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    with open("data/login.json" , 'r') as Login:
        dados = json.load(Login)

    for dado in dados:
        if dado["usuario"] == usuario and dado["senha"] == senha:

            return redirect("/Index")
        else:
            flash("Error no Login")
        
    return redirect("/")

# Ir para a tela inicial e mostrar as soma
@app.route('/Index')
def Index():
    session.clear()
    return render_template("index.html" , entrada=dadosEntrada.SomaEntradas(), saida=dadosSaida.SomaSaida(), total=round((dadosSaida.SomaSaida() - dadosEntrada.SomaEntradas()),2))


#Pagina Onde o Usuário podera ver as entradas e adiconar mais entrada
@app.route("/entrada")
def Entrada():

    return render_template("entrada.html", resultaTipo=dadosEntrada.GetTipo(),
                            resultaValor=dadosEntrada.GetValor(),
                            resultaData=dadosEntrada.GetData(), 
                            tamanho=dadosEntrada.GetTamanho(), 
                            notas=dadosEntrada.GetNota(), 
                            vencimento=dadosEntrada.GetVencimento())

@app.route("/saida")
def Saida():
    return render_template("saida.html", resultaTipo=dadosSaida.GetTipo(),
                            resultaValor=dadosSaida.GetValor(), 
                            resultaData=dadosSaida.GetData(), 
                            tamanho=dadosSaida.GetTamanho(),
                            notas=dadosSaida.GetNota(),
                            vencimento=dadosSaida.GetVencimento())


@app.route("/AddEntrada", methods = ["POST"])
def AddEntrada():
    tipo = request.form.get("TipoEntrada")
    valor = request.form.get("Valor")
    data = formatarData(request.form.get("data"))
    nota = request.form.get("nota")
    divisao = request.form.get("selecaoOpcoes")
    vencimento = formatarData(request.form.get("Vencimento"))


    if tipo == "":
        flash("Tipo de Entrada Está Nula")
        return redirect("/entrada")
    
    elif valor == "":
        flash("Tipo de Valor Está Nula")
        return redirect("/entrada")
    
    elif data == "":
        flash("Tipo de Data Está Nula")
        return redirect("/entrada")
    
    elif nota == "":
        flash("Tipo de Nota Está Nula")
        return redirect("/entrada")
    
    else:
        try:
            valor = float(valor)
            valor = float(valor)

            if divisao == "1":
                dadosEntrada.SetValores(tipo,valor,data ,nota , divisao, vencimento)
                dadosEntrada.AddPlanilha(tipo,valor,data ,nota, divisao, vencimento)
                flash("Aualizada com Sucesso")

                return redirect("/entrada")
            elif divisao == "2":
                vencimento2 = formatarData(request.form.get("Vencimento2"))
                dadosEntrada.SetValores(tipo,valor,data,nota , divisao,vencimento, vencimento2)
                dadosEntrada.AddPlanilha(tipo,valor,data,nota, divisao,vencimento, vencimento2)
                flash("Aualizada com Sucesso")

                return redirect("/entrada")
            
            elif divisao == "3":
                vencimento2 = formatarData(request.form.get("Vencimento2"))
                vencimento3 = formatarData(request.form.get("Vencimento3"))
                dadosEntrada.SetValores(tipo,valor,data,nota , divisao,vencimento, vencimento2, vencimento3)
                dadosEntrada.AddPlanilha(tipo,valor,data,nota, divisao,vencimento, vencimento2, vencimento3)
                flash("Aualizada com Sucesso")

                return redirect("/entrada")
            
            elif divisao == "4":
                vencimento2 = formatarData(request.form.get("Vencimento2"))
                vencimento3 = formatarData(request.form.get("Vencimento3"))
                vencimento4 = formatarData(request.form.get("Vencimento4"))
                dadosEntrada.SetValores(tipo,valor,data,nota , divisao, vencimento, vencimento2, vencimento3, vencimento4)
                dadosEntrada.AddPlanilha(tipo,valor,data,nota, divisao, vencimento, vencimento2,vencimento3, vencimento4)
                flash("Aualizada com Sucesso")

                return redirect("/entrada")

        except ValueError :
            flash("Somente Numeros No Campo Valor")
            return redirect("/entrada")

@app.route("/AddSaida", methods = ["POST"])
def AddSaida():
    tipo = request.form.get("TipoEntrada")
    valor = request.form.get("Valor")
    data = formatarData(request.form.get("data"))
    nota = request.form.get("nota")
    divisao = request.form.get("selecaoOpcoes")
    vencimento = formatarData(request.form.get("Vencimento"))

    if tipo == "":
        flash("Tipo de Saida Está Nula")
        return redirect("/saida")
    
    elif valor == "":
        flash("Tipo de Valor Está Nula")
        return redirect("/saida")
    
    elif data == "":
        flash("Tipo de Data Está Nula")
        return redirect("/saida")
    
    elif nota == "":
        flash("Tipo de Nota Está Nula")
        return redirect("/saida")
    
    else:
        try:
            valor = float(valor)

            if divisao == "1":
                dadosSaida.SetValores(tipo,valor,data ,nota , divisao, vencimento)
                dadosSaida.AddPlanilha(tipo,valor,data ,nota, divisao, vencimento)
                flash("Aualizada com Sucesso")

                return redirect("/saida")
            elif divisao == "2":
                vencimento2 = formatarData(request.form.get("Vencimento2"))
                dadosSaida.SetValores(tipo,valor,data,nota , divisao,vencimento, vencimento2)
                dadosSaida.AddPlanilha(tipo,valor,data,nota, divisao,vencimento, vencimento2)
                flash("Aualizada com Sucesso")

                return redirect("/saida")
            
            elif divisao == "3":
                vencimento2 = formatarData(request.form.get("Vencimento2"))
                vencimento3 = formatarData(request.form.get("Vencimento3"))
                dadosSaida.SetValores(tipo,valor,data,nota , divisao,vencimento, vencimento2, vencimento3)
                dadosSaida.AddPlanilha(tipo,valor,data,nota, divisao,vencimento, vencimento2, vencimento3)
                flash("Aualizada com Sucesso")

                return redirect("/saida")
            
            elif divisao == "4":
                vencimento2 = formatarData(request.form.get("Vencimento2"))
                vencimento3 = formatarData(request.form.get("Vencimento3"))
                vencimento4 = formatarData(request.form.get("Vencimento4"))
                dadosSaida.SetValores(tipo,valor,data,nota , divisao,vencimento, vencimento2, vencimento3, vencimento4)
                dadosSaida.AddPlanilha(tipo,valor,data,nota, divisao, vencimento, vencimento2,vencimento3, vencimento4)
                flash("Aualizada com Sucesso")

                return redirect("/saida")


        except ValueError :
            flash("Somente Numeros No Campo Valor")
            return redirect("/saida")

@app.route("/vencimento-saida")
def vencimento():
    #Pegando a Data Atual
    data_atual = datetime.now()
    data_atual = formatarData(data_atual)

    vencimento = SaidaDados.RetornoVencimentoSaida(data_atual)
    pesquija = session.get('pesquisa', "")


    if len(pesquija) == 0:
        flash("Sem Resultado")
        return render_template("vencimento-saida.html",
                                DataAtual = data_atual,
                                tamanho = len(vencimento["Tipo"]),
                                vencimento= vencimento["Vencimento"].tolist(),
                                notas= vencimento["Nota"].tolist(),
                                resultaTipo = vencimento["Tipo"].tolist(),
                                resultaValor = vencimento["Valor"].tolist(),
                                tamanhoPesquija = 0
                                )
    else:
        if pesquija is None:
                flash("Sem Resultado")
                return render_template("vencimento-saida.html",
                                        DataAtual = data_atual,
                                        tamanho = len(vencimento["Tipo"]),
                                        vencimento= vencimento["Vencimento"].tolist(),
                                        notas= vencimento["Nota"].tolist(),
                                        resultaTipo = vencimento["Tipo"].tolist(),
                                        resultaValor = vencimento["Valor"].tolist(),
                                        tamanhoPesquija = 0
                                        )
        else:
            flash("Resultado Ta Tabela de Baixo")
            pesquija = pd.DataFrame(pesquija)
            return render_template("vencimento-saida.html",
                            DataAtual = data_atual,
                            tamanho = len(vencimento["Tipo"]),
                            vencimento= vencimento["Vencimento"].tolist(),
                            notas= vencimento["Nota"].tolist(),
                            resultaTipo = vencimento["Tipo"].tolist(),
                            resultaValor = vencimento["Valor"].tolist(),

                                tamanhoPesquija = len(pesquija["Tipo"]),
                                vencimentoPesquija= pesquija["Vencimento"].tolist(),
                                vencimentoPesquija2= pesquija["Vencimento2"].tolist(),
                                vencimentoPesquija3= pesquija["Vencimento3"].tolist(),
                                vencimentoPesquija4= pesquija["Vencimento4"].tolist(),
                                notasPesquija = pesquija["Nota"].tolist(),
                                resultaTipoPesquija = pesquija["Tipo"].tolist(),
                                resultaValorPesquija = pesquija["Valor"].tolist(),
                                resultaDivididoPesquija = pesquija["Divisao"].tolist(),
                            )


@app.route("/vencimento-entrada")
def vencimentoEntrada():
    #Pegando a Data Atual
    data_atual = datetime.now()
    data_atual = formatarData(data_atual)

    vencimento = EntradaDados.RetornoVencimentoEntrada(data_atual)
    pesquija = session.get('pesquisaEntrada', "")


    if len(pesquija) == 0:
        flash("Sem Resultado")
        return render_template("vencimento-entrada.html",
                                DataAtual = data_atual,
                                tamanho = len(vencimento["Tipo"]),
                                vencimento= vencimento["Vencimento"].tolist(),
                                notas= vencimento["Nota"].tolist(),
                                resultaTipo = vencimento["Tipo"].tolist(),
                                resultaValor = vencimento["Valor"].tolist(),
                                tamanhoPesquija = 0
                                )
    else:
        if pesquija is None:
                flash("Sem Resultado")
                return render_template("vencimento-entrada.html",
                                        DataAtual = data_atual,
                                        tamanho = len(vencimento["Tipo"]),
                                        vencimento= vencimento["Vencimento"].tolist(),
                                        notas= vencimento["Nota"].tolist(),
                                        resultaTipo = vencimento["Tipo"].tolist(),
                                        resultaValor = vencimento["Valor"].tolist(),
                                        tamanhoPesquija = 0
                                        )
        else:
            flash("Resultado Ta Tabela de Baixo")
            pesquija = pd.DataFrame(pesquija)
            return render_template("vencimento-entrada.html",
                            DataAtual = data_atual,
                            tamanho = len(vencimento["Tipo"]),
                            vencimento= vencimento["Vencimento"].tolist(),
                            notas= vencimento["Nota"].tolist(),
                            resultaTipo = vencimento["Tipo"].tolist(),
                            resultaValor = vencimento["Valor"].tolist(),

                                tamanhoPesquija = len(pesquija["Tipo"]),
                                vencimentoPesquija= pesquija["Vencimento"].tolist(),
                                vencimentoPesquija2= pesquija["Vencimento2"].tolist(),
                                vencimentoPesquija3= pesquija["Vencimento3"].tolist(),
                                vencimentoPesquija4= pesquija["Vencimento4"].tolist(),
                                notasPesquija = pesquija["Nota"].tolist(),
                                resultaTipoPesquija = pesquija["Tipo"].tolist(),
                                resultaValorPesquija = pesquija["Valor"].tolist(),
                                resultaDivididoPesquija = pesquija["Divisao"].tolist(),
                            )


@app.route("/BuscarPorDataEntrada", methods = ["POST"])
def BuscarVencimentoEntrada():
    DataInicial = formatarData(request.form.get("DataInicialEntrada"))
    MetodoPesquisa = request.form.get("selecaoOpcoes")

    print(DataInicial)
    if DataInicial == "":
        flash("Data Não Definida")
        return redirect("/vencimento-entrada")

    print(f"Opção {MetodoPesquisa}")
    if MetodoPesquisa == "1":
            session['pesquisaEntrada'] = EntradaDados.RetornoPesquijaVencimentoEntrada(MetodoPesquisa,DataInicial)
       
    elif MetodoPesquisa == "2":
            DataFinal = formatarData(request.form.get("DataFinalEntrada"))
            session['pesquisaEntrada'] = EntradaDados.RetornoPesquijaVencimentoEntrada(MetodoPesquisa,DataInicial,DataFinal)
        
    elif MetodoPesquisa == "3":
            session['pesquisaEntrada'] = EntradaDados.RetornoPesquijaVencimentoEntrada(MetodoPesquisa,DataInicial)

    return redirect("/vencimento-entrada")


@app.route("/BuscarPorData", methods = ["POST"])
def BuscarVencimento():
    DataInicial = formatarData(request.form.get("DataInicial"))
    MetodoPesquisa = request.form.get("selecaoOpcoes")

    if DataInicial == "":
        flash("Data Não Definida")
        return redirect("/vencimento-saida")

    print(f"Opção {MetodoPesquisa}")
    if MetodoPesquisa == "1":
            session['pesquisa'] = dadosSaida.RetornoPesquijaVencimento(MetodoPesquisa,DataInicial)
       
    elif MetodoPesquisa == "2":
            DataFinal = formatarData(request.form.get("DataFinal"))
            session['pesquisa'] = dadosSaida.RetornoPesquijaVencimento(MetodoPesquisa,DataInicial,DataFinal)
        
    elif MetodoPesquisa == "3":
            session['pesquisa'] = dadosSaida.RetornoPesquijaVencimento(MetodoPesquisa,DataInicial)

    

    return redirect("/vencimento-saida")

def converter_data(data_str):
    return datetime.strptime(data_str, "%d/%m/%y")

def formatarData(data):
    # Converta a data para um objeto datetime, caso ainda não seja
    if not isinstance(data, datetime):
        data = datetime.strptime(data, "%Y-%m-%d")

    # Formate a data no formato "dd/mm/yyyy"
    data_formatada = data.strftime("%d/%m/%Y")

    return data_formatada


def start_server():
    app.run()




if __name__ == '__main__':
    app.run()
    #flask_thread = threading.Thread(target=start_server)
    #flask_thread.daemon = True
    #flask_thread.start()
   
   # Aguarde um momento para garantir que o servidor Flask esteja em execução
    #import time
    #time.sleep(1)

    # Abra o WebView para acessar o aplicativo Flask
    #webview.create_window("Fluxo - Caixa", "http://localhost:5000")
    #webview.start()