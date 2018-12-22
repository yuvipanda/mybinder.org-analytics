install.packages(c('purrr', 'devtools'))
purrr::walk2(.x = c("rmarkdown", "purrr", "ggplot2", "knitr", "checkmate"), .y = c("1.10", "0.2.5", "3.1.0", "1.20", "1.8.5"), ~devtools::install_version(package = .x, version = .y))

