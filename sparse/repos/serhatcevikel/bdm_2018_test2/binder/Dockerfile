#FROM ubuntu:bionic --user
#FROM  postgres:10.5
FROM debian:buster-20181112

# create user
ENV NB_USER jovyan
ENV NB_UID 1000
ENV HOME /home/${NB_USER}

USER root
RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER} && \
    echo "jovyan:jovyan" | chpasswd && \
    usermod -aG sudo ${NB_USER}

# Make sure the contents of our repo are in ${HOME}
COPY . ${HOME}

RUN apt update && \
    apt dist-upgrade -y && \
    apt autoremove -y && \
    apt install -y man manpages \
    python3-pip \
    sudo r-base libssl-dev \
    libpq-dev libcairo2-dev parallel default-jre \
    libunwind-dev expect curl libcurl4-gnutls-dev \
    wget less htop lynx pandoc \
    gnuplot-x11 csvkit git \
    vim screen net-tools \
    libssl-dev libsasl2-dev libxml2-dev libxml2-utils \
    tidy basex jq gnupg mongodb; \


    #apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4 && \
    #echo "deb http://repo.mongodb.org/apt/debian stretch/mongodb-org/4.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list && \
    #apt update && \
    #apt install -y mongodb-org; \   

    # install q 
    #qdeblink=$(lynx -listonly -nonumbers -dump "https://github.com/harelba/q/releases" | grep -P "\.deb$" | head -1); \
    #qdebfile=${qdeblink##*/}; \

    #wget -P ${HOME}/binder $qdeblink; \
    #dpkg -i ${HOME}/binder/$qdebfile; \

    # install latest notebook and other pip packages
    pip3 install --no-cache notebook beakerx sos sos-notebook \
        quilt bash_kernel pgcli ipython-sql postgres_kernel \
        pgspecial jupyter_contrib_nbextensions \
        imongo-kernel ipython_mongo; \

    # install xidel
    wget "https://netcologne.dl.sourceforge.net/project/videlibri/Xidel/Xidel%200.9.8/xidel_0.9.8-1_amd64.deb" && \
    dpkg -i xidel_0.9.8-1_amd64.deb; \


    #jdbc for postgresql
    #wget -P /usr/lib/jvm/default-java/lib https://jdbc.postgresql.org/download/postgresql-42.2.5.jar; \


    # java env variables 
    echo "JAVA_HOME=/usr/lib/jvm/default-java" >> /etc/environment; \
    echo "CLASSPATH=$JAVA_HOME/lib/postgresql-42.2.5.jar" >> /etc/environment; \

    ## install R kernel for jupyter
    Rscript $HOME/binder/rpack.R; \

    # rc configuration
    echo "startup_message off" >> /etc/screenrc; \
    #echo "screen" >> /etc/profile; \
    
    # install node
    curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash - && \
        apt install -y nodejs build-essential; \

    # change postgres password
    # echo "postgres:postgres" | chpasswd; \
    
    # pg config
    # perl -i -pe 's/(md5|peer)$/trust/g' /etc/postgresql/11/main/pg_hba.conf; \

    # make jovyan sudoer with no password prompt
    echo "jovyan ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/jovyan; \

    # take care of sh symlink
    if [ -e /usr/bin/sh ]; \
    then \
        rm /usr/bin/sh; \
    fi; \

    ln -s /usr/bin/bash /usr/bin/sh; \
    #RUN pg_createcluster -u postgres -g postgres 10 main
    
    jupyter-nbextensions-configurator RISE nbpresent; \

    ## install beaker kernels
    beakerx install; \

    # tldr
    npm install tldr -g; \
    
    # own home directory by user
    chown -R ${NB_UID} ${HOME}

USER ${NB_USER}

# nbpresent
RUN python3 -m bash_kernel.install; \
    python3 -m sos_notebook.install; \
    jupyter contrib nbextension install --user; \
    jupyter nbextensions_configurator enable --user; \
    jupyter nbextension install nbpresent --py --overwrite --user; \
    jupyter nbextension enable nbpresent --py --user; \
    jupyter serverextension enable nbpresent --py --user; \
    jupyter-nbextension enable codefolding/main --user; \
    jupyter-nbextension install rise --py --user; \
    jupyter-nbextension enable splitcell/splitcell --user; \
    jupyter-nbextension enable hide_input/main --user; \
    jupyter-nbextension enable nbextensions_configurator/tree_tab/main --user; \
    jupyter-nbextension enable nbextensions_configurator/config_menu/main --user; \
    jupyter-nbextension enable contrib_nbextensions_help_item/main  --user; \
    jupyter-nbextension enable scroll_down/main --user; \
    jupyter-nbextension enable toc2/main --user; \
    jupyter-nbextension enable autoscroll/main  --user; \
    jupyter-nbextension enable rubberband/main --user; \
    jupyter-nbextension enable exercise2/main --user; \
    cp $HOME/binder/common.json $HOME/.jupyter/nbconfig/common.json; \

    # update tldr cache
    tldr -u; \

    # bashrc
    echo "export JAVA_HOME=/usr/lib/jvm/default-java" >> $HOME/.bashrc; \
    echo "export LC_ALL=C.UTF-8" >> $HOME/.bashrc; \
    echo "export LANG=C.UTF-8" >> $HOME/.bashrc; \
    echo "export EDITOR=vim" >> $HOME/.bashrc; \
    #echo "screen" >> $HOME/.bashrc; \

    ## pgcli default options
    #mkdir -p $HOME/.config/pgcli; \
    #cp $HOME/binder/pgcli_config $HOME/.config/pgcli/config; \

    # quilt
    quilt install serhatcevikel/bdm_data; \
    quilt export serhatcevikel/bdm_data $HOME/data; \

    # gunzip database
    #gunzip -k $HOME/data/imdb/imdb.sql.gz; \

    # run expect script for parallel
    expect ${HOME}/binder/expect_script; \

    # extract tsv files onto tsv2
    #datadir=$HOME/data; \
    #imdbdir=$datadir/imdb; \

    #mkdir -p $imdbdir/tsv2; \

    #find $imdbdir/tsv -mindepth 1 | \
    #parallel -k -j0 "basenm=\$(basename {}); gunzip -c {} > ${imdbdir}/tsv2/\${basenm%.gz};";

    # extract comtrade files
    datadir=$HOME/data; \
    comtradedir=$datadir/comtrade_s1; \
    
    mkdir -p $comtradedir/2010e; \
    
    find $comtradedir/2010 -mindepth 1 | \
    parallel -k -j0 "basenm=\$(basename {}); gunzip -c {} > ${comtradedir}/2010e/\${basenm%.gz};";
    


# start postgresql and create imdb database
#USER root
#RUN service postgresql start && \
#    createdb -U postgres imdb2 && \
#    gunzip -c $HOME/data/imdb/imdb.sql.gz | psql imdb2 postgres;
    #psql imdb2 postgres < $HOME/data/imdb/imdb.sql; 


# start mongo
#USER root
#RUN mkdir -p /home/jovyan/mongo; \
#    mongod --dbpath /home/jovyan/mongo && \
#    for file in $HOME/data/comtrade_s1/2010e/*.json; do mongoimport --db comtrade --collection 2010s1 $file; done;


# Specify the default command to run
USER ${NB_USER}
ENV SHELL /usr/bin/bash
WORKDIR ${HOME}
#RUN cd ${HOME}
#USER postgres
#CMD ["/usr/lib/postgresql/10/bin/pg_ctl", "-D", "/var/lib/postgresql/10/main", "-l", "logfile", "start"; "jupyter", "notebook", "--ip", "0.0.0.0"; "su", "-", "jovyan"]
#ENTRYPOINT ["sudo", "-u", "postgres", "/usr/lib/postgresql/10/bin/pg_ctl", "-D", "/etc/postgresql/10/main", "start"; "sudo", "-u", "jovyan", "jupyter", "notebook", "--notebook-dir='/home/jovyan'", "--ip", "0.0.0.0"]
#CMD service postgresql start && jupyter notebook --notebook-dir="/home/jovyan" --ip 0.0.0.0
#CMD ["jupyter", "notebook", "--ip", "0.0.0.0"]
#CMD sudo -i -u postgres /bin/bash -c "/usr/lib/postgresql/10/bin/pg_ctl -D /etc/postgresql/10/main -l /var/lib/postgresql/logfile start" && sudo -i -u jovyan /bin/bash -c "jupyter notebook --notebook-dir='/home/jovyan' --ip 0.0.0.0"
#CMD /usr/lib/postgresql/10/bin/pg_ctl -D /etc/postgresql/10/main -l /var/lib/postgresql/logfile start && jupyter notebook --notebook-dir='/home/jovyan' --ip 0.0.0.0
#CMD postgresql start
#ENTRYPOINT ["service", "postgresql", "start"]
