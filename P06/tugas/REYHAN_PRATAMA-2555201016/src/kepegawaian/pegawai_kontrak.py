
from src.kepegawaian.pegawai import Pegawai


class PegawaiKontrak(Pegawai):
    """Pegawai kontrak dengan potongan berdasarkan kehadiran."""

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
        persentase_kehadiran: int,
    ) -> None:
        if not 0 <= persentase_kehadiran <= self.BATAS_PERSENTASE:
            raise ValueError("Persentase kehadiran harus 0 sampai 100")

        super().__init__(nip, nama, gaji_pokok)
        self._persentase_kehadiran = persentase_kehadiran

    @property
    def persentase_kehadiran(self) -> int:
        return self._persentase_kehadiran

    def hitung_penghasilan(self, potongan: int = 0) -> int:
        """Menghitung gaji berdasarkan kehadiran dan potongan."""
        potongan_kehadiran = (
            self.gaji_pokok * (100 - self.persentase_kehadiran) // 100
        )
        total_potongan = potongan_kehadiran + potongan
        return super().hitung_penghasilan(total_potongan)
    BATAS_PERSENTASE = 100
