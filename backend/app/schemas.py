from enum import Enum
from pydantic import BaseModel, Field

class KategoriMenu(str, Enum):
    kopi = "kopi"
    non_kopi = "non-kopi"
    makanan = "makanan"

class MenuCreate(BaseModel):
    nama: str = Field(min_length=2, max_length=80)
    sku: str = Field(pattern=r"^KOPI-\d{3}$")
    kategori: KategoriMenu
    harga: float = Field(gt=0)

class MenuOut(BaseModel):
    id: int
    nama: str
    sku: str
    kategori: KategoriMenu
    harga: float