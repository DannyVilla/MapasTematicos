# global - maine map app
# 7/26/2018

# load libraries
library(shinydashboard)
library(shiny)
library(googlesheets)
library(tidyverse)
library(ggmap)
library(leaflet)
library(shinydashboard)
library(plotly)
library(raster)

#library(shiny.i18n)

# make icons for categories listed in googlesheet
maine_icons <- awesomeIconList(
  Capital = makeAwesomeIcon(icon = "cutlery", library = "fa", markerColor = "green"),
  Huasteca_Alta = makeAwesomeIcon(icon = "cutlery", library = "fa", markerColor = "beige"),
  Huasteca_Baja = makeAwesomeIcon(icon = "cutlery", library = "fa", markerColor = "lightred"),
  Las_Montanas = makeAwesomeIcon(icon = "cutlery", library = "fa", markerColor = "purple"),
  Los_Tuxtlas   = makeAwesomeIcon(icon = "cutlery", library = "fa", markerColor = "blue"),
  Nautla  = makeAwesomeIcon(icon = "cutlery", library = "fa", markerColor = "orange"),
  Olmeca = makeAwesomeIcon(icon = "cutlery", library = "fa", markerColor = "lightgray"),
  Papaloapan = makeAwesomeIcon(icon = "cutlery", library = "fa", markerColor = "lightblue"),
  Sotavento = makeAwesomeIcon(icon = "cutlery", library = "fa", markerColor = "lightgreen"),
  Totonaca = makeAwesomeIcon(icon = "cutlery", library = "fa", markerColor = "cadetblue")
  # "fire","beer", "graduation-cap", "eye","shopping-cart"
)
pal <- list(
  Capital =  "#E44C28",
  Huasteca_Alta = "#3CA635",
  Huasteca_Baja = "#96B921",
  Las_Montanas = "#e564b8",
  Los_Tuxtlas   = "#44ADAF",
  Nautla  = "#FDAF3F",
  Olmeca = "#B5DCF2",
  Papaloapan = "#3D4890",
  Sotavento = "#846789",
  Totonaca ="#D0D108"
)

# setup basemap
m <-
  leaflet() %>%
  addTiles(group = "OSM") %>%
  addProviderTiles(providers$CartoDB.Positron, group = "Grises") %>%
  addProviderTiles(providers$Esri.NatGeoWorldMap, group = "Relieve") %>%
  addLayersControl(baseGroups = c("OSM", "Grises","Relieve"))
