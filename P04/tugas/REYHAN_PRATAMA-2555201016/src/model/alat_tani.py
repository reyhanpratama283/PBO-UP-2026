from typing import Final


class AlatTani:
    """Mewakili alat pertanian yang dapat disewakan."""

    TARIF_MINIMUM: Final[int] = 10_000
    TARIF_MAKSIMUM: Final[int] = 5_000_000
    PERSEN_DENDA_HARIAN: Final[int] = 10
    PEMISAH_BARIS: Final[str] = ";"

    _jumlah_terdaftar: int = 0

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        if not kode.strip():
            raise ValueError("Kode tidak boleh kosong")
        if not nama.strip():
            raise ValueError("Nama tidak boleh kosong")

        self._kode = kode
        self._nama = nama
        self._tarif_harian = 0
        self.tarif_harian = tarif_harian
        AlatTani._jumlah_terdaftar += 1

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def tarif_harian(self) -> int:
        return self._tarif_harian

    @tarif_harian.setter
    def tarif_harian(self, nilai: int) -> None:
        if not AlatTani.tarif_wajar(nilai):
            raise ValueError(
                f"Tarif harus antara "
                f"{AlatTani.format_rupiah(AlatTani.TARIF_MINIMUM)} dan "
                f"{AlatTani.format_rupiah(AlatTani.TARIF_MAKSIMUM)}, "
                f"diterima {AlatTani.format_rupiah(nilai)}"
            )
        self._tarif_harian = nilai

    @staticmethod
    def tarif_wajar(nilai: int) -> bool:
        return AlatTani.TARIF_MINIMUM <= nilai <= AlatTani.TARIF_MAKSIMUM

    @staticmethod
    def format_rupiah(nilai: int) -> str:
        return "Rp" + f"{nilai:,}".replace(",", ".")

    @classmethod
    def jumlah_terdaftar(cls) -> int:
        return cls._jumlah_terdaftar

    @classmethod
    def dari_baris_csv(cls, baris: str) -> "AlatTani":
        bagian = baris.split(cls.PEMISAH_BARIS)

        if len(bagian) != 3:
            raise ValueError("Baris harus berisi kode, nama, dan tarif")

        kode, nama, tarif = bagian

        try:
            nilai_tarif = int(tarif.strip())
        except ValueError as exc:
            raise ValueError("Tarif harus berupa angka") from exc

        return cls(kode.strip(), nama.strip(), nilai_tarif)

    def denda_keterlambatan(self, hari_terlambat: int) -> int:
        if hari_terlambat < 0:
            raise ValueError("Hari keterlambatan tidak boleh negatif")

        return (
            self.tarif_harian
            * self.PERSEN_DENDA_HARIAN
            // 100
            * hari_terlambat
        )