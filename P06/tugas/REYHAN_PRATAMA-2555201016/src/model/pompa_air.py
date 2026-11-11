
"""Model pompa air sebagai jenis alat pertanian."""

from typing import Final

from src.model.alat_tani import AlatTani


class PompaAir(AlatTani):
    """Mewakili pompa air yang membutuhkan biaya solar."""

    HARGA_SOLAR_PER_LITER: Final[int] = 7_000
    LITER_PER_SERATUS_DEBIT: Final[int] = 3
    JUMLAH_KOLOM_POMPA_CSV: Final[int] = 4

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
        debit: int,
    ) -> None:
        super().__init__(kode, nama, tarif_harian)

        if debit <= 0:
            raise ValueError("Debit harus lebih dari nol")

        self._debit = debit

    @property
    def debit(self) -> int:
        return self._debit

    @classmethod
    def dari_baris_csv(cls, baris: str) -> PompaAir:
        bagian = baris.strip().split(cls.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_KOLOM_POMPA_CSV:
            raise ValueError("Data pompa air harus berisi 4 bagian")

        kode, nama, tarif, debit = bagian

        try:
            nilai_tarif = int(tarif.strip())
            nilai_debit = int(debit.strip())
        except ValueError as exc:
            raise ValueError("Tarif dan debit harus berupa angka") from exc

        return cls(
            kode.strip(),
            nama.strip(),
            nilai_tarif,
            nilai_debit,
        )

    def konsumsi_solar_harian(self) -> int:
        return (self._debit * self.LITER_PER_SERATUS_DEBIT) // 100

    def biaya_sewa(self, jumlah_hari: int) -> int:
        biaya_dasar = super().biaya_sewa(jumlah_hari)
        biaya_solar = (
            self.konsumsi_solar_harian()
            * self.HARGA_SOLAR_PER_LITER
            * jumlah_hari
        )

        return biaya_dasar + biaya_solar
