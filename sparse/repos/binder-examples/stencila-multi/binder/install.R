source('https://bioconductor.org/biocLite.R')
biocLite('graph')

devtools::install_github('stencila/r', ref = '361bbf560f3f0561a8612349bca66cd8978f4f24')
stencila::register()

install.packages("ggplot2")
