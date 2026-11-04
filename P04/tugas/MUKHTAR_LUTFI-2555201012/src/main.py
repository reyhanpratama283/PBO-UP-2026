
from src.kios import Kios
from src.model.alat_tani import AlatTani


def tampilkan_kios() -> None:
    produk = Kios(
        kode="BRG001",
        nama_produk="Beras",
        harga_modal=10000,
        harga_jual=12000,
        stok=20,
    )

    print(Kios.NAMA_KIOS)
    print("-" * 48)
    print(f"{'Kode':<10} {'Nama Produk':<15} {'Harga Jual':>12} {'Stok':>6}")
    print("-" * 48)
    print(
        f"{produk.kode:<10} "
        f"{produk.nama_produk:<15} "
        f"{produk.harga_jual:>12,} "
        f"{produk.stok:>6}"
    )


def tampilkan_alat_tani() -> None:
    print("\nPRAKTIKUM ALAT TANI")
    print("-" * 48)

    jumlah_awal = AlatTani.jumlah_terdaftar()
    print(f"Jumlah alat sebelum dibuat: {jumlah_awal}")

    data_alat = [
        "TR-01;Traktor;150000",
        "PA-01;Pompa Air;75000",
        "JM-01;Mesin Jagung;100000",
        "RM-01;Mesin Rumput;50000",
    ]

    for baris in data_alat:
        alat = AlatTani.dari_baris_csv(baris)
        status = "Wajar" if AlatTani.tarif_wajar(alat.tarif_harian) else "Tidak wajar"

        print(
            f"{alat.kode:<8} "
            f"{alat.nama:<18} "
            f"{AlatTani.format_rupiah(alat.tarif_harian):>14} "
            f"→ {status}"
        )

    print(f"Jumlah alat setelah dibuat: {AlatTani.jumlah_terdaftar()}")


def main() -> None:
    tampilkan_kios()
    tampilkan_alat_tani()


if __name__ == "__main__":
    main()
