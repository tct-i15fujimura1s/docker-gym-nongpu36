
FROM jnishii/docker-gym-nongpu
ENV DEBIAN_FRONTEND noninteractive

RUN sudo python3 -m pip install --upgrade pip
RUN python3 -m pip install nbgrader
RUN jupyter nbextension install --system --py nbgrader --overwrite
RUN jupyter nbextension enable --system --py nbgrader
RUN jupyter serverextension enable --system --py nbgrader

ENV DEBIAN_FRONTEND teletype


ENV USER jovyan
ENV HOME /home/${USER}

# X
ENV DISPLAY :0.0
VOLUME /tmp/.X11-unix
VOLUME ${HOME}
USER ${USER}

#CMD [ "/bin/bash" ]

# Jupyter notebook with virtual frame buffer
CMD cd ${HOME} \
    && xvfb-run -s "-screen 0 1024x768x24" \
    /usr/local/bin/jupyter notebook \
    --port=8888 --ip=0.0.0.0 --allow-root 



