# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "dune-client==1.10.0",
#     "marimo>=0.21.1",
#     "matplotlib==3.10.8",
#     "pandas==3.0.1",
# ]
# ///

import marimo

__generated_with = "0.21.1"
app = marimo.App(
    width="medium",
    css_file="/usr/local/_marimo/custom.css",
    auto_download=["html"],
)


@app.cell
def _():
    import pandas as pd
    from dune_client.client import DuneClient


    # 1. API SETUP
    DUNE_API_KEY = "iEuaSNBZeMLZcwoqQdAqWa1uVUgyQ8d3" 
    dune = DuneClient(DUNE_API_KEY)
    QUERY_ID = 6897733

    # 2. PULL DATA FROM BLOCKCHAIN
    print("⏳ Menjemput data dari server Dune...\n")
    hasil_kueri = dune.get_latest_result(QUERY_ID)
    df = pd.DataFrame(hasil_kueri.result.rows)


    print("📊 CUPLIKAN TABEL DATA MENTAH:")
    print(df.head())
    print("-" * 50)

    # 3. DATA CLEANING PROCESS
    # Kita ganti kata 'taker' dengan nama kolom yang BENAR yaitu 'whale_address'
    df_bersih = df.dropna(subset=['whale_address'])


    total_uang_whale = df_bersih['amount_usd'].sum()


    print("✅ LAPORAN MANAJER:")
    print(f"Total uang yang diputar oleh 50 Whale koin LINK dalam 7 hari terakhir adalah: ${total_uang_whale:,.2f}")
    return (df_bersih,)


@app.cell
def _(df_bersih):
    import matplotlib.pyplot as plt

    print("🎨 Sedang menggambar grafik untuk Manajer...")

    # 1. Kita ambil data bersih yang tadi, lalu kita urutkan dari yang terbesar
    # (Mengingat kembali pelajaran awal kita tentang sort_values!)
    df_top_5 = df_bersih.sort_values(by='amount_usd', ascending=False).head(5)

    # 2. Kita siapkan kanvas gambarnya
    plt.figure(figsize=(10, 6))

    # 3. Kita buat Bar Chart (Sumbu X = Alamat Dompet, Sumbu Y = Nilai Dolar)
    # Karena alamat dompet terlalu panjang, kita persingkat 6 huruf depannya saja
    alamat_pendek = df_top_5['whale_address'].str[:6] + "..." 

    plt.bar(alamat_pendek, df_top_5['amount_usd'], color='skyblue', edgecolor='black')

    # 4. Kita beri judul dan label yang rapi agar HRD terkesan
    plt.title('Top 5 Whale Koin LINK (24 jam terakhir)', fontsize=14, fontweight='bold')
    plt.xlabel('Alamat Dompet (Whale)', fontsize=12)
    plt.ylabel('Nilai Transaksi (USD)', fontsize=12)

    # Menambahkan format angka agar mudah dibaca (opsional tapi profesional)
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    # 5. Tampilkan grafiknya!
    plt.show()
    return


if __name__ == "__main__":
    app.run()
