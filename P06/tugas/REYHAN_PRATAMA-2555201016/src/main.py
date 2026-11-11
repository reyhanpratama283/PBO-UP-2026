from src.model.alamat import Alamat
from src.model.penyewa import Penyewa
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.sewa import Sewa
from src.model.traktor import Traktor


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

    traktor = Traktor(
        "TR-01",
        "Traktor Kubota",
        150_000,
        8,
    )

    pompa = PompaAir(
        "PA-01",
        "Pompa Air",
        75_000,
        600,
    )

    perontok = Perontok(
        "PR-01",
        "Mesin Perontok",
        200_000,
        900,
    )

    sewa = Sewa("SW-001", penyewa)
    sewa.tambah_alat(traktor, 3)
    sewa.tambah_alat(pompa, 2)
    sewa.tambah_alat(perontok, 1)

    print("=== NOTA PENYEWAAN ALAT PERTANIAN ===")
    print(sewa.nota())


if __name__ == "__main__":
    main()
