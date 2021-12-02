### PYMATH ###
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
from tkinter import *
from tkinter import filedialog
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import webbrowser


class Aplication():

    def __init__(self): # Define os parâmetros da classe
        '''
        Função que define os parâmetros da classe
        Todas esse parâmetros serão iniciados junto com o início do programa
        '''
        root = Tk() # Janela da Interface
        self.root = root
        self.arquivo_salvo = False
        self.tela() # Função de configurações da Janela
        self.frames() # Função de divisões da Tela
        self.label() # Função de criação dos Textos
        self.botoes() # Função de criação dos Botões
        self.Menus() # Função de Barra de Menu
        root.mainloop() # Faz a Interface rodar em loop

    def tela(self): # Configurações da Tela
        '''
        Função que define as configurações da tela, como:
        - Título;
        - Cor de fundo;
        - Tamanho.
        '''
        self.root.title("Pymath") # Título
        self.root.configure(background = 'turquoise1') # Cor principal 
        self.root.geometry("750x650") # Tamanho da Interface 
        self.root.resizable(False, False) # Tamanho fixo

    def frames(self): # Divisões da Tela
        '''
        Função de cria os frames da tela e configurações:
        - Em que Interface está inserido;
        - Cor e grossura da Borda;
        - Cor do Frame.
        '''
        # Caixa 1 - Introdução #
        self.frame_1 = Frame(self.root, bd = 4, bg = 'white', highlightbackground = 'gray60', highlightthickness = 4)
        self.frame_1.place(relx = 0.05, rely = 0.02, relwidth = 0.42, relheight = 0.2)
        # Caixa 2 - Arquivo #
        self.frame_2 = Frame(self.root, bd = 4, bg = 'white', highlightbackground = 'gray60', highlightthickness = 4)
        self.frame_2.place(relx = 0.05, rely = 0.24, relwidth = 0.42, relheight = 0.06)
        # Caixa 4 - Erro #
        self.frame_4 = Frame(self.root, bd = 4, bg = 'white', highlightbackground = 'gray60', highlightthickness = 4)
        self.frame_4.place(relx = 0.05, rely = 0.32, relwidth = 0.42, relheight = 0.06)
        # Caixa 6 - Regressão Linear Simples #
        self.frame_6 = Frame(self.root, bd = 4, bg = 'white', highlightbackground = 'gray60', highlightthickness = 4)
        self.frame_6.place(relx = 0.09, rely = 0.43, relwidth = 0.35, relheight = 0.08)
        # Caixa 7 - Padrão #
        self.frame_7 = Frame(self.root, bd = 4, bg = 'white', highlightbackground = 'gray60', highlightthickness = 4)
        self.frame_7.place(relx = 0.05, rely = 0.53, relwidth = 0.42, relheight = 0.1)
        # Caixa 8 - MonoLog #
        self.frame_8 = Frame(self.root, bd = 4, bg = 'white', highlightbackground = 'gray60', highlightthickness = 4)
        self.frame_8.place(relx = 0.05, rely = 0.65, relwidth = 0.42, relheight = 0.1)
        # Caixa 9 - DiLog #
        self.frame_9 = Frame(self.root, bd = 4, bg = 'white', highlightbackground = 'gray60', highlightthickness = 4)
        self.frame_9.place(relx = 0.05, rely = 0.77, relwidth = 0.42, relheight = 0.1)
        # Caixa 10 - Cálculos #
        self.frame_10 = Frame(self.root, bd = 4, bg = 'white', highlightbackground = 'gray60', highlightthickness = 4)
        self.frame_10.place(relx = 0.52, rely = 0.02, relwidth = 0.42, relheight = 0.85)

    def label(self): # Criação dos Textos
        '''
        Cria Labels (textos) e Entrys (caixas de entarda) dentro da interface.
        Esses Labels e Entrys estrão posicionados dem determinados frames.
        '''
        # Texto 1 - Introdução
        self.lb_intro = Label(self.frame_1, text="Bem-Vindo ao Pymath!", bd=4, bg='gray86', fg='black', font=('Cambria Math',20))
        self.lb_intro.place(relx=0, rely=0, relwidth=1, relheight=1)
        # Texto 3 - Erro
        self.lb_erro = Label(self.frame_4, text="Desvio Padrão de Dados:", bd=1, bg='white', fg='black')
        self.lb_erro.place(relx=0, rely=0)
        # Entrada 2 - Erro
        self.erro_entry = Entry(self.frame_4, bd=2)
        self.erro_entry.place(relx=0.46, rely=0, relwidth=0.54, relheight=1)
        # Texto 4 - Cálculos
        self.lb_calculos = Label(self.frame_10, text="Cálculos:", bd=4, bg='gray86', fg='black', font=('Cambria Math',20))
        self.lb_calculos.place(relx=0, rely=0, relwidth=1, relheight=0.1)

    def upload_arq(self): # Função para abrir o seletro de arquvios
        '''
        Abre o Seletor de Arquivo e salva o Arquivo de Dados selecionado pelo usuário
        '''
        if self.arquivo_salvo == False:
            self.file = filedialog.askopenfilename(filetypes=[('Arquivos Texto','*.txt'), ('Todos os Arquviso', '*.*')])
            self.arq = open(self.file,'r')
            self.arquivo_salvo = True
        else:
            self.arq = open(self.file,'r')
        x, y = np.genfromtxt(self.arq, unpack=True)
        return x, y

    def read_arq(self): # Função que le os dados X e Y do Arquvio
        '''
        Le o arquivo de Dados previamente selecionado pelo usuário
        '''
        x, y = np.genfromtxt(self.arq, unpack=True)
        return x, y

    def erro(self): # Função que receberá o valor para as Barras de Erro
        '''
        Recebe o Desvio Padrão dos Dados inserido pelo usuário na Entry da Interface
        '''
        erro = self.erro_entry.get() # Caixa de entrada do Desvio Padrão
        erro = float(erro) # Transforma o Desvio Padrão em um número decimal
        return erro

    def reg_lin(self): # Função da Regressão Linear
        '''
        Realiza os cálculos da Regressão Linear Simples.
        Cria o arquivo PDF com as contas da Regressão Linear Simples.
        '''
        x, y = self.upload_arq() # Chama os dados de X e Y
        n = x.size # Determina a quantidade de valor de X e, consequentemente, Y.
        # FÓRMULAS #
        Sx = sum(x) # Soma de todos os valores de X.
        Sy = sum(y) # Soma de todos os valores de Y.
        Sx2 = (x**2).sum() # Soma de todos os valores de X elevados a 2.
        Sy2 = (y**2).sum() # Soma de todos os valores de Y elevados a 2.
        Sxy = (x*y).sum() # Soma de todos os valores de X multiplicados aos valores de Y.

        Mx = np.mean(x) # Valor médio de X.
        My = np.mean(y) # Valor médio de Y.
            
        A = Sx2 - (Sx**2)/n
        B = Sxy - (Sx*Sy)/n
        C = Sy2 - (Sy**2)/n
            
        a = B/A
        a = float("%.4f" % a)
        b = My - a*Mx
        b = float("%.4f" % b)

        CORR = np.sqrt((B**2)/(A*C))
        func = f'{b:+} {a:+}x' # Função na forma de y = b + ax
        yi = [b + a*m for m in x]

        # Texto com os símbolos e resultados da Regressão Linear #
        calculos = f'''
        ∑x = {"%.4f" % Sx}      
        ∑y = {"%.4f" % Sy}      
        ∑(x²) = {"%.4f" % Sx2}      
        ∑(y²) = {"%.4f" % Sy2}      
        ∑(x.y) = {"%.4f" % Sxy}     

        μx = {"%.4f" % Mx}      
        μy = {"%.4f" % My}      

        A = {"%.4f" % A}        
        B = {"%.4f" % B}        
        C = {"%.4f" % C}        

        a = {a}     
        b = {b}     

        CORR = {"%.4f" % CORR}      

        y = {func}      
        '''
        
        # PDF que contém o Texto anterior #
        pdf = canvas.Canvas("Regressao_Linear.pdf", pagesize = A4) # Gerando PDF
        pdf.setFont("Times-Roman", 14) # Definindo fonte e tamanho
        pdf.drawCentredString(297, 250, 'Obrigado por usar o Pymath!') # Mensagem de agradecimento
        pdf.drawString(90, 675, 'Cálculos da Regressão Linear:') # Definido o conteúdo do PDF
        pdf.drawString(90, 650, f'∑X = {Sx}')
        pdf.drawString(90, 625, f'∑Y = {Sy}')
        pdf.drawString(90, 600, f'∑(X²) = {Sx2}')
        pdf.drawString(90, 575, f'∑(Y²) = {Sy2}')
        pdf.drawString(90, 550, f'∑(X.Y) = {Sxy}')
        pdf.drawString(90, 500, f'μx = {Mx}')
        pdf.drawString(90, 525, f'μy = {My}')
        pdf.drawString(90, 475, f'A = {A}')
        pdf.drawString(90, 450, f'B = {B}')
        pdf.drawString(90, 425, f'C = {C}')
        pdf.drawString(90, 375, f'CORR = {CORR}')
        pdf.drawCentredString(297, 325, 'Equação da reta:')
        pdf.drawCentredString(297, 300, f'y = {func}')

        return calculos, yi, pdf

    def impres_reglin(self): # Função que imprime a Regressão Linear na Interface
        '''
        Exibe os cálculos da Regressão Linear Simples na interface.
        Faz o download do PDF para o usuário.
        '''
        calculos, yi, pdf = self.reg_lin() # Chama o texto com os símbolos e resultados da Regressão Linear
        self.imp = Label(self.frame_10, text=f'{calculos}', font=('Arial', 14), bg='white')
        self.imp.place(relx = 0.16, rely = 0.15, relwidth = 0.70, relheight = 0.80)
        self.imp.pack
        pdf.save()

    def graf_padrao(self): # Função que criará o Gráfico em escala Padrão
        '''
        Cria o Gráfico em escala Linear, com Barras de Erro e Reta da Regressão Linear Simples
        '''
        x, y = self.upload_arq() # Chama os dados de X e Y
        calculos, yi, pdf = self.reg_lin()
        erro = self.erro() # Chama o valor do Erro
        fig = plt.figure() # Cria uma Figura para o Gráfico
        grid = gs.GridSpec(7, 3) # Define o tamanho como uma grade para a Figura
        grafico = fig.add_subplot(grid[:5, :]) # Define o espaço da Figura que será ocupada pelo Gráfico
        grafico.grid(True) # Ativa as linhas de grade no Gráfico
        plt.title('Gráfico Padrão X × Y') # Título do Gráfico
        plt.plot(x, yi) # Cria a Reta da Regressão Linear Simples
        plt.errorbar(x, y, yerr=erro, fmt='ro', ecolor='black', linestyle=None, capsize=2) # Cria as Barras de Erro, com pontos vermelhos (ro)
        plt.xscale('linear') # Escala linear do Eixo X
        plt.yscale('linear') # Escala linear do Eixo Y
        plt.show() # Exibe o Gráfico
    def graf_mlog(self): # Função que criará o Gráfico em escala Mono-Log
        '''
        Cria o Gráfico em escala Mono-Log
        Eixo X em escala linear e Eixo Y em escala logarítmica
        '''
        x, y = self.upload_arq() # Chama os dados de X e Y
        fig = plt.figure() # Cria uma Figura para o Gráfico
        grid = gs.GridSpec(7, 3) # Define o tamanho como uma grade para a Figura
        grafico = fig.add_subplot(grid[:5, :]) # Define o espaço da Figura que será ocupada pelo Gráfico
        grafico.grid(True) # Ativa as linhas de grade no Gráfico
        plt.title('Gráfico Mono-Log X × Y') # Título do Gráfico
        plt.plot(x, y, '-o') # Os pontos de X e Y serão marcados por pontos (o) e ligados por linhas contínuas (-)
        plt.xscale('linear') # Escala linear do Eixo X
        plt.yscale('log') # Escala logarítmica do Eixo Y
        plt.show() # Exibe o Gráfico
    def graf_dlog(self): # Função que criará o Gráfico em escala Di-Log
        '''
        Cria o gráfico em escala Di-Log, com ambos os eixos com escala logarítmica
        '''
        x, y = self.upload_arq() # Chama os dados de X e Y
        fig = plt.figure() # Cria uma Figura para o Gráfico
        grid = gs.GridSpec(7, 3) # Define o tamanho como uma grade para a Figura
        grafico = fig.add_subplot(grid[:5, :]) # Define o espaço da Figura que será ocupada pelo Gráfico
        grafico.grid(True) # Ativa as linhas de grade no Gráfico
        plt.title('Gráfico Di-Log X × Y') # Título do Gráfico
        plt.plot(x, y, '-o') # Os pontos de X e Y serão marcados por pontos (o) e ligados por linhas contínuas (-)
        plt.xscale('log') # Escala logarítmica do Eixo X
        plt.yscale('log') # Escala logarítmica do Eixo Y
        plt.show() # Exibe o Gráfico

    def botoes(self): # Função de criação dos Botões
        '''
        Cria os botões presnetes na interface, com os seguintes comando:
        - Fazer upload do Arquivo de Dados;
        - Cálcular e exibir a Regressão Linear, além de fazer o download do arquivo PDF;
        - Plotar os gráficos, cada um por um botão específico.
        '''
        # Botão 1 - Upload Arquivo
        self.bt_uparq = Button(self.frame_2, text = "Inserir Arquvio de Dados", command=self.upload_arq, bd = 2, bg = 'gray88', fg = 'black', font = ('Cambria Math', 9))
        self.bt_uparq.place(relx = 0, rely = 0, relwidth = 0.99, relheight = 1)
        # Botão 3 - Regressão 
        self.bt_regress = Button(self.frame_6, text = "Regressão Linear Simples", command=self.impres_reglin, bd = 4, bg = 'gray88', fg = 'black', font = ('Cambria Math', 13))
        self.bt_regress.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        # Botão 4 - Gráfico Padrão 
        self.bt_pad = Button(self.frame_7, text = "Gráfico Padrão", command=self.graf_padrao, bd = 4, bg = 'gray88', fg = 'black', font = ('Cambria Math', 16))
        self.bt_pad.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        # Botão 5 - Gráfico MonoLog
        self.bt_mono = Button(self.frame_8, text = "Gráfico Mono-Log", command=self.graf_mlog, bd = 4, bg = 'gray88', fg = 'black', font = ('Cambria Math', 16))
        self.bt_mono.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        # Botão 6 - Gráfico DiLog
        self.bt_di = Button(self.frame_9, text = "Gráfico Di-Log", command=self.graf_dlog, bd = 4, bg = 'gray88', fg = 'black', font = ('Cambria Math', 16))
        self.bt_di.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

    def Menus(self): # Função que cria o Menu
        '''
        Cria a Barra de Menu, com as seguintes funções:
        - Botão para reiniciar o programa, limpando o Arquivo de Dados, o valor do Desvio Padrão dos Dados 
        e a exibição da Regressão Linear Simples;
        - Botão de ajuda, que leva o usuário ao site do Pymath
        '''
        menubar = Menu(self.root) # Cria a barra de Menu
        self.root.config(menu=menubar)
        menu_opc = Menu(menubar, tearoff=0) # Cria 1ª Caixa na barra de Menu
        menu_ajd = Menu(menubar, tearoff=0) # Cria 2ª Caixa na barra de Menu
        menubar.add_cascade(label = "Opções", menu = menu_opc) # Nomeia de 'Opções' a 1ª Caixa do Menu
        menubar.add_cascade(label = "Ajuda", menu = menu_ajd) # Nomeia de 'Ajuda' a 2ª Caixa do Menu
        def reset(): # Função para Reiniciar o Pymath
            '''
            Função de permite a reinicialização.
            '''
            self.arquivo_salvo = False
            self.erro_entry.delete(0, END) # Limpa a entrada do Desvio Padrão
            # Limpa os cálculos da Regressão Linear
            self.imp = Label(self.frame_10, text="", font = ('Arial', 14), bg='white')
            self.imp.place(relx = 0.16, rely = 0.15, relwidth = 0.70, relheight = 0.80)
            self.imp.pack
        def openweb(): # Função com o link do Site do Pymath
            '''
            Função com o link do site do Pymath
            '''
            url = "https://sites.google.com/usp.br/pymath/como-utilizar-o-pymath" # Link do Site do Pymath
            webbrowser.open_new(url)
        menu_opc.add_command(label="Reiniciar", command=reset) # Botão que executa a Reinicialização
        menu_ajd.add_command(label = "Site Python", command=openweb) # Botão que abre o Site do Pymath

    help(__init__)
    help(tela)
    help(frames)
    help(label)
    help(upload_arq)
    help(read_arq)
    help(erro)
    help(reg_lin)
    help(impres_reglin)
    help(graf_padrao)
    help(graf_mlog)
    help(graf_dlog)
    help(botoes)
    help(Menus)

Aplication()