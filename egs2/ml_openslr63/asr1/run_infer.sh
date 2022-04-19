#!/usr/bin/env bash
# Set bash to 'debug' mode, it will exit on :
# -e 'error', -u 'undefined variable', -o ... 'error in pipeline', -x 'print commands',
set -e
set -u
set -o pipefail

./asr.sh \
    --ngpu 1 \
    --skip_data_prep true \
    --skip_train true \
    --asr_exp exp/asr_train_asr_conformer_s3prlfrontend_hubert_fused_raw_ml_bpe150_sp \
    --lm_exp exp/lm_train_lm_ml_bpe150