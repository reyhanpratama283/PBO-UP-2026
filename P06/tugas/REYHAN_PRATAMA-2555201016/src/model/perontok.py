
"""Model mesin perontok sebagai jenis alat pertanian."""

from src.model.alat_tani import AlatTani


class Perontok(AlatTani):
    """Mewakili mesin perontok dengan minimal sewa dua hari."""

    MINIMAL_HARI_SEWA = 2
    JUMLAH_KOLOM_CSV_PERONTOK = 4

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
        kapasitas: int,
    ) -> None:
        super().__init__(kode, nama, tarif_harian)

        if kapasitas <= 0:
            raise ValueError("Kapasitas harus lebih dari nol")

        self._kapasitas = kapasitas

    @property
    def kapasitas(self) -> int:
        return self._kapasitas

    @classmethod
    def dari_baris_csv(cls, baris: str) -> Perontok:
        bagian = baris.strip().split(cls.PEMISAH_BARIS)

        if len(bagian) != cls.JUMLAH_KOLOM_CSV_PERONTOK:
            raise ValueError("Data perontok harus berisi 4 bagian")

        kode, nama, tarif, kapasitas = bagian

        try:
            nilai_tarif = int(tarif.strip())
            nilai_kapasitas = int(kapasitas.strip())
        except ValueError as exc:
            raise ValueError(
                "Tarif dan kapasitas harus berupa angka"
            ) from exc

        return cls(
            kode.strip(),
            nama.strip(),
            nilai_tarif,
            nilai_kapasitas,
        )

    @classmethod
    def hari_ditagih(cls, jumlah_hari: int) -> int:
        if jumlah_hari < 1:
            raise ValueError("Jumlah hari sewa minimal 1")

        return max(jumlah_hari, cls.MINIMAL_HARI_SEWA)

    def biaya_sewa(self, jumlah_hari: int) -> int:
        hari = self.hari_ditagih(jumlah_hari)
        return super().biaya_sewa(hari)
