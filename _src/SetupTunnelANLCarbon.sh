#!/bin/bash

ssh -v -N -L ${1}:clogin:22 ANLGateway
