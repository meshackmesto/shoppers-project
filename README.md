## MESHACK ORINA

## PROJECT NAME: SHOPPERS

## DATE:12/06/2024

## Introduction

The Shoppers Management system is designed to help store managers efficiently manage their product inventory, track stock levels, and monitor sales. This system provides an intuitive interface for adding, updating, and viewing products.

## Features

1.Add new products
2.View all products
3.Update stock levels
4.Track sales and order history
5.Customers purchase


## TABLES

   ## products
    1.id: Integer, Primary Key
    2.name: String, not null
    3.description: Text
    4.price: Float, not null
    5.stock_quantity: Integer


   ## sales
    1.id: Integer, primary key
    2.product_id: Integer, foreign key to products
    3.quantity: Integer, not null
    4.sale_date: DateTime, default is current time


   ## customers
    1.id: Integer, primary key
    2.Product_id: integer, foreign key to products 
    3.name: String, not null
    4.email: String, not null, unique
    5.phone: String
    6.address: Text
