FROM rocker/binder

USER root

RUN apt-get update && \
    apt-get install -y zlib1g-dev libxml2-dev libpng-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
    
RUN Rscript -e "install.packages(c('devtools', 'webshot', 'knitr', 'rmarkdown', 'BiocManager')); BiocManager::install(c('KEGGREST', 'KEGGgraph', 'BiocStyle', 'RCy3')); devtools::install_github('afukushima/MSEApdata', build_vignettes = TRUE); devtools::install_github('afukushima/MSEAp', build_vignettes = TRUE)"

COPY . ${HOME}
RUN chown -R ${NB_USER} ${HOME}
USER ${NB_USER}
