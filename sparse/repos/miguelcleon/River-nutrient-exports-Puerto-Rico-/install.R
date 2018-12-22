rprofile_path = file.path(Sys.getenv("HOME"), ".Rprofile")
write('\noptions(repos=c(getOption(\'repos\'),
          CRAN=\'https://cloud.r-project.org\',
          USGS=\'https://owi.usgs.gov/R\'))\n',
      rprofile_path, 
      append =  TRUE)
install.packages('smwrBase')
install.packages('rloadest')
install.packages('car')
install.packages('unitted')
install.packages('dplyr')
packageurl <- "https://github.com/USGS-R/loadflex/archive/v1.0.1.tar.gz"
install.packages(packageurl, repos=NULL, type="source")
install.packages('dplyr')
