# server - maine map app
# 7/26/2018

function(input, output){

  # source geocoding script to geocode any new locations to googlesheet
  source("geocode_locations.R")

  # make popup text with name, address, notes, and link to website
  mun_ver <- shapefile("/Users/alseides/COESPO/Mapa_Sofia/Julio/Veracruz_Shape1.shp")
  maine <-
    maine %>%
    mutate(popup = paste("<b><a href='", Proyeccion_2019,"'>", Municipio,"</a></b>", "<br/>",
                         Poblacion_2015, ', ', Proporcion_2015, "<br/>", sep=''))
  mytext=paste("<b><a>","Municipo: ","<b>", mun_ver$NOM_MUN,"<br/>", "Region: ", mun_ver$region,"</a></b>","<br/>", sep="") %>%
    lapply(htmltools::HTML)

  # create leaflet map output
  output$maine_map <- renderLeaflet({

    # clear markers
    # the m leaflet object is created in global.r
    # markers are cleared on refresh so new locations can be added
    m <-
      m %>%
      clearMarkers()

    # add one overlay layer for each marker in maine_icons using purrr
    # use walk from per to return m after adding each layer
    #input$location_types %>%                     # get names of markers in awesomeIconList
     # walk(function(x)                         # then walk through vector of names one at a time
      #  m <<-
       #   m %>% addAwesomeMarkers(             # creating a new awesome marker layer
        #    data = filter(maine, Region == x), # for each category in the maine data
         #   group = x,
          #  icon = maine_icons[[x]],
           # popup = ~popup))

    #input$location_types %>%
     # walk(function(x)                         # then walk through vector of names one at a time
      #  m <<-
      #    m %>% addCircles(data = filter(maine, Region == x),lng = ~lon, lat = ~lat, weight = 1,
       #        radius = ~sqrt(Poblacion_2015) * 30, popup = ~Municipio))



    input$location_types %>%
      walk(function(x)                         # then walk through vector of names one at a time
        m <<-
          m %>% addPolygons(data = subset(mun_ver , region == x),
            fill=TRUE,
            fillColor = pal[[x]],
            weight = 1,
            opacity = 5,
            color = "#EAEDED",
            dashArray = "3",
            fillOpacity = .1,
            #popup = ~NOM_MUN,
            highlight = highlightOptions(
              weight = 3,
              color = "#666",
              dashArray = "",
              fillOpacity = 0.7,
              bringToFront = TRUE),
            label =   mytext,
            labelOptions = labelOptions(
              style = list("font-weight" = "normal",
                           padding = "3px 8px"),
                           textsize = "13px",
                           direction = "auto")))

    m
  })

  # create data table of locations that are visible on the map
  output$maine_table <- DT::renderDataTable({

    # get current bounds of map
    bounds <- input$maine_map_bounds
    latRng <- range(bounds$north, bounds$south)
    lngRng <- range(bounds$east, bounds$west)


    maine %>%
      # apply type filter from sidebar
      filter(Region %in% input$location_types) %>%
      # apply map filters
      filter(lon >= lngRng[1],
             lon <= lngRng[2],
             lat >= latRng[1],
             lat <= latRng[2]) %>%
      dplyr::select(Municipio, Region, Poblacion_2015, Proporcion_2015,Proyeccion_2019,Proporcion_2019)
  }, rownames = FALSE,options = list(lengthMenu = c(5,10), pageLength = 5,searching = TRUE,paging = TRUE)) # because rownames :(,

  #output$rPlot <- renderPlot({

    # Render a barplot
    #x<-table(maine$category)
    #color<-c("#69A223","#FFCA92","#FF8E7F","#CC50B4","#38AADD","#F2952F")
    #par(mar=c(2, 0, 0, 0.5));
    #par(xpd = T, mar = par()$mar + c(0,0,0,7))
    #barplot(x,legend=names(x),horiz=TRUE,col=color,xaxt='n',yaxt='n',space=0.1, legend.text=TRUE,
    #args.legend=list(x="bottom",bty = "n",ncol=3,inset = -.15,cex = 0.9))
  #})

  sR<- reactive({
    R<-input$location_types
  })


  output$values <- renderText({
    x<-list(r=sR())
    x1<-x$r
    t1<-paste("Regi??n:",x1)
    t1
    #t2<-paste("2015:",suma_region1)
    #t3<-paste("2019:",suma_region2)
    #list(t1,"Poblacion Total",t2,t3)
  })


  #output$rPlot <-renderPlot({
   # x<-list(r=sR())
    #x1<-x$r
    #region_data <- subset(maine, Region==x1)
    #suma_region1<-sum(region_data$Poblacion_2015)
    #suma_region2<-sum(region_data$Proyeccion_2019)
    #color<-c("#69A223","#FFCA92","#FF8E7F","#CC50B4","#38AADD","#F2952F")
    #par(mar=c(2, 0, 0, 0.5));
    #par(xpd = T, mar = par()$mar + c(0,0,0,0))
    #x<-c(suma_region1,suma_region2)
    #x<-c(1:2)
    #barplot(x,legend=names(x),horiz=FALSE,col=sample(color,2),xaxt='n',yaxt='n',space=0.1, legend.text=TRUE,
    #        args.legend=list(x="bottom",bty = "n",ncol=2,inset = -.15,cex = 0.9))
  #})

  output$rPlot <-renderPlotly({


    data <- read.csv("https://raw.githubusercontent.com/plotly/datasets/master/school_earnings.csv")

    data$State <- as.factor(c('Massachusetts', 'California', 'Massachusetts', 'Pennsylvania', 'New Jersey', 'Illinois', 'Washington DC',
                              'Massachusetts', 'Connecticut', 'New York', 'North Carolina', 'New Hampshire', 'New York', 'Indiana',
                              'New York', 'Michigan', 'Rhode Island', 'California', 'Georgia', 'California', 'California'))
    par(xpd = T, mar = par()$mar + c(0,0,0,0))
    p <- plot_ly(data, x = ~Women, y = ~Men, text = ~School, type = 'scatter', mode = 'markers', size = ~Gap, color = ~State, colors = 'Paired',
                 #Choosing the range of the bubbles' sizes:
                 sizes = c(5, 20),
                 marker = list(opacity = 0.5, sizemode = 'diameter')) %>% config(displayModeBar = F)%>%
      layout(#title = 'Gender Gap in Earnings per University',
             xaxis = list(title = FALSE,showgrid = FALSE,showticklabels = FALSE),
             yaxis = list(title = FALSE,showgrid = FALSE,showticklabels = FALSE),
             showlegend = FALSE, margin = list(l = 0, r = 0, b = 0, t = 0, pad = 4))
  })
}
