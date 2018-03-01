#!/bin/bash

ssh -v -N -L ${1}:${2}.nst.anl.gov:22 ANLGateway
