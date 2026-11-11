
from src.kepegawaian.pegawai import Pegawai


class PegawaiTetap(Pegawai):
    """Pegawai tetap yang mendapatkan tunjangan tetap."""

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
        tunjangan: int,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok)

        if tunjangan < 0:
            raise ValueError("Tunjangan tidak boleh negatif")

        self._tunjangan = tunjangan

    @property
    def tunjangan(self) -> int:
        return self._tunjangan

    def hitung_penghasilan(self, potongan: int = 0) -> int:
        """Gaji pokok setelah potongan ditambah tunjangan."""
        return super().hitung_penghasilan(potongan) + self.tunjangan
