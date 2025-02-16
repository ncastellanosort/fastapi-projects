from sqlmodel import SQLModel, Field


class Car(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    image_url: str = Field(default=None)
    year: int = Field(default=None)
    brand: str = Field(default=None)
    model: str = Field(default=None)
    description: str = Field(default=None)
    max_speed: int = Field(default=None)
    acceleration_0_100: float = Field(default=None)
    hp: int = Field(default=None)
    engine: str = Field(default=None)
    transmission: str = Field(default=None)
    base_price: float = Field(default=None)
    country_manufacture: str = Field(default="Suecia")


class CarUpdate(SQLModel):
    id: int | None = None
    image_url: str | None = None
    year: int | None = None
    brand: str | None = None
    model: str | None = None
    description: str | None = None
    max_speed: int | None = None
    acceleration_0_100: float | None = None
    hp: int | None = None
    engine: str | None = None
    transmission: str | None = None
    base_price: float | None = None
    country_manufacture: str | None = None
