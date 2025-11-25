import pandas as pd

class Analyticis:
    def __init__(self, transaksi_file='data/transaksi.csv'):
        self.transaksi_file = transaksi_file
        self.data_transaksi = self.load_transaksi()
        
    def load_transaksi(self):
        try:
            return pd.read_csv(self.transaksi_file)
        except FileNotFoundError:
            print('FIle transaksi.csv tidak ditemukan')
            return pd.DataFrame()
        
    def menu_terlaris(self, jumlah_teratas=5):
        if self.data_transaksi.empty:
            print('Belum ada data transaksi')
            return pd.DataFrame
        
        data_grup = self.data_transaksi.groupby('nama_menu')['jumlah'].sum()

        data_grup_sorted = data_grup.sort_values(ascending=False)

        top_menu = data_grup_sorted.head(jumlah_teratas)
        return top_menu
    
    def total_penjualan_harian(self):
        if self.data_transaksi.empty:
            print('Belum ada data transaksi')
            return pd.DataFrame()
        
        total_harian = self.data_transaksi.groupby('tanggal')['total_harga'].sum()
        return total_harian
    
    def total_penjualan(self):
        if self.data_transaksi.empty:
            return 0
        
        total_keseluruhan = self.data_transaksi['total_harga'].sum()
        return total_keseluruhan
    
