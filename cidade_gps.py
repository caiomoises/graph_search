from dataclasses import dataclass

@dataclass
class Cidade:
    id: int
    estado: str
    cidade: str

@dataclass
class GPS:
    id: int
    la: float
    lo: float

@dataclass
class DataItem:
    key: int
    city: Cidade
    GPS: GPS