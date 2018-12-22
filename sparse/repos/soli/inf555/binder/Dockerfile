FROM registry.gitlab.inria.fr/soliman/inf555:latest
LABEL Author="Sylvain Soliman <Sylvain.Soliman@inria.fr>"
LABEL Maintainer="Sylvain Soliman <Sylvain.Soliman@inria.fr>"

USER root

WORKDIR /home/$NB_USER

ADD cours8/slides_fages8.pdf td8/ /home/$NB_USER/

RUN chown -R $NB_USER:users /home/$NB_USER/

USER $NB_USER

RUN rm -Rf .jupyter && ln -s work/.jupyter .

# trust all existing notebooks
RUN find . -name '*.ipynb' -print0 | xargs -0 jupyter trust
