from src.model.alat_tani import AlatTani


class BarisSewa:
    """Mewakili satu baris alat dalam transaksi penyewaan."""

    def __init__(self, alat: AlatTani, jumlah_hari: int) -> None:
        if jumlah_hari <= 0:
            raise ValueError("Jumlah hari harus lebih dari 0")

        self._alat = alat
        self._jumlah_hari = jumlah_hari

        # Menyimpan data alat saat transaksi dibuat.
        self._kode_alat = alat.kode
        self._nama_alat = alat.nama
        self._tarif_saat_sewa = alat.tarif_harian

    @property
    def alat(self) -> AlatTani:
        return self._alat

    @property
    def jumlah_hari(self) -> int:
        return self._jumlah_hari

    @property
    def kode_alat(self) -> str:
        return self._kode_alat

    @property
    def nama_alat(self) -> str:
        return self._nama_alat

    @property
    def tarif_saat_sewa(self) -> int:
        return self._tarif_saat_sewa

    def subtotal(self) -> int:
        return self._tarif_saat_sewa * self._jumlah_hari

    def baris_nota(self) -> str:
        tarif = AlatTani.format_rupiah(self._tarif_saat_sewa)
        subtotal = AlatTani.format_rupiah(self.subtotal())
        return (
            f"{self._nama_alat} {self._jumlah_hari} hr "
            f"x {tarif} = {subtotal}"
        )
