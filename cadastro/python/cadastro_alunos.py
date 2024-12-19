import tkinter as tk
from tkinter import messagebox, ttk

class CadastroAlunosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de notas de Alunos")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        self.notas = []  # Lista para armazenar os dados
        self.total_alunos = 0  # Número total de alunos
        self.aluno_atual = 0  # Contador para o aluno atual
        
        # Frame principal
        self.frame_principal = tk.Frame(root, bg="grey70", padx=10, pady=10)
        self.frame_principal.pack(fill="both", expand=True)

        

        # Título
        tk.Label(self.frame_principal, text="Notas de Alunos", 
         font=("Arial", 18, "bold"), 
         bg="white", fg="black", 
         relief="ridge", borderwidth=10).pack(pady=10)

        
        # Entrada do número de alunos
        self.frame_input = tk.Frame(self.frame_principal, bg="azure4")
        self.frame_input.pack(pady=10)
        
        # Label com borda
        label_quantos_alunos = tk.Label(self.frame_input, text="Quantos alunos?", 
                                font=("Arial", 12), 
                                bg="lightgray", fg="black", 
                                borderwidth=3, relief="ridge")
        label_quantos_alunos.grid(row=0, column=0, padx=5, pady=5)
        self.entry_alunos = tk.Entry(self.frame_input, font=("Arial", 12), 
                                 borderwidth=3, relief="ridge", bg="white")
        self.entry_alunos.grid(row=0, column=1, padx=5, pady=5)

        
        # Botão iniciar
        tk.Button(self.frame_input, text="Iniciar Cadastro", bg="light slate gray", fg="white", font=("Arial", 12), command=self.iniciar_cadastro).grid(row=0, column=2, padx=5)
        
        # Frame para tabela
        self.frame_tabela = tk.Frame(self.frame_principal)
        self.frame_tabela.pack(fill="both", expand=True, pady=10)

        # Tabela Treeview
        self.tree = ttk.Treeview(self.frame_tabela, columns=("CGM", "Nota"), show="headings", height=10)
        self.tree.heading("CGM", text="CGM")
        self.tree.heading("Nota", text="Nota")
        self.tree.pack(fill="both", expand=True)

    # Função para iniciar o cadastro
    def iniciar_cadastro(self):
        try:
            self.total_alunos = int(self.entry_alunos.get())
            self.aluno_atual = 1  # Começa pelo primeiro aluno
            self.janela_cadastro()
        except ValueError:
            messagebox.showerror("Erro", "Insira um número válido de alunos.")
    
    # Função para abrir a janela de cadastro de cada aluno
    def janela_cadastro(self):
        # Verifica se ainda há alunos a serem cadastrados
        if self.aluno_atual > self.total_alunos:
            messagebox.showinfo("Concluído", "Todos os dados foram registrados com sucesso!")
            return
        
        janela = tk.Toplevel(self.root)
        janela.title(f"Cadastro do Aluno {self.aluno_atual}")
        janela.geometry("400x200")
        janela.resizable(False, False)
        
        tk.Label(janela, text=f"Aluno {self.aluno_atual}", font=("Arial", 14)).pack(pady=10)
        
        # Entrada CGM
        tk.Label(janela, text="CGM:", font=("Arial", 12)).pack()
        entry_cgm = tk.Entry(janela, font=("Arial", 12))
        entry_cgm.pack(pady=5)
        
        # Entrada Nota
        tk.Label(janela, text="Nota:", font=("Arial", 12)).pack()
        entry_nota = tk.Entry(janela, font=("Arial", 12))
        entry_nota.pack(pady=5)
        
        # Salvar dados
        def salvar():
            cgm = entry_cgm.get()
            try:
                nota = float(entry_nota.get())
                self.notas.append((cgm, nota))
                self.tree.insert("", "end", values=(cgm, nota))
                messagebox.showinfo("Sucesso", f"Dados do aluno {self.aluno_atual} salvos!")
                janela.destroy()
                self.aluno_atual += 1  # Próximo aluno
                self.janela_cadastro()  # Abre a próxima janela
            except ValueError:
                messagebox.showerror("Erro", "A nota deve ser um número válido.")
        
        tk.Button(janela, text="Salvar", bg="green", fg="white", font=("Arial", 12), command=salvar).pack(pady=10)

# Inicializar o aplicativo
if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroAlunosApp(root)
    root.mainloop()
