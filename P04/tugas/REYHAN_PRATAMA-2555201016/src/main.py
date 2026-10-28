from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa


def main() -> None:
    alamat = Alamat(
        jalan="Jalan Merdeka No. 10",
        kota="Bangkinang",
        provinsi="Riau",
        kode_pos="28411",
    )

    alat = AlatTani(
        kode="TR-01",
        nama="Traktor Roda Dua Kubota",
        tarif_harian=150000,
    )

    penyewa = Penyewa(
        nama="Reyhan Pratama",
        nik="1234567890123456",
        telepon="081234567890",
        alamat=alamat,
    )

    print("=== Data Alat Tani ===")
    print(f"Kode  : {alat.kode}")
    print(f"Nama  : {alat.nama}")
    print(f"Tarif : {AlatTani.format_rupiah(alat.tarif_harian)}/hari")

    print("\n=== Data Penyewa ===")
    print(f"Nama    : {penyewa.nama}")
    print(f"NIK     : {penyewa.nik}")
    print(f"Telepon : {penyewa.telepon}")
    print(f"Alamat  : {penyewa.alamat}")


if __name__ == "__main__":
    main()