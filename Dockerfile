# FROM rpa-image-vnc:latest
FROM bot-runner:latest

# CMD ["./opt/entrypoint.sh", ">", "vnc.log", "2>&1", "&"]
# RUN export DISPLAY=$HOST_IP:99

# set the working directory
WORKDIR /code

# install dependencies
COPY ./requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the src to the folder
COPY ./src ./src

# copy the env file
COPY ./.env ./

# Copy the entrypoint
COPY ./entrypoint.sh ./

# start the server
# CMD ["tail", "-F", "anything"]
# ENTRYPOINT ["python3", "./src/main.py"]
ENTRYPOINT ["./entrypoint.sh"]

# ENV DOCKER_CMD=startvnc.sh

# USER root
# ENTRYPOINT ["/sbin/my_init", "--", "/sbin/setuser", "root"]
# CMD ["$DOCKER_CMD"]

# docker build -t botcity-input-forms-docker .
# docker run -dit --name bot -p 5900:5900 --shm-size=1g --privileged botcity-input-forms-docker