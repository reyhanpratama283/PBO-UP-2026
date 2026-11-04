
from typing import ClassVar, Final


class Kios:
    """Kelas untuk mengelola barang yang dijual di kios."""

    # Konstanta kelas
    MARGIN_MINIMUM: Final[float] = 0.10
    MARGIN_MAKSIMUM: Final[float] = 1.00
    NAMA_KIOS: Final[str] = "Kios UMKM Bangkinang"

    # Penghitung jumlah produk
    _jumlah_terdaftar: ClassVar[int] = 0

    def __init__(
        self,
        kode: str,
        nama_produk: str,
        harga_modal: int,
        harga_jual: int,
        stok: int,
    ) -> None:
        if not kode.strip():
            raise ValueError("Kode produk tidak boleh kosong.")

        if not nama_produk.strip():
            raise ValueError("Nama produk tidak boleh kosong.")

        if harga_modal <= 0:
            raise ValueError("Harga modal harus lebih dari nol.")

        if harga_jual <= 0:
            raise ValueError("Harga jual harus lebih dari nol.")

        if stok < 0:
            raise ValueError("Stok tidak boleh negatif.")

        if not self.harga_wajar(harga_modal, harga_jual):
            raise ValueError("Harga jual tidak wajar.")

        self._kode = kode.strip()
        self._nama_produk = nama_produk.strip()
        self._harga_modal = harga_modal
        self._harga_jual = harga_jual
        self._stok = stok

        Kios._jumlah_terdaftar += 1



    @staticmethod
    def harga_wajar(harga_modal: int, harga_jual: int) -> bool:
        """Memeriksa apakah harga jual masuk batas keuntungan."""
        if harga_modal <= 0 or harga_jual <= 0:
            return False

        margin = (harga_jual - harga_modal) / harga_modal

        return (
            Kios.MARGIN_MINIMUM
            <= margin
            <= Kios.MARGIN_MAKSIMUM
        )


    @classmethod
    def dari_baris_csv(cls, baris: str) -> "Kios":
        bagian = baris.strip().split("|")

        if len(bagian) != 5:
            raise ValueError("Format data produk salah.")

        kode, nama, modal, jual, stok = bagian

        return cls(
            kode=kode.strip(),
            nama_produk=nama.strip(),
            harga_modal=int(modal.strip()),
            harga_jual=int(jual.strip()),
            stok=int(stok.strip()),
        )

    @classmethod
    def jumlah_terdaftar(cls) -> int:
        return cls._jumlah_terdaftar
    
    @property
    def kode(self) -> str:
        return self._kode

    @property
    def nama_produk(self) -> str:
        return self._nama_produk

    @property
    def harga_modal(self) -> int:
        return self._harga_modal

    @property
    def harga_jual(self) -> int:
        return self._harga_jual

    @property
    def stok(self) -> int:
        return self._stok

class KatalogProduk:
    """Mengelola kumpulan produk yang terdaftar di kios."""

    def __init__(self) -> None:
        self._produk: list[Kios] = []

    def tambah(self, produk: Kios) -> None:
        """Menambahkan produk ke katalog."""
        for item in self._produk:
            if item.kode == produk.kode:
                raise ValueError("Kode produk sudah terdaftar.")
        self._produk.append(produk)

    def semua_produk(self) -> list[Kios]:
        """Mengembalikan daftar produk di katalog."""
        return list(self._produk)

    def cari(self, kode: str) -> Kios | None:
        """Mencari produk berdasarkan kode."""
        for produk in self._produk:
            if produk.kode == kode:
                return produk
        return None
