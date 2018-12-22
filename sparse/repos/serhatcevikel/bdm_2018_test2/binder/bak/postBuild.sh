#!/bin/bash

# install nbextension files
# edit nbconvert config files
jupyter contrib nbextension install --user

# configuring the notebook server to load the server extension
jupyter nbextensions_configurator enable --user

cat | perl -pe 'chomp if eof' > ~/.jupyter/nbconfig/common.json <<EOF
{
  "nbext_hide_incompat": false
}
EOF

python -m bash_kernel.install
python -m sos_notebook.install
beakerx install

# nbpresent
jupyter nbextension install nbpresent --py --overwrite --user
jupyter nbextension enable nbpresent --py --user
jupyter serverextension enable nbpresent --py --user

jupyter-nbextension enable codefolding/main
jupyter-nbextension install rise --py --sys-prefix --user
jupyter-nbextension enable splitcell/splitcell --user
jupyter-nbextension enable hide_input/main --user
jupyter-nbextension enable nbextensions_configurator/tree_tab/main --user
jupyter-nbextension enable nbextensions_configurator/config_menu/main --user
jupyter-nbextension enable contrib_nbextensions_help_item/main  --user
jupyter-nbextension enable scroll_down/main --user
jupyter-nbextension enable toc2/main --user
jupyter-nbextension enable autoscroll/main  --user
jupyter-nbextension enable rubberband/main --user
jupyter-nbextension enable exercise2/main --user

#jupyter labextension install @jupyterlab/toc
#jupyter labextension enable @jupyterlab/toc

# quilt
quilt install serhatcevikel/bdm_data
quilt export serhatcevikel/bdm_data ~/data

# tldr
npm install tldr
mkdir -p /home/jovyan/.local/bin
ln -s /home/jovyan/node_modules/tldr/bin/tldr /home/jovyan/.local/bin/tldr
tldr -u

expect <<EOF
spawn parallel --citation
expect "> "
set send_human {.1 .3 1 .05 2}
send -h "will cite\r"
EOF
