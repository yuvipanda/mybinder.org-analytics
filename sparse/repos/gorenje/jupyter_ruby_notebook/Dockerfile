FROM gorenje/jupyter-ruby-notebook

RUN gem install thin nokogiri term-ansicolor cheat pry highline rqrcode

USER jovyan

COPY --chown=jovyan:users sinatra.ipynb work
COPY --chown=jovyan:users mechanize.ipynb work
COPY --chown=jovyan:users require_local.ipynb work
COPY --chown=jovyan:users qr_code.ipynb work
COPY --chown=jovyan:users hello_world.rb work
