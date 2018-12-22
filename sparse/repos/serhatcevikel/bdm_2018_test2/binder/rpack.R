    cranlist <- c("httr", "devtools",
                    "listviewer", "XML", "htmltidy", "xml2", "jsonlite", "mongolite")
    # later tidyverse and plotly

    githublist <- c("IRkernel/IRkernel")

    #mirid <- match("tr", getCRANmirrors()[,8])
    #chooseCRANmirror(graphics=FALSE, ind=mirid)

    ## cran packages
    for (package in cranlist)
    { 
        if (!require(package, character.only = T, quietly = T))
        {
            install.packages(package)
        }
    }

    ## install IR kernel
    if (!require('IRkernel', character.only = T, quietly = T)) {
        devtools::install_github('IRkernel/IRkernel')
        IRkernel::installspec(user = FALSE)
    }

    # install juniper
    #JuniperKernel::installJuniper(useJupyterDefault = T)
