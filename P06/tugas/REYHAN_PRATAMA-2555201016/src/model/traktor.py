"""Model traktor sebagai jenis alat pertanian."""

from typing import Final

from src.model.alat_tani import AlatTani


class Traktor(AlatTani):
    """Mewakili traktor yang membutuhkan biaya operator."""

    ONGKOS_OPERATOR_HARIAN: Final[int] = 100_000

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
        tenaga_kuda: int,
    ) -> None:
        super().__init__(kode, nama, tarif_harian)

        if tenaga_kuda <= 0:
            raise ValueError("Tenaga kuda harus lebih dari nol")

        self._tenaga_kuda = tenaga_kuda

    @property
    def tenaga_kuda(self) -> int:
        return self._tenaga_kuda

    def biaya_sewa(self, jumlah_hari: int) -> int:
        biaya_dasar = super().biaya_sewa(jumlah_hari)
        biaya_operator = self.ONGKOS_OPERATOR_HARIAN * jumlah_hari

        return biaya_dasar + biaya_operator
