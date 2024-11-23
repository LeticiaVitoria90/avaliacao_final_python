import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path  # Caminho para o arquivo
        self.data = None  # Aqui os dados serão armazenados

    def load_data(self):
        self.data = pd.read_csv(self.file_path)
        print("Dados carregados com sucesso!")

    def preprocess_data(self):       
        self.data['Order_Date'] = pd.to_datetime(self.data['Order_Date'])
        self.data['Ship_Date'] = pd.to_datetime(self.data['Ship_Date'])
        self.data.fillna({'Postal_Code': 0}, inplace=True)  # Preenche valores faltantes
        print("Pré-processamento concluído!")

    def dataset_info(self):        
        print("Informações do Dataset:")
        print(f"- Total de linhas: {self.data.shape[0]}")
        print(f"- Total de colunas: {self.data.shape[1]}")
        print("- Nomes das colunas:", list(self.data.columns))
        print("- Amostra dos dados:")
        print(self.data.head())

    def get_data(self):        
        return self.data


loader = DataLoader("sales.superstore.csv")
loader.load_data()
loader.dataset_info()
loader.preprocess_data()
data = loader.get_data()
