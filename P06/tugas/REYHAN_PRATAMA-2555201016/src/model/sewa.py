from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa
from src.model.penyewa import Penyewa


class Sewa:
    """Mewakili transaksi penyewaan alat pertanian."""

    BATAS_ALAT_PER_SEWA: int = 10

    def __init__(self, nomor: str, penyewa: Penyewa) -> None:
        if not nomor.strip():
            raise ValueError("Nomor sewa tidak boleh kosong")

        self._nomor = nomor
        self._penyewa = penyewa
        self._baris: list[BarisSewa] = []

    @property
    def nomor(self) -> str:
        return self._nomor

    @property
    def penyewa(self) -> Penyewa:
        return self._penyewa

    @property
    def baris(self) -> tuple[BarisSewa, ...]:
        return tuple(self._baris)

    def tambah_alat(self, alat: AlatTani, jumlah_hari: int) -> None:
        if len(self._baris) >= self.BATAS_ALAT_PER_SEWA:
            raise ValueError("Maksimal 10 jenis alat dalam satu sewa")

        for baris in self._baris:
            if baris.kode_alat == alat.kode:
                raise ValueError("Alat yang sama tidak boleh ditambahkan dua kali")

        self._baris.append(BarisSewa(alat, jumlah_hari))

    def total(self) -> int:
        return sum(baris.subtotal() for baris in self._baris)

    def nota(self) -> str:
        rincian = "\n".join(
            baris.baris_nota() for baris in self._baris
        )

        return (
            f"Nomor Sewa: {self._nomor}\n"
            f"Penyewa: {self._penyewa.identitas()}\n"
            f"{rincian}\n"
            f"Total: {AlatTani.format_rupiah(self.total())}"
        )
