from tkinter import *
import math

def limpar_frame2():
    # Limpa o frame 2
    for widget in fr_frame2.winfo_children():
        widget.destroy()
        
def limpar_frame3():
    # Limpa o frame 3
    for widget in fr_frame3.winfo_children():
        widget.destroy()

# pede os dados da planta e inclui no arquivo plantas.txt
def incluir():
    fr_frame3.grid_remove()
    limpar_frame3()
    limpar_frame2()

    label_planta = Label(fr_frame2, text="Insira os Dados Abaixo")
    label_planta.grid(column=1, row=2, padx=10, pady=10)

    entry_planta = Entry(fr_frame2, width=10)
    entry_planta.grid(column=2, row=4, padx=10, pady=10)
    label_resultado = Label(fr_frame2, text="Nome da planta: ")
    label_resultado.grid(column=1, row=4, padx=10, pady=10)

    entry_fase = Entry(fr_frame2, width=10)
    entry_fase.grid(column=2, row=5, padx=10, pady=10)
    label_resultado = Label(fr_frame2, text="Fase da vida da planta:\n(crescimento inicial, desenvolvimento vegetativo, reprodução) ")
    label_resultado.grid(column=1, row=5, padx=10, pady=10)

    entry_adubo = Entry(fr_frame2, width=10)
    entry_adubo.grid(column=2, row=6, padx=10, pady=10)
    label_resultado = Label(fr_frame2, text="Adubo recomendado(N/P/K):\nEx: 4/14/8 ")
    label_resultado.grid(column=1, row=6, padx=10, pady=10)

    button = Button(fr_frame2, text="Enviar", command=lambda: salvar_dados(entry_planta, entry_fase, entry_adubo, label_resultado))
    button.grid(column=1, row=7, padx=10, pady=10)
    
def salvar_dados(entry_planta, entry_fase, entry_adubo, label_resultado):
    planta = entry_planta.get()
    fase = entry_fase.get()
    adubo = entry_adubo.get()

    with open("plantas.txt", "a") as arquivo_planta:
        arquivo_planta.write(f"{planta};{fase};{adubo};\n")
    
# exclui a planta e seus dados do plantas.txt
def excluir():
    fr_frame3.grid_remove()
    limpar_frame2()
    
    planta_excluir = Entry(fr_frame2, width=10)
    planta_excluir.grid(column=1, row=3)
    label_resultado = Label(fr_frame2, text="Insira o nome da planta a ser removida: ")
    label_resultado.grid(column=1, row=2)
    
    button = Button(fr_frame2, text="Enviar", command=lambda: excluir_dados(planta_excluir))
    button.grid(column=1, row=4)

def excluir_dados(planta_excluir):
    linhas_sem_palavra = []
    
    planta = planta_excluir.get()
    
    # le os arquivos dentro do arquivo e escreve novamente aqueles que não tem a planta desejada
    with open("plantas.txt", "r+") as arquivo_planta:
        linha = arquivo_planta.readline()
    
        while linha:
            if planta not in linha:
                linhas_sem_palavra.append(linha)
            linha = arquivo_planta.readline()
            
    arquivo_planta.close()
        
    with open("plantas.txt", "w") as arquivo_planta:
        arquivo_planta.writelines(linhas_sem_palavra)
        
    arquivo_planta.close()

# botoes para decidir entre incluir e excluir dados
def personalizar():
    fr_frame3.grid_remove()    
    limpar_frame2()
    
    botao_incluir = Button(fr_frame2, text="Incluir Dados", command=incluir)
    botao_incluir.grid(column=1, row=1, padx=10, pady=10)
    
    botao_excluir = Button(fr_frame2, text="Excluir Dados", command=excluir)
    botao_excluir.grid(column=2, row=1, padx=10, pady=10)
    
# le todas as linhas de plantas.txt e as escreve na tela
def informacoes():
    fr_frame3.grid_remove()
    limpar_frame2()

    plantas_lista = []
    with open("plantas.txt", "r") as arquivo_planta:
        linha = arquivo_planta.readline()
        while linha:
            item = linha.strip().split(';')
            planta = item[0]
            fase = item[1]
            npk = item[2]
            texto_formatado = f"{planta}\n{fase}\n{npk}"
            plantas_lista.append(texto_formatado)
            linha = arquivo_planta.readline()

    for i, item in enumerate(plantas_lista):
        label_planta = Label(fr_frame2, bg='white', text=item)
        label_planta.grid(column=1, row=i+1, padx=20, pady=20)
        
# pede qual o recipiente que sera utilizado e calcula conforme especificado
def adubo():
    fr_frame3.grid()
    limpar_frame3()
    limpar_frame2()
    botao_tronco_piramide = Button(fr_frame2, text="Tronco Pirâmide", command=tronco_piramide)
    botao_tronco_piramide.grid(column=1, row=0, padx=20, pady=20)
    
    botao_tronco_cone = Button(fr_frame2, text="Tronco de Cone", command=tronco_cone)
    botao_tronco_cone.grid(column=1, row=1, padx=20, pady=20)
    
    botao_cone = Button(fr_frame2, text="Cone", command=cone)
    botao_cone.grid(column=1, row=2, padx=20, pady=20)
    
    botao_cilindro = Button(fr_frame2, text="Cilindro", command=cilindro)
    botao_cilindro.grid(column=1, row=3, padx=20, pady=20)

    botao_cubo = Button(fr_frame2, text="Cubo", command=cubo)
    botao_cubo.grid(column=1, row=4, padx=20, pady=20)
    
def cubo():
    limpar_frame3()

    label_altura = Label(fr_frame3, text="Altura (cm): ", bg='white')
    label_altura.grid(column=2, row=2, padx=20, pady=20)
    entry_altura = Entry(fr_frame3)
    entry_altura.grid(column=3, row=2, padx=20, pady=20)
    
    i = 2

    nome_fase(i)

    button_calcular = Button(fr_frame3, text="Enviar", command=lambda: calcular_cubo(entry_altura))
    button_calcular.grid(column=2, row=7, padx=20, pady=20)
    
def cilindro():
    limpar_frame3()

    label_raio = Label(fr_frame3, text="Raio (cm): ", bg='white')
    label_raio.grid(column=2, row=2, padx=20, pady=20)
    entry_raio = Entry(fr_frame3)
    entry_raio.grid(column=3, row=2, padx=20, pady=20)

    label_altura = Label(fr_frame3, text="Altura (cm): ", bg='white')
    label_altura.grid(column=2, row=3, padx=20, pady=20)
    entry_altura = Entry(fr_frame3)
    entry_altura.grid(column=3, row=3, padx=20, pady=20)
    
    i = 3

    nome_fase(i)

    button_calcular = Button(fr_frame3, text="Enviar", command=lambda: calcular_cilindro(entry_raio, entry_altura))
    button_calcular.grid(column=2, row=7, padx=20, pady=20)
    
def cone():
    limpar_frame3()

    label_raio = Label(fr_frame3, text="Raio (cm): ", bg='white')
    label_raio.grid(column=2, row=2, padx=20, pady=20)
    entry_raio = Entry(fr_frame3)
    entry_raio.grid(column=3, row=2, padx=20, pady=20)

    label_altura = Label(fr_frame3, text="Altura (cm): ", bg='white')
    label_altura.grid(column=2, row=3, padx=20, pady=20)
    entry_altura = Entry(fr_frame3)
    entry_altura.grid(column=3, row=3, padx=20, pady=20)
    
    i = 3

    nome_fase(i)

    button_calcular = Button(fr_frame3, text="Enviar", command=lambda: calcular_cone(entry_raio, entry_altura))
    button_calcular.grid(column=2, row=7, padx=20, pady=20)
    
def tronco_piramide():
    limpar_frame3()

    label_base_maior = Label(fr_frame3, text="Base Maior (cm²): ", bg='white')
    label_base_maior.grid(column=2, row=2, padx=20, pady=20)
    entry_base_maior = Entry(fr_frame3)
    entry_base_maior.grid(column=3, row=2, padx=20, pady=20)

    label_base_menor = Label(fr_frame3, text="Base Menor (cm²): ", bg='white')
    label_base_menor.grid(column=2, row=3, padx=20, pady=20)
    entry_base_menor = Entry(fr_frame3)
    entry_base_menor.grid(column=3, row=3, padx=20, pady=20)

    label_altura = Label(fr_frame3, text="Altura (cm): ", bg='white')
    label_altura.grid(column=2, row=4, padx=20, pady=20)
    entry_altura = Entry(fr_frame3)
    entry_altura.grid(column=3, row=4, padx=20, pady=20)
    
    i = 4

    nome_fase(i)

    button_calcular = Button(fr_frame3, text="Enviar", command=lambda: calcular_piramide(entry_base_maior, entry_base_menor, entry_altura))
    button_calcular.grid(column=2, row=7, padx=20, pady=20)
    
def tronco_cone():
    limpar_frame3()

    label_raio_maior = Label(fr_frame3, text="Raio Maior (cm): ", bg='white')
    label_raio_maior.grid(column=2, row=2, padx=20, pady=20)
    entry_raio_maior = Entry(fr_frame3)
    entry_raio_maior.grid(column=3, row=2, padx=20, pady=20)

    label_raio_menor = Label(fr_frame3, text="Raio Menor (cm): ", bg='white')
    label_raio_menor.grid(column=2, row=3, padx=20, pady=20)
    entry_raio_menor = Entry(fr_frame3)
    entry_raio_menor.grid(column=3, row=3, padx=20, pady=20)

    label_altura = Label(fr_frame3, text="Altura (cm): ", bg='white')
    label_altura.grid(column=2, row=4, padx=20, pady=20)
    entry_altura = Entry(fr_frame3)
    entry_altura.grid(column=3, row=4, padx=20, pady=20)

    i = 4

    nome_fase(i)

    button_calcular = Button(fr_frame3, text="Enviar", command=lambda: calcular_tronco_cone(entry_raio_maior, entry_raio_menor, entry_altura))
    button_calcular.grid(column=2, row=7, padx=20, pady=20)

# pede os dados da planta para recomendar o npk
def nome_fase(i):
    global entry_nome
    global entry_fase

    label_nome = Label(fr_frame3, text="Nome da Planta: ", bg='white')
    label_nome.grid(column=2, row=i+1, padx=20, pady=20)
    entry_nome = Entry(fr_frame3)
    entry_nome.grid(column=3, row=i+1, padx=20, pady=20)

    label_fase = Label(fr_frame3, text="Fase da Vida:\n(crescimento inicial;\n desenvolvimento vegetativo;\n reprodução) ", bg='white')
    label_fase.grid(column=2, row=i+2, padx=20, pady=20)
    entry_fase = Entry(fr_frame3)
    entry_fase.grid(column=3, row=i+2, padx=20, pady=20)
    
# converte nome e fase para string e calcula o volume do vaso
def calcular_cubo(entry_altura):
    altura = float(entry_altura.get())

    global entry_nome, entry_fase
    nome = entry_nome.get()
    fase = entry_fase.get()

    volume = altura ** 3
    volume_litros = volume / 1000  # Convertendo para litros

    procurar_npk(nome, fase, volume_litros)

def calcular_cilindro(entry_raio, entry_altura):
    raio = float(entry_raio.get())
    altura = float(entry_altura.get())

    global entry_nome, entry_fase
    nome = entry_nome.get()
    fase = entry_fase.get()

    volume = math.pi * (raio ** 2) * altura
    volume_litros = volume / 1000  # Convertendo para litros

    procurar_npk(nome, fase, volume_litros)

def calcular_cone(entry_raio, entry_altura):
    raio = float(entry_raio.get())
    altura = float(entry_altura.get())

    global entry_nome, entry_fase
    nome = entry_nome.get()
    fase = entry_fase.get()

    volume = (math.pi * (raio ** 2) * altura) / 3
    volume_litros = volume / 1000  # Convertendo para litros

    procurar_npk(nome, fase, volume_litros)

def calcular_tronco_cone(entry_raio_maior, entry_raio_menor, entry_altura):
    raio_maior = float(entry_raio_maior.get())
    raio_menor = float(entry_raio_menor.get())
    altura = float(entry_altura.get())

    global entry_nome, entry_fase
    nome = entry_nome.get()
    fase = entry_fase.get()

    volume = (math.pi * altura * (raio_maior ** 2 + raio_maior * raio_menor + raio_menor ** 2)) / 3
    volume_litros = volume / 1000  # Convertendo para litros

    procurar_npk(nome, fase, volume_litros)

def calcular_piramide(entry_base_maior, entry_base_menor, entry_altura):
    base_maior = float(entry_base_maior.get())
    base_menor = float(entry_base_menor.get())
    altura = float(entry_altura.get())

    global entry_nome, entry_fase
    nome = entry_nome.get()
    fase = entry_fase.get()

    volume = (altura / 3) * (base_maior * base_menor + math.sqrt(base_maior * base_menor))
    volume_litros = volume / 1000  # Convertendo para litros

    procurar_npk(nome, fase, volume_litros)

def volume_litro(volume):
    return volume / 1000  # converte volume(cm³) para volume(L)
    
# procura o npk no documento plantas.txt
def procurar_npk(nome, fase, volume):
    limpar_frame3()
    
    global npk
    global entry_nome
    global entry_fase
    
    with open("plantas.txt", "r") as arquivo_planta:
        linha = arquivo_planta.readline()

        while linha:
            procurar = linha.split(';')
            if procurar[0].strip() == nome and procurar[1].strip() == fase:
                npk = procurar[2].strip()
                break
            linha = arquivo_planta.readline()

    arquivo_planta.close()
    
    if npk:
        label_npk = Label(fr_frame3, text=f"O adubo registrado encontra-se como {npk}\nDeseja prosseguir com este valor?", bg='white')
        label_npk.grid(column=2, row=2, padx=20, pady=20)
        
        button_sim = Button(fr_frame3, text="Sim", command=lambda: valor_recomendado(nome, volume))
        button_sim.grid(column=2, row=3, padx=20, pady=20)
        
        button_nao = Button(fr_frame3, text="Não", command=lambda: valor_diferente(nome, volume))
        button_nao.grid(column=2, row=4, padx=50, pady=50)
    else:
        label_npk = Label(fr_frame3, text="Não foi encontrada nenhuma recomendação no sistema", bg='white')
        label_npk.grid(column=2, row=2, padx=20, pady=20)

def nutrientes(volume):
    
    global npk
    
    nutrientes_npk = npk.split('/')
    nitrogenio = nutrientes_npk[0]
    fosforo = nutrientes_npk[1]
    potassio = nutrientes_npk[2]
    
    nitrogenio = int(nitrogenio)
    fosforo = int(fosforo)
    potassio = int(potassio)

    menor_valor_nutrientes = min(nitrogenio, fosforo, potassio)

    nitrogenio_proporcional = nitrogenio / menor_valor_nutrientes
    fosforo_proporcional = fosforo / menor_valor_nutrientes
    potassio_proporcional = potassio / menor_valor_nutrientes

    quantidade = volume / menor_valor_nutrientes
    
    return quantidade, nitrogenio_proporcional, fosforo_proporcional, potassio_proporcional, menor_valor_nutrientes

def valor_recomendado(nome, volume):
    limpar_frame3()

    quantidade, nitrogenio_proporcional, fosforo_proporcional, potassio_proporcional, menor_valor_nutrientes = nutrientes(volume)

    label_resultado = Label(fr_frame3, text=f"\n\nPara {nome}, você precisará de aproximadamente {quantidade:.2f} kg \nda fórmula {npk} para o vaso de volume {volume:.2f} litros.", bg='white')
    label_resultado.grid(column=1, row=2, padx=20, pady=20)

    
def valor_diferente(nome, volume):
    limpar_frame3()
    
    quantidade, nitrogenio_proporcional, fosforo_proporcional, potassio_proporcional, quantidade_necessaria = nutrientes(volume)
    
    label_resultado = Label(fr_frame3, text=f"\nOs nutrientes possuem a proporção de {int(nitrogenio_proporcional)}-{int(fosforo_proporcional)}-{int(potassio_proporcional)}", bg='white')
    label_resultado.grid(column=1, row=2, padx=20, pady=20)
    
    label_resultado = Label(fr_frame3, text="Insira a quantidade desejada de nutrientes", bg='white')
    label_resultado.grid(column=1, row=3, padx=20, pady=20)
    
    label_resultado = Label(fr_frame3, text="Nitrogenio", bg='white')
    label_resultado.grid(column=1, row=4, padx=20, pady=20)
    
    nitrogenio_entry = Entry(fr_frame3)
    nitrogenio_entry.grid(column=2, row=4, padx=20, pady=20)
    
    label_resultado = Label(fr_frame3, text="Fósforo", bg='white')
    label_resultado.grid(column=1, row=5, padx=20, pady=20)
    
    fosforo_entry = Entry(fr_frame3)
    fosforo_entry.grid(column=2, row=5, padx=20, pady=20)
    
    label_resultado = Label(fr_frame3, text="Potássio", bg='white')
    label_resultado.grid(column=1, row=6, padx=20, pady=20)
    
    potassio_entry = Entry(fr_frame3)
    potassio_entry.grid(column=2, row=6, padx=20, pady=20)
    
    label_resultado = Label(fr_frame3, text="Dimensões do Terreno", bg='white')
    
    label_resultado = Label(fr_frame3, text="largura", bg='white')
    label_resultado.grid(column=1, row=7, padx=20, pady=20)

    largura_entry = Entry(fr_frame3)
    largura_entry.grid(column=2, row=7, padx=20, pady=20)
    
    label_resultado = Label(fr_frame3, text="comprimento", bg='white')
    label_resultado.grid(column=1, row=8, padx=20, pady=20)

    comprimento_entry = Entry(fr_frame3)
    comprimento_entry.grid(column=2, row=8, padx=20, pady=20)
    
    label_resultado = Label(fr_frame3, text="profundidade", bg='white')
    label_resultado.grid(column=1, row=9, padx=20, pady=20)

    profundidade_entry = Entry(fr_frame3)
    profundidade_entry.grid(column=2, row=9, padx=20, pady=20)

    botao = Button(fr_frame3, text="Enviar", command=lambda: dimensao(comprimento_entry, largura_entry, profundidade_entry, nitrogenio_entry, fosforo_entry, potassio_entry))
    botao.grid(column=2, row=10, padx=20, pady=20)


def dimensao(comprimento_entry, largura_entry, profundidade_entry, nitrogenio_entry, fosforo_entry, potassio_entry):

    comprimento = float(comprimento_entry.get())
    largura = float(largura_entry.get())
    profundidade = float(profundidade_entry.get())

    nitrogenio = int(nitrogenio_entry.get())
    fosforo = int(fosforo_entry.get())
    potassio = int(potassio_entry.get())

    resultado_valor_diferente(comprimento, largura, profundidade, nitrogenio, fosforo, potassio)
    

    
def resultado_valor_diferente(comprimento, largura, profundidade, nitrogenio, fosforo, potassio):
    limpar_frame3()

    volume = comprimento * largura * profundidade
    
    quantidade, nitrogenio_proporcional, fosforo_proporcional, potassio_proporcional, quantidade_necessaria = nutrientes(volume)
    
    quantidade_adubo = (quantidade_necessaria * volume)/100
    
    label_resultado = Label(fr_frame3, text=f"\n\nPara a área de {largura}m x {comprimento}m e profundidade de {profundidade}cm, você precisará de aproximadamente {quantidade_adubo:.2f} kg da fórmula {nitrogenio}-{fosforo}-{potassio}.", bg='white')
    label_resultado.grid(column=2, row=2, padx=20, pady=20)

# calcula o tamanho do vaso conforme a fase da vida da planta
def vaso():
    limpar_frame3()
    fr_frame3.grid()
    limpar_frame2()

    resultado_label = Label(fr_frame2, bg='white', text="Idade da planta", relief="raised").grid(column=1, row=1)

    botao_jovem = Button(fr_frame2, text="Jovem", command=jovem).grid(column=1, row=2)

    botao_adulta = Button(fr_frame2, text="Adulta", command=adulta).grid(column=1, row=3)

def adulta():
    limpar_frame3()
    
    diametro_label = Label(fr_frame3, text="Diâmetro da Raiz", bg='white')
    diametro_label.grid(column=2, row=1)
    diametro_entry = Entry(fr_frame3)
    diametro_entry.grid(column=2, row=2)

    altura_label = Label(fr_frame3, text="Altura da Raiz", bg='white')
    altura_label.grid(column=2, row=3)
    altura_entry = Entry(fr_frame3)
    altura_entry.grid(column=2, row=4)

    botao_diametro = Button(fr_frame3, text="Enviar", command=lambda: converter_entry_adulta(diametro_entry, altura_entry))
    botao_diametro.grid(column=2, row=5)

def jovem():
    limpar_frame3()

    diametro_label = Label(fr_frame3, text="Diâmetro da Raiz", bg='white')
    diametro_label.grid(column=2, row=1)
    diametro_entry = Entry(fr_frame3)
    diametro_entry.grid(column=2, row=2)

    altura_label = Label(fr_frame3, text="Altura da Raiz", bg='white')
    altura_label.grid(column=2, row=3)
    altura_entry = Entry(fr_frame3)
    altura_entry.grid(column=2, row=4)

    botao_diametro = Button(fr_frame3, text="Enviar", command=lambda: converter_entry_jovem(diametro_entry, altura_entry))
    botao_diametro.grid(column=2, row=5)

# converte para float e calcula o diametro
def converter_entry_jovem(diametro_entry, altura_entry):
    diametro = float(diametro_entry.get())
    altura = float(altura_entry.get())

    diametro_recomendado_jovem(diametro, altura)

def converter_entry_adulta(diametro_entry, altura_entry):
    diametro = float(diametro_entry.get())
    altura = float(altura_entry.get())

    diametro_recomendado_adulta(diametro, altura)

def diametro_recomendado_adulta(diametro, altura):
    limpar_frame3()

    diametro_vaso_minimo = (diametro + 5)
    diametro_vaso_maximo = (diametro + 10)

    altura_vaso_minimo = (altura + 5)
    altura_vaso_maximo = (altura + 10)

    label_resultado = Label(fr_frame3, text=f"Diâmetro de vaso recomendado: {diametro_vaso_minimo} - {diametro_vaso_maximo}cm \nAltura de vaso recomendo: {altura_vaso_minimo} - {altura_vaso_maximo} cm", bg='white')
    label_resultado.grid(column=3, row=5)

def diametro_recomendado_jovem(diametro, altura):
    limpar_frame3()

    diametro_vaso_minimo = (diametro + 2)
    diametro_vaso_maximo = (diametro + 4)

    altura_vaso_minimo = (altura + 5)
    altura_vaso_maximo = (altura + 10)

    label_resultado = Label(fr_frame3, text=f"Diâmetro de vaso recomendado: {diametro_vaso_minimo} - {diametro_vaso_maximo}cm \nAltura de vaso recomendo: {altura_vaso_minimo} - {altura_vaso_maximo} cm", bg='white')
    label_resultado.grid(column=3, row=5)

def centralizar_janela(janela, largura=800, altura=600):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    pos_x = (largura_tela / 2) - (largura / 2)
    pos_y = (altura_tela / 2) - (altura / 2)
    janela.geometry(f'{largura}x{altura}+{int(pos_x)}+{int(pos_y)}')

# tela inicial
def criar_interface():
    global janela
    global fr_frame2
    global fr_frame3
    global npk
    global entry_nome
    global entry_fase
    
    entry_nome = None
    entry_fase = None
    npk = None

    janela = Tk()
    janela.title("AdubaLivre")
    centralizar_janela(janela)
    janela.configure(bg='white')

    janela.grid_columnconfigure(1, weight=1)
    janela.grid_rowconfigure(0, weight=1)

    # Frame principal para ações
    fr_frame1 = Frame(janela, borderwidth=1, relief="sunken")
    fr_frame1.grid(column=0, row=0, padx=10, pady=10, sticky="nw")
    fr_frame1.configure(bg='#4C72B0')

    # Frame para informações
    fr_frame2 = Frame(janela, borderwidth=1, relief="sunken")
    fr_frame2.grid(column=1, row=0, padx=10, pady=10, sticky="nw")
    fr_frame2.configure(bg='white')
    
    fr_frame3 = Frame(janela, borderwidth=1, relief="raised")
    fr_frame3.grid(column=2, row=0, padx=10, pady=10, sticky="nw")
    fr_frame3.configure(bg='white')

    # linhas vazias
    texto_orientacao = Label(fr_frame1, bg='#4C72B0',  text="")
    texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

    texto_orientacao = Label(fr_frame1, bg='#4C72B0',  text="")
    texto_orientacao.grid(column=0, row=1, padx=10, pady=10)

    texto_orientacao = Label(fr_frame1, bg='#4C72B0',  text="")
    texto_orientacao.grid(column=0, row=3, padx=10, pady=10)

    # botoes e texto na tela principal
    texto_orientacao = Label(fr_frame1, bg='#4C72B0', fg='white', text="Aduba Livre", font=('Tahoma', 14))
    texto_orientacao.grid(column=0, row=2, padx=10, pady=10)

    botao_personalizar = Button(fr_frame1, text="Personalizar", font=('Tahoma', 8), command=personalizar, width=13)
    botao_personalizar.grid(column=0, row=4, padx=10, pady=10)

    botao_informacoes = Button(fr_frame1, text="Informações", font=('Tahoma', 8), command=informacoes, width=13)
    botao_informacoes.grid(column=0, row=5, padx=10, pady=10)
    
    botao_calcular_adubo = Button(fr_frame1, text="Calcular Adubo", font=('Tahoma', 8), command=adubo, width=13)
    botao_calcular_adubo.grid(column=0, row=6, padx=10, pady=10)

    botao_calcular_vaso = Button(fr_frame1, text="Calcular Vaso", font=('Tahoma', 8), command=vaso, width=13)
    botao_calcular_vaso.grid(column=0, row=7, padx=10, pady=10)

    texto_orientacao = Label(fr_frame1, bg='#4C72B0',  text="")
    texto_orientacao.grid(column=0, row=8, padx=10, pady=10)

    texto_orientacao = Label(fr_frame1, bg='#4C72B0',  text="")
    texto_orientacao.grid(column=0, row=9, padx=10, pady=10)

    texto_orientacao = Label(fr_frame1, bg='#4C72B0',  text="")
    texto_orientacao.grid(column=0, row=10, padx=10, pady=10)

    janela.mainloop()

criar_interface()