
from src.kepegawaian.pegawai import Pegawai


class PegawaiHarian(Pegawai):
    """Pegawai yang penghasilannya dihitung berdasarkan hari kerja."""

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
        jumlah_hari: int,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok)

        if jumlah_hari <= 0:
            raise ValueError("Jumlah hari harus lebih dari 0")

        self._jumlah_hari = jumlah_hari

    @property
    def jumlah_hari(self) -> int:
        return self._jumlah_hari

    def hitung_penghasilan(self, potongan: int = 0) -> int:
        """Menghitung penghasilan harian setelah potongan."""
        penghasilan = self.gaji_pokok * self.jumlah_hari
        if potongan < 0 or potongan > penghasilan:
            raise ValueError("Potongan tidak valid")
        return penghasilan - potongan
