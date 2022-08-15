FROM python:3.8-alpine

ARG run_env
ENV env $run_env

LABEL "channel"="SolveMe"
LABEL "creator"="SolveMe community"

WORKDIR /solveme_pytest/

COPY . .

RUN apk update && apk upgrade && apk add bash

RUN pip3 install -r requirements.txt

CMD pytest -m "$env" -s -v tests/*
