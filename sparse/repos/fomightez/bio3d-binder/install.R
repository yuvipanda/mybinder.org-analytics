install.packages("tidyverse")
install.packages("rmarkdown")
install.packages("httr")
#install.packages("bio3d") #seemed to fail with XML, see https://bitbucket.org/Grantlab/bio3d/issues/545/error-xml-content-does-not-seem-to-be-xml
install.packages("devtools")
install.packages("XML")
library(devtools)
install_bitbucket("Grantlab/bio3d", subdir="ver_devel/bio3d/") #needed for XML, see https://bitbucket.org/Grantlab/bio3d/issues/545/error-xml-content-does-not-seem-to-be-xml
