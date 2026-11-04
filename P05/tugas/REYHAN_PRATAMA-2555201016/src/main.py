
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa


def main() -> None:
    alamat = Alamat(
        "Jl. Merdeka",
        "Bangkinang",
        "Riau",
        "28412",
    )

    penyewa = Penyewa(
        "Reyhan Pratama",
        "1234567890123456",
        "08123456789",
        alamat,
    )

    traktor = AlatTani("TR-01", "Traktor Kubota", 150_000)
    pompa = AlatTani("PA-01", "Pompa Air", 75_000)

    sewa = Sewa("SW-001", penyewa)
    sewa.tambah_alat(traktor, 3)
    sewa.tambah_alat(pompa, 2)

    print("=== NOTA PENYEWAAN ALAT PERTANIAN ===")
    print(sewa.nota())


if __name__ == "__main__":
    main()
