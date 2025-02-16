from fastapi import APIRouter, HTTPException, status, Depends, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlmodel import Session, select
from db.postgres_conn import get_db_session
from typing import Annotated
from models.car import Car, CarUpdate

car_rt = APIRouter(prefix="/car")


@car_rt.get("/get_cars")
def get_cars(
    session: Session = Depends(get_db_session),
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    cars = session.exec(select(Car).offset(offset).limit(limit)).all()
    return cars


@car_rt.post("/post_car")
def post_car(car: Car, session: Session = Depends(get_db_session)):
    session.add(car)
    session.commit()
    session.refresh(car)
    car_info = jsonable_encoder(car)
    return JSONResponse(content=car_info, status_code=status.HTTP_201_CREATED)


@car_rt.get("/{id}")
def get_car_id(id: int, session: Session = Depends(get_db_session)):
    car = session.get(Car, id)
    if not car:
        raise HTTPException(
            detail="car not found", status_code=status.HTTP_404_NOT_FOUND
        )
    car_data = jsonable_encoder(car)
    return JSONResponse(content=car_data, status_code=status.HTTP_200_OK)


@car_rt.delete("/delete/{id}")
def get_car(id: int, session: Session = Depends(get_db_session)):
    car = session.get(Car, id)
    if not car:
        raise HTTPException(
            detail="car not found", status_code=status.HTTP_404_NOT_FOUND
        )
    session.delete(car)
    session.commit()
    car_data = jsonable_encoder(car)
    return JSONResponse(
        content={"status": "deleted", "content": car_data},
        status_code=status.HTTP_200_OK,
    )


@car_rt.patch("/update/{id}", response_model=Car)
def update_author(id: int, car: CarUpdate, session: Session = Depends(get_db_session)):
    car_db = session.get(Car, id)
    if not car_db:
        raise HTTPException(
            detail="car not found", status_code=status.HTTP_404_NOT_FOUND
        )

    car_data = car.model_dump(exclude_unset=True)

    car_db.sqlmodel_update(car_data)
    session.add(car_db)
    session.commit()
    session.refresh(car_db)
    car_info = jsonable_encoder(car_db)
    return JSONResponse(content=car_info, status_code=status.HTTP_200_OK)
