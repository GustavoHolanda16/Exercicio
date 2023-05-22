from tkinter import *
from openpyxl import Workbook

def calcular_investimento():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    valor = float(entry_valor.get())
    porcentagem = float(entry_porcentagem.get())

    resultado = valor * (1 + porcentagem / 100)

    entry_resultado.delete(0, END)
    entry_resultado.insert(0, resultado)

    salvar_dados(nome, telefone, valor, porcentagem, resultado)

def salvar_dados(nome, telefone, valor, porcentagem, resultado):
    planilha = Workbook()
    planilha_ativa = planilha.active

    planilha_ativa.append(['Nome', 'Telefone', 'Valor investido', 'Porcentagem', 'Resultado'])
    planilha_ativa.append([nome, telefone, valor, porcentagem, resultado])

    planilha.save('dados.xlsx')

# Criar a janela
janela = Tk()
janela.title('Investimento')

# Criar os campos de entrada
Label(janela, text='Nome:').grid(row=0, column=0)
entry_nome = Entry(janela)
entry_nome.grid(row=0, column=1)

Label(janela, text='Telefone:').grid(row=1, column=0)
entry_telefone = Entry(janela)
entry_telefone.grid(row=1, column=1)

Label(janela, text='Valor investido:').grid(row=2, column=0)
entry_valor = Entry(janela)
entry_valor.grid(row=2, column=1)

Label(janela, text='Porcentagem:').grid(row=3, column=0)
entry_porcentagem = Entry(janela)
entry_porcentagem.grid(row=3, column=1)

Label(janela, text='Resultado:').grid(row=4, column=0)
entry_resultado = Entry(janela)
entry_resultado.grid(row=4, column=1)

# Criar o botão de calcular
Button(janela, text='Calcular', command=calcular_investimento).grid(row=5, column=1)

janela.mainloop()
