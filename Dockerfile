FROM python:3.12.4-alpine3.20
# update apk repo
RUN echo "https://dl-4.alpinelinux.org/alpine/v3.20/main" >> /etc/apk/repositories && \
    echo "https://dl-4.alpinelinux.org/alpine/v3.20/community" >> /etc/apk/repositories


# Get all the prereqs
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-2.30-r0.apk
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-bin-2.30-r0.apk

# install chromedriver, midnightcommander, allure-reports
RUN apk update && \
    apk add openjdk11-jre curl tar && \
    apk add --no-cache chromium chromium-chromedriver tzdata && \
    apk add mc && \
    curl -o allure-2.19.0.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.19.0/allure-commandline-2.19.0.tgz && \
    tar -zxvf allure-2.19.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.19.0/bin/allure /usr/bin/allure && \
    rm allure-2.19.0.tgz

WORKDIR /swgoh_test_project/

# Copy the dependencies files to the working directory
COPY ./pyproject.toml ./uv.lock /swgoh_test_project/

# Install uv and Python dependencies
RUN pip install uv
RUN uv sync