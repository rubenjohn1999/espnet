#!/bin/bash


. ./path.sh || exit 1;
. ./cmd.sh || exit 1;
. ./db.sh || exit 1;

# general configuration
stage=0       # start from 0 if you need to start from data preparation
stop_stage=1
# inclusive, was 100
SECONDS=0

log() {
    local fname=${BASH_SOURCE[1]##*/}
    echo -e "$(date '+%Y-%m-%dT%H:%M:%S') (${fname}:${BASH_LINENO[0]}:${FUNCNAME[1]}) $*"
}


# Set bash to 'debug' mode, it will exit on :
# -e 'error', -u 'undefined variable', -o ... 'error in pipeline', -x 'print commands',
set -e
set -u
set -o pipefail

. utils/parse_options.sh

log "data preparation started"

mkdir -p ${MALAYALAM}
if [ -z "${MALAYALAM}" ]; then
    log "Fill the value of 'MALAYALAM' of db.sh"
    exit 1
fi


workspace=$PWD

if [ ${stage} -le 0 ] && [ ${stop_stage} -ge 0 ]; then
    log "sub-stage 0: Download Data to downloads"

    cd ${MALAYALAM}
    gdown --id 1xJX4--ahGgItJAoMnT99wrLAHDiUpaY6
    unzip -o monolingual_audio.zip
    rm -f monolingual_audio.zip
    mv monolingual_audio/* .
    rm -r monolingual_audio
    cd $workspace
fi

if [ ${stage} -le 1 ] && [ ${stop_stage} -ge 1 ]; then
    log "sub-stage 1: Preparing Data for openslr"

    python3 local/data_prep_mono.py -d ${MALAYALAM}
    utils/spk2utt_to_utt2spk.pl data/mono_ml/spk2utt > data/mono_ml/utt2spk
    utils/fix_data_dir.sh data/mono_ml
fi

log "Successfully finished. [elapsed=${SECONDS}s]"
