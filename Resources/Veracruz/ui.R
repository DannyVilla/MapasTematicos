
# ui - maine map app
# 7/26/2018

# create shinydashboard page
  # dashboard header
header<-dashboardHeader(
  title = "VeraDatos",
  titleWidth = 250
)

# dashboard sidebar
side<-dashboardSidebar(
    # allow user to select multiple categories of location
  sidebarMenu(
    menuItem("Mapa", tabName = "dashboard", icon = icon("th")),
    menuItem("Gr??ficos", tabName = "widgets", icon = icon("bar-chart-o")),
    menuItem("Datos", tabName = "widgets", icon = icon("table")),
    menuItem("Reporte", tabName = "widgets", icon = icon("list-alt"))
  ),
  disable = FALSE,
  width = NULL,
  collapsed = TRUE

)

# dashboard body
body<-dashboardBody(

    # map
    #fluidRow(
      column(width =3,
             fluidRow(width =12,
               box(width =NULL,
                 #height = 510,
                 title = "Indicador",
                 status = "warning",
                 #color="yellow",
                 solidHeader = TRUE,
                 collapsible = TRUE,
                 selectInput("hola",
                             " ",
                             choices = names(maine_icons),
                             selected = names(maine_icons),
                             multiple = FALSE)
               )
             ),
             fluidRow(width =12,
                      box(width =NULL,
                          #height = 510,
                          title = "Regi??n",
                          status = "warning",
                          #color="#FFFACD",
                          solidHeader = TRUE,
                          collapsible = TRUE,
                          selectInput("location_types",
                                      " ",
                                      choices = names(maine_icons),
                                      selected = names(maine_icons),
                                      multiple = TRUE)
                      )
             ),
             fluidRow(width =12,
               box(width =NULL,
               #height = 300,
               title = "Sumario",
               status = "warning",
               #color="#FFFACD",
               solidHeader = TRUE,
               collapsible = TRUE,
               verbatimTextOutput('values')#,
               #plotOutput("rPlot",height = "150px")
               #plotlyOutput("rPlot",height = "150px")
               )
      )),
      column(width =9,
      box(width =NULL,
        #width = 9,
        title = "Mapa",
        status = "warning",
        #color="#FFFACD",
        solidHeader = TRUE,
        collapsible = TRUE,
        leafletOutput("maine_map",height = 500)
      )
    ),#),

    # data table
    fluidRow(
     box(
        width = 12,
        title = "Panorama General",
        status = "warning",
        color="#FFFACD",
        solidHeader = TRUE,
        collapsible = TRUE,
        height = "300px",
        HTML(
          paste0('
                 <div class="piktowrapper-embed" scrolling="yes" style="height: 100px; position: center;" data-uid="36624990-jamapa"><div class="pikto-canvas-wrap"><div class="pikto-canvas"><div class="embed-loading-overlay" style="width: 75%; height: 75%; position: absolute; text-align: center;"><img width="40px" alt="Loading..." style="margin-top: 100px" src="https://create.piktochart.com/loading.gif"/><p style="margin: 0; padding: 0; font-family: Lato, Helvetica, Arial, sans-serif; font-weight: 600; font-size: 16px">Loading...</p></div></div></div></div><script>(function(d){var js, id="pikto-embed-js", ref=d.getElementsByTagName("script")[0];if (d.getElementById(id)) { return;}js=d.createElement("script"); js.id=id; js.async=true;js.src="https://create.piktochart.com/assets/embedding/embed.js";ref.parentNode.insertBefore(js, ref);}(document));</script>
                 ')
          )
          )
        #DT::dataTableOutput("maine_table"))
    ))

dashboardPage(
  header,
  #dashboardSidebar(disable = TRUE),
  side,
  body,
  skin = "yellow"
)
