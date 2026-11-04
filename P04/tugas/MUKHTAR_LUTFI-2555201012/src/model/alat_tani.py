"""Model domain: alat yang disewakan UPJA."""

from typing import Final


class AlatTani:
    """Satu unit alat pertanian beserta tarif hariannya."""

    TARIF_MINIMUM: Final[int] = 10_000
    TARIF_MAKSIMUM: Final[int] = 5_000_000
    PERSEN_DENDA_HARIAN: Final[int] = 10
    PEMISAH_BARIS: Final[str] = ";"

    _jumlah_terdaftar: int = 0

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        self._kode = kode
        self._nama = nama
        self._tarif_harian = 0
        self.tarif_harian = tarif_harian

        AlatTani._jumlah_terdaftar += 1

    @staticmethod
    def tarif_wajar(nilai: int) -> bool:
        """Memeriksa apakah tarif berada dalam batas yang ditentukan."""
        return (
            isinstance(nilai, int)
            and not isinstance(nilai, bool)
            and AlatTani.TARIF_MINIMUM
            <= nilai
            <= AlatTani.TARIF_MAKSIMUM
        )

    @staticmethod
    def format_rupiah(nilai: int) -> str:
        """Mengubah angka menjadi format mata uang rupiah."""
        return "Rp" + f"{nilai:,}".replace(",", ".")

    @classmethod
    def jumlah_terdaftar(cls) -> int:
        """Mengembalikan jumlah objek AlatTani yang telah dibuat."""
        return cls._jumlah_terdaftar

    @classmethod
    def dari_baris_csv(cls, baris: str) -> "AlatTani":
        """Membuat objek AlatTani dari satu baris data."""
        bagian = baris.strip().split(cls.PEMISAH_BARIS)

        if len(bagian) != 3:
            raise ValueError(
                "Baris CSV harus berisi kode, nama, dan tarif harian."
            )

        kode, nama, tarif_teks = bagian

        try:
            tarif = int(tarif_teks.strip())
        except ValueError:
            raise ValueError("Tarif harian harus berupa angka.") from None

        return cls(kode.strip(), nama.strip(), tarif)

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
        if not self.tarif_wajar(nilai):
            raise ValueError(
                "Tarif harus antara "
                f"{self.format_rupiah(self.TARIF_MINIMUM)} dan "
                f"{self.format_rupiah(self.TARIF_MAKSIMUM)}."
            )

        self._tarif_harian = nilai

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa berdasarkan jumlah hari."""
        if jumlah_hari < 0:
            raise ValueError("Jumlah hari tidak boleh negatif.")

        return self._tarif_harian * jumlah_hari

    def denda_keterlambatan(self, hari_terlambat: int) -> int:
        """Menghitung denda berdasarkan jumlah hari keterlambatan."""
        if hari_terlambat < 0:
            raise ValueError("Hari keterlambatan tidak boleh negatif.")

        denda_per_hari = (
            self._tarif_harian * self.PERSEN_DENDA_HARIAN // 100
        )
        return denda_per_hari * hari_terlambat

    def keterangan(self) -> str:
        """Mengembalikan keterangan alat untuk daftar sewa."""
        return (
            f"[{self.kode}] {self.nama} — "
            f"{self.format_rupiah(self.tarif_harian)}/hari"
        )
    