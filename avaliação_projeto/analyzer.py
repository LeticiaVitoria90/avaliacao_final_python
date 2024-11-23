import pandas as pd

class DataLoader:
    def __init__(self, file_path):        
        self.file_path = file_path 
        self.data = None 

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


class DataAnalyzer:
    def __init__(self, data):        
        self.data = data

    def volume_by_category_and_subcategory(self):        
        print("\nVolume por categoria e subcategoria:")
        volume = self.data.groupby(['Category', 'Sub-Category']).size()
        print(volume)

    def product_popularity(self):        
        print("\nPopularidade de produtos:")
        popularity = self.data['Product_Name'].value_counts()
        print(popularity)

    def average_delivery_time_by_category(self):
        print("\nTempo médio de entrega por categoria:")
        self.data['Delivery_Time'] = (self.data['Ship_Date'] - self.data['Order_Date']).dt.days
        delivery_time = self.data.groupby('Category')['Delivery_Time'].mean()
        print(delivery_time)

    def top_customers_by_frequency(self):
        print("\nClientes mais frequentes:")
        frequent_customers = self.data['Customer_Name'].value_counts().head(10)
        print(frequent_customers)

    def sales_seasonality(self):
        print("\nSazonalidade nas vendas:")
        self.data['Month'] = self.data['Order_Date'].dt.month
        seasonality = self.data.groupby('Month').size()
        print(seasonality)

    def demand_prediction(self):
        print("\nPrevisão de demanda por mês:")
        self.data['Month'] = self.data['Order_Date'].dt.to_period('M')
        demand_prediction = self.data.groupby('Month').size()
        print(demand_prediction)



def run_analysis(file_path):
    loader = DataLoader(file_path)
    loader.load_data()
    loader.dataset_info()
    loader.preprocess_data()

    data = loader.get_data()

    analyzer = DataAnalyzer(data)

    analyzer.volume_by_category_and_subcategory()
    analyzer.product_popularity()
    analyzer.average_delivery_time_by_category()
    analyzer.top_customers_by_frequency()
    analyzer.sales_seasonality()
    analyzer.demand_prediction()


file_path = "sales.superstore.csv"

run_analysis(file_path)
