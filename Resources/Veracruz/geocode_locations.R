maine_sheet <- gs_key("1axLq5FMqHyay9Z8ZorSDl-0vJeuk7WMylIWNJ0hyzj0", 
                      lookup = FALSE,
                      visibility = "private") # see: https://stackoverflow.com/questions/32537882/adding-rows-to-a-google-sheet-using-the-r-package-googlesheets

# read maine place data into a dataframe 
maine <- gs_read(maine_sheet) 

# create df of locations without lat/lon
new_locations <- 
  maine %>% 
  filter(is.na(lon)) %>% 
  mutate(location = paste(Poblacion_2015, Proporcion_2015, "Maine", sep = ", ")) %>% 
  dplyr::select(-lon, -lat) 

# if there are new locations (i.e. non-geocoded locations) geocode them 
# then combine back with previously geocoded locations
# and replace exisiting data in google sheet
if(nrow(new_locations) > 0){
  # geocode new locations 
  new_locations <- 
    new_locations %>%
    dplyr::select(location) %>% 
    map_df(~geocode(., override_limit = TRUE)) %>% 
    bind_cols(new_locations, .) %>% 
    dplyr::select(-location)
  
  # create df of locations with lat/lon 
  old_locations <- 
    maine %>% 
    filter(!is.na(lon))
  
  # combine new and old locations 
  maine <- 
    new_locations %>% 
    bind_rows(old_locations)
  
  # write data with new lat/lon to googlesheet
  gs_edit_cells(ss = maine_sheet, 
                ws = "Maine", 
                input = maine, 
                anchor = "A1",
                trim = TRUE,
                col_names = TRUE)
  
  #mun_ver <- shapefile("/Users/sofia.huerta.p/Desktop/Veracruz_Shape.shp")
}