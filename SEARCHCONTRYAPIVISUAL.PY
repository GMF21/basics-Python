import requests
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import io

class CountryInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Consulta de Países")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.configure(bg='#f0f0f0')
        
        # Configurar estilo
        self.style = ttk.Style()
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10, 'bold'))
        self.style.configure('Title.TLabel', font=('Arial', 16, 'bold'), foreground='#1e3c72')
        self.style.configure('Result.TLabel', font=('Arial', 10, 'bold'), foreground='#333')
        
        # Criar interface
        self.create_widgets()
    
    def create_widgets(self):
        # Título
        title_label = ttk.Label(self.root, text="🌍 Consulta de Países", style='Title.TLabel')
        title_label.pack(pady=20)
        
        # Descrição
        desc_label = ttk.Label(self.root, 
                              text="Obtenha informações detalhadas sobre qualquer país do mundo.\nDigite o nome do país abaixo e clique em buscar.",
                              justify=tk.CENTER)
        desc_label.pack(pady=10)
        
        # Frame de busca
        search_frame = ttk.Frame(self.root)
        search_frame.pack(pady=20, padx=20, fill=tk.X)
        
        # Entrada de texto
        self.country_var = tk.StringVar()
        country_entry = ttk.Entry(search_frame, textvariable=self.country_var, font=('Arial', 12), width=30)
        country_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        country_entry.bind('<Return>', lambda event: self.search_country())
        
        # Botão de busca
        search_btn = ttk.Button(search_frame, text="Buscar", command=self.search_country)
        search_btn.pack(side=tk.RIGHT)
        
        # Frame de resultados
        self.result_frame = ttk.LabelFrame(self.root, text="Informações do País")
        self.result_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        self.result_frame.pack_forget()  # Esconder inicialmente
        
        # Bandeira
        self.flag_label = ttk.Label(self.result_frame)
        self.flag_label.pack(pady=10)
        
        # Nome do país
        self.name_label = ttk.Label(self.result_frame, style='Title.TLabel')
        self.name_label.pack(pady=5)
        
        # Frame para informações
        info_frame = ttk.Frame(self.result_frame)
        info_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # Labels de informação
        self.create_info_row(info_frame, "Capital:", "capital_label")
        self.create_info_row(info_frame, "População:", "population_label")
        self.create_info_row(info_frame, "Região:", "region_label")
        self.create_info_row(info_frame, "Sub-região:", "subregion_label")
        self.create_info_row(info_frame, "Moeda:", "currency_label")
        self.create_info_row(info_frame, "Idioma(s):", "languages_label")
        self.create_info_row(info_frame, "Área:", "area_label")
        self.create_info_row(info_frame, "Fuso horário:", "timezone_label")
        
        # Botão para nova busca
        new_search_btn = ttk.Button(self.root, text="Nova Busca", command=self.new_search)
        new_search_btn.pack(pady=10)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Digite o nome de um país e clique em Buscar")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def create_info_row(self, parent, label_text, attr_name):
        row_frame = ttk.Frame(parent)
        row_frame.pack(fill=tk.X, pady=5)
        
        label = ttk.Label(row_frame, text=label_text, style='Result.TLabel', width=12, anchor=tk.E)
        label.pack(side=tk.LEFT)
        
        value_label = ttk.Label(row_frame, text="", width=30, anchor=tk.W)
        value_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 0))
        
        setattr(self, attr_name, value_label)
    
    def search_country(self):
        country = self.country_var.get().strip()
        
        if not country:
            messagebox.showwarning("Aviso", "Por favor, digite o nome de um país.")
            return
        
        self.status_var.set("Buscando informações...")
        self.root.update()
        
        try:
            url = f"https://restcountries.com/v3.1/name/{country}"
            resposta = requests.get(url)
            
            if resposta.status_code == 200:
                dados = resposta.json()
                pais_info = dados[0]
                self.display_country_info(pais_info)
                self.status_var.set("Informações carregadas com sucesso!")
            else:
                messagebox.showerror("Erro", "País não encontrado! Verifique o nome e tente novamente.")
                self.status_var.set("País não encontrado")
                
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Erro", f"Erro de conexão: {str(e)}")
            self.status_var.set("Erro de conexão")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro inesperado: {str(e)}")
            self.status_var.set("Erro ao carregar informações")
    
    def display_country_info(self, pais_info):
        # Nome do país
        self.name_label.config(text=pais_info['name']['common'])
        
        # Bandeira
        try:
            flag_url = pais_info['flags']['png']
            flag_response = requests.get(flag_url)
            flag_image = Image.open(io.BytesIO(flag_response.content))
            flag_image = flag_image.resize((120, 80), Image.Resampling.LANCZOS)
            flag_photo = ImageTk.PhotoImage(flag_image)
            self.flag_label.config(image=flag_photo)
            self.flag_label.image = flag_photo  # Manter referência
        except:
            self.flag_label.config(image='')
        
        # Informações
        self.capital_label.config(text=pais_info.get('capital', ['N/A'])[0])
        
        populacao = pais_info.get('population', 0)
        self.population_label.config(text=f"{populacao:,}".replace(",", "."))
        
        self.region_label.config(text=pais_info.get('region', 'N/A'))
        self.subregion_label.config(text=pais_info.get('subregion', 'N/A'))
        
        # Moeda
        if 'currencies' in pais_info:
            moeda_codigo = list(pais_info['currencies'].keys())[0]
            moeda_nome = pais_info['currencies'][moeda_codigo]['name']
            moeda_simbolo = pais_info['currencies'][moeda_codigo].get('symbol', '')
            self.currency_label.config(text=f"{moeda_nome} ({moeda_simbolo})")
        else:
            self.currency_label.config(text="N/A")
        
        # Idiomas
        if 'languages' in pais_info:
            idiomas = list(pais_info['languages'].values())
            self.languages_label.config(text=", ".join(idiomas))
        else:
            self.languages_label.config(text="N/A")
        
        # Área
        area = pais_info.get('area', 0)
        if area > 0:
            self.area_label.config(text=f"{area:,.0f} km²".replace(",", "."))
        else:
            self.area_label.config(text="N/A")
        
        # Fuso horário
        if 'timezones' in pais_info:
            self.timezone_label.config(text=", ".join(pais_info['timezones']))
        else:
            self.timezone_label.config(text="N/A")
        
        # Mostrar frame de resultados
        self.result_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
    
    def new_search(self):
        self.country_var.set("")
        self.result_frame.pack_forget()
        self.status_var.set("Digite o nome de um país e clique em Buscar")

def main():
    root = tk.Tk()
    app = CountryInfoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
